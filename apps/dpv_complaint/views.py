from django.http import HttpResponse
from django.urls import reverse_lazy
from django.shortcuts import render, redirect
from django.utils import timezone

from .forms import *
from .models import *

# Create your views here.

# Index

def index_Complaint(request):
    index_name = 'Indice de las Quejas'
    elems = Complaint.objects.all()
    return render(request, "dpv_complaint/index_complaint.html", { 'index' : elems, 'index_name' : index_name })

def index_PresentedComplaint(request):
    index_name = 'Indice Quejas sin Asignar'
    elems = PresentedComplaint.objects.all()
    return render(request, "dpv_complaint/index_complaint.html", { 'index' : elems, 'index_name' : index_name })

def index_WaitingForDistribution(request):
    index_name = 'Indice de Quejas en espera de su distribucion'
    elems = WaitingForDistribution.objects.all()
    return render(request, "dpv_complaint/index_complaint.html", {'index': elems, 'index_name' : index_name })

def index_AsignedToTecnic(request):
    index_name = 'Quejas asignadas a los tecnicos'
    elems = AsignedToTecnic.objects.all()
    return render(request, "dpv_complaint/index_complaint.html", {'index': elems, 'index_name' : index_name })

def index_FinishedComplaint(request):
    index_name = 'Indice de Quejas Finalizadas'
    elems = FinishedComplaint.objects.all()
    return render(request, "dpv_complaint/index_complaint.html", { 'index' : elems, 'index_name' : index_name})

def index_Accepted(request):
    index_name = 'Indice de Quejas Aceptadas'
    elems = FinishedComplaint.objects.all()
    return render(request, "dpv_complaint/index_complaint.html", { 'index' : elems, 'index_name' : index_name})
