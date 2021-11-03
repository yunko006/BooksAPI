from django.urls import path
from .views import BookListCreate

app_name = 'books_api'

urlpatterns = [
    path('', BookListCreate.as_view(), name='listcreate'),

]
