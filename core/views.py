from django.shortcuts import render
from django.http import HttpResponse
from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView, View, TemplateView
from core.models import Card, Category
from django.shortcuts import render, get_object_or_404, redirect
import random
from Gallery.forms import FilterForm
from django.db.models import Q


def all(request):
    '''
    вьюха для просмотра постов по категориям
    '''
    form = FilterForm(request.GET.get('q'))
    context = {
        'form': form,
    }
    return render(request, 'all.html', context)


# def search(request):
#     form = FilterForm(request.GET.get('q'))
#     query = form(request.GET.get('category'))
#     query2 = form(request.GET.get('god_grad'))
#     if (not query) & (not query2):
#         object_list = Card.objects.all()
#     else:
#         object_list = Card.objects.filter(
#             Q(category_id__exact =query), Q(god_grad__icontains=query2)
#         )
#     context = {
#         'form': form,
#         'object_list': object_list,
#     }
#     return render(request, 'all.html', context)

class SearchResultsView(ListView):
    model = Card
    template_name = 'search_results.html'
 
    def get_queryset(self): # новый
        query = self.request.GET.get('category')
        query2 = self.request.GET.get('god_grad')
        if (not query) & (not query2):
            object_list = Card.objects.all()
        else:
            object_list = Card.objects.filter(
                Q(category_id__exact =query), Q(god_grad__icontains=query2)
            )
        return object_list


def cat_sort(request):
    categories = Category.objects.filter()
    
    context = {
        'categories': categories,
    }
    return render(request, 'cat-sort.html', context)


def cat_ord(request, category_id):
    '''
    вьюха для просмотра постов по категориям
    '''
    form = FilterForm(request.GET)
    category = get_object_or_404(Category, id=category_id)
    cards = Card.objects.filter(category=category).order_by('-god_grad')
    categories = Category.objects.get(id=category_id)
    if form.is_valid():
        if form.cleaned_data["god_grad"]:
            cards = cards.filter(god_grad__exact=form.cleaned_data["god_grad"])
    context = {
        'categories': categories,
        'cards': cards,
        'form': form,
    }
    return render(request, 'cat.html', context)


def slide(request):
    '''
    вьюха для вывода gj категориям
    '''
    items = list(Card.objects.all())
    cards = random.sample(items, 5)
    context = {
        'cards': cards,
    }
    return render(request, 'index.html', context)


class CardView(DetailView):
    '''
    вьюха для просмотра поста
    '''
    model = Card
    context_object_name = 'card'
    pk_url_kwarg = 'card_id'
    template_name = 'card-detail.html'

    def get(self, request, card_id, *args, **kwargs):
        self.object = self.get_object()
        context = self.get_context_data(object=self.object)
        return self.render_to_response(context)


def cat_sort(request):
    categories = Category.objects.filter()
    
    return {
        'categories': categories,
    }


