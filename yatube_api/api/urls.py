from django.urls import include, path
from rest_framework.authtoken import views
from rest_framework.routers import SimpleRouter

from .views import CommentViewSet, GroupViewSet, PostViewSet

router_1 = SimpleRouter()

router_1.register(r'v1/posts', PostViewSet, basename='post')
router_1.register(r'v1/groups', GroupViewSet, basename='group')
router_1.register(
    r'v1/posts/(?P<post_id>\d+)/comments',
    CommentViewSet,
    basename='comment'
)

urlpatterns = [
    path('v1/api-token-auth/', views.obtain_auth_token),
    path('', include(router_1.urls)),
]
