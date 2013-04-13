#!/usr/bin/env python
"""warccontent - simple WARC archive content browser"""

import os
import sys
from urlparse import urlparse
from optparse import OptionParser
import pickle
from urlparse import urlsplit
import webserver

from hanzo.warctools import WarcRecord, expand_files

from urltree import UrlTree


parser = OptionParser(usage="%prog [options] warc (warc ...)")
parser.add_option("-p", "--persist-linkts", dest="persist_links", help="Persist link index")
parser.set_defaults(persist_links=True)

def main(argv):
    (options, input_files) = parser.parse_args(args=argv[1:])

    print "parsing WARC archives"

    all_urls = []

    for filename in expand_files(input_files):

        print "WARC: "+filename

        link_cache_filename = filename+'.urls'
        if options.persist_links and os.path.exists(link_cache_filename):
            url_fh = open(link_cache_filename,'r')
            urls = pickle.load(url_fh)
            url_fh.close()
            all_urls+= urls
        else:
            urls = []
            fh = WarcRecord.open_archive(filename, gzip="auto")
            for record in fh:

                record=record
                """@type : ArchiveRecord """

                if not record.is_response():
                    continue

                urls.append(record.url)

            # urls.sort(cmp=url_cmp)
            if options.persist_links:
                url_fh = open(link_cache_filename,'w+')
                pickle.dump(urls, url_fh)
                url_fh.close()

            fh.close()
            all_urls+= urls


    urltree = UrlTree()
    for url in all_urls:
        urltree.add_url(url)

    webserver.run(urltree)

def run():
    sys.exit(main(sys.argv))

if __name__ == '__main__':
    run()