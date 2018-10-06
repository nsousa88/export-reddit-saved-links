#!/usr/bin/env python

import praw
import OAuth2Util
import webbrowser

import sys
reload(sys)
sys.setdefaultencoding('utf-8')

#enter username and password
username = ""
password = ""

r = praw.Reddit("get all saved links")
o = OAuth2Util.OAuth2Util(r, configfile="oauthconfigurations.ini")
o.refresh(force=True)

me = r.get_me()

savedPosts = me.get_saved(limit=None)

f = open('/~/redditsavedlinks.html', 'w')

f.write ("<!DOCTYPE html>\n<head>\n<title>\nAll saved posts from reddit\n</title>\n<style type=\"text/css\">\n" +
	".even{\nbackground-color: #E8E8E8;\n}\n" +
	".odd{\nbackground-color: #C0C0C0;\n}\n" +
	"</style>\n</head>\n<body>\n\n")

f.write ("All saved posts from reddit<br /><br />\n\n")

f.write ("<table id=\"table\" align=\"center\">\n" +
	"<thead>\n" +
	"<tr>\n" +
	"<td>title</td>\n" +
	"<td>post id</td>\n" +
	"<td>subreddit</td>\n" +
	"<td>score</td>\n" +
	"<td>comments</td>\n" +
	"<td>nsfw</td>\n" +
	"<td>url</td>\n" +
	"</tr>\n" +
	"</thead>\n" +
	"<tbody>\n")

count = 0
for post in savedPosts:
		if (count%2 == 0):
			f.write ("<tr class = \"even\">\n")
		else:
			f.write ("<tr class = \"odd\">\n")
		f.write ("<td>{0}</td>\n" .format(post.title))
		f.write ("<td><a href=\"http://redd.it/{0}\">http://redd.it/{0}</a></td>\n" .format(post.id))
		f.write ("<td>{0}</td>\n" .format(post.subreddit))
		f.write ("<td>{0}</td>\n" .format(post.score))
		f.write ("<td>{0}</td>\n" .format(post.num_comments))
		f.write ("<td>{0}</td>\n" .format(post.over_18))
		f.write ("<td><a href=\"{0}\">{0}</a></td>\n" .format(post.url))
		f.write ("</tr>\n\n")
		post.unsave()
		count = count +1

f.write ("</tbody>\n</table>\n")

f.write ("Done: count = {0}\n" .format(count))

f.write ("\n</body>\n</html>")
f.close()

webbrowser.get("firefox").open_new_tab("/~/redditsavedlinks.html")
