from django.contrib.auth import authenticate
from django_filters.rest_framework import DjangoFilterBackend
from rest_framework.parsers import MultiPartParser
from rest_framework.permissions import IsAuthenticatedOrReadOnly
from rest_framework.response import Response
from rest_framework.viewsets import ModelViewSet

from .models import Sponsor, Users, Student
from .serializer import LoginModelSerializer, SponsorModelSerializer, SponsorUpdateSerializer
from .permision import IsSuperuser
from .serializer import StudentModelSerializer


# Create your views here.

class LoginView(ModelViewSet):
    queryset = Users.objects.all()
    serializer_class = LoginModelSerializer
    parser_classes = [MultiPartParser, ]

    def perform_create(self, serializer):
        instance = serializer.save()
        instance.set_password(instance.password)
        instance.save()

    # def create(self, request, *args, **kwargs):
    #
    #     username = request.data.get("username")
    #     password = request.data.get("password")
    #     user = authenticate(username=username, password=password)
    #     if user:
    #         refresh = RefreshToken.for_user(user)
    #         return Response({"refresh": str(refresh), "access": str(refresh.access_token)})  # noqa
    #     else:
    #         return Response({"error": "Invalid credentials"}, status=status.HTTP_401_UNAUTHORIZED)


#     # fields = '__all__'
# class LoginView(CreateAPIView):
#     queryset = Login.objects.all()
#     serializer_class = LoginModelSerializer
#     permission_classes = [AllowAny]
#
#     def create(self, request, *args, **kwargs):
#         username = request.data.get("username")
#         password = request.data.get("password")
#         user = authenticate(username=username, password=password)
#         if user:
#             refresh = RefreshToken.for_user(user)
#             return Response({"refresh": str(refresh), "access": str(refresh.access_token)})  # noqa
#         else:
#             return Response({"error": "Invalid credentials"}, status=status.HTTP_401_UNAUTHORIZED)


class SponsorModelViewSet(ModelViewSet):
    queryset = Sponsor.objects.all()
    serializer_class = SponsorModelSerializer
    parser_classes = [MultiPartParser, ]
    filter_backends = [DjangoFilterBackend]
    filterset_fields = ['ariza', 'summa', 'created_at']
    http_method_names = ['get', 'post']


class StudentModelViewSet(ModelViewSet):
    permission_classes = (IsSuperuser,)
    queryset = Student.objects.all()
    serializer_class = StudentModelSerializer
    parser_classes = [MultiPartParser, ]
    filter_backends = [DjangoFilterBackend]
    filterset_fields = ['student_category', 'otm']
    http_method_names = ['get']


class SponsorModelUpdateViewSet(ModelViewSet):
    serializer_class = SponsorUpdateSerializer
    parser_classes = [MultiPartParser, ]
    http_method_names = ['get', 'post']
    permission_classes = (IsAuthenticatedOrReadOnly,)

    def put(self, request, *args, **kwargs):
        instance = self.get_object()
        serializer = self.get_serializer(instance, data=request.data)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        return Response(serializer.data)

    def get_queryset(self):
        queryset = Sponsor.objects.filter(user_id=self.request.user_id)
        return queryset
