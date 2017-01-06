from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.
def home_method(request):
  return render(request, 'home.html')

def contact_method(request):
  return render(request, 'contact.html')
