from django.contrib import admin
from .models import HeroType, HeroReview, Store, HeroCertificate
# Register your models here.

class HeroReviewInline(admin.TabularInline):
    model = HeroReview
    extra = 2

class HeroTypeAdmin(admin.ModelAdmin):
    list_display = ('name','type','date_added')
    inlines = [HeroReviewInline]

class StoreAdmin(admin.ModelAdmin):
    list_display = ('name','location')
    filter_horizontal = ('hero_types')

class HeroCertificateAdmin(admin.ModelAdmin):
    list_display= ('hero', 'ceritficate_number')

admin.site.register(HeroType, HeroTypeAdmin)
admin.site.register(HeroReview, HeroReviewInline)
admin.site.register(Store, StoreAdmin)
admin.site.register(HeroCertificate, HeroCertificateAdmin)