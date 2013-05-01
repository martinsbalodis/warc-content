#!/usr/bin/env python
"""warccontent - simple WARC archive content browser"""

import os
import sys
from urlparse import urlparse
from optparse import OptionParser
import pickle
from urlparse import urlsplit
import webserver
import re

from hanzo.warctools import WarcRecord, expand_files

from urltree import UrlTree


parser = OptionParser(usage="%prog [options] warc (warc ...)")
parser.add_option("-p", "--persist-linkts", dest="persist_links", help="Persist link index")
parser.add_option("-i", "--ignore-links", dest="ignore_links", help="A file which consists of regular expressions for "
                                                                    "links to ignore. Use ^$ for expressions")
parser.add_option("-w", "--web-start", action="store_true", dest="web_start", help="Start a web server")
parser.add_option("-d", "--dump-links", dest="dump_links", help="A file where to dump parsed links")
parser.add_option("-c", "--content-type", dest="content_type", help="Filter by content type. For example text/html")
parser.add_option("-n", "--content-type-not", dest="content_type_not", help="Filter what content type should not be. For example text/html")

parser.set_defaults(persist_links=True, ignore_links=None, web_start=False, dump_links=None, content_type=False, content_type_not=False)

def prepare_link_ignore_re(ignore_links):

    if ignore_links is None:
        return []

    link_ignore_expressions = []
    with open(ignore_links) as f:
        expressions = f.readlines()
        for expression in expressions:
            if expression:
                link_ignore_expressions.append(re.compile(expression.strip()))
                print "expression: " + expression.strip()

    return link_ignore_expressions


def main(argv):
    (options, input_files) = parser.parse_args(args=argv[1:])

    # prepare regular expressions
    link_ignore_expressions = prepare_link_ignore_re(options.ignore_links)

    print "parsing WARC archives"

    all_urls = []

    for filename in expand_files(input_files):

        print "WARC: "+filename

        link_cache_filename = filename+'.urls'
        if options.persist_links and os.path.exists(link_cache_filename):
            url_fh = open(link_cache_filename, 'r')
            urls = pickle.load(url_fh)
            url_fh.close()
            all_urls += urls
        else:
            urls = []
            fh = WarcRecord.open_archive(filename, gzip="auto")
            for record in fh:

                record = record
                """@type : ArchiveRecord """

                if not record.is_response():
                    continue

                urls.append({
                    'url': record.url,
                    'content-type': record.content_content_type
                })

            # urls.sort(cmp=url_cmp)
            if options.persist_links:
                url_fh = open(link_cache_filename, 'w+')
                pickle.dump(urls, url_fh)
                url_fh.close()

            fh.close()
            all_urls += urls

    if options.dump_links is not None:

        f = open(options.dump_links, 'w+')
        all_urls.sort()
        for url in all_urls:
            # skip ignorable links
            skip_addition = False
            for expression in link_ignore_expressions:
                if expression.match(url['url']):
                    skip_addition = True
                    break
            if not skip_addition:
                f.write(url['url'])
                f.write('\n')
        f.close()

    if options.web_start is not False:
        urltree = UrlTree()
        for url in all_urls:
            # skip filtered links via regex
            skip_addition = False
            for expression in link_ignore_expressions:
                if expression.match(url['url']):
                    skip_addition = True
                    break
            # skip links filtered by content_type filter
            if options.content_type:
                if not url['content-type'].startswith(options.content_type):
                        skip_addition = True
            if options.content_type_not:
                if url['content-type'].startswith(options.content_type_not):
                        skip_addition = True

            if not skip_addition:
                urltree.add_url(url['url'])
        print "Total urls: "+str(urltree.childcount)
        webserver.run(urltree)

def run():
    sys.exit(main(sys.argv))

if __name__ == '__main__':
    run()