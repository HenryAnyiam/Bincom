from django.shortcuts import render
from django.http import HttpResponseRedirect
from django.urls import reverse
from django.views.generic import TemplateView, ListView, DeleteView, View
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.mixins import LoginRequiredMixin
from .forms import UserSignUpForm, TaskCreateForm
from .models import Task


# Create your views here.
class CreateUserView(TemplateView):

    template_name = "signup.html"

    def get(self, request):
        """get page"""
        form = UserSignUpForm()
        return render(request, self.template_name, {'form': form})

    def post(self, request):
        """add user"""
        form = UserSignUpForm(request.POST)

        if form.is_valid():
            user = form.save()
            login(request, user)
            return HttpResponseRedirect(reverse("main_app:home"))
        else:
            return render(request, self.template_name, {'form': form, 'error': form.errors})


class LoginView(TemplateView):

    template_name = "login.html"

    def get(self, request):
        """get page"""
        return render(request, self.template_name)

    def post(self, request):
        """login user"""
        username = request.POST.get("username")
        password = request.POST.get("password")

        if not username or not password:
            return render(request, self.template_name, {"error": "All fields required"})
        user = authenticate(request, username=username, password=password)
        if not user:
            return render(request, self.template_name, {"error": "Incorrect Username/Password"})
        login(request, user)
        return HttpResponseRedirect(reverse("main_app:home"))


class TaskCreateView(LoginRequiredMixin, View):

    login_url = "/login"

    def post(self, request):
        """add new task"""

        form = TaskCreateForm(request.POST)
        if form.is_valid():
            task = form.save()
            print(task)
            print(request.user.tasks.order_by("created_at"))
        else:
            queryset = request.user.tasks.order_by("-created_at")
            render(request, self.template_name, {"objects": queryset, "error": form.errors})
        return HttpResponseRedirect(reverse("main_app:home"))


class TaskListView(LoginRequiredMixin, TemplateView):

    template_name = "index.html"
    login_url = "/login"

    def get(self, request):
        """get all tasks"""
        queryset = request.user.tasks.order_by("-created_at")
        return render(request, self.template_name, {"objects": queryset})


class TaskDeleteView(LoginRequiredMixin, View):

    login_url = '/login'

    def post(self, request) -> str:
        task = request.user.tasks.filter(id=request.POST.get("task_id"))
        if task:
            task[0].delete()
        return HttpResponseRedirect(reverse("main_app:home"))

class LogoutView(View):

    def get(self, request):
        """log a user out"""
        if request.user:
            logout(request)
        return HttpResponseRedirect(reverse('main_app:login'))
