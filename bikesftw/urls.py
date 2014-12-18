from django.conf.urls import patterns, include, url
from django.views.generic import TemplateView
from . import views

urlpatterns = patterns('',
	url(r'^home/$', TemplateView.as_view(template_name="bikesftw/home.html"), name='home'),
    url(r'^$', TemplateView.as_view(template_name="bikesftw/home.html"), name='home'),
	url(r'^sign_in/$', TemplateView.as_view(template_name="bikesftw/sign_in.html"), name='sign_in'),
 	url(r'^sign_out/$', TemplateView.as_view(template_name="bikesftw/sign_out.html"), name='sign_out'),
    url(r'^quickref/$', TemplateView.as_view(template_name="bikesftw/quickref.html"), name='quickref'),
    url(r'^knowledge/$', TemplateView.as_view(template_name="bikesftw/knowledge.html"), name='knowledge'),
    url(r'^bike_disp/$', views.bike_disp),
    url(r'^bike_edit/$', TemplateView.as_view(template_name="bikesftw/bike_edit.html"), name='bike_edit'),
    url(r'^maint_disp/$', TemplateView.as_view(template_name="bikesftw/maint_disp.html"), name='maint_disp'),
    url(r'^maint_edit/$', TemplateView.as_view(template_name="bikesftw/maint_edit.html"), name='maint_edit'),
    url(r'^repairlog/$', TemplateView.as_view(template_name="bikesftw/repairlog.html"), name='repairlog'),
    url(r'^qa_disp/$', TemplateView.as_view(template_name="bikesftw/qa_disp.html"), name='qa_disp'),
    url(r'^qa_post/$', TemplateView.as_view(template_name="bikesftw/qa_post.html"), name='qa_post'),
    url(r'^qa_reply/$', TemplateView.as_view(template_name="bikesftw/qa_reply.html"), name='qa_reply'),
    url(r'^myfeed/$', TemplateView.as_view(template_name="bikesftw/myfeed.html"), name='myfeed'),
)