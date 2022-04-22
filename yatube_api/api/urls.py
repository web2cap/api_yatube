from django.urls import include, path
from rest_framework import routers
from rest_framework.authtoken import views

from .views import CommentViewSet, GroupViewSet, PostViewSet, UserViewSet

app_name = "posts"

router = routers.DefaultRouter()
router.register(r"posts", PostViewSet, basename="posts")
router.register(r"groups", GroupViewSet, basename="groups")
router.register(r"users", UserViewSet, basename="users")
router.register(
    r"posts/(?P<post_id>[^/.]+)/comments", CommentViewSet, basename="comments"
)

urlpatterns = [
    path("v1/", include(router.urls)),
    path("v1/api-token-auth/", views.obtain_auth_token, name="auth_token"),
]
