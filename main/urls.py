from django.urls import path
from .views import *

urlpatterns = [
    # >>>>>>>>>>>>>>>>> FILTER Employee <<<<<<<<<<<<<<<<<<<< #
    path('filter-employee-username/', filter_employee_username),
    path('filter-emoloyee-experience/', filter_emoloyee_experience),
    path('filter-emoloyee-salary/', filter_emoloyee_salary),
    path('filter-employee-garage/', filter_employee_garage),


    # >>>>>>>>>>>>>>>>>>>>>>> FILTER Order <<<<<<<<<<<<<<<<<<<<<<<< #
    path('filter-order-name/', filter_order_name),
    path('filter-order-is-delivery/', filter_order_is_delivery),
    path('filter-order-car-name/', filter_order_car_name),
    path('filter-order-car-number/', filter_order_car_number),
    path('filter-order-owner-phone-number/', filter_order_owner_phone_number),
    path('filter-order-master-employee/', filter_order_master_employee),
    path('filter-order-service-cost/', filter_order_service_cost),


    # >>>>>>>>>>>>>>>>>>>>>>>> FILTER Payment <<<<<<<<<<<<<<<<<<<<<<<<<<<< #
    path('filter-payment-admin/', filter_payment_admin),
    path('filter-payment-order/', filter_payment_order),
    path('filter-payment-code/', filter_payment_code),
    path('filter-payment-date/', filter_payment_date),
    path('filter-payment-by-payment-type/', filter_payment_by_payment_type),
    path('filter-payment-by-payment-status/', filter_payment_by_payment_status),


    # >>>>>>>>>>>>>>>>>> FILTER Garage <<<<<<<<<<<<<<< #
    path('filter-garage-number/', filter_garage_number),


    # >>>>>>>>>>>>>>>>>>> FILTER Comment <<<<<<<<<<<<<<<<<<< #
    path('filter-comment-order/', filter_comment_order),
    path('filter-comment-status/', filter_comment_status),
    path('filter-comment-created-at/', filter_comment_created_at),


    # >>>>>>>>>>>>>>> FILTER Attendance <<<<<<<<<<<<<<<<<<<<<< #
    path('filter-attendence-employee/', filter_attendence_employee),
    path('filter-attendence-date/', filter_attendence_date),
]