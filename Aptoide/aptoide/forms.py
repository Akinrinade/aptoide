# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from django import forms
from selectable.forms import AutoCompleteSelectField, AutoComboboxSelectWidget

from .lookups import MyLookup


#
# class myform(forms.ModelForm):
#
#     # choices=autocomplete.Select2ListChoiceField(choice_list=openmy_file,
#     #     widget=autocomplete.ListSelect2(url='my-autocomplete')
#     # )
#     class Meta:
#         model=my_options
#         fields=('__all__')
#         autocomplete_fields = 'app_options'
#         widgets = {
#             "app_options": autocomplete.ListSelect2(url='my-autocomplete'),
#         }


class myform(forms.Form):
    apps_options =AutoCompleteSelectField(lookup_class=MyLookup, widget=AutoComboboxSelectWidget)
    # class Meta:
        #
        # fields = ('app_options',)
        # widgets = {
        #     'app_options': autocomplete.ListSelect2(url='my-autocomplete'),
        # }