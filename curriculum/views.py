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

# darslar ro'yhati uchun view
class LessonListView(DetailView):
    context_object_name = 'subjects'
    model = Subject
    template_name = 'curriculum/lesson_list_view.html'


# dars ma'lumotlari view si
class LessonDetailView(DetailView):
    context_object_name = 'lessons'
    model = Lesson
    template_name = 'curriculum/lesson_detail_view.html'