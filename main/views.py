from django.shortcuts import render
from .models import *
from rest_framework.decorators import api_view
from rest_framework.response import Response
from .serializers import *


"""  Start EMPLOYEE model  """
@api_view(['GET'])
def filter_employee_username(request):
    username = request.GET.get('username')
    users = Employee.objects.filter(user__icontains=username).order_by('-id')
    ser = EmployeeSer(users, many=True)
    return Response(ser.data)

@api_view(['GET'])
def filter_emoloyee_experience(request):
    experience = request.GET.get('experience')
    users = Employee.objects.filter(experience__icontains=experience).order_by('-id')
    ser = EmployeeSer(users, many=True)
    return Response(ser.data)

@api_view(['GET'])
def filter_emoloyee_salary(request):
    salary = request.GET.get('salary')
    users = Employee.objects.filter(salary__icontains=salary).order_by('-id')
    ser = EmployeeSer(users, many=True)
    return Response(ser.data)

@api_view(['GET'])
def filter_employee_garage(request):
    garage_id = request.GET.get('room_id')
    users = Garage.objects.filter(garage_id=garage_id).order_by('-id')
    ser = GarageSer(users, many=True)
    return Response(ser.data)



"""  Start ORDER model  """
@api_view(['GET'])
def filter_order_name(request):
    owner_name = request.GET.get('owner_name')
    users = Order.objects.filter(owner_name=owner_name).order_by('-id')
    ser = OrderSer(users, many=True)
    return Response(ser.data)


@api_view(['GET'])
def filter_order_is_delivery(request):
    is_delivery = request.GET.get('is_delivery')
    users = Order.objects.filter(is_delivery=is_delivery).order_by('-id')
    ser = OrderSer(users, many=True)
    return Response(ser.data)


@api_view(['GET'])
def filter_order_car_name(request):
    car_name = request.GET.get('car_name')
    users = Order.objects.filter(car_name=car_name).order_by('-id')
    ser = OrderSer(users, many=True)
    return Response(ser.data)


@api_view(['GET'])
def filter_order_car_number(request):
    car_number = request.GET.get('car_number')
    users = Order.objects.filter(car_number=car_number).order_by('-id')
    ser = OrderSer(users, many=True)
    return Response(ser.data)


@api_view(['GET'])
def filter_order_owner_phone_number(request):
    owner_phone_number = request.GET.get('owner_phone_number')
    users = Order.objects.filter(owner_phone_number=owner_phone_number).order_by('-id')
    ser = OrderSer(users, many=True)
    return Response(ser.data)


@api_view(['GET'])
def filter_order_master_employee(request):
    master_employee_id = request.GET.get('master_employee_id')
    users = Order.objects.filter(master_employee_id=master_employee_id).order_by('-id')
    ser = OrderSer(users, many=True)
    return Response(ser.data)


@api_view(['GET'])
def filter_order_service_cost(request):
    service_cost = request.GET.get('service_cost')
    users = Order.objects.filter(service_cost=service_cost).order_by('-id')
    ser = OrderSer(users, many=True)
    return Response(ser.data)


""" start PAYMENT model """

@api_view(['GET'])
def filter_payment_admin(request):
    admin_id = request.GET.get('admin_id')
    users = Payment.objects.filter(admin_id=admin_id).order_by('-id')
    ser = PaymentSer(users, many=True)
    return Response(ser.data)


@api_view(['GET'])
def filter_payment_order(request):
    order_id = request.GET.get('order_id')
    users = Payment.objects.filter(order_id=order_id).order_by('-id')
    ser = PaymentSer(users, many=True)
    return Response(ser.data)


@api_view(['GET'])
def filter_payment_code(request):
    code = Payment.GET.get('code')
    users = Payment.objects.filter(code=code).order_by('code')
    ser = PaymentSer(users, many=True)
    return Response(ser.data)


@api_view(['GET'])
def filter_payment_date(request):
    date = Payment.GET.get('date')
    users = Payment.objects.filter(date=date).order_by('date')
    ser = PaymentSer(users, many=True)
    return Response(ser.data)


@api_view(['GET'])
def filter_payment_by_payment_type(request):
    payment_type = Payment.GET.get('payment_type')
    users = Payment.objects.filter(payment_type=payment_type).order_by('payment_type')
    ser = PaymentSer(users, many=True)
    return Response(ser.data)


@api_view(['GET'])
def filter_payment_by_payment_status(request):
    payment_status = Payment.GET.get('payment_status')
    users = Payment.objects.filter(payment_status=payment_status).order_by('payment_status')
    ser = PaymentSer(users, many=True)
    return Response(ser.data)


""" start GARAGE model"""

@api_view(['GET'])
def filter_garage_number(request):
    number = Garage.GET.get('number')
    users = GarageSer.objects.filter(number=number).order_by('number')
    ser = GarageSer(users, many=True)
    return Response(ser.data)


""" start COMMENT model """

@api_view(['GET'])
def filter_comment_order(request):
    order_id = request.GET.get('order_id')
    users = Comment.objects.filter(order_id=order_id).order_by('order_id')
    ser = CommentSer(users, many=True)
    return Response(ser.data)


@api_view(['GET'])
def filter_comment_status(request):
    status = request.GET.get('status')
    users = Comment.objects.filter(status=status).order_by('status')
    ser = CommentSer(users, many=True)
    return Response(ser.data)


@api_view(['GET'])
def filter_comment_created_at(request):
    created_at = request.GET.get('created_at')
    created_at = request.GET.get('')
    users = Comment.objects.filter(created_at=created_at).order_by('created')
    ser = CommentSer(users, many=True)
    return Response(ser.data)


"""  Start ATTENDANCE model  """
@api_view(['GET'])
def filter_attendence_employee(request):
    employee_id = request.GET.get('employee_id')
    users = Attendence.objects.filter(employee_id=employee_id).order_by('-id')
    ser = AttendenceSer(users, many=True)
    return Response(ser.data)


@api_view(['GET'])
def filter_attendence_date(request):
    date = request.GET.get('date')
    users = Attendence.objects.filter(date=date).order_by('-id')
    ser = AttendenceSer(users, many=True)
    return Response(ser.data)
