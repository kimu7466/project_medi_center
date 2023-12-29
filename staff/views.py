from django.shortcuts import render, redirect
from .models import StaffRegister


def staff_authenticated(view_func):
    def wrapper(request, *args, **kwargs):
        if 'staff_id' in request.session:
            return view_func(request, *args, **kwargs)
        else:
            return redirect('login_view')  

    return wrapper

def login_view(request):
    if request.method == 'POST':
        login_id_ = request.POST['login_id']
        password_ = request.POST['password']
        try:
            print(login_id_, password_)
            get_staff = StaffRegister.objects.get(staff_id=login_id_)
            print(get_staff.email)

        except StaffRegister.DoesNotExist:
            print("Invalid staff_id or password")
        else:
            print(password_ == get_staff.password)
            if password_ == get_staff.password:
                request.session['staff_id'] = login_id_
                return redirect('dashboard_view')
                print("Now, you are logged in")
            else:
                print("Invalid staff_id or password")
    return render(request, 'login.html')

def forgot_password_view(request):
    return render(request, 'forgot-password.html')

def otp_verify_view(request):
    return render(request, 'otp-verification.html')