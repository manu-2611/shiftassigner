from django.urls import path

from report.views.users import CreateUserView,RetrieveUpdateDestroyUserView

from report.views.profile import CreateProfileView

from report.views.shift import CreateShiftView, RetrieveUpdateDestroyShiftrView

from report.views.shift_list import ListShiftView

urlpatterns = [
    path('user', CreateUserView.as_view()),
    path('user/<str:pk>', RetrieveUpdateDestroyUserView.as_view()),
    path('profile', CreateProfileView.as_view()),
    path('shift', CreateShiftView.as_view()),
    path('shift/<str:pk>', RetrieveUpdateDestroyShiftrView.as_view()),
    path('shift_list', ListShiftView.as_view()),

]