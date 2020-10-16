from django.urls import path
from .views import UploadFileView, ChartView, DeleteFaceView, FacebookDownloadView

urlpatterns = [
    path("", UploadFileView.as_view(), name="index"),
    path("index", ChartView.as_view(), name="facebook"),
    path("delete", DeleteFaceView.as_view(), name="delete"),
    path("how_to_download_facebook_messanger", FacebookDownloadView.as_view(), name="download")
]
