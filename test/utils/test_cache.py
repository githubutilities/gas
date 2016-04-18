#-*- coding: utf-8 -*-

import unittest

from gas.utils import pickle_helper

class CacheTest(unittest.TestCase):
    def test(self):
    	dic = {'hello': 'world'}
    	pickle_helper.save('dic', dic)
    	s = pickle_helper.load('dic')
    	self.assertEqual(s, {'hello': 'world'})
