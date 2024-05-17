from django.views.generic import ListView

from .models import Post


# Create your views here.

# Home View
class HomePageView(ListView):
    model = Post
    template_name = "home.html"
