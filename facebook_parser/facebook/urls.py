from django.urls import path
from .views import UploadFileView

urlpatterns = [
    path('facebook_form/', UploadFileView.as_view(), name='facebook')
]