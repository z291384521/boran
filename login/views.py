from login.models import UserInfo
from login.models import Department, UserInfo
from django.shortcuts import render, HttpResponse, redirect

# 创建视图函数
# Create your views here.


def index(request):
    return HttpResponse("欢迎使用")


def user_list(request):
    # 去app目录下的templates目录寻找user_list.html
    # (根据app的注册顺序，逐一去他们的templates目录中找)
    return render(request, "user_list.html")


def user_add(request):
    return render(request, "user_add.html")


def template(request):
    name = "你的名字"
    roles = ["管理员", "ceo", "保安"]
    user_info = {"name": "郭智商", "salary": 10000, "role": "ceo"}
    data_list = [
        {"name": "郭智商", "salary": 10000, "role": "ceo"},
        {"name": "郭智商1", "salary": 10000, "role": "ceo1"},
        {"name": "郭智商1", "salary": 10000, "role": "ceo1"},
    ]
    return render(request, "template.html", {"n1": name, "n2": roles, "n3": user_info})


def something(request):
    # request是一个对象用来存储 封装了用户发过来的所有请求相关数据
    print("返回的类容是", request.method)
    # 2 再URL上传传递/request/?n1=123&n2=9999
    print("获得传递值", request.GET)
    # 返回的数据
    # 返回的类容是 GET
    # 获得传递值 < QueryDict: {'n1': ['123'], 'n2': ['9999']} >
    # 3在请求中提交数据
    print("request.Post", request.POST)
    # request.Post <QueryDict: {}>
    # return HttpResponse("返回的类容")
    # [响应] 直接返回
    # return HttpResponse()
    # [响应] 渲染
    # return render()
    # [响应] 重定向
    return redirect("http://www.baidu.com")


def logintest(request):
    if request.method == "GET":
        return render(request, "login.html")
    elif request.method == "POST":
        print(request.POST)
        username = request.POST.get("user")
        paw = request.POST.get("paw")
        print(username, paw)
        if username == "zrq" and paw == "123456":
            return HttpResponse("登录成功")
        else:
            return render(request, "login.html", {"error_msg": "登陆失败"})


def ORM(request):
    # 插入数据
    # Department.objects.create(title="销售部")
    # Department.objects.create(title="IT部")
    # Department.objects.create(title="运营部")
    UserInfo.objects.create(name="哈哈哈", password="123", age=19)
    UserInfo.objects.create(name="哈哈哈哈", password="123", age=19)
    UserInfo.objects.create(name="哈哈哈哈", password="123", age=19)
    # 删除数据
    UserInfo.objects.filter(id=3).delete()
    return HttpResponse("成功")


def info_list(request):
    all_info = UserInfo.objects.all()
    return render(request, "info_list.html", {"data_list": all_info})


def info_add(request):
    if request.method == "GET":
        return render(request, "info_add.html")
    elif request.method == "POST":
        print(request)
        username = request.POST.get("user")
        paw = request.POST.get("pwd")
        age = request.POST.get("age")

        UserInfo.objects.create(name=username, password=paw, age=age)
        return redirect("/info_list")


def info_delete(request):
    nid = request.GET.get("nid")
    UserInfo.objects.filter(id=nid).delete()
    return HttpResponse("删除成功")
