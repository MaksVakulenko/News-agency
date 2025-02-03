from django.urls import path
from .views import (
    NewspaperListView,
    NewspaperDetailView,
    NewspaperCreateView,
    NewspaperUpdateView,
    NewspaperDeleteView,
    TopicListView,
    TopicCreateView,
    TopicUpdateView,
    TopicDeleteView,
    RedactorListView,
    RedactorDetailView,
)

app_name = "newspaper"

urlpatterns = [
    path("", NewspaperListView.as_view(), name="newspaper-list"),
    path(
        "newspaper/<int:pk>/",
        NewspaperDetailView.as_view(),
        name="newspaper-detail",
    ),
    path(
        "newspaper/create/",
        NewspaperCreateView.as_view(),
        name="newspaper-create",
    ),
    path(
        "newspaper/<int:pk>/update/",
        NewspaperUpdateView.as_view(),
        name="newspaper-update",
    ),
    path(
        "newspaper/<int:pk>/delete/",
        NewspaperDeleteView.as_view(),
        name="newspaper-delete",
    ),
    path("topic/", TopicListView.as_view(), name="topic-list"),
    path("topic/create/", TopicCreateView.as_view(), name="topic-create"),
    path("topic/<int:pk>/update/", TopicUpdateView.as_view(), name="topic-update"),
    path("topic/<int:pk>/delete/", TopicDeleteView.as_view(), name="topic-delete"),
    path("redactors/", RedactorListView.as_view(), name="redactor-list"),
    path("redactor/<int:pk>/", RedactorDetailView.as_view(), name="redactor-detail"),
]
