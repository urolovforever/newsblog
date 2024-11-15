from django.shortcuts import render
from django.urls import reverse_lazy
from django.views.generic import CreateView,DeleteView,UpdateView

from .models import New, Category, Region


# Create your views here.
def home(request):
    first_news = New.objects.first()
    three_news = New.objects.all()[1:4]
    return render(request, 'home.html', {
        'first_news': first_news,
        'three_news': three_news,
    })


def all_news(request):
    all_news = New.objects.all()
    return render(request, 'all-news.html', {
        'all_news': all_news
    })


def detail(request, id):
    news = New.objects.get(id=id)
    category = Category.objects.get(id=news.category.id)
    rel_news = New.objects.filter(category=category).exclude(id=id)
    context = {'news': news,
               'category': category,
               'rel_news': rel_news}
    return render(request, 'detail.html', context)


def all_category(request):
    cats = Category.objects.all()
    return render(request, 'category.html', {
        'cats': cats
    })


def category(request, id):
    category = Category.objects.get(id=id)
    news = New.objects.filter(category=category)
    return render(request, 'category-news.html', {
        'all_news': news,
        'category': category
    })

def all_region(request):
    regs = Region.objects.all()
    return render(request, 'region.html', {
        'regs': regs
    })
def region(request, pk):
    region = Region.objects.get(id=pk)
    regs = New.objects.filter(region=region)
    return render(request, 'region-news.html', {
        'all_regs' :regs,
        'region':region
    })
class Create_post(CreateView):
    model = New
    template_name = 'create-post.html'
    fields = ['category', 'region', 'title', 'text', 'image', 'author']

class Edit_post(UpdateView):
    model = New
    template_name = 'edit-post.html'
    fields = ['category', 'region', 'title', 'text']

class Delete_post(DeleteView):
    model = New
    template_name = 'delete-post.html'
    success_url = reverse_lazy('home')