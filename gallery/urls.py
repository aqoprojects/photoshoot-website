from django.urls import path
from django.views.generic import TemplateView
from .views import homePage, aboutPage, servicesPage, portfolioPage

app_name = 'gallery'

urlpatterns = [
    path('', homePage.as_view(), name='home'),
    path('about/', aboutPage.as_view(), name="about"),
    path('services/', servicesPage.as_view(), name="services"),
    path('portfolio/', portfolioPage.as_view(), name="portfolio"),
]