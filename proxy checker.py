import urllib.request

proxy_handler = urllib.request.ProxyHandler({'http': 'http://142.54.226.214'})
opener = urllib.request.build_opener(proxy_handler)

try:
    response = opener.open('http://www.google.com')
    print("Proxy is working.")
except urllib.error.URLError:
    print("Proxy is not working.")
