from django.urls import reverse_lazy
from django.shortcuts import render, redirect


from .forms import *
from .models import *


def main_view(request):
    return render(request, "dpv_complaint/complaint_main_page.html")


def from_waiting_for_distribution_to_assigned_to_technician(request, complaint_id):
    form_name = "Quejas Aceptadas"
    if request.method == "POST":
        form = AssignedToTechnicalForm(request.POST)
        if form.is_valid():
            post = form.save(commit=False)
            post.enter_date = timezone.now()
            post.complaint = Complaint.objects.get(id=complaint_id)
            post.complaint.status = 'Esperando Respuesta de Tecnico'
            post.complaint.save()
            post.id = post.pk
            post.save()
            return redirect(reverse_lazy("index_asigned_to_tecnic", tecnic_id=post.tecnic.id))
    else:
        form = AssignedToTechnicalForm()
    return render(request, "dpv_complaint/single_form.html", {'form': form, 'form_name': form_name})


def watch_complaint(request, complaint_id):
    complaint = Complaint.objects.filter(id=complaint_id)
    return render(request, "dpv_complaint/watch_complaint.html", { 'complaint': complaint })


def from_assigned_to_technician_to_finished_complaint(request, complaint_id, tecnic_id):
    _form_name = "Dar Respuesta a la Queja"
    if request.method == "POST":
        _form = FinishedComplaintForm(request.POST)
        if _form.is_valid() and complaint_id is not None and tecnic_id is not None:
                _post = _form.save(commit=False)
                _post.enterDate = timezone.now()
                _post.complaint = Complaint.objects.get(id=complaint_id)
                _post.technical = Technical.objects.get(id=tecnic_id)
                _post.id = _post.pk
                _post.save()
                return redirect(reverse_lazy('index_asigned_to_tecnic'))
    else:
        _form = FinishedComplaintForm()
    return render(request, "dpv_complaint/asigned_to_finished.html", {'form': _form, 'form_name': _form_name})


def index_accepted_all(request, accepted_id):
    elms = Accepted.objects.get(id=accepted_id)
    return render(request, 'dpv_complaint/watch_accepted.html', {'index': elms})


def from_finished_complaint_to_accepted_complaint(request, complaint_id, tecnic_id):
    _form_name = "Quejas Aceptadas"
    if request.method == "POST":
        _form = AcceptedForm(request.POST)
        if _form.is_valid():
            _post = _form.save(commit=False)
            _post.finishedDate = timezone.now()
            if (complaint_id is not None) and (tecnic_id is not None):

                _post.complaint = Complaint.objects.get(id=complaint_id)
                _post.technical_work_in_complaint = Technical.objects.get(id=tecnic_id)
                _post.boss_accepted = Perfil.objects.get(id=1)
                _post.id = _post.pk
                _post.save()
                return redirect(reverse_lazy('index_accepted_all'))
    else:
        _form = AcceptedForm()
    return render(request, "dpv_complaint/single_form.html", {'form': _form, 'form_name': _form_name })