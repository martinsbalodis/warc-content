from unittest import TestCase
from warccontent.urltree import UrlTree
import pprint

class TestUrlTree(TestCase):
    def test_add_url_simple(self):
        urltree = UrlTree()
        urltree.add_url('http://example.com/')
        self.assertEquals(urltree.urltree, {
            'childcount': 1,
            'path': 'root',
            'children': [
                {'path': 'example.com/',
                 'childcount': 1,
                 'children':
                     [
                         {
                             'url': 'http://example.com/',
                             'leaf': True,
                         }
                     ]
                }
            ]})


    def test_add_url_tree(self):
        urltree = UrlTree()
        urltree.add_url('http://example.com/')
        urltree.add_url('http://example.com/a/')
        urltree.add_url('http://example.com/a/b/')
        self.maxDiff = None
        print urltree.urltree
        self.assertEquals(urltree.urltree, {
            'path':'root',
            'childcount':3,
            'children':[
                {
                    'path':'example.com/',
                    'childcount':3,
                    'children':[
                        {
                            'url':'http://example.com/',
                            'leaf':True
                        },
                        {
                            'path':'a/',
                            'childcount':2,
                            'children':[
                                {
                                    'url':'http://example.com/a/',
                                    'leaf':True
                                },
                                {
                                    'path':'b/',
                                    'childcount':1,
                                    'children':[
                                        {
                                            'url':'http://example.com/a/b/',
                                            'leaf':True
                                        }
                                    ]
                                }
                            ]
                        }
                    ]
                }
            ],

        })