from django.contrib.auth import get_user_model
from django.core.mail import send_mail
from django.db.models import Q, Subquery
from django.http import HttpResponse
from django.shortcuts import redirect, render
from .forms import ProductForm
from .models import SignUpData, UserComplaint, Product, Admin,cart
def homepage(request):
    return render(request,"home.html")
def ownerpage(request):
    auname = request.session["uname"]
    usersdata = SignUpData.objects.all()
    userscount = SignUpData.objects.count()
    return render(request, "owner.html", {"users": usersdata,"count":userscount,"auname":auname})
def ownercontactpage(request):
    auname = request.session["uname"]
    complaintdata = UserComplaint.objects.all()
    complaintscount = UserComplaint.objects.count()
    return render(request, "ownercontact.html", {"complaints": complaintdata,"count":complaintscount,"auname":auname})
def admin1page(request):
    usersdata = SignUpData.objects.all()
    userscount = SignUpData.objects.count()
    return render(request,"admin.html",{"users": usersdata,"count":userscount})
def loginpage(request):
    return render(request,"login.html")
def userhome(request):
    if 'uname' in request.session:
        return render(request, "userhome.html", {'x': request.session['uname']})
    else:
        return HttpResponse("<b>Session TimeOut</b>")

def SignUpDatafunction(request):
    name = request.POST['name']
    emailid = request.POST['email']
    pwd=request.POST['pass']
    signobj = SignUpData(sign_name=name,sign_email=emailid,sign_password=pwd)
    SignUpData.save(signobj)
    subject = 'Welcome to Pooja Software Solutions'
    message = 'Congratutations you are recruited for this company'
    email_from = 'amssdp@outlook.com'
    recipient_list = [emailid]
    send_mail(subject, message, email_from, recipient_list, fail_silently=False)
    return render(request,"login.html")
def deleteuser(request,uid):
    SignUpData.objects.filter(id=uid).delete()
    return redirect("owner")
def deleteusercompliant(request,uid):
    UserComplaint.objects.filter(id=uid).delete()
    return redirect("ownercontact")
def Contactfunction(request):
    name = request.POST['Name']
    emailid = request.POST['Email']
    msg=request.POST['Mensage']
    contactobj= UserComplaint(user_name=name,user_email=emailid,user_query=msg)
    UserComplaint.save(contactobj)
    return render(request,"home.html")
def checkuserlogin(request):
    emailid=request.POST["logemail"]
    pwd=request.POST["logpass"]
    flag=SignUpData.objects.filter(Q(sign_email=emailid) & Q(sign_password=pwd))
    flag1 = Admin.objects.filter(Q(email=emailid) & Q(password=pwd))
    if flag1:
        admin = Admin.objects.get(email=emailid)
        usersdata = SignUpData.objects.all()
        userscount = SignUpData.objects.count()
        request.session["emailid"] = admin.email
        request.session["uname"] = admin.username
        return render(request, "owner.html",{"uname": admin.username,"users": usersdata,"count":userscount})
    else:
        if flag:
            user = SignUpData.objects.get(sign_email=emailid)
            request.session["uname"] = user.sign_name
            request.session["email"] = user.sign_email
            return render(request, "userhome.html", {"uname": user.sign_name,"user":user})
        else:
            return render(request, "logfail.html")
def empchangepwd(request):
    if 'uname' in request.session:
        x=request.session['uname']
        ename=request.session["uname"]
        return render(request,"userchangepwd.html",{"ename":ename})
    else:
        return render(request,"sessiontime.html")



def empupdatepwd(request):
    uname=request.session["uname"]
    opwd=request.POST["opwd"]
    npwd=request.POST["npwd"]
    flag = SignUpData.objects.filter(Q(sign_name=uname)&Q(sign_password=opwd))

    if flag:

        SignUpData.objects.filter(sign_name=uname).update(sign_password=npwd)
        msg = "Password Updated Successfully"
        error="no"
        return render(request, "userchangepwd.html", {"uname": uname,"msg":msg,"error":error})
    else:
        msg = "Old Password is Incorrect"
        error = "yes"
        return render(request, "userchangepwd.html", {"uname": uname,"msg":msg,"error":error})
def userlogout(request):
    request.session.flush()
    return render(request,"home.html")
def contactpage(request):
    return render(request,"contact.html")
def carproducts(request):
    return render(request,"category.html")
def carburetor(request):
    return render(request,"carburetor.html")
def credit(request):
    return render(request,"credit.html")
def about(request):
    return render(request,"about.html")
# def viewaproducts(request):
#     auname=request.session["uname"]
#     productlist = Product.objects.all()
#     count = Product.objects.count()
#     return render(request,"viewaproducts.html",{"auname":auname,"productlist":productlist,"count":count})
def viewaproducts(request):
    mail=request.session["emailid"]
    p = Admin.objects.filter(email=mail)
    key = p[0].secure_key
    productlist = Product.objects.filter(secure_key=key)
    count = Product.objects.filter(secure_key=key).count()
    # productlist = Product.objects.all()
    # count = Product.objects.count()
    return render(request,"viewaproducts.html",{"productlist":productlist,"count":count})
def userviewaproducts(request):
    auname=request.session["uname"]
    productlist = Product.objects.all()
    count = Product.objects.count()
    return render(request,"userviewaproducts.html",{"auname":auname,"productlist":productlist,"count":count})
def addproduct(request):
    auname = request.session["uname"]
    form = ProductForm()
    if request.method == "POST":
        formdata = ProductForm(request.POST,request.FILES)
        if formdata.is_valid():
            formdata.save()
            msg="Product Added Successfully"
            return render(request, "addproduct.html", {"auname":auname,"productform": form,"msg":msg})
        else:
            msg = "Failed to Add Product"
            return render(request, "addproduct.html", {"auname":auname,"productform": form, "msg": msg})
    return render(request,"addproduct.html",{"auname":auname,"productform":form})
def deleteproduct(request,uid):
    Product.objects.filter(id=uid).delete()
    return redirect("viewaproducts")

def getcategory(request,id):
    pro=Product.objects.filter(category=id)
    return render(request,"category.html",{"pro":pro})

def add_cart(request):
    user=request.session["email"]
    prid=request.POST["pid"]
    print(prid)
    cartobj=cart(mail=user,pid=prid)
    cart.save(cartobj)
    return redirect('/cart')

def get_cart(request):
    user = request.session["email"]
    pro=cart.objects.filter(mail=user)
    pcount = cart.objects.filter(mail=user).count()
    products = Product.objects.filter(id__in=Subquery(pro.values('pid')))
    total = sum([Product.price for Product in products])
    return render(request, "cart.html", {"pro": products,"count":pcount,"price":total})

def deletecartproduct(request,uid):
    cart.objects.filter(pid=uid).delete()
    return redirect("getcart")
def clearcartafterpayment(request):
    user = request.session["email"]
    cart.objects.filter(mail=user).delete()
    return redirect("userhome")
