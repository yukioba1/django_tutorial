from django.urls import path
from . import views

app_name = "numapp"

urlpatterns = [
    path('inputNum/', views.input_num),
    path('printMsg/', views.print_msg),
    path('greet/<int:pk>', views.greeting),
]
