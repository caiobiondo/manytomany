from django.conf.urls import url, include
from .views import FluxoViewSet, calculaRarocViewSet
from rest_framework.routers import DefaultRouter

router = DefaultRouter()
router.register("calculararoc",calculaRarocViewSet, basename="calculararoc")
router.register("fluxo", FluxoViewSet, basename="fluxo")

urlpatterns = [
    url('', include(router.urls))


]
