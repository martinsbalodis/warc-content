from unittest import TestCase
from warccontent.urltree import UrlTree
import pprint

class TestUrlTree(TestCase):
    def test_add_url_simple(self):
        urltree = UrlTree()
        urltree.add_url('/')
        self.assertEquals(urltree.urltree, {
            'childcount': 1,
            'path': 'root',
            'children': [
                {'path': '/',
                 'childcount': 1,
                 'children':
                     [
                         {'url': '/'}
                     ]
                }
            ]})


    def test_add_url_tree(self):
        urltree = UrlTree()
        urltree.add_url('/')
        urltree.add_url('/a/')
        urltree.add_url('/a/b/')
        self.maxDiff = None

        self.assertEquals(urltree.urltree, {
            'childcount': 3,
            'path': 'root',
            'children': [
                {
                    'path': '/',
                    'childcount': 3,
                    'children': [
                        {
                            'url': '/'
                        },
                        {
                            'childcount': 2,
                            'path': 'a/',
                            'children': [
                                {
                                    'url': '/a/'
                                },
                                {
                                    'childcount': 1,
                                    'path': 'b/',
                                    'children': [
                                        {
                                            'url': '/a/b/'
                                        }
                                    ],
                                }
                            ],
                        }
                    ],
                }
            ]
        })