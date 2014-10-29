from django.views.generic import TemplateView


class MainView(TemplateView):
    template_name = "projects/main_page.html"


class SearchView(TemplateView):
    template_name = "projects/search.html"


class DisplayView(TemplateView):
    template_name = "projects/display.html"


class ProjectView(TemplateView):
    template_name = "projects/createproject.html"


class TestView(TemplateView):
    template_name = "projects/test.html"