from django.urls import path, include
from webapps import views
from webapps.views import router


urlpatterns = [
    path('register', views.AccountCreate.as_view()),
    path('', include(router.urls)),

]
