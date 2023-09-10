from django.shortcuts import render
# my imports
from apps.index.models import Settings,Video,Services
from apps.secondary.models import About,News
from apps.team.models import Team
# Create your views here.
def about(request):
    video = Video.objects.latest('id')
    services = Services.objects.all()
    setting = Settings.objects.latest('id')
    about = About.objects.latest('id')
    team = Team.objects.all()
    return render(request, 'about.html', locals())