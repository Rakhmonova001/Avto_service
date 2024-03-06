from django.urls import path
from .views import *

urlpatterns = [
    path('login-user/', login_user_view),
    path('signup/', singup_user_view),
    path('logout-user/', logout_user_view),
    path('edit-user/<int:pk>/', edit_user_view),
    path('delete-user/<int:pk>/', delete_user_view),
]