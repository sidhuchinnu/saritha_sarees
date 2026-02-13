from django.shortcuts import render
from adminapp.models import AdminUser
from userapp.models import Users
def all_users(request):
    return render(request, 'dashboard.html')

def admin_login_page(request):
    return render(request, 'admin_login.html')

def admin_login(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')
        admins = AdminUser.objects.filter(username=username, password=password).first()
        if admins.username == username and admins.password == password:
            return render(request, 'admin_dash.html')
    return render(request, 'admin_login.html')

def all_users(request):
    users = Users.objects.all()
    return render(request, 'all_users.html', {'alluser': users})