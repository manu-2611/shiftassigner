from rest_framework.generics import CreateAPIView, RetrieveUpdateDestroyAPIView
from rest_framework.permissions import AllowAny, IsAuthenticated
from report.models import User
from report.serializers.profile import SingInProfileSerializers


class CreateProfileView(CreateAPIView):
    
    serializer_class = SingInProfileSerializers
    permission_classes = (AllowAny,)

    def get_serializer_context(self):
        return {"view": self}


class RetrieveUpdateDestroyUserView(RetrieveUpdateDestroyAPIView):

    queryset = User.objects.all()
    lookup_field = "pk"
    serializer_class = SingInProfileSerializers
    permission_classes = (IsAuthenticated, )

