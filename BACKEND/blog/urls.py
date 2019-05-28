from django.urls import path
from rest_framework.routers import DefaultRouter
from . import views

router = DefaultRouter()
router.register('list', views.ListViewSet)

urlpatterns = [
    # path('', views.PostList.as_view()),
    path('<int:pk>/', views.PostDetail.as_view()),
]

urlpatterns += router.urls
