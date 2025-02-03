from django.shortcuts import render, get_object_or_404, redirect
from django.urls import reverse_lazy
from django.views import generic
from .models import Newspaper, Topic, Redactor
from .forms import NewspaperForm


class NewspaperListView(generic.ListView):
    model = Newspaper
    template_name = "newspaper/newspaper_list.html"
    context_object_name = "newspapers"


class NewspaperDetailView(generic.DetailView):
    model = Newspaper
    template_name = "newspaper/newspaper_detail.html"


class NewspaperCreateView(generic.CreateView):
    model = Newspaper
    form_class = NewspaperForm
    template_name = "newspaper/newspaper_form.html"
    success_url = reverse_lazy("newspaper:newspaper-list")


class NewspaperUpdateView(generic.UpdateView):
    model = Newspaper
    form_class = NewspaperForm
    template_name = "newspaper/newspaper_form.html"
    success_url = reverse_lazy("newspaper:newspaper-list")


class NewspaperDeleteView(generic.DeleteView):
    model = Newspaper
    template_name = "newspaper/newspaper_confirm_delete.html"
    success_url = reverse_lazy("newspaper:newspaper-list")


class TopicListView(generic.ListView):
    model = Topic
    template_name = "newspaper/topic_list.html"
    context_object_name = "topics"


class TopicCreateView(generic.CreateView):
    model = Topic
    fields = ["name"]
    template_name = "newspaper/topic_form.html"
    success_url = reverse_lazy("newspaper:topic-list")


class TopicUpdateView(generic.UpdateView):
    model = Topic
    fields = ["name"]
    template_name = "newspaper/topic_form.html"
    success_url = reverse_lazy("newspaper:topic-list")


class TopicDeleteView(generic.DeleteView):
    model = Topic
    template_name = "newspaper/topic_confirm_delete.html"
    success_url = reverse_lazy("newspaper:topic-list")


class RedactorListView(generic.ListView):
    model = Redactor
    template_name = "newspaper/redactor_list.html"
    context_object_name = "redactors"


class RedactorDetailView(generic.DetailView):
    model = Redactor
    template_name = "newspaper/redactor_detail.html"
    context_object_name = "redactor"
