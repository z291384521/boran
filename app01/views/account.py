from django.shortcuts import render
from app01.utils.bootstrap import BootStrapForm
from app01.utils.encrypt import md5
from django import forms

class LoginForm(forms.Form):
    username = forms.CharField(
        label="用户名",
        widget=forms.TextInput,
        required=True
    )
    password = forms.CharField(
        label="密码",
        widget=forms.PasswordInput(render_value=True),
        required=True
    )

    code = forms.CharField(
        label="验证码",
        widget=forms.TextInput,
        required=True
    )
    
    def clean_password(self):
        pwd = self.cleaned_data.get("password")
        return md5(pwd)
def login(request):
    """ 登录 """
    # form = LoginForm()
    # print("fotm",form)
    return render(request, 'login.html')