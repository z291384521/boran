def depart_list(request):
    queryset = Department.objects.all()
    print(queryset)
    return render(request, "depart_list.html", {"queryset": queryset})

from django.shortcuts import render, HttpResponse, redirect

from app01.models import Department
def depart_add(request):
    """添加部门"""

    if request.method == "GET":
        return render(request, "depart_add.html")
    title = request.POST.get("title")
    # 保存到数据库
    Department.objects.create(title=title)
    # 重定向回到列表
    return redirect("/depart/list")


def depart_delete(request):
    nid = request.GET.get("nid")
    Department.objects.filter(id=nid).delete()
    return redirect("/depart/list")



def depart_edit(request, nid):
    if request.method == "GET":
        # 根据nid 获取它的数据
        row_object = Department.objects.filter(id=nid).first()
        return render(request, "depart_edit.html", {"row_object": row_object})
    title = request.POST.get("title")
    Department.objects.filter(id=nid).update(title=title)
    return redirect("/depart/list")
