scpd-downloader
===============

Usage: python download.py [file]

The file should contain a list, consisting of one url per line, of resource
urls, each looking like `mms://.../[filename].wmv`.

The download script will download the files to the current folder with a
consistent naming convention based on class name and lecture date.

A good way of obtaining these urls one by one is to inspect the source code of
a SCPD video page with the WMP (not SL) option selected. This is laborious but
very simple.

The easiest way I've found of collecting all the urls for a class quickly is to
load one of the WMP SCPD video pages and recognize that every time one of the
lecture links in the right hand pane (under the 'Lectures' tab), the JavaScript
function 'openVideoWindow' gets invoked, a function which assigns
'WMPObject.URL' the very URL we're looking to download. Chrome's inspector
allows you to modify this function; I suggest the following modification:

```
urls = []
function openVideoWindow(...) {
  ...
  // part of the function that assigns WMPObject.URL
  urls.push(WMPObject.URL)
  ...
}
```

Now, clicking all the lecture links sequentially will populate `urls` with the
desired urls to download.
