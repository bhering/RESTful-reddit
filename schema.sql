CREATE TABLE post (
	id integer primary key autoincrement,
	title string,
	author string,
	timestamp datetime,
	ups integer,
	downs integer,
	num_comments integer
);

