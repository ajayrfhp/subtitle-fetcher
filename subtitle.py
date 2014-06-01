import urllib2
import urllib
import os
import hashlib
import sys

user_agent='SubDB/1.0 (ajayrfhp/0.1; https://github.com/ajayrfhp/experiments-with-python--D)'
moviename=sys.argv[1]
language='en'
action='download'
base_url='http://api.thesubdb.com/?'
def get_hash(name):
    readsize = 64 * 1024
    with open(name, 'rb') as f:
        size = os.path.getsize(name)
        data = f.read(readsize)
        f.seek(-readsize, os.SEEK_END)
        data += f.read(readsize)
    return hashlib.md5(data).hexdigest()
hashed=get_hash(moviename)

content={
		'action':action,
		'hash':hashed,
		'language':language,
		} 
url=base_url+urllib.urlencode(content)
#url='http://api.thesubdb.com/?action=download&hash=edc1981d6459c6111fe36205b4aff6c2&language=pt,en'

req=urllib2.Request(url)

req.add_header('User-Agent', user_agent)

res=urllib2.urlopen(req)

subtitles=res.read()


#print subtitles

index=moviename.rfind('.')

file_name=moviename[0:index]+'.srt'

print file_name

try:
	f=open(file_name,'a')
	f.close()
	f=open(file_name,'w')
	f.write(subtitles)
	f.close()
	print 'success'
except:
	print 'failure'
