warc-content
============

Simple warc archive content browser. This tool takes warc archives
as input, indexes them and creates a simple web page where you can
browse crawled urls in a tree grid.

I personaly will use this tool to locate useless links in crawled pages.
For example - calendars, print pages, image generators.

This is how the webpage looks:

![warc content webpage example](https://raw.github.com/martinsbalodis/warc-content/master/warccontent.png "warc content webpage example")

# Usage

```bash
./warccontent.py ~/warcs/*.warc.gz
```
Wait till data gets indexed and then open `http://localhost:8080/` in
your browser.


# features to add in the future
 * content size counter
 * regex tool to test against urls
 * multiple core support for thos gziped archives

# known issues
 * warc-tools library doesn't handle well large files within archives. Large files can cause MemoryError

# License
GPLv3