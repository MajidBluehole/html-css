from django.shortcuts import render

# Create your views here.
def index(request):
    return render(request,'index.html')

def social(request):
    return render(request,'social.html')