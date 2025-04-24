from django.shortcuts import render
from django.views.generic import ListView, DetailView, View
from .models import Photo,Service, Review, Pricing

class homePage(ListView):
    template_name = 'index.html'
    model = Photo
    context_object_name = 'gallery'

    def get_context_data(self, *args, **kwargs):
        context = super().get_context_data(**kwargs)
        context['services'] = Service.objects.all()
        context['reviews'] = Review.objects.all()
        context['plans'] = Pricing.objects.all()
        return context

class aboutPage(View):
    template_name = 'about-us.html'

    def get(self, request, *args, **kwargs):
        services = Service.objects.all()
        reviews = Review.objects.all()
        context = {'services': services, 'reviews': reviews}
        return render(request, self.template_name, context)

class servicesPage(View):
    template_name = 'services.html'

    def get(self, request, *args, **kwargs):
        services = Service.objects.all()
        reviews = Review.objects.all()
        context = {'services': services, 'reviews': reviews}
        return render(request, self.template_name, context)

    def get_context_data(self, *args, **kwargs):
        context = super().get_context_data(**kwargs)
        context['services'] = Service.objects.all()
        context['reviews'] = Review.objects.all()
        context['plans'] = Pricing.objects.all()
        return context

class portfolioPage(ListView):
    template_name = 'portfolio.html'
    model = Photo
    context_object_name = 'gallery'

    def get_context_data(self, *args, **kwargs):
        context = super().get_context_data(**kwargs)
        context['reviews'] = Review.objects.all()
        return context

class pricingPage(View):
    template_name = 'pricing.html'

    def get(self, request, *args, **kwargs):
        price_plans = Pricing.objects.all()
        context = {'plans': price_plans}
        context['reviews'] = Review.objects.all()
        return render(request, self.template_name, context)

class supportPage(View):
    template_name = "contact-us.html"

    def get(self, request, *args, **kwargs):
        price_plans = Pricing.objects.all()
        context = {'plans': price_plans}
        context['reviews'] = Review.objects.all()
        return render(request, self.template_name, context)