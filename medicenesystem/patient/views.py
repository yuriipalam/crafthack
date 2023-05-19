from django.shortcuts import render, get_object_or_404
from django.contrib.auth.decorators import login_required
from django.shortcuts import render
from .models import User, Patient


def profile(request):
    patient = get_object_or_404(Patient, pk=request.user.id)
    return render(request, 'patient/patient.html', context={'p': patient, 'pillows': patient.instruction.pillows.all()})
