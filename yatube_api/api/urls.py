from django.urls import include, path
from rest_framework import routers
from rest_framework.authtoken import views

from .views import CommentViewSet, GroupViewSet, PostViewSet, UserViewSet

app_name = "posts"

router = routers.DefaultRouter()
router.register(r"posts", PostViewSet)
router.register(r"groups", GroupViewSet)
router.register(r"groups", GroupViewSet)
### api/v1/posts/{post_id}/comments/
### api/v1/posts/{post_id}/comments/{comment_id}/

urlpatterns = [
    path("", include(router.urls)),
    path("api-token-auth/", views.obtain_auth_token),
]
