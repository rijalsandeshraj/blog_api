from django.urls import path
from rest_framework.routers import DefaultRouter

from . import views

router = DefaultRouter()
router.register('', views.PostViewSet)

urlpatterns = [
    # path('', views.PostList.as_view()),
    path('<int:pk>/', views.PostDetail.as_view()),
    path('user-create/', views.UserCreateAPIView.as_view()),
]

urlpatterns += router.urls
