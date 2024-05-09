from django.shortcuts import get_object_or_404, render, redirect,HttpResponse
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth import authenticate, login
from django.contrib import messages
from django.contrib.auth.models import User
from .models import Patient
from django.urls import reverse
from django.utils.html import format_html


def display(request, Name):
    AllPost = Patient.objects.filter(Name=Name)
    context = {"AllPost": AllPost}
    return render(request, "index.html", context)

def details(request):
    if request.method == "POST":
        Name = request.POST.get("Name")
        Blood_group = request.POST.get("Blood_group")
        Age = request.POST.get("Age")
        Disease = request.POST.get("Disease")
        Location = request.POST.get("Location")
        query = Patient(Name=Name, Blood_group=Blood_group, Age=Age, Disease=Disease, Location=Location)
        query.save()

        # Build the response HTML
        response_html = format_html('''
            Successfully Saved<br><br>
            <a href="{}" class="btn btn-primary">Add Patient</a>
            <a href="{}" class="btn btn-secondary">View Saved Details</a>
            ''',
            reverse('add_patient'),  # URL to add another patient
            reverse('view_patient', kwargs={'Name': Name})  # URL to view this patient's details
        )
        return HttpResponse(response_html)
    return render(request, "details.html")


def view_all_patients(request):
    patients = Patient.objects.all()
    return render(request, "all_patients.html", {"patients": patients})


def update_patient(request, id):
    patient = get_object_or_404(Patient, id=id)
    if request.method == "POST":
        patient.Name = request.POST.get("Name", "")
        patient.Blood_group = request.POST.get("Blood_group", "")
        patient.Age = request.POST.get("Age", "")
        patient.Disease = request.POST.get("Disease", "")
        patient.Location = request.POST.get("Location", "")
        patient.save()
        return redirect('view_all_patients')
    return render(request, "patient_form.html", {"patient": patient})

def delete_patient(request, id):
    patient = get_object_or_404(Patient, id=id)
    if request.method == "POST":
        patient.delete()
        return redirect('view_all_patients')
    return render(request, "confirm_delete.html", {"patient": patient})

def base(request):
    return render(request, 'base.html')

def signup(request):
    if request.method == "POST":
        username = request.POST.get('username')
        email = request.POST.get('email')
        password1 = request.POST.get('password')
        password2 = request.POST.get('confirm-password')

        if password1 == password2:
            if User.objects.filter(username=username).exists():
                messages.error(request, "Username already exists.")
                return redirect('/signup')

            if User.objects.filter(email=email).exists():
                messages.error(request, "Email already registered.")
                return redirect('/signup')
            if password!= c-password: # type: ignore
              messages.error(request, "Passwords do not match")
            return redirect('/signup')

            # No need to check for password existence since it's not stored directly in the User model

        else:
              myuser = User.objects.create_user(username=username, email=email, password=password1)
              myuser.save()
              messages.success(request, "User created successfully. Please log in.")
              return redirect('login')

    else:
            messages.error(request, "Passwords do not match.")
    return render(request, 'signup.html')


def user_login(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            return HttpResponse("login successfully")  # Redirect to the home page after successful login
        else:
            messages.error(request, 'Invalid username or password.')
    return render(request, 'login.html')
