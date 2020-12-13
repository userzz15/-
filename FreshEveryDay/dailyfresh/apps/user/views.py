from django.shortcuts import render, redirect
from django.core.urlresolvers import reverse
import re
from .models import User


# Create your views here.
def register(request):
    """显示注册界面"""
    return render(request, "register.html")


def register_handle(request):
    """进行注册处理"""
    # 获取数据
    user_name = request.POST.get("user_name")
    pwd = request.POST.get("pwd")
    email = request.POST.get("email")
    allow = request.POST.get("allow")
    # 数据校验
    if not all([user_name, pwd, email]):
        return render(request, "register.html", {'errmsg': '数据不完整'})
    if not re.match(r'^[a-z0-9][\w.\-]*@[a-z0-9\-]+(\.[a-z]{2,5}){1,2}$', email):
        return render(request, "register.html", {'errmsg': '输入邮箱格式不正确'})
    if allow != 'on':
        return render(request, "register.html", {'errmsg': '请同意协议'})
    try:
        user = User.objects.get(user_name=user_name)
    except:
        user = None
    if not user:
        return render(request, "register.html", {'errmsg': '用户名已存在'})
    # 获取数据
    user = User.objects.create_user(user_name, email, pwd)
    user.is_active = 0
    user.save()
    # 返回
    return redirect(reverse('goods:index'))
