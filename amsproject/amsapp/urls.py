from django.contrib import admin
from django.urls import path
from . import views
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('admin/', admin.site.urls),
    path("",views.homepage,name="home"),
    path("login",views.loginpage,name="login"),
    path("SignUpDatafunction",views.SignUpDatafunction,name="SignUpDatafunction"),
    path("Contactfunction",views.Contactfunction,name="Contactfunction"),
    path("owner",views.ownerpage,name="owner"),
    path("ownercontact", views.ownercontactpage, name="ownercontact"),
    path("admin1",views.admin1page,name="admin1"),
    path("contact",views.contactpage,name="contact"),
    path("carproducts",views.carproducts,name="carproducts"),
    path("carburetor",views.carburetor,name="carburetor"),
    path("credit",views.credit,name="credit"),
    path("about",views.about,name="about"),
    path("checkuserlogin",views.checkuserlogin,name="checkuserlogin"),
    path("userhome",views.userhome,name="userhome"),
    path("userlogout",views.userlogout,name="userlogout"),
    path("deleteuser/<int:uid>",views.deleteuser,name="deleteuser"),
    path("deleteusercompliant/<int:uid>",views.deleteusercompliant,name="deleteusercompliant"),
    path('empchangepwd', views.empchangepwd, name="empchangepwd"),
    path('empupdatepwd', views.empupdatepwd, name="empupdatepwd"),
    path("addproduct", views.addproduct, name="addproduct"),
    path("viewaproducts", views.viewaproducts, name="viewaproducts"),
    path("userviewaproducts", views.userviewaproducts, name="userviewaproducts"),
    path("deleteproduct/<int:uid>",views.deleteproduct,name="deleteproduct"),

    path("category/<str:id>",views.getcategory,name="getcategory"),
    path('addcartfun',views.add_cart,name="addcartfun"),
    path('cart/',views.get_cart,name="getcart"),
    path("deletecartproduct/<int:uid>",views.deletecartproduct,name="deletecartproduct"),
    path("clearcartafterpayment",views.clearcartafterpayment,name="clearcartafterpayment"),
]
if settings.DEBUG:
        urlpatterns += static(settings.MEDIA_URL,document_root=settings.MEDIA_ROOT)
