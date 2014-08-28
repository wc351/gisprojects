from django.views.generic import TemplateView


class MainView(TemplateView):
    template_name = "main_page.html"


class SearchView(TemplateView):
    template_name = "search_page.html"


class DisplayView(TemplateView):
    template_name = "display_page.html"