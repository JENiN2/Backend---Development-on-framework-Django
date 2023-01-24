from urllib import request

response = request.urlopen('http://example.com')
print(response)

print(response.status)
print(response.getcode())
print(response.msg)
print(response.reason)
print()

print(response.headers)
print()

print(response.getheaders())
print()

print(response.headers.get('Etag'))
print()

print(response.getheader('Etag'))
print()

print(response.url)
print()
