from django.urls import path
from django import urls
from .views import EnchereDetail, EnchereList

urlpatterns = [
    path('encheres/', EnchereList.as_view(), name='Encheres'),
    path('enchere/<int:pk>', EnchereDetail.as_view(), name='Enchere')
]