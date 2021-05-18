from django.urls import path
#from .views import kategorie_list, restauracja_kategorie_detail
from  .views import RestauracjaKategorieList, RestauracjaKategorieDetail, DaniaList, DaniaDetail
from . import views
# urlpatterns = [
#     path('restauracja-kategorie', kategorie_list),
#     path('restauracja-kategorie/<int:pk>', restauracja_kategorie_detail),
# ]

urlpatterns = [
     path('kategorie', views.RestauracjaKategorieList.as_view(), name = RestauracjaKategorieList.view_name),
     path('kategorie/<int:pk>', views.RestauracjaKategorieDetail.as_view(), name = RestauracjaKategorieDetail.view_name),
     path('dania', views.DaniaList.as_view(), name = DaniaList.view_name),
     path('dania/<int:pk>', views.DaniaDetail.as_view(), name = DaniaDetail.view_name),
     path('', views.ApiRoot.as_view(), name=views.ApiRoot.view_name)

]