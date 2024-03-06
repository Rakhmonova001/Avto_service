from rest_framework import serializers
from .models import *


class UserSer(serializers.ModelSerializer):
    class Meta:
        depth = 1
        model = User
        fields = ('username', 'phone_number', 'address')


class EmployeeSer(serializers.ModelSerializer):
    class Meta:
        depth = 1
        model = Employee
        fields = ('user', 'profession', 'salary', 'age', 'address', 'experience', 'work_time', 'rating', 'garage')


class CassaSer(serializers.ModelSerializer):
    class Meta:
        model = Cassa
        fields = "__all__"


class OrderSer(serializers.ModelSerializer):
    class Meta:
        depth = 1
        model = Order
        fields = ('owner_name', 'is_delivery', 'address', 'car_name', 'car_number', 'qr_code', 'owner_phone_number', 'is_active', 'master_employee', 'problem', 'service_cost', 'start_time')


class PaymentSer(serializers.ModelSerializer):
    class Meta:
        depth = 1
        model = Payment
        fields = ('admin', 'order', 'code', 'date', 'payment_type', 'payment_status', 'qr_code')


class GarageSer(serializers.ModelSerializer):
    class Meta:
        depth = 1
        model = Garage
        fields = "__all__"


class CommentSer(serializers.ModelSerializer):
    class Meta:
        depth = 1
        model = Comment
        fields = ('order', 'text', 'text', 'created_at')


class AttendanceSer(serializers.ModelSerializer):
    class Meta:
        depth = 1
        model = Attendance
        fields = ('employee', 'date', 'check_in', 'check_out')
