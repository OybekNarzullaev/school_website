from django.shortcuts import render
from django.views.generic import (ListView, DetailView)
from .models import Standard, Subject, Lesson

# Create your views here.
class StandardListView(ListView):
    context_object_name = 'standards'
    model = Standard
    template_name = 'curriculum/standard_list_view.html'


# fanlar uchun views
class SubjectListView(DetailView):
    context_object_name = 'standards'
    model = Standard
    template_name = 'curriculum/subject_list_view.html'