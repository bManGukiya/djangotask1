# your_app_name/urls.py
from django.urls import path,include
from .views import Imageview
from rest_framework import routers

# router = routers.DefaultRouter()
# router.register('Image',views.Imageview)

urlpatterns = [
    path("images/",Imageview.as_view(),),
]
