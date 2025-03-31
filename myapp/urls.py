from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),  # Use 'home' instead of 'predictor'
    path('predict/', views.predict_form, name='predict_form'),
    path('result/', views.formInfo, name='form_info'),
]
