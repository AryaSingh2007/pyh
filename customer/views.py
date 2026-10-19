from django.shortcuts import render,redirect

# Create your views here.
def index(request):
    return render(request,"customer/index.html")

def profile(request):
    return render(request,"customer/profile.html")

def logout(request):
    user=request.session.get("email")
    if user:
        del request.session["email"]
        del request.session["uname"]
        del request.session["upic"]
        return redirect("/user/index/")
    return render(request,"customer/logout.html")

def products(request):
    return render(request,"customer/products.html")