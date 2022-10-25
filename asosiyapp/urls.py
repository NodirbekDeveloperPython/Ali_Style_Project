from django.urls import path
from .views import *
from userapp.views import *
urlpatterns = [
    path('', HomeView.as_view(), name='home'),
    path('bolimlar/', BolimlarView.as_view(), name='bolimlar'),
    path('bolim/<str:nom>/', BolimIchkiView.as_view(), name='bolim_ichki'),
    path('grid/', GridView.as_view(), name='grid_view'),
    path('page_product/', PageProductView.as_view(), name='page_product'),

    path('login/', LoginView.as_view(), name='login'),
    path('logout/', LogoutView.as_view(), name='logout'),

    path('ichki/<int:pk>/', IchkiView.as_view(), name='ichki-mahsulotlar'),
    path('mahsulot/<int:pk>/', MahsulotView.as_view(), name='mahsulot'),
    path('mahsulot/tanlangan/', TanlanganView.as_view()),
    path('mahsulot/savat/', SavatView.as_view()),
    path('mahsulot/buyurtma/', BuyurtmaView.as_view()),
    path('mahsulot/register/', RegisterView.as_view()),
]