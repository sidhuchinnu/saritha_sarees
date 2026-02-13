from django.conf import settings
from django.conf.urls.static import static
from django.contrib import admin
from django.urls import path
from main import views
from userapp import views as user_views
from adminapp import views as admin_views

urlpatterns = [
    path('admin/', admin.site.urls),

    path('', views.home, name='home'),
    path('admin_login', admin_views.admin_login_page, name='admin_login'),
    path('admin_login_auth', admin_views.admin_login, name='admin_login_auth'),
    path('all_users', admin_views.all_users, name='all_users'),
    path('stock', views.stock, name='stock'),
    path('dashboard', user_views.dashboard, name='dashboard'),
    path('aboutus', views.aboutus, name='aboutus'),
    path('contact', views.contact, name='contact'),
    path('register', views.register, name='register'),
    path('login', views.login, name='login'),
    path('add_user', user_views.add_user, name='add_user'),
    path('user_login', user_views.user_login, name='user_login'),
    path('otp_login', user_views.otp_login, name='otp_login'),
    path('send_otp', user_views.send_otp, name='send_otp'),
    path('verify_otp', user_views.verify_otp, name='verify_otp'),

  
]+ static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
