from django.urls import path
from .views import CreateUserView, LoginView, TaskCreateView, TaskListView, TaskDeleteView, LogoutView


app_name = "main_app"

urlpatterns = [
        path("", TaskListView.as_view(), name="home"),
        path("signup", CreateUserView.as_view(), name="signup"),
        path("login", LoginView.as_view(), name="login"),
        path("create_task", TaskCreateView.as_view(), name="create_task"),
        path("delete_task", TaskDeleteView.as_view(), name="delete_task"),
        path("logout", LogoutView.as_view(), name="logout"),
    ]
