# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from django import forms
from selectable.forms import AutoCompleteSelectField, AutoComboboxSelectWidget

from .lookups import MyLookup




class myform(forms.Form):
    apps_options =AutoCompleteSelectField(lookup_class=MyLookup, widget=AutoComboboxSelectWidget)
