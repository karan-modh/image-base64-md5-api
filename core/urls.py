from django.urls import path
from .views import *

urlpatterns = [
    path('api', FileUploadView.as_view(), name='api'),
    path('', FormDisplayView.as_view())
]
