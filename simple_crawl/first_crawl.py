import urllib2

def download(url, num_retries=2):
    print('Downloading ' + url)
    try:
        html = urllib2.urlopen(url).read()
    except urllib2.URLError as e:
        print('Download error ' + str(e.reason))
        html = None
        if num_retries > 0 and e.code in range(500, 601):
            return download(url, num_retries-1)
    return html
