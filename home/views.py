from django.shortcuts import render
from django.views.generic import TemplateView


class Home(TemplateView):
    template_name = "home/index.html"

    def get(self, request, *args, **kwargs):
        context = {

        }
        return render(request, self.template_name, context)
class Tracker(TemplateView):
    template_name = 'tracker.html'

    def get(self, request, *args, **kwargs):
        context = {

        }
        return render(request, "home/tracker.html", context)