from django.contrib import admin
from django import forms
from django.db.models import Q
from django.conf import settings
from django.contrib.auth import get_user_model
from .models import Population
# Register your models here.

USER = get_user_model()

class PopulationFormAdmin(forms.ModelForm):

    birthdate = forms.DateField(widget=forms.NumberInput(attrs={'type': 'date'}))

    def __init__(self, *args, **kwargs):
        self.request = kwargs.pop('request')
        posbon_user = USER.objects.get(Q(username=self.request.user.username) & Q(groups__name="PosbonlarGroup"))
        super().__init__(*args, **kwargs)
        if posbon_user.is_superuser:
            return super().__init__(*args, **kwargs)
        else:
            self.fields['posbon_name'] = forms.CharField(
                initial=posbon_user,
                label="Posbon",
                disabled=True
            )
            self.fields['city'] = forms.CharField(
                initial=posbon_user.region,
                label="Shahar/Tuman",
                disabled=True
            )
            self.fields['quarter'] = forms.CharField(
                initial=posbon_user.get_mahalla,
                label="MFY nomi",
                disabled=True
            )
        # self.fields['posbon'].queryset = USER.objects.filter(Q(is_staff=True) & ~Q(is_superuser=True))

    class Meta:
        model = Population
        exclude = ['posbon']
        fields = "__all__"


class PopulationAdmin(admin.ModelAdmin):
    form = PopulationFormAdmin
    list_display = ('person_name', 'get_posbon')
    list_display_links = ('person_name',)

    def save_model(self, request, obj, form, change):
        obj.posbon = request.user
        super().save_model(request, obj, form, change)

    def get_posbon(self, instance):
        return instance.posbon

    def get_queryset(self, request):
        qs = super(PopulationAdmin, self).get_queryset(request)
        if request.user.is_superuser and request.user.is_staff:
            return qs.all()
        else:
            return qs.filter(posbon=request.user)

    def get_form(self, request, obj=None, **kwargs):
        PopulationFormAdmin = super(PopulationAdmin, self).get_form(request, obj, **kwargs)

        class RequestPopulationForm(PopulationFormAdmin):
            def __new__(cls, *args, **kwargs):
                kwargs['request'] = request
                return PopulationFormAdmin(*args, **kwargs)
        return RequestPopulationForm


admin.site.register(Population, PopulationAdmin)



# class GetQuarterFromCity(forms.ModelForm):
#     def __init__(self, *args, **kwargs):
#         super(GetQuarterFromCity, self).__init__(*args, **kwargs)
#         self.fields['staff_member'].queryset = MahhalaFY.objects.filter(
#             staff_member=self.instance.quarter.id)




