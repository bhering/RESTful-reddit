import http.client
import json
from pprint import pprint

def do_fetch(rest_arg='/r/artificial/hot'):
	conn = http.client.HTTPSConnection("api.reddit.com")

	headers = {
	   		'Cache-Control': "no-cache",
    		'User-agent': "bhering bot 0.2"
	    }

	conn.request("GET", rest_arg, headers=headers)

	res = conn.getresponse()
	data = res.read()

	return json.loads(data.decode("utf-8")), res.status, res.reason


def extract_posts(data):
	posts,_,_=data
	posts=posts['data']['children']
	for post in posts:
		post_data=post['data']
		yield 	{
					'title':post_data['title'],
					'author':post_data['author'],
					'timestamp':post_data['created_utc'],
					'ups':post_data['ups'],
					'downs':post_data['downs'],
					'num_comments':post_data['num_comments'],
				}


if __name__=="__main__":
	raw_data=do_fetch()
	posts=[post for post in extract_posts(raw_data)]
	pprint(posts)
