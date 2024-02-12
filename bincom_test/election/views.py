from django.shortcuts import render
from .models import PollingUnit, LGA


# Create your views here.

def index(requests):
    """home page"""
    return render(requests, 'election/index.html')


def get_pu_results(request):
    """get polling unit request"""
    error = None
    results = None
    unit = None
    polling_units = PollingUnit.objects.all()
    post = False
    if request.method == 'POST':
        post = True
        id = request.POST.get('uniqueid')
        try:
            id = int(id)
            unit = PollingUnit.objects.filter(uniqueid=id)
        except ValueError:
            unit = PollingUnit.objects.filter(polling_unit_name=id)
            if not unit:
                unit = PollingUnit.objects.filter(polling_unit_name__contains=id)
        if unit:
            unit = unit[0]
            results = unit.results.all()
        else:
            error = "Polling Unit Not Found"
    return render(request, 'election/pu_results.html',
                  {'polling_units': polling_units,
                   'unit': unit, 
                   'error': error,
                   'title': 'PU Results',
                   'results': results,
                   'post': post,})


def get_total_results(request):
    """get total result of an LGA"""
    LGAs = LGA.objects.all()
    error = None
    pollingunits = {}
    total = {}
    lga_name = None
    post = False
    if request.method == 'POST':
        post = True
        lga_id = request.POST.get('lga_id')
        if not lga_id:
            error = "You did not make a valid selection"
        else:
            lga = LGA.objects.filter(lga_id=lga_id)
            if lga:
                lga = lga[0]
                lga_name = lga.lga_name
                polls = lga.polling_units.all()
                pollingunits = {i.polling_unit_name.title():
                                {j.party_abbreviation:
                                 j.party_score for j in i.results.all()} for i in polls}
                for poll in pollingunits:
                    items = pollingunits[poll].items()
                    for party_name, party_score in items:
                        if party_name in total:
                            total[party_name] += party_score
                        else:
                            total[party_name] = party_score
    return render(request, 'election/lga_results.html',
                  {'LGAs': LGAs,
                   'error': error,
                   'pollingunits': pollingunits,
                   'total': total,
                   "lga_name": lga_name,
                   'post': post,})
