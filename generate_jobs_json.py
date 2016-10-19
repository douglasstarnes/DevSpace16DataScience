# feedparser is not part of the standard library.  If anaconda is installed, the command 'conda install feedparser' will install it.
import feedparser
import json

def get_id(haystack):
   needle = haystack[len(base):]
   first_slash = needle.find('/')
   return needle[:first_slash]

url = 'http://careers.stackoverflow.com/jobs/feed'
base = 'https://stackoverflow.com/jobs/'

feed = feedparser.parse(url)

jobs = []

for entry in feed['entries']:
     job = {}
     if 'tags' in entry.keys(): job['tags'] = [tag['term'] for tag in entry['tags']]
     if 'title' in entry.keys(): job['title'] = entry['title']
     if 'location' in entry.keys(): job['location'] = entry['location']
     if 'author' in entry.keys(): job['author'] = entry['author']
     if 'id' in entry.keys(): job['id'] = get_id(entry['id'])
     jobs.append(job)

f = open('socjobs.json', 'w')
f.write(json.dumps(jobs))
f.close()
