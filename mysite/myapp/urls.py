from django.conf.urls import include, url
from . import views
# Create your views here.

urlpatterns = [
    url(r'^$', views.index, name='index'),
    url(r'^about', views.about, name='about'),
    url(r'^contact', views.contact, name='contact'),
    url(r'^services', views.services, name='services'),
    url(r'^faq', views.faq, name='faq'),
    url(r'^portfolio', views.portfolio, name='portfolio'),
    url(r'^pricing', views.pricing, name='pricing'),
    url(r'^index', views.index, name='index'),

]