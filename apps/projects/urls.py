from django.conf.urls import url, patterns

from apps.projects.views import MainView, SearchView, DisplayView, ProjectView, TestView


urlpatterns = patterns('',

    url(r'^$', MainView.as_view(), name="main_page"),
    url(r'^search/', SearchView.as_view(), name="search"),
    url(r'^display/', DisplayView.as_view(), name="display"),
    url(r'^createproject/', ProjectView.as_view(), name="projectdisply"),
    url(r'^test/', TestView.as_view(), name="test"),

)
