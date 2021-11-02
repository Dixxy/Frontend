from django.urls import path

from pages.views import HomeView, AboutView, ContactView, TravelView, DestinationView, BlogView, ElementView, \
    SingleBlogView

app_name = 'pages'

urlpatterns = [
    path('', HomeView.as_view(), name='home'),
    path('about/', AboutView.as_view(), name='about'),
    path('contact/', ContactView.as_view(), name='contact'),
    path('travel/', TravelView.as_view(), name='travel'),
    path('destination/', DestinationView.as_view(), name='destination'),
    path('blog/', BlogView.as_view(), name='blog'),
    path('element/', ElementView.as_view(), name='element'),
    path('single/', SingleBlogView.as_view(), name='single')
]

