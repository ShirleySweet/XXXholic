from django.conf.urls import patterns, include, url
from web.views import person,mission,daily_report,load
#from django.contrib import admin
from django.conf import settings

urlpatterns = patterns('',
    # Examples:
    # url(r'^$', 'webTest.views.home', name='home'),
    # url(r'^blog/', include('blog.urls')),
    url(r'^person/$',person),
    url(r'^mission/$',mission),
    url(r'^report/$',daily_report),
    url(r'^load/$',load),
    (r'^static/(?P<path>.*)$','django.views.static.serve',{'document_root':settings.STATIC_URL}),
    #url(r'^admin/', include(admin.site.urls)),
)
