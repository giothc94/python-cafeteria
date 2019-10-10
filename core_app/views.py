from django.shortcuts import render, HttpResponse

# Create your views here.
def home(request):
    # return HttpResponse('home')
    return render(request,'core_app/index.html')

def about(request):
    return render(request,'core_app/about.html')

def services(request):
    return render(request,'core_app/services.html')

def store(request):
    return render(request,'core_app/store.html')

def contact(request):
    return render(request,'core_app/contact.html')

def blog(request):
    return render(request,'core_app/blog.html')

def sample(request):
    return render(request,'core_app/sample.html')