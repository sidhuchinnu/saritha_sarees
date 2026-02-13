from django.shortcuts import *
from userapp.models import Users
from django.core.mail import send_mail
from shop import settings
import random
import pyttsx3 as pt

# Create your views here.


#otp genarating function
def genarate_otp():
    otp = ""
    for i in range(6):
        otp += str(random.randint(0, 9))
    return otp

#speacking function
def speak(text):
    engine = pt.init()
    engine.setProperty('rate', 150)  # Set speech rate
    engine.setProperty('volume', 0.9)  # Set volume level
    engine.setProperty('voice', 'english+f')  # Set voice (you can choose different voices available on your system)
    #changing voice to female

    engine.say(text)
    engine.runAndWait()





def register(request):
    return render(request, 'reg.html')

def dashboard(request):
    return render(request,'dashboard.html')

def add_user(request):
    if request.method == 'POST':
        name = request.POST['name']
        email = request.POST['email']
        password = request.POST['password']
        profile = request.FILES.get('profile')
       

        user = Users(
            name=name,
            email=email,
            password=password,
            profile=profile
             )
        send_mail(
            subject='Welcome to Saritha Sarees',
            message=f'Hi {name}, thank you for registering at Saritha Sarees.',
            from_email=settings.EMAIL_HOST_USER,
            recipient_list=[email],
            fail_silently=False,
            )
        user.save()   
        speak(f"Welcome {name}, you have been successfully registered.")
        return render(request, 'reg.html', {'message': 'User registered successfully!'})
    return render(request, 'reg.html')


def user_login(request):
    if request.method == 'POST':
        email = request.POST['email']
        password = request.POST['password']

        user = Users.objects.filter(email=email, password=password).first()
        if user.email == email and user.password == password:
            return render(request,'dashboard.html',{'alluser': user})
        else:
            return render(request, 'login.html', {'error': 'Invalid email or password'})
       


def otp_login(request):
    return render(request, 'otp_login.html')

def verify_otp(request):
    if request.method == 'POST':
        email = request.POST['email']
        entered_otp = request.POST['otp']
        user = Users.objects.filter(email=email).first()
        if user and user.otp == entered_otp:
            user.otp = ''  # Clear OTP after successful login
            user.save()
            return render(request, 'dashboard.html', {'alluser': user})
        else:
            return render(request, 'verify_otp.html', {'email': email, 'error': 'Invalid OTP. Please try again.'})

def send_otp(request):
    if request.method == 'POST':
        email = request.POST['email']
        print("EMAIL:",email)
        user = Users.objects.filter(email=email).first()
        if user:
            otp = genarate_otp()
            user.otp = otp
            user.save()
            send_mail(
                subject='Your OTP for Saritha Sarees Login',
                message=f'Hi {user.name}, your OTP for login is {otp}.',
                from_email=settings.EMAIL_HOST_USER,
                recipient_list=[email],
                fail_silently=False,
            )
            return render(request, 'verify_otp.html', {'email': email, 'message': 'OTP sent to your email.'})
        else:
            return render(request, 'otp_login.html', {'error': 'Email not found.'})
        
