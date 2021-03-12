from django.urls import path, re_path
from . import views

urlpatterns = [
    path("", views.project_index, name="project_index"),
    path("portfolio/", views.project_list, name="project_list"),
    path("project/<slug:slug>/", views.project_detail, name="project_detail"),
    path("category/<category>/", views.project_category, name="project_category"),
    path("tag/<tag>/", views.project_tag, name="project_tag"),
]
