from django.urls import path
from .views import *


urlpatterns = [
    #>>>>>>>>>>>>>>>>> CRUD urls Employee Items <<<<<<<<<<<<< #
    path('get-employee-items/', GetAllEmployeeItems.as_view()),
    path('create-employee/', CreateEmployeeApiView.as_view()),
    path('update-employee/', UpdateEmployeeApiView.as_view()),
    path('delete-employee/', DeleteEmployeeApiView.as_view()),


    #>>>>>>>>>>>>> CRUD urls Cassa Items <<<<<<<<<<<<< #
    path('get-cassa-items/', GetAllCassaItems.as_view()),
    path('create-cassa/', CreateCassaApiView.as_view()),
    path('update-cassa/', UpdateCassaApiView.as_view()),
    path('delete-cassa/', DeleteCassaApiView.as_view()),


    # >>>>>>>>>>>>>>> CRUD urls Order Items <<<<<<<<<<<<<<< #
    path('get-order-items/', GetAllOrderItems.as_view()),
    path('create-order/', CreateOrderApiView.as_view()),
    path('update-order/', UpdateOrderApiView.as_view()),
    path('delete-order/', DeleteOrderApiView.as_view()),


    # >>>>>>>>>>>>>>> CRUD urls Payment Items <<<<<<<<<<<< #
    path('get-payment-items/', GetAllPaymentItems.as_view()),
    path('create-payment/', CreatePaymentApiView.as_view()),
    path('update-payment/', UpdatePaymentApiView.as_view()),
    path('delete-payment/', DeletePaymentApiVew.as_view()),


    # >>>>>>>>>>>>>> CRUD urls Garage Items <<<<<<<<<<<<<< #
    path('get-garage-items/', GetAllGarageItems.as_view()),
    path('create-garage/', CreatePaymentApiView.as_view()),
    path('update-garage/', UpdateGarageApiView.as_view()),
    path('delete-garage/', DeleteGarageApiView.as_view()),


    # >>>>>>>>>>>>>> CRUD urls Comment Items <<<<<<<<<<<< #
    path('get-comment-items/', GetAllCommentItems.as_view()),
    path('create-comment/', CreateCommentApiView.as_view()),
    path('update-comment/', UpdateCommentApiView.as_view()),
    path('delete-comment/', DeleteCommentApiView.as_view()),


    # >>>>>>>>>>>> CRUD urls Attendance Items <<<<<<<<<<<< #
    path('get-attendance-items/', GetAllAttendanceItems.as_view()),
    path('create-attendance/', CreateAttendanceApiView.as_view()),
    path('update-attendance/', UpdateAttendanceApiView.as_view()),
    path('delete-comment/', DeleteAttendanceApiView.as_view()),
]