from django.shortcuts import render

# Create your views here.

def index(request):
    return render(request,'SuperAdmin_index.html')
def trainees(request):
    return render(request,'trainees.html')