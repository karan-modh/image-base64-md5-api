from django.urls import path
from .views import *

urlpatterns = [
    path('post', FileUploadView.as_view()),
    path('', FormDisplayView.as_view())
]
