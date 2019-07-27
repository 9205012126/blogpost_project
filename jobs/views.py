from django.shortcuts import render
from jobs.models import Jobs

def home(request):
    jobs = Jobs.objects.all()
    return render(request,'jobs/home.html',
                  {'jobs':jobs})
