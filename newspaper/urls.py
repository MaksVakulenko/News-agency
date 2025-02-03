from django.urls import path
from . import views

app_name = "newspaper"

urlpatterns = [
    path("", views.NewspaperListView.as_view(), name="newspaper-list"),
    path(
        "newspaper/<int:pk>/",
        views.NewspaperDetailView.as_view(),
        name="newspaper-detail",
    ),
    path(
        "newspaper/create/",
        views.NewspaperCreateView.as_view(),
        name="newspaper-create",
    ),
    path(
        "newspaper/<int:pk>/update/",
        views.NewspaperUpdateView.as_view(),
        name="newspaper-update",
    ),
    path(
        "newspaper/<int:pk>/delete/",
        views.NewspaperDeleteView.as_view(),
        name="newspaper-delete",
    ),
]
