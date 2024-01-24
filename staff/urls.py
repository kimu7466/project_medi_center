from django.urls import path
from .views import *

urlpatterns = [
    path('', login_view, name='login_view'),
    path('signup_view', signup_view, name='signup_view'),
    path('forgot_password_view/', forgot_password_view, name='forgot_password_view'),
    path('otp_verify_view/', otp_verify_view, name='otp_verify_view'),
    path('resend_otp_view/', resend_otp_view, name='resend_otp_view'),
    path('logout/', logout, name='logout')
]
