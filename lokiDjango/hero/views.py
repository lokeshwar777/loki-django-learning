from django.shortcuts import render
from .models import HeroType
from django.shortcuts import get_object_or_404

# Create your views here.
def all_hero(request):
    heroes = HeroType.objects.all()
    return render(request, 'hero/all_hero.html', {'heroes':heroes})

def hero_detail(request, hero_id):
    hero = get_object_or_404(HeroType, pk=hero_id)
    return render(request,'hero/hero_detail.html',{'hero':hero})