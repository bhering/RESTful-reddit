import http.client
import json
import schedule
import sqlite3
from sys import argv
import time

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
		yield 	[
					post_data['title'],
					post_data['author'],
					post_data['created_utc'],
					post_data['ups'],
					post_data['downs'],
					post_data['num_comments'],
				]

# there should be a more elegant way than this, but for now, this is what i'm using
def db_handler(data, db_url='./posts.db'):
	db=sqlite3.connect(db_url)
	db.row_factory=sqlite3.Row
	for d in data:
		db.execute(
		'insert into post (title, author, timestamp, ups, downs, num_comments)'+
		' values (?, ?, ?, ?, ?, ?)', d )
	db.commit()
	db.close()

def job():
	db_handler(extract_posts(do_fetch()))


if __name__=="__main__":
	if len(argv) < 2:
		job()

	else:
		# while i'm using this API i could totally do a cron job instead
		schedule.every().day.at(argv[1]).do(job)
		while True:
			schedule.run_pending()
			time.sleep(60)
