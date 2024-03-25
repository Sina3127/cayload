from django.shortcuts import render
from django.views.generic import TemplateView

from home.models import Company, Instagram
from track.models import Track


class Tracker(TemplateView):
    template_name = 'track/tracking.html'

    def get(self, request, *args, **kwargs):
        companys = Company.objects.last()
        instagram = Instagram.objects.all()

        context = {
            'companys': companys,
            'instagram': instagram
        }

        return render(request, "track/tracking.html", context)

    def post(self, request, *args, **kwargs):
        container_number = request.POST.get('container_number')
        hbl_number = request.POST.get('hbl_number')
        mbl_number = request.POST.get('mbl_number')

        if container_number:
            track = Track.objects.filter(container_number=container_number).first()
        elif hbl_number:
            track = Track.objects.filter(hbl_number=hbl_number).first()
        elif mbl_number:
            track = Track.objects.filter(mbl_number=mbl_number).first()
        else:
            track = None

        companys = Company.objects.last()
        instagram = Instagram.objects.all()

        context = {
            'track': track,
            'companys': companys,
            'instagram': instagram
        }
        return render(request, "track/results.html", context)