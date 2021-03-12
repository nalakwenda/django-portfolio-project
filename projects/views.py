from django.shortcuts import render
from django.core.paginator import Paginator, PageNotAnInteger, EmptyPage

# Create your views here.
from django.shortcuts import render

from .models import Project


def pagination(posts,request):
    page = request.GET.get('page', 1)

    paginator = Paginator(posts, 3)
    try:
        entries = paginator.page(page)
    except PageNotAnInteger:
        entries = paginator.page(1)
    except EmptyPage:
        entries = paginator.page(paginator.num_pages)
    return entries

def project_index(request):

    projects = Project.objects.all()

    context = {

        'projects': projects

    }

    return render(request, 'project_index.html', context)

def project_detail(request, slug):

    project = Project.objects.get(slug=slug)

    context = {

        'project': project

    }

    return render(request, 'project_detail.html', context)
def project_category(request, category):

    posts = Project.objects.filter(categories__name__contains=category).order_by(
        "-created_on"
    )
    context = {"category": category, "entries":pagination(posts,request)  }
    return render(request, "project_list.html", context)

def project_list(request):
    
    posts = Project.objects.all().order_by(
        "-created_on"
    )
    context = { "entries":pagination(posts,request)}
    return render(request, "project_list.html", context)

def project_tag(request, tag):
    
    posts = Project.objects.filter(technology__slug=tag).order_by(
        "-created_on"
    )

    context = {"tag": tag, "entries": pagination(posts,request) }
    return render(request, "project_list.html",context)
