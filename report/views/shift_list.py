from rest_framework.generics import ListAPIView
from rest_framework.permissions import AllowAny, IsAuthenticated
from report.models import Shift
from report.serializers.shift_list import ShiftListSerializer


class ListShiftView(ListAPIView):
    
        
    queryset = Shift.objects.all()
    serializer_class = ShiftListSerializer
    permission_classes = (IsAuthenticated,)

    def get_serializer_context(self):
        return {"view":self}


