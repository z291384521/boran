from django.shortcuts import render, redirect

# Create your views here.

from app01.models import  UserInfo,Gameaccount

from django import forms


def index(request):
    return render(request, "index.html")


def user_list(request):
    queryset = UserInfo.objects.all()
    print(queryset)
    for obj in queryset:
        print(obj.sex)
        # 显示选择器下面的结果
        print(obj.get_sex_display())
        print(obj.depart.title)
    return render(request, "userlist.html", {"queryset": queryset})


# class MyForm(Form):
#     user = forms.CharFiedld(widget=forms.Input)

#将文本变成html
from django.utils.safestring import mark_safe
#分页插件 
from django.core.paginator import Paginator
def game_list(request):
    
    print("链接",request.GET.urlencode())
    """添加测试数据"""
    # for i  in range(27):
    #     num = 159100000000+i
    #     pa=11000000+i
    #     Gameaccount.objects.create(account=num,password=pa,price=1000)

  

    """分页逻辑"""
    # page = int(request.GET.get("page",1))
    # page_size = 10
    # start=(page-1)*page_size
    # end = page * page_size 
    # # total_count=Gameaccount.objects.filter(**data_dict)[start:end].count()
    # total_count=Gameaccount.objects.count()
    # #获得余数
    # page_count,div= divmod(total_count,page_size)
    # if div:
    #     page_count+=1
    # page__string_list=[]
    # for i in range(1,page_count+1):
    #     ele = '<li><a href="?page={}">{}</a></li>'.format(i,i)
    #     page__string_list.append(ele)
    # page__string=mark_safe("".join(page__string_list))
    
    """搜索逻辑"""
    data_dict={}
    value =request.GET.get("q")
    if value:
        data_dict["account__contains"]=value
    # res=Gameaccount.objects.filter(**data_dict).order_by("-id")
    res=Gameaccount.objects.filter(**data_dict)
    print(res)
    """
    对查询的数据进行分页 使用  Paginator
    """
    #当前页码
    page =request.GET.get("page")
    
    if not page:
        page=1
        print("没有获得页数默认为1")
    else:
        page=int(page)
    p=Paginator(res,10)
    max_page=int(p.num_pages)
    print("一共的页码",p.num_pages)
    res = p.page(page).object_list
    """查看前后多少页"""
    plus=2
    start_page=in_range(page-plus,1,max_page)
    end_page=in_range(page+plus,1,max_page)
    """如果小于plus"""
    # if page<=plus+1:
    #     start_page=1
    #     end_page=plus*2+1
    page__string_list=[]
    for i in range(start_page,end_page+1):
        if i == page:
            ele = '<li class="active"><a href="?page={}&&q={}">{}</a></li>'.format(i,value,i)
        else:
            ele = '<li ><a href="?page={}&&q={}">{}</a></li>'.format(i,value,i)
        page__string_list.append(ele)
    page__string=mark_safe("".join(page__string_list))

    # gameinfo=Gameaccount.objects.all()
    # return render(request,"gamelist.html",{"queryset":res,
    # "page__string":page__string})
    return render(request,"gamelist.html",{"queryset":res,"max_page":max_page,"page__string":page__string})
"""范围函数"""
def in_range(n, start, end = 0):
  if(start>end):
    tem=end
    end=start
    start=tem
    print("大小错了自动转换end 与stat对调")
  if start <= n <= end:
    return n
  if n >= end:
    return end
  if n<=start:
    return start

def game_add(request):
    if request.method == "GET":
        #传递设定可以选择的值
        form =GameModelForm()
        return render(request,"gameadd.html",{"form":form})
    form = GameModelForm(data=request.POST)
    if form.is_valid():
        form.save()
        return redirect("/game/list")
    return render(request,"gameadd.html",{"form":form})
from django.core.validators import RegexValidator
class GameModelForm(forms.ModelForm):
    account = forms.CharField(label="手机号",validators=[RegexValidator(r"^159[0-9]+$","数字必须以159开头")])
    class Meta:
            model=Gameaccount
            #自定义字段
            fields=["account","password","price","status","isban_status"]
            #全部字段
            # fields="__all__"
            #除了下面这个字段
            # exclude = ["level"]
    def __init__(self,*args,**kwargs) -> None:
        super().__init__(*args,**kwargs) 
        for name,field in self.fields.items():
            print(name,field)
            field.widget.attrs = {"class":"form-control","placeholder":field.label}



def game_edit(request,nid):
    row_object = Gameaccount.objects.filter(id=nid).first()
    if request.method == "GET":
        # 更具ID获得数据到的数据
        print(row_object)
        form =GameeditModelForm(instance=row_object)
        return render(request,"gameedit.html",{"form":form})
    form = GameeditModelForm(data=request.POST,instance=row_object)
    if form.is_valid():
        form.save()
        return redirect("/game/list")
    return render(request,"gameadd.html",{"form":form})
from django.core.exceptions import ValidationError
class GameeditModelForm(forms.ModelForm):
    #不可以更改
    # account = forms.CharField(disabled=True,label="手机号")
    class Meta:
            model=Gameaccount
            #自定义字段
            fields=["account","password","price","status","isban_status"]
            #全部字段
            # fields="__all__"
            #除了下面这个字段
            # exclude = ["level"]
    def __init__(self,*args,**kwargs) -> None:
        super().__init__(*args,**kwargs) 
        for name,field in self.fields.items():
            print(name,field)
            field.widget.attrs = {"class":"form-control","placeholder":field.label}
    #验证输入钩子方法 自定义方法一定要先定义 
    # 程序会自动运行此方法来进行校验
    def clean_account(self):
        txt_account = self.cleaned_data["account"]
        
        if len(txt_account) != 11:
            #验证不符合不通过
            raise ValidationError("格式错误")
        #查询数据库有没有相同的账号
        # exists=Gameaccount.objects.filter(account=txt_account).exists()
        #查询排除自己的手机号 再查看有没有相同的手机号
        exists=Gameaccount.objects.exclude(id=self.instance.pk).filter(account=txt_account).exists()
        if exists:
            raise ValidationError("手机号已经存在")
        return txt_account
    

def game_delete(request,nid):
    nid = request.GET.get("nid")
    Gameaccount.objects.filter(id=nid).delete()
    return redirect("/game/list")