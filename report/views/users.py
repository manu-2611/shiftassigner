from rest_framework.generics import ListCreateAPIView, RetrieveUpdateDestroyAPIView
from rest_framework.permissions import AllowAny, IsAuthenticated
from report.models import User
from report.serializers.user import UserSerializer


class CreateUserView(ListCreateAPIView):
    
    queryset = User.objects.all()
    serializer_class = UserSerializer
    permission_classes = (AllowAny,)


class RetrieveUpdateDestroyUserView(RetrieveUpdateDestroyAPIView):

    queryset = User.objects.all()
    lookup_field = "pk"
    serializer_class = UserSerializer
    permission_classes = (IsAuthenticated, )

