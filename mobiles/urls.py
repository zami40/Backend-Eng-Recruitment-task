from django.urls import path
from .views import MobileList, MobileDetail, MobileCreate, MobileDelete, MobileUpdate, MobileSearch

urlpatterns = [
    path ('',MobileList.as_view(), name='mobiles'),
    path ('mobile/<int:pk>/', MobileDetail.as_view(), name='mobile'),
    path ('mobile-create/', MobileCreate.as_view(), name='mobile-create'),
    path ('mobile-update/<int:pk>/', MobileUpdate.as_view(), name='mobile-update'),
    path ('mobile-delete/<int:pk>/', MobileDelete.as_view(), name='mobile-delete'),
    path ('mobile-search/', MobileSearch.as_view(), name='mobile-search'),

]