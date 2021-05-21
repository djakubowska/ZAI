from django.urls import path
#from .views import kategorie_list, restauracja_kategorie_detail
from  .views import RestauracjaKategorieList, RestauracjaKategorieDetail, DaniaList, DaniaDetail, ZamowieniaList, ZamowieniaDetail, PlatnoscList, PlatnoscDetail, StolikKlientList, StolikKlientDetail
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
     path('zamowienia', views.ZamowieniaList.as_view(), name=ZamowieniaList.view_name),
     path('zamowienia/<int:pk>', views.ZamowieniaDetail.as_view(), name=ZamowieniaDetail.view_name),
     path('platnosc', views.PlatnoscList.as_view(), name=PlatnoscList.view_name),
     path('platnosc/<int:pk>', views.PlatnoscDetail.as_view(), name=PlatnoscDetail.view_name),
     path('stolik_klient', views.StolikKlientList.as_view(), name=StolikKlientList.view_name),
     path('stolik_klient/<int:pk>', views.StolikKlientDetail.as_view(), name=StolikKlientDetail.view_name),
     path('', views.ApiRoot.as_view(), name=views.ApiRoot.view_name)

]