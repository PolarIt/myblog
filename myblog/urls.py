from django.conf.urls import patterns, include, url
from rest_framework.routers import DefaultRouter
from blog import views

router = DefaultRouter()
router.register(r'post', views.PostViewSet)
router.register(r'category', views.CategoryViewSet)


urlpatterns = patterns('',
    url(r'^', include(router.urls)),
    url(r'^api-auth/', include('rest_framework.urls', namespace='rest_framework')),
)
