from django.shortcuts import render

# Create your views here.

def index(request):
    return render(request,'SuperAdmin_index.html')
def SuperAdmin_trainees(request):
    return render(request,'SuperAdmin_trainees.html')
def SuperAdmin_ActiveTrainees(request):
    return render(request,'SuperAdmin_ActiveTrainees.html')
def SuperAdmin_PassiveTrainees(request):
    return render(request,'SuperAdmin_PassiveTrainees.html')
def SuperAdmin_ActiveTraineeProfile(request):
    return render(request,'SuperAdmin_ActiveTrainerProfile.html')
def SuperAdmin_PassiveTraineeProfile(request):
    return render(request,'SuperAdmin_PassiveTrainerProfile.html')
def SuperAdmin_Machines(request):
    return render(request,'SuperAdmin_Machines.html')
def SperAdmin_dumbell(request):
    return render(request,'SperAdmin_dumbell.html')