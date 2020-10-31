from django.shortcuts import render, redirect, get_object_or_404, reverse
from .models import *


def redirect_to_tags(request):
    return redirect('tags_list', permanent=True)

class ObjectDetailMixin:
    model = None
    template = None

    def get(self, request, slug):
        """Функция для деталей объекта"""
        obj = get_object_or_404(self.model, slug__iexact=slug)
        context = {self.model.__name__.lower(): obj} #example 'post': post
        return render(request, self.template, context)


class ObjectCreateMixin:
    model_form = None #PostForm
    template = None #html
    redirect_to_tags = False

    def get(self, request):
        """Функция для взятия объекта с сервера"""
        form = self.model_form() #PostForm or TagForm
        context = {'form': form}
        return render(request, self.template, context)

    def post(self, request):
        bound_form = self.model_form(request.POST)
        if bound_form.is_valid():
            new_obj = bound_form.save()
            if self.redirect_to_tags:
                return redirect_to_tags(request)
            else:
                return redirect(new_obj)
        return render(request, self.template, {'form': bound_form})


class ObjectUpdateMixin:
    model = None
    model_form = None
    template = None

    def get(self, request, slug):
        obj = get_object_or_404(self.model, slug__iexact=slug)
        bound_form = self.model_form(instance=obj)
        context = {'form': bound_form, self.model.__name__.lower(): obj}
        return render(request, self.template, context=context)

    def post(self, request, slug):
        obj = get_object_or_404(self.model, slug__iexact=slug)
        bound_form = self.model_form(request.POST, instance=obj)
        if bound_form.is_valid():
            new_obj = bound_form.save()
            return redirect(new_obj)
        context = {'form': bound_form, self.model.__name__.lower(): obj}
        return render(request, self.template, context=context)


class ObjectDeleteMixin:
    model = None
    template = None
    redirect_url = None

    def get(self, request, slug):
        obj = get_object_or_404(self.model, slug__iexact=slug)
        context = {self.model.__name__.lower(): obj}
        return render(request, self.template, context)

    def post(self, request, slug):
        obj = get_object_or_404(self.model, slug__iexact=slug)
        obj.delete()
        return redirect(reverse(self.redirect_url))
