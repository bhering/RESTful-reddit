import http.client

conn = http.client.HTTPSConnection("api.reddit.com")

headers = {
    'Cache-Control': "no-cache",
    'User-agent': "bhering bot 0.2"
    }

conn.request("GET", "/r/artificial/hot", headers=headers)

res = conn.getresponse()
data = res.read()

print(res.status, res.reason)
print(data.decode("utf-8"))
