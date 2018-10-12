from django.shortcuts import render
from django.urls import reverse_lazy
from . import models
# Create your views here.
from django.views.generic import ListView,DetailView,TemplateView,CreateView,UpdateView,DeleteView

class Index(TemplateView):
    template_name = 'index.html'



class List(ListView):
    template_name = 'list.html'
    model = models.School



class Detail(DetailView):
    context_object_name = 'school_detail'
    template_name = 'school_detail.html'
    model = models.School


class SchoolCreateView(CreateView):
    fields = ('name','principle','location')
    model = models.School



class SchoolUpdateView(UpdateView):
    fields = ('name','principle')
    model = models.School

class SchoolDeleteView(DeleteView):
    model = models.School
    success_url = reverse_lazy("app_one:list")