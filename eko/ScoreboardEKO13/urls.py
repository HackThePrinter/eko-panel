from django.conf.urls import url
from django.views.generic import TemplateView

from . import views

urlpatterns = [
    url(r'^$', views.index, name='index'),
    url(r'^rules/$', TemplateView.as_view(template_name='ScoreboardEKO13/rules.html'), name='rules'),
]
