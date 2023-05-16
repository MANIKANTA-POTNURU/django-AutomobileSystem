from django.contrib import admin
from .models import SignUpData, Admin
from .models import UserComplaint,Product,cart
admin.site.register(SignUpData)
admin.site.register(UserComplaint)
admin.site.register(Product)
admin.site.register(Admin)
admin.site.register(cart)