from django import forms
from .models import  Product
from django import forms
class ProductForm(forms.ModelForm):
    class Meta:
        model = Product
        fields = "__all__"
        labels = {"category":"Select Category"}
class PasswordResetForm(forms.Form):
    email = forms.EmailField()
