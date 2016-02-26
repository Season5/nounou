from django.conf.urls import patterns, url
from django.contrib import admin
from nounou import views



from .views import(
	main,

	)




urlpatterns = patterns('',
        url(r'^$', views.index, name='index'),
        #url(r'^main/$', views.main, name='main'),
        url(r'^main/$', main),
        
        )

