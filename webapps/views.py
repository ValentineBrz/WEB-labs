from webapps.serializers import *
from webapps.models import *
from rest_framework import viewsets, permissions, generics, routers
from .permissions import IsAdminOrReadOnly
from django.http import HttpResponse
from django.shortcuts import render


def index(request):
    articles = [user for user in Article.objects.all()]
    return render(request, 'index.html', {
        'articles': articles
    })


def room(request, article_id):
    # Send article by id to user
    article = Article.objects.get(id=article_id)
    comments = [c for c in Comment.objects.filter(article_id=article_id)]
    if article:
        return render(request, 'room.html', {
            'article_id': article_id,
            'comments': comments,
            'article': article
        })
    else:
        return HttpResponse('Wrong Article id')


def users_online(request):
    if request.user.is_authenticated:
        connected_users = [user for user in ConnectedUsers.objects.all()]
        return render(request, 'online.html', {
            'connected_users': connected_users
        })


class AccountViewSet(viewsets.ModelViewSet):
    queryset = Account.objects.all()
    serializer_class = AccountSerializer
    permission_classes = [IsAdminOrReadOnly]


class AccountCreate(generics.CreateAPIView):
    queryset = Account.objects.all()
    serializer_class = AccountCreateSerializer
    permission_classes = [permissions.AllowAny]


class ArticleViewSet(viewsets.ModelViewSet):
    queryset = Article.objects.all()
    serializer_class = ArticleSerializer
    permission_classes = [permissions.IsAuthenticatedOrReadOnly]


class CommentViewSet(viewsets.ModelViewSet):
    queryset = Comment.objects.all()
    serializer_class = CommentSerializer
    permission_classes = [permissions.IsAuthenticatedOrReadOnly]


router = routers.DefaultRouter()
router.register(r'article', ArticleViewSet)
router.register(r'comment', CommentViewSet)
router.register(r'account', AccountViewSet)

