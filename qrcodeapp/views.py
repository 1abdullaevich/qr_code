from django.shortcuts import render
from django.conf import settings
from qrcode import *
from user.models import DashboardModel
import time
from django.core.paginator import Paginator
def qr_gen_view(request):
    if request.method == 'POST':
        data = request.POST
        title = data.get("data")
        title = title.strip()
        img = make(title)
        img_name = f'qr_{time.time()}.png'
        img.save(settings.MEDIA_ROOT / img_name)
        obj = DashboardModel.objects.create(title=title, qr_img=img_name, user=request.user)
        obj.save()
        print(obj.qr_img)
        return render(request, 'main/index.html', {'img_name': img_name})
    return render(request, 'main/index.html')


def dashboard_view(request):
    q = request.GET.get('q', '')
    objs = DashboardModel.objects.filter(user=request.user)
    stuff = Paginator(objs, 3)
    if q:
        objs = objs.filter(title__icontains=q)
    return render(request, 'main/dashboard.html', context={
        'objs': objs,
        'q': q
    })


def page_not_found_404(request, exception):
    return render(request, 'layouts/page_not_found.html', status=404)
