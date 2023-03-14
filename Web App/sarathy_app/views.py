from django.db.models.fields import NullBooleanField
from django.shortcuts import render
from django.db import connection
#from django.http import HttpResponse
#from first_app.models import truck_driver
from first_app.forms import newTruckDriverForm, newSellerDetailForm, truckDriver_user_passForm, newTruckDetailsForm, newSellerJobForm, seller_user_passForm
from django.conf import settings
User = settings.AUTH_USER_MODEL
# Create your views here.

# def index(request):
#     return HttpResponse("Hello World!")

def index(request):
    return render(request, 'first_app/index.html')

def whosignup(request):
    return render(request, 'first_app/whosignup.html')

def login_who(request):
    return render(request, 'first_app/login_who.html')

def about(request):
    return render(request, 'first_app/about.html')

def next1(request):
    if request.method == "POST":
        form = newSellerJobForm(request.POST)
        if form.is_valid():
            print("VALIDATION SUCCESS!")
            print("goods: "+str(form.cleaned_data['goods']))
            print("source: "+ str(form.cleaned_data['source']))
            form.save(commit=True)
        else:
            return ("Error in the form")
    return render(request, 'first_app/next1.html')

def seller_details(request):
    sd_form = newSellerDetailForm()
    if request.method == "POST":
        form = seller_user_passForm(request.POST)

        if form.is_valid():
            print("VALIDATION SUCCESS!")
            print("username: "+form.cleaned_data['username'])
            print("email: "+form.cleaned_data['email'])
            user = form.save()
            user.set_password(user.password)
            user.save()
            form.save(commit=True)
        else:
            return ("Error in the form")
    return render(request, 'first_app/seller_details.html', {'sd_form': sd_form})

def username_pass_seller(request):
    seller_user = seller_user_passForm()
    return render(request, 'first_app/username_pass_seller.html', {'seller_user':seller_user})

def signup(request):
    return render(request, 'first_app/signup.html')

def job_seller(request):
    job_form = newSellerJobForm()
    if request.method == "POST":
        print('hellllloooooo')
        form = seller_user_passForm(request.POST)
        if form.is_valid():
            print("VALIDATION SUCCESS!")
            print("Username: "+str(form.cleaned_data['username']))
            print("Password: "+ str(form.cleaned_data['password']))
            form.save()
        else:
            return ("Error in the form")
    return render(request, 'first_app/job_seller.html', {'job_form': job_form})

def truck_driver_login(request):
    return render(request, 'first_app/truck_driver_login.html')

def seller_login(request):
    seller_login = seller_user_passForm()
    if request.method == "POST":
        form = newSellerDetailForm(request.POST)
        if form.is_valid():
            print("VALIDATION SUCCESS!")
            print("tradelicense no: "+str(form.cleaned_data['trade_license_no']))
            form.save(commit=True)
        else:
            return ("Error in the form")
    return render(request, 'first_app/seller_login.html', {'seller_login': seller_login})


def next(request):
    if request.method == "POST":
        form = newTruckDetailsForm(request.POST)
        if form.is_valid():
            print("VALIDATION SUCCESS!")
            print("License: "+str(form.cleaned_data['license_no']))
            print("Truck Capacity: "+ str(form.cleaned_data['truck_capacity']))
            form.save(commit=True)
        else:
            return ("Error in the form")
    return render(request, 'first_app/next.html')

def truck_details(request):
    truck_form = newTruckDetailsForm()
    if request.method == "POST":
        form = newTruckDriverForm(request.POST)
        if form.is_valid():
            print("VALIDATION SUCCESS!")
            print("Aadhar: "+str(form.cleaned_data['aadhar_no']))
            print("Fname: "+ str(form.cleaned_data['fname']))
            form.save(commit=True)
        else:
            return ("Error in the form")
    return render(request, 'first_app/truck_details.html', {'truck_form': truck_form})


def truck_driver_details(request):
    form = newTruckDriverForm()
    if request.method == "POST":
        user_form = truckDriver_user_passForm(request.POST)

        if user_form.is_valid():
            print("VALIDATION SUCCESS!")
            print("Username: "+user_form.cleaned_data['username'])
            print("Password: "+user_form.cleaned_data['password'])
            user = user_form.save()
            user.set_password(user.password)
            user.save()
            user_form.save(commit=True)
        else:
            return ("Error in the form")
    return render(request, "first_app/truck_driver_details.html", {'form': form})


def username_pass_truckdriver(request): 
    user_form = truckDriver_user_passForm()
    return render(request, 'first_app/username_pass_truckdriver.html', {'user_form':user_form})

def my_custom_sql(self):
    with connection.cursor() as cursor:
        cursor.execute("select * from first_app_truck_driver")
        row = cursor.fetchall()
        return row






