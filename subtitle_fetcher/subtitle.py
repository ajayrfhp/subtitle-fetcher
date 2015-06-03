import urllib2
import urllib
import os
import hashlib
import sys

def get_hash(name):
    readsize = 64 * 1024
    with open(name, 'rb') as f:
        size = os.path.getsize(name)
        data = f.read(readsize)
        f.seek(-readsize, os.SEEK_END)
        data += f.read(readsize)
    return hashlib.md5(data).hexdigest()

def main():
    user_agent = 'SubDB/1.0 (ajayrfhp/0.1; https://github.com/ajayrfhp/experiments-with-python--D)'
    movie_path = sys.argv[1]
    moviename = os.path.join(os.getcwd(), movie_path)
    language = 'en'
    action = 'download'
    base_url = 'http://api.thesubdb.com/?'
    hashed = get_hash(moviename)

    content = {
        'action': action,
        'hash': hashed,
        'language': language,
    }

    url = base_url + urllib.urlencode(content)
    req = urllib2.Request(url)
    req.add_header('User-Agent', user_agent)
    res = urllib2.urlopen(req)
    subtitles = res.read()

    index = moviename.rfind('.')
    file_name = moviename[0:index] + '.srt'
    print file_name
    with open(file_name, 'w') as f:
        f.write(subtitles)
