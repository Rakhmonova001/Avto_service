from django.shortcuts import render
from rest_framework.generics import ListAPIView, ListCreateAPIView, UpdateAPIView, DestroyAPIView
from main.models import *
from main.serializers import *


""" start CRUD Employee model """
#read_employee_object
class GetAllEmployeeItems(ListAPIView):
    queryset = Employee.objects.all().order_by('-id')
    serializer_class = EmployeeSer


#create_employee_object
class CreateEmployeeApiView(ListCreateAPIView):
    queryset = Employee.objects.all()
    serializer_class = EmployeeSer


#update_employee_object
class UpdateEmployeeApiView(UpdateAPIView):
    queryset = Employee.objects.all()
    serializer_class = EmployeeSer


#delete_employee_objects
class DeleteEmployeeApiView(DestroyAPIView):
    queryset = Employee.objects.all()
    serializer_class = EmployeeSer


""" start CRUD Cassa model """
#read_cassa_objects
class GetAllCassaItems(ListAPIView):
    queryset = Cassa.objects.all().order_by('-id')
    serializer_class = CassaSer


#create_cassa_objects
class CreateCassaApiView(ListCreateAPIView):
    queryset = Cassa.objects.all()
    serializer_class = CassaSer


#update_cassa_objects
class UpdateCassaApiView(UpdateAPIView):
    queryset = Cassa.objects.all()
    serializer_class = CassaSer


#delete_cassa_objects
class DeleteCassaApiView(DestroyAPIView):
    queryset = Cassa.objects.all()
    serializer_class = CassaSer


""" start  CRUD Order model """
#read_order_objects
class GetAllOrderItems(ListAPIView):
    queryset = Order.objects.all()
    serializer_class = OrderSer


#create_order_objects
class CreateOrderApiView(ListCreateAPIView):
    queryset = Order.objects.all()
    serializer_class = OrderSer


#update_order_objects
class UpdateOrderApiView(UpdateAPIView):
    queryset = Order.objects.all()
    serializer_class = OrderSer


#delete_order_objects
class DeleteOrderApiView(DestroyAPIView):
    queryset = Order.objects.all()
    serializer_class = OrderSer


""" start CRUD Payment model """
#read_payment_objects
class GetAllPaymentItems(ListAPIView):
    queryset = Payment.objects.all().order_by('-id')
    serializer_class = PaymentSer


#create_payment_objects
class CreatePaymentApiView(ListCreateAPIView):
    queryset = Payment.objects.all()
    serializer_class = PaymentSer


#update_payment_objects
class UpdatePaymentApiView(UpdateAPIView):
    queryset = Payment.objects.all()
    serializer_class = PaymentSer


#delete_payment_objects
class DeletePaymentApiVew(DestroyAPIView):
    queryset = Payment.objects.all()
    serializer_class = PaymentSer


""" start CRUD Garage model """
#read_garage_objects
class GetAllGarageItems(ListAPIView):
    queryset = Garage.objects.all()
    serializer_class = GarageSer


#create_garage_objects
class CreateGarageApiView(ListCreateAPIView):
    queryset = Garage.objects.all()
    serializer_class = GarageSer


#update_garage_objects
class UpdateGarageApiView(UpdateAPIView):
    queryset = Garage.objects.all()
    serializer_class = GarageSer


#delete_garage_objects
class DeleteGarageApiView(DestroyAPIView):
    queryset = Garage.objects.all()
    serializer_class = GarageSer


""" start CRUD Comment model """
#read_comment_objects
class GetAllCommentItems(ListAPIView):
    queryset = Comment.objects.all().order_by('-id')
    serializer_class = CommentSer


#create_comment_objects
class CreateCommentApiView(ListCreateAPIView):
    queryset = Comment.objects.all()
    serializer_class = CommentSer


#update_comment_objects
class UpdateCommentApiView(UpdateAPIView):
    queryset = Comment.objects.all()
    serializer_class = CommentSer


#delete_comment_objects
class DeleteCommentApiView(DestroyAPIView):
    queryset = Comment.objects.all()
    serializer_class = CommentSer


""" start CRUD Attendance model """
#read_attendance_objects
class GetAllAttendanceItems(ListAPIView):
    queryset = Attendance.objects.all().order_by('-id')
    serializer_class = AttendanceSer


#create_attendance_objects
class CreateAttendanceApiView(ListCreateAPIView):
    queryset = Attendance.objects.all()
    serializer_class = AttendanceSer


#update_attendance_objects
class UpdateAttendanceApiView(UpdateAPIView):
    queryset = Attendance.objects.all()
    serializer_class = AttendanceSer


#delete_attendance_objects
class DeleteAttendanceApiView(DestroyAPIView):
    queryset = Attendance.objects.all()
    serializer_class = AttendanceSer
