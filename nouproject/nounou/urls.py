from django.conf.urls import patterns, url
from django.contrib import admin
from nounou import views



from .views import(
	index,
	main,
	reggy,

	)




urlpatterns = patterns('',
        url(r'^', views.index, name='index'),
        url(r'^main/$', main),
        url(r'^reggy/$', reggy),
        
        )

