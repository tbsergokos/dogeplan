from django.shortcuts import render
from django.views.generic import TemplateView,ListView,DetailView,RedirectView
def home_view(request):
  template_name='landing/home.html'
  return render(request,template_name)