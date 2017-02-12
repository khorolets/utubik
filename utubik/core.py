"""
utubik - is a helper class to perform some actions with YouTube's videos (mostly reading)
"""
import json
import requests
from urllib import parse


class YouTube(object):
    def __init__(self, url):
        self.url = url
        self.id = self._get_id()
        self.data = self._process_url()

    def _process_url(self):
        r = requests.get('http://www.youtube.com/oembed?url=%s&format=json' % self.url)
        data = json.loads(r.text)
        data['thumbnail_url'] = data['thumbnail_url'].replace('hqdefault', 'maxresdefault')
        return data

    def _get_id(self):
        y = parse.urlparse(self.url)
        try:
            return parse.parse_qs(y.query)['v'][0]
        except:
            return None

    def _additional_info(self):
        # https://www.googleapis.com/youtube/v3/videos?part=recordingDetails,snippet,player,contentDetails&id=iI51Gh5HI0o&key=AIzaSyD7JirBUVOhmjWVPIGbS9x8dvN71-Unhoc
        raise NotImplemented()

    @staticmethod
    def find_urls_in_text(text):
        """
        Finds all matches of youtube's urls in given text and returns it as a list.
        If no urls have been found method returns False
        Args:
            text: srting/unicode

        Returns:
            False/list of string links
        """
        youtube_regex = re.compile(r'(youtu(?:\.be/([-\w]+)|be\.com/watch\?v=[-\w]+))\S*')

        youtube_regex_match = youtube_regex.findall(text)
        if len(youtube_regex_match):
            return [match[0] for match in youtube_regex_match]

        return False
