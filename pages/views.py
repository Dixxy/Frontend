from django.views.generic import TemplateView


class HomeView(TemplateView):
    template_name = 'index.html'


class AboutView(TemplateView):
    template_name = 'about.html'


class ContactView(TemplateView):
    template_name = 'contact.html'


class TravelView(TemplateView):
    template_name = 'travel_destination.html'


class DestinationView(TemplateView):
    template_name = 'destination_details.html'


class BlogView(TemplateView):
    template_name = 'blog.html'


class ElementView(TemplateView):
    template_name = 'elements.html'


class SingleBlogView(TemplateView):
    template_name = 'single-blog.html'
