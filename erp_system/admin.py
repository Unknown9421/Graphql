from django.contrib import admin
from .models import *

# Register your models here.


class CountryAdmin(admin.ModelAdmin):

    fieldsets =[
        ('Name',                                {'fields': ['name']}),
        ('Description',                         {'fields': ['description']}),
        ('Area',                                {'fields': ['area']}),
        ('Population',                          {'fields': ['population']})
    ]


class EmployeeAdmin(admin.ModelAdmin):

    fieldsets = [
        ('First Name',                          {'fields': ['first_name']}),
        ('Last Name',                           {'fields': ['last_name']}),
        ('Description',                         {'fields': ['description']}),
        ('Country',                             {'fields': ['country']}),
        ('Rank',                                {'fields': ['rank']}),
        ('Email',                               {'fields': ['email']}),
        ('Point',                               {'fields': ['point']})
    ]


class ProjectImageAdmin(admin.ModelAdmin):
    fieldsets = [
        ('Image Name',                          {'fields': ['name']}),
        ('Image',                               {'fields': ['image']}),
        ('Description',                         {'fields': ['description']}),
        ('avatar',                              {'fields': ['avatar']}),
    ]


admin.site.register(Country, CountryAdmin)
admin.site.register(Employee, EmployeeAdmin)
admin.site.register(ProjectPicture, ProjectImageAdmin)