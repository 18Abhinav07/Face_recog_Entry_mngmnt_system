from django.shortcuts import render, redirect
from django.contrib import messages
from django.contrib.auth import authenticate, login, logout
from django.http import JsonResponse
from .forms import *
from .models import *
import datetime


def home(request):
    print(datetime.datetime.now())
    return render(request, "BASE/home.html", {})


def login_user(request, user_group):

    if request.method == "POST":
        username = request.POST["username"]
        password = request.POST["password"]
        user_auth = authenticate(request, username=username, password=password)

        if user_auth is not None:
            if user_auth.groups.filter(name="admin").exists():
                login(request, user_auth)
                messages.success(request, "You have been logged in as an Admin.")
                request.session["username"] = username
                return render(request, "ADMINS/admin.html", {"user_group": user_group})

            elif user_auth.groups.filter(name="guard").exists():
                login(request, user_auth)
                messages.success(request, "You have been logged in as an Guard.")
                request.session["username"] = username
                return render(
                    request,
                    "GUARDS/guard.html",
                    {
                        "user_group": user_group,
                        "form1": AddInstituteAdmittedDetailsForm,
                        "form2": AddNIPDetailsForm,
                    },
                )

            else:
                messages.success(
                    request,
                    "There was an error in logging you in, You are not an Admin.",
                )
                return redirect("home")
        else:
            messages.success(
                request, "There was an error in logging you in, Please try again."
            )
            return redirect("home")

    else:
        if user_group == "admin":
            return render(request, "BASE/login.html", {"user_group": user_group})
        elif user_group == "guard":
            return render(request, "BASE/login.html", {"user_group": user_group})
        else:
            messages.success(
                "You are not meeting the required demands. Please try a valid method."
            )
            return redirect("home")


def upload_image(request):
    if request.method == "POST" and request.FILES["image"]:
        image_file = request.FILES["image"]
        image_format = image_file.content_type

        return JsonResponse({"success": "Image successfully uploaded"}, status=200)
    else:
        return JsonResponse({"error": "No image file found"}, status=400)


def add_student_record(request):
    if request.user.is_authenticated:
        if request.method == "POST":
            form = AddInstituteAdmittedDetailsForm(request.POST)
            if form.is_valid():
                form.save()
                messages.success(request, "Record Added Successfully...")
                return redirect("add_student_record")
        else:
            form1 = AddInstituteAdmittedDetailsForm()
            form2 = AddNIPDetailsForm()
        return render(request, "GUARDS/guard.html", {"form1": form1, "form2": form2})
    else:
        messages.success(request, "You Must Be Logged In...")
        return redirect("home")


def add_non_record(request):
    if request.user.is_authenticated:
        if request.method == "POST":
            form = AddNIPDetailsForm(request.POST)
            if form.is_valid():
                form.save()
                messages.success(request, "Record Added Successfully...")
                return redirect("add_non_record")
        else:
            form1 = AddInstituteAdmittedDetailsForm()
            form2 = AddNIPDetailsForm()
        return render(request, "GUARDS/guard.html", {"form1": form1, "form2": form2})
    else:
        messages.success(request, "You Must Be Logged In...")
        return redirect("home")


def new_user(request):
    if request.user.is_authenticated:
        form = SignUpForm()
        return render(request, "BASE/register.html", {"form": form})
    else:
        messages.success(request, "You Must Be Logged In...")
        return redirect("home")


def register(request):
    if request.method == "POST":
        form = SignUpForm(request.POST)
        if form.is_valid():
            user = form.save(commit=False)
            user.set_password(form.cleaned_data["password1"])
            user.save()
            form.save_m2m()
            group = form.cleaned_data["group"]
            group.user_set.add(user)
            messages.success(request, "The user was successfully created.")
            redirect("new_user")
    else:
        form = SignUpForm(request.POST)
    return render(request, "BASE/register.html", {"form": form})


def get_students_data(request):
    entries1 = INSTITUTE_ADMITTED.objects.filter(batch="First Year")
    entries2 = INSTITUTE_ADMITTED.objects.filter(batch="Second Year")
    entries3 = INSTITUTE_ADMITTED.objects.filter(batch="Third Year")
    entries4 = INSTITUTE_ADMITTED.objects.filter(batch="Fourth Year")
    entries5 = INSTITUTE_ADMITTED.objects.filter(batch="M.Tech")
    entries6 = INSTITUTE_ADMITTED.objects.filter(batch="PhD")
    data = (entries1, entries2, entries3, entries4, entries5, entries6)
    

    return render(request, "DATA/students_data.html", {"data":data})


def filter_student_records(request):
    if request.method == "POST":
        name = request.POST.get("name")
        roll_no = request.POST.get("roll_no")
        if roll_no == '':
           roll_no = None
        batch = request.POST.get("batch")
        
        entries1 = ()
        entries2 = ()
        entries3 = ()

        if name is not None:
            entries1 = INSTITUTE_ADMITTED.objects.filter(name=name)
        if roll_no is not None:
            entries2 = INSTITUTE_ADMITTED.objects.filter(roll_no=roll_no)
        if batch is not None:
            entries3 = INSTITUTE_ADMITTED.objects.filter(batch=batch)

        filter_dict = {"name": name, "roll_no": roll_no, "batch": batch}

        if name is None and roll_no is None and batch is None:
           return redirect("get_students_data")

        return render(
            request,
            "DATA/students_data.html",
            {
                "entries1": entries1,
                "entries2": entries2,
                "entries3": entries3,
                "filter_dict": filter_dict
            },
        )
    else:
        return redirect("get_students_data")


def get_details(request):
    entries = NON_INSTITUTE_ADMITTED.objects.all()
    return render(request, "DATA/details.html", {"entries": entries})


def logout_user(request):
    logout(request)
    messages.success(request, "Logged out successfully")
    return redirect("home")
