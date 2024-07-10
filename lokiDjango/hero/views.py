from django.shortcuts import render
from .models import HeroType
from django.shortcuts import get_object_or_404
from .forms import HeroTypeForm

# Create your views here.
def all_hero(request):
    heroes = HeroType.objects.all()
    return render(request, 'hero/all_hero.html', {'heroes':heroes})

def hero_detail(request, hero_id):
    hero = get_object_or_404(HeroType, pk=hero_id)
    return render(request,'hero/hero_detail.html',{'hero':hero})

def hero_store_view(request):
    stores = None
    if request.method == 'POST':
        form = HeroTypeForm(request.POST)
        if form.is_valid():
            hero_type = form.cleaned_data['hero_type']
            stores = Store.objects.filter(hero_types=hero_type)
    else:
        form = HeroTypeForm()
    return render(request, 'hero/hero_stores.html',{'stores':stores, 'form':form})