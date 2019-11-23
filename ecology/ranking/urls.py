from django.urls import path,include
from django.contrib import admin
from django.conf.urls.static import static
from django.conf import settings
admin.autodiscover()

from .views import main_method,render_survey


urlpatterns = [
    path('',main_method,name="main_method"),
    path('survey/',render_survey,name="survey"),
]