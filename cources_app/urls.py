from django.urls import path     
from . import views
urlpatterns = [ path('', views.index),
               path('form', views.index, name='cources'),
               path('cources/destroy/<int:id>', views.destroy,name='destroy'),
               path('delete/<int:id>', views.delete,name='delete'),
                   
                     ]
