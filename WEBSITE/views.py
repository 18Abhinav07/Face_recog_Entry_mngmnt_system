from django.shortcuts import render, redirect
from django.contrib import messages
from django.contrib.auth import authenticate, login, logout
from django.http import JsonResponse



def home(request):
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
                return render(request, "GUARDS/guard.html", {"user_group": user_group})

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
    if request.method == 'POST' and request.FILES['image']:
        image_file = request.FILES['image']
        
        
        return JsonResponse({'success': 'Image successfully uploaded'}, status=200)
    else:
        return JsonResponse({'error': 'No image file found'}, status=400)
             
        
        
def logout_user(request):
    logout(request)
    messages.success(request, "Logged out successfully")
    return redirect("home")

