from django.urls import path
from .views import BookListView

app_name = 'Books'

urlpatterns = [
    path('', BookListView.as_view(template_name='Books/index.html')),
]
