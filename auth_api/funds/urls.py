from django.conf.urls import url
from rest_framework.urlpatterns import format_suffix_patterns
from funds import views
 
urlpatterns = [
    url(r'^funds/$', views.FundList.as_view(), name='fund-list'),
    url(r'^funds/(?P<pk>[0-9]+)/$', views.FundDetail.as_view(), name='fund-detail'),
]