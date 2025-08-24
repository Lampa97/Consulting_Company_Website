from django.urls import reverse_lazy
from django.views.generic import (CreateView, DeleteView, DetailView, ListView,
                                  TemplateView, UpdateView)

from .forms import CategoryForm
from .models import Category


class CategoryListView(ListView):
    model = Category
    template_name = "website/category_list.html"
    context_object_name = "categories"

    def get_queryset(self):
        return Category.objects.all()


class CategoryCreateView(CreateView):
    model = Category
    template_name = "website/category_form.html"
    form_class = CategoryForm
    success_url = reverse_lazy("website:category-list")


class CategoryUpdateView(UpdateView):
    model = Category
    template_name = "website/category_form.html"
    form_class = CategoryForm
    success_url = reverse_lazy("website:category-list")


class CategoryDeleteView(DeleteView):
    model = Category
    template_name = "website/category_confirm_delete.html"
    success_url = reverse_lazy("website:category-list")


class CategoryDetailView(DetailView):
    model = Category
    template_name = "website/category_detail.html"
    context_object_name = "category"


class ContactView(TemplateView):
    template_name = "website/contacts.html"


class AboutView(TemplateView):
    template_name = "website/about.html"
