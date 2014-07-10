from django.conf.urls import patterns, url
from mydbapp import views

urlpatterns = patterns('',
    url(r'^$', views.index, name='index'),
    url(r'^about/$', views.about, name='about'),

    url(r'^add_employee/$', views.add_employee, name='add_employee'),
    url(r'^get_employee/$', views.get_employee, name='get_employee'),

    #to view/edit a specific employee entry?
    #url(r'^employee/(?P<emp_no_url>\w+', views.employee, name='employee'),
)
