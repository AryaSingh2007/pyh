from django.shortcuts import render,redirect
from .models import *
from django.http import HttpResponse

# Create your views here.
def index(request):
    cdata=tbl_category.objects.all().order_by("-id")[0:6]
    pdata=tbl_product.objects.all().order_by("-total_discount")
    md={"categories":cdata,"products":pdata}
    return render(request,"user/index.html",md)

def contact(request):
    mydict={}
    if request.method=="POST":
        a=request.POST.get("name")
        b=request.POST.get("mobile")
        c=request.POST.get("email")
        d=request.POST.get("message")
        tblcontact(name=a,mobile=b,email=c,message=d).save()
        mydict={"msg":"Thank you for contact with us"}
    return render(request,"user/contact.html",mydict)

def about(request):
    return render(request,"user/about.html")

def gallery(request):
    data=tblgallery.objects.all()
    mydict={'gdata':data}
    return render(request,"user/gallery.html",mydict)

def team(request):
    data=tblteam.objects.all()
    mydict={'tdata':data}
    return render(request,"user/team.html",mydict)

def profile(request):
    return render(request,"user/profile.html")

def uprofile(request):
    return render(request,"uprofile.html")

def registration(request):
    if request.method=="POST":
        Name=request.POST.get("name")
        Email=request.POST.get("email")
        Mobile=request.POST.get("mobile")
        Password=request.POST.get("password")
        Address=request.POST.get("address")
        ppic=request.FILES["fu"]
        x=tbl_register.objects.all().filter(email=Email).count()
        if x==0:
            tbl_register(name=Name,email=Email,mobile=Mobile,password=Password,address=Address,profile_picture=ppic).save()
            return HttpResponse("<script>alert('You are registered successfully...');location.href='/user/registration/'</script>")
        else:
            return HttpResponse("<script>alert('You are already registered');location.href='/user/registration/'</script>")
    return render(request,"user/register.html")

def login(request):
    if request.method=="POST":
        Email=request.POST.get("email")
        Password=request.POST.get("password")
        x=tbl_register.objects.all().filter(email=Email,password=Password).first()
        if x:
            request.session["email"]=str(x.email)
            request.session["uname"]=str(x.name)
            request.session["upic"]=str(x.profile_picture)
            return HttpResponse("<script>alert('You are Login successfully');location.href='/customer/index/'</script>")
        else:
            return render(request,"user/login.html",{"msg":"Your Email id or Password is incorrect"})
    return render(request,"user/login.html")

def dashboard(request):
    return render(request,"dashboard.html")

def products(request):
    x=request.GET.get("cid")
    cdata=tbl_category.objects.all().order_by("-id")
    pdata=""
    if x is not None:
      pdata=tbl_product.objects.all().filter(category=x)
    else:
       pdata=tbl_product.objects.all().order_by("-id")

    if request.method=="POST":
        pid=request.POST.get("pid")
        pname=request.POST.get("pname")
        ppic=request.POST.get("ppic")
        pprice= float(request.POST.get("pprice"))
        pdiscount=request.POST.get("pdiscount")
        pweight=request.POST.get("pweight")
        pquantity=int(request.POST.get("pquantity"))
        totalprice=pprice*pquantity
        user=request.session.get("email")
        if user:
            if pquantity>0:
                tbl_cart(userid=user,pid=pid,product_name=pname,product_picture=ppic,price=pprice,discount_price=pdiscount,product_quantity=pquantity,product_weight=pweight,total_price=totalprice).save()
                return HttpResponse("<script>alert('your item is added in  cart');location.href='/user/products/'</script>")
            else:
                return HttpResponse("<script>alert('please increase your product quantity');location.href='/user/products/'</script>")
        else:
            return HttpResponse("<script>alert('you have to login first');location.href='/user/login/'</script>")

    
    
    md={"categories":cdata,"products":pdata}
    return render(request,"user/products.html",md)

def cart(request):
    cartid=request.GET.get("cid")
    email=request.session.get("email")
    cartItems=tbl_cart.objects.all().filter(userid=email)
    if cartid is not None:
        tbl_cart.objects.all().filter(id=cartid).delete()
        return HttpResponse("<script>alert('Your item deleted successfully');location.href='/user/cart/'</script>")

    return render(request,"user/cart.html",{"data":cartItems})
