import re
import sys
import json
import urllib
import argparse
import requests
import datetime
import BeautifulSoup

_name = 'SmiteRank'
_usage = 'get-rank.py [options...] [IGN] [MODE]'
_description = 'Gets the smite rank of the streamer'
_author = 'Chris Diesch'
_version = '1.0.0'

_parser = argparse.ArgumentParser(prog=_name, usage=_usage, description=_description)

_parser.add_argument('ign')
_parser.add_argument('mode')
_parser.add_argument('-p', '--platform', default='PC', choices=['PC', 'pc',
                                                                'Xbox', 'xbox',
                                                                'Playstation', 'playstation'])

_ARGS = None

command = '!rank'
IGN_TO_SG = 'http://smite.guru/profile/$platform/$player_name/ranked'
PLATFORM_MAPPING = {'pc': 'pc', 'xbox': 'xb', 'playstation': 'ps'}

RANK_REGEX = r'.*%(?P<division>[A-Za-z ]*)' \
             r'(?P<elo>[0-9,]*)Elo' \
             r'(?P<tp>[0-9]*)TP' \
             r'(?P<win>[0-9]*)W' \
             r'(?P<loss>[0-9]*L)' \
             r'(?P<wr>[0-9.]*)%' \
             r'(?P<matches>[0-9]*).*'


def load_ranked_info():
    # convert the player name and platform to the url required ones (MUST ENSURE THE NAME IS URL SAFE!)
    platform_url = PLATFORM_MAPPING[_ARGS.platform]
    ign_url = urllib.quote(_ARGS.ign, safe='')
    # create the necessary url
    sg_url = IGN_TO_SG.replace('$platform', platform_url).replace('$player_name', ign_url)
    try:
        # data = urllib2.Request(sg_url, headers=hdr)
        # page = BeautifulSoup.BeautifulSoup(urllib2.urlopen(data))
        page = BeautifulSoup.BeautifulSoup(requests.get(sg_url).text)
        result = parse_page(page)
        result['url'] = sg_url
    except Exception as ex:
        time_stamp = datetime.datetime.now().strftime('%Y/%m/%d %H:%M:%S')
        result = 'Unable to load smite guru data for %s (Check here: %s)' % (_ARGS.ign, sg_url)
        sys.stderr.write('%s Unable to load SmiteGuru data!\n'
                         '   Exception: %s\n'
                         '   URL: "%s"' % (time_stamp, str(ex), sg_url))
    # convert the dict to a json string
    return json.dumps(result)


def parse_page(page):
    rank_data = ''
    results = page.findAll('div', {'class': 'widget'})
    for result in results:
        text = str(result.text)
        if _ARGS.mode in text:
            rank_data = text.replace(_ARGS.mode, '')
            break
    info = re.match(RANK_REGEX, rank_data)
    if info is not None:
        info = info.groupdict()
    else:
        info = {}
    return info

if __name__ == '__main__':
    _ARGS = _parser.parse_args()
    _ARGS.platform = _ARGS.platform.lower()
    print(load_ranked_info())

