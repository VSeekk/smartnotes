from typing import Any
from django.db.models.query import QuerySet
from django.shortcuts import render
from .models import Notes
from django.views.generic import ListView, DetailView, CreateView, UpdateView
from django.http import HttpResponseRedirect
from .forms import NotesForm
from django.views.generic.edit import DeleteView
from django.contrib.auth.mixins import LoginRequiredMixin
# Create your views here.

class NotesDeleteView(DeleteView):
    model= Notes
    success_url='/smart/notes'
    template_name ='notes/notes_delete.html'


class NotesUpdateView(UpdateView):
    model= Notes
    success_url='/smart/notes'
    form_class = NotesForm

class NotesCreateView(CreateView):
    model= Notes
    success_url='/smart/notes'
    form_class = NotesForm

    def form_valid(self, form):
        self.object = form.save(commit=False)
        self.object.user =self.request.user
        self.object.save()
        return HttpResponseRedirect(self.get_success_url())


class NotesListView(LoginRequiredMixin, ListView):
    model = Notes
    context_object_name= "notes"
    template_name ='notes/notes_list.html'
    login_url = "/admin"

   


    def get_queryset(self):
        return self.request.user.notes.all()

class NotesDetailView(DetailView):
    model= Notes
    context_object_name = "note"


    