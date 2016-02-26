from django.conf.urls import patterns, url
from nounou import views

urlpatterns = patterns('',
        url(r'^$', views.index, name='index'),
        # url(r'^$,', views.main, name='main')
        )

