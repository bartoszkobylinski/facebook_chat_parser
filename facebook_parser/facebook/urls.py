from django.urls import path
from .views import UploadFileView, ChartView, DeleteFaceView

urlpatterns = [
    path("", UploadFileView.as_view(), name="index"),
    path("index", ChartView.as_view(), name="facebook"),
    path("delete", DeleteFaceView.as_view(), name="delete"),
]
