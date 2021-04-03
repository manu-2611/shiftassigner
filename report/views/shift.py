from rest_framework.generics import CreateAPIView, RetrieveUpdateDestroyAPIView
from rest_framework.permissions import AllowAny, IsAuthenticated
from report.models import Shift
from report.serializers.shift import ShiftSerializer


class CreateShiftView(CreateAPIView):
    
        
    queryset = Shift.objects.all()
    serializer_class = ShiftSerializer
    permission_classes = (IsAuthenticated,)

    def get_serializer_context(self):
        return {"view":self}




class RetrieveUpdateDestroyShiftrView(RetrieveUpdateDestroyAPIView):

    queryset = Shift.objects.all()
    lookup_field = "pk"
    serializer_class = ShiftSerializer
    permission_classes = (IsAuthenticated, )

    def get_serializer_context(self):
        return {"view":self}

