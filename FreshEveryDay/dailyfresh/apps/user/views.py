from django.shortcuts import render


# Create your views here.
def register(request):
    """显示注册界面"""
    return render(request, "register.html")


def register_handle(request):
    """进行注册处理"""
    user_name = request.POST.get("user_name")
    pwd = request.POST.get("pwd")

