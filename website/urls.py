from django.urls import path

from . import views

app_name = "website"


urlpatterns = [
    path("", views.CategoryListView.as_view(), name="category-list"),
    path(
        "category/create/", views.CategoryCreateView.as_view(), name="category-create"
    ),
    path(
        "category/<str:slug>/update/",
        views.CategoryUpdateView.as_view(),
        name="category-update",
    ),
    path(
        "category/<str:slug>/delete/",
        views.CategoryDeleteView.as_view(),
        name="category-delete",
    ),
    path(
        "category/<str:slug>/",
        views.CategoryDetailView.as_view(),
        name="category-detail",
    ),
    path("contact/", views.ContactView.as_view(), name="contact"),
    path("about/", views.AboutView.as_view(), name="about"),
]
