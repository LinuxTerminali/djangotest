from django.conf.urls import url
from . import views
from django.contrib.auth import views as auth_views

urlpatterns = [
    url(r'^$', auth_views.LoginView.as_view(), {
        'template_name': 'accounts/login.html'}, name='login'),
    url(r'^login/$', auth_views.LoginView.as_view(),
        {'template_name': 'accounts/login.html'}, name='login'),
    url(r'^logout/$', auth_views.LogoutView.as_view(),
        {'template_name': 'accounts/logout.html'}, name='logout'),
    url(r'^register/$', views.register, name='register'),
    url(r'^profile/$', views.view_profile, name='view_profile'),
    url(r'^invite/$', views.invite_employee, name='invite_employee'),
    url(r'^invite/(?P<pk>\d+)/$', views.invite_employee,
        name='invite_employee_with_pk'),
    url(r'^myemployee/', views.myemployee, name='myemployee'),
    url(r'^invite_status/', views.invite_status, name='invite_status'),
    url(r'^invitations/$', views.recievied_invitations,
        name='recievied_invitations'),
    url(r'^invitations/<int:pk>/<string:result>/',
        views.recievied_invitations, name='recievied_invitations_with_pk'),
    url(r'^profile/(?P<pk>\d+)/$', views.view_profile, name='view_profile_with_pk'),
    url(r'^profile/edit/$', views.edit_profile, name='edit_profile'),



]
