# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from django.test import TestCase

import json

from django.test import RequestFactory
from .lookups import MyLookup
from .models import choice_list, file_path, openmy_file, file_len

class ThingLookupTestCase(TestCase):

    def LaodFile(self):
        """test Loaded file"""
        self.loadfile = openmy_file(file_path)
        self.assertTrue (len(self.loadfile))

    def test_results(self):
        "Test Choice_list in memory is same as choice list loaded"
        self.assertEqual(len(choice_list), file_len)


    def test_results(self):
        "Test Choice_list."
        self.factory = RequestFactory()
        self.lookup = MyLookup()
        request = self.factory.get("/", {'term': 'Fa'})
        response = self.lookup.results(request)
        data = json.loads(response.content)['data']
        print len(data)
        print data
        self.assertTrue(len(data))
