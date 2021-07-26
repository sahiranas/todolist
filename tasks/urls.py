
from django.urls import path
from tasks import views

urlpatterns = [
    path('',views.home),
    path('update/<int:pk>',views.update),
    path('delete/<int:pk>',views.delete),
]
