from django.shortcuts import render

# my imports
from apps.index.models import Settings
from apps.team.models import Team
# Create your views here.

def team(request):
    setting = Settings.objects.latest('id')
    team = Team.objects.all()
    return render(request, 'team.html', locals())
    