from django.urls import path, include
from webapps import views
from webapps.views import router
from webapps.models import ConnectedUsers


urlpatterns = [
    path('register', views.AccountCreate.as_view()),
    path('', include(router.urls)),
    path('online/', views.users_online),
    path('room/', views.index, name='index'),
    path('room/<str:article_id>/', views.room, name='article_id'),
]

ConnectedUsers.objects.all().delete()
