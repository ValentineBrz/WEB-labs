from webapps.serializers import *
from webapps.models import *
from rest_framework import viewsets, permissions, generics, routers
from .permissions import IsAdminOrReadOnly


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

