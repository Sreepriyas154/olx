"""
URL configuration for olx project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import  path
from api.views import Productsview,Productdetailview
from api.views import Reviewview,ReviewDetailview
from api.views import Productviewsetview
from api.views import Productmodelviewsetview,Reviewsmodelviewsetview,Usersview
from rest_framework.routers import DefaultRouter
router=DefaultRouter()
router.register("api/v1/products",Productviewsetview,basename="product")
router.register("api/v2/products",Productmodelviewsetview,basename="model")
router.register("api/v1/reviews",Reviewsmodelviewsetview,basename="review")
router.register("register",Usersview,basename="user")
urlpatterns = [
    path('admin/', admin.site.urls),
    path('products',Productsview.as_view()),
    path("products/<int:id>",Productdetailview.as_view()),
    path("reviews",Reviewview.as_view()),
    path("reviews/<int:id>",ReviewDetailview.as_view()),
]+router.urls
