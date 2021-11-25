from django.urls import include, path
from rest_framework.authtoken import views
from rest_framework.routers import SimpleRouter

from .views import CommentViewSet, GroupViewSet, PostViewSet

router = SimpleRouter()

router.register(r'api/v1/posts', PostViewSet)
router.register(r'api/v1/groups', GroupViewSet)
router.register(
    r'api/v1/posts/(?P<pk>\d+)/comments', 
    CommentViewSet,
    basename='comments'
)

urlpatterns = [
    path('api/v1/api-token-auth/', views.obtain_auth_token),
    path('', include(router.urls)),
]

#urlpatterns = [
    #path('api/v1/api-token-auth/', views.obtain_auth_token),
    #path('api/v1/posts/', api_posts),
    #path('api/v1/posts/<int:pk>/', api_posts_detail),
    #path('api/v1/groups/', #api_posts_detail),
    #path('api/v1/groups/<int:pk>/', #api_posts_detail),
    #path('api/v1/posts/<int:pk>/comments/', #api_posts_detail),
    #path('api/v1/posts/<int:pk>/comments/<int:pk>/', #api_posts_detail),
#]
