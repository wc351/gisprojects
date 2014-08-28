from django.conf.urls import patterns, include, url
from django.contrib import admin
from apps.views import MainView, SearchView, DisplayView



admin.autodiscover()

urlpatterns = patterns('',
    # Examples:
    # url(r'^$', 'gisprojects.views.home', name='home'),
    # url(r'^blog/', include('blog.urls')),

    url(r'^admin/', include(admin.site.urls)),
    url(r'^$', MainView.as_view(), name="main_page"),
    url(r'^search/', SearchView.as_view(), name="search_page"),
    url(r'^display/', DisplayView.as_view(), name="display_page"),

)
