# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from django.shortcuts import render
from .forms import myform


def myview(request):
    """Create a simple view to display the form"""

    template = 'aptoide.html' #template name
    form = myform     #form name

    return render(request, template, {'form': form})

