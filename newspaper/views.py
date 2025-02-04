from django.views import generic
from .forms import NewspaperForm, RedactorCreationForm
from .models import Newspaper, Topic
from django.contrib.auth.mixins import LoginRequiredMixin

from django.urls import reverse_lazy
from .models import Redactor


class NewspaperListView(LoginRequiredMixin, generic.ListView):
    model = Newspaper
    template_name = "newspaper/newspaper_list.html"
    context_object_name = "newspapers"
    paginate_by = 6

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["topics"] = Topic.objects.all()
        return context

    def get_queryset(self):
        queryset = super().get_queryset()
        search = self.request.GET.get("search")
        topic = self.request.GET.get("topic")

        if search:
            queryset = queryset.filter(title__icontains=search)
        if topic:
            queryset = queryset.filter(topic__id=topic)

        return queryset


class NewspaperDetailView(LoginRequiredMixin, generic.DetailView):
    model = Newspaper
    template_name = "newspaper/newspaper_detail.html"


class NewspaperCreateView(LoginRequiredMixin, generic.CreateView):
    model = Newspaper
    form_class = NewspaperForm
    template_name = "newspaper/newspaper_form.html"
    success_url = reverse_lazy("newspaper:newspaper-list")


class NewspaperUpdateView(LoginRequiredMixin, generic.UpdateView):
    model = Newspaper
    form_class = NewspaperForm
    template_name = "newspaper/newspaper_form.html"
    success_url = reverse_lazy("newspaper:newspaper-list")


class NewspaperDeleteView(LoginRequiredMixin, generic.DeleteView):
    model = Newspaper
    template_name = "newspaper/newspaper_confirm_delete.html"
    success_url = reverse_lazy("newspaper:newspaper-list")


class TopicListView(LoginRequiredMixin, generic.ListView):
    model = Topic
    template_name = "newspaper/topic_list.html"
    context_object_name = "topics"
    paginate_by = 10


class TopicCreateView(LoginRequiredMixin, generic.CreateView):
    model = Topic
    fields = ["name"]
    template_name = "newspaper/topic_form.html"
    success_url = reverse_lazy("newspaper:topic-list")


class TopicUpdateView(LoginRequiredMixin, generic.UpdateView):
    model = Topic
    fields = ["name"]
    template_name = "newspaper/topic_form.html"
    success_url = reverse_lazy("newspaper:topic-list")


class TopicDeleteView(LoginRequiredMixin, generic.DeleteView):
    model = Topic
    template_name = "newspaper/topic_confirm_delete.html"
    success_url = reverse_lazy("newspaper:topic-list")


class RedactorListView(LoginRequiredMixin, generic.ListView):
    model = Redactor
    template_name = "newspaper/redactor_list.html"
    context_object_name = "redactors"
    paginate_by = 6


class RedactorDetailView(LoginRequiredMixin, generic.DetailView):
    model = Redactor
    template_name = "newspaper/redactor_detail.html"
    context_object_name = "redactor"


class RedactorCreateView(LoginRequiredMixin, generic.CreateView):
    model = Redactor
    form_class = RedactorCreationForm
    template_name = "newspaper/redactor_form.html"
    success_url = reverse_lazy("newspaper:redactor-list")


class RedactorUpdateView(LoginRequiredMixin, generic.UpdateView):
    model = Redactor
    fields = ["username", "first_name", "last_name", "email", "years_of_experience"]
    template_name = "newspaper/redactor_form.html"
    success_url = reverse_lazy("newspaper:redactor-list")


class RedactorDeleteView(LoginRequiredMixin, generic.DeleteView):
    model = Redactor
    template_name = "newspaper/redactor_confirm_delete.html"
    success_url = reverse_lazy("newspaper:redactor-list")
