from urlparse import urlsplit

def url_paths(url):
    url = urlsplit(url)
    path = url.netloc+url.path

    if path.endswith('/'):
        return path[:-1].split("/")
    else:
        return path.split("/")

class UrlTree(object):

    def __init__(self):
        self.urltree = {
            'children':[],
            'childcount': 0,
            'path': 'root',
        }

        self.urltree_skeleton = {
            'children':{},
        }

    def add_url(self, url):
        paths = url_paths(url)

        urltree_skeleton = self.urltree_skeleton
        urltree = self.urltree
        self._add_url(paths, urltree, urltree_skeleton, url)

    def _add_url(self, paths, urltree, urltree_skeleton, url):

        if(len(paths) < 1):
            urltree['children'].append({
                'url': url,
                'leaf': True,
            })
            urltree['childcount'] +=1
            return

        path = paths[0]+'/'
        if path not in urltree_skeleton['children']:
            urltree_skeleton['children'][path] = {
                'children': {},
                'urltree' : {
                    'path':path,
                    'childcount':0,
                    'children': []
                }
            }
            urltree['children'].append(urltree_skeleton['children'][path]['urltree'])

        urltree['childcount'] +=1
        urltree = urltree_skeleton['children'][path]['urltree']
        urltree_skeleton = urltree_skeleton['children'][path]
        self._add_url(paths[1:], urltree, urltree_skeleton, url)


