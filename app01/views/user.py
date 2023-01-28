
from django.shortcuts import render, HttpResponse, redirect

# Create your views here.

from app01.models import Department, UserInfo
def user_add(request):
    if request.method == "GET":
        """添加用户"""
        gender_choices = UserInfo.gender_choices
        depart_list = Department.objects.all()
        context = {"gender_choices": gender_choices,
                   "depart_list": depart_list}
        return render(request, "uesradd.html", context)
    name = request.POST.get("name")
    password = request.POST.get("password")
    age = request.POST.get("age")
    ac = request.POST.get("ac")
    ctime = request.POST.get("ctime")
    sex = request.POST.get("sex")
    dp = request.POST.get("dp")
    # 以上数据都需要进行校验
    UserInfo.objects.create(
        name=name, password=password, age=age, account=ac, create_time=ctime, sex=sex, depart_id=dp)
    return redirect("/user/list")

from django import forms
class UserModelForm(forms.ModelForm):
    # 重写name的规则 最少3个字符
    name = forms.CharField(min_length=3,label="用户名")
    class Meta:
        model=UserInfo
        fields=["name","password","age","sex","account","depart","create_time"]
        # 给输入的样式
        # widgets={
        #     "name":forms.TextInput(attrs={"class":"form-control"}),
        #     "password":forms.TextInput(attrs={"class":"form-control"}),
        #     "sex":forms.TextInput(attrs={"class":"form-control"}),
        #     "account":forms.TextInput(attrs={"class":"form-control"}),
        # }
    def __init__(self,*args,**kwargs) -> None:
        super().__init__(*args,**kwargs) 
        for name,field in self.fields.items():
            print(name,field)
            field.widget.attrs = {"class":"form-control"}
def user_model_form_add(request):
    if request.method == "GET":
        """添加用户 使用modelform版本来进行创建三"""
        form =UserModelForm()
        print(form)
        return render(request,"usermodelformadd.html",{"form":form})
    # 校验数据是不是合格的
    form =UserModelForm(data=request.POST)
    if form.is_valid():
        print("数据合格 进行保存")
        form.save()
        return redirect("/user/list")
    return render(request,"usermodelformadd.html",{"form":form})

def user_edit(request,nid):
    row_object = UserInfo.objects.filter(id=nid).first()
    if request.method == "GET":
        # 更具ID获得数据到的数据
        
        print(row_object)
        form =UserModelForm(instance=row_object)
        return render(request,"useredit.html",{"form":form})
    # 更新数据 
    # row_object = UserInfo.objects.filter(id=nid).first()
    form =UserModelForm(data=request.POST,instance=row_object)
    if form.is_valid():
        print("数据合格 进行保存")
        form.save()
        return redirect("/user/list")
    return render(request,"usermodelformadd.html",{"form":form})

def user_delete(request):
    nid = request.GET.get("nid")
    UserInfo.objects.filter(id=nid).delete()
    return redirect("/use/list")

def user_list(request):
    queryset = UserInfo.objects.all()
    return render(request,"userlist.html",{"queryset":queryset})
