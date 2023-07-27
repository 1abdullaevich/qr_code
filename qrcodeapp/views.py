from django.shortcuts import render, redirect
from django.conf import settings
from qrcode import *
from user.models import DashboardModel
from django.utils.translation import gettext_lazy as _
import time
from django.core.paginator import Paginator
from django.contrib.auth.decorators import login_required


def qr_gen_view(request):
    if request.method == 'POST':
        try:
            data = request.POST
            title = data.get("data")
            title = title.strip()
            img = make(title)
            img_name = f'qr_{time.time()}.png'
            img.save(settings.MEDIA_ROOT / img_name)
            obj = DashboardModel.objects.create(title=title, qr_img=img_name, user=request.user)
            obj.save()
            print(obj.qr_img)
        except:
            data = request.POST
            title = data.get("data")
            title = title.strip()
            img = make(title)
            img_name = f'qr_{time.time()}.png'
            img.save(settings.MEDIA_ROOT / img_name)
            print(img)
        return render(request, 'main/index.html', {'img_name': img_name})
    return render(request, 'main/index.html')


@login_required
def dashboard_view(request):
    q = request.GET.get('q', '')
    objs = DashboardModel.objects.filter(user=request.user)
    get_page = request.GET.get('page', 1)
    stuff = Paginator(objs, 2)
    page = stuff.page(get_page)
    print(q)
    if q:
        objs = objs.filter(title__icontains=q)
    return render(request, 'main/dashboard.html', context={
        'objs': page,
        'count': objs,
        'stuffs': stuff,
        'q': q
    })


def page_not_found_404(request, exception):
    return render(request, 'layouts/page_not_found.html', status=404)


def about_us_view(request):
    return render(request, 'main/about-us.html')


def privacy_view(request):
    return render(request, 'main/privacy.html')
