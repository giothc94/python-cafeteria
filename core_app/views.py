from django.shortcuts import render, HttpResponse

# Create your views here.
def home(request):
    # return HttpResponse('home')
    return render(request,'core_app/index.html')

def about(request):
    return render(request,'core_app/about.html')

def store(request):
    return render(request,'core_app/store.html')