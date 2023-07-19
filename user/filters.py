import django_filters

from .models import *

class filterdata_filter(django_filters.FilterSet):
    class Meta:
        model = DashboardModel
        fields = '__all__'
        exclude = 'qr_img, user '