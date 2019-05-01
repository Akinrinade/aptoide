"""Lookup file as specified by Dajngo selectable for
    filtering list
"""

from __future__ import unicode_literals

from selectable.base import LookupBase
from selectable.registry import registry
from .models import choice_list


class MyLookup(LookupBase):
    """ A simple call to filter list based on received query term"""
    def get_query(self, request, term):
        data = choice_list
        return [x[0] for x in data if x[0].lower().startswith(term.lower())]


registry.register(MyLookup) #register the lookup