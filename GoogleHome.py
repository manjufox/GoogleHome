
import pychromecast
from gtts_token import gtts_token
import urllib.parse
import sys

chromecasts = pychromecast.get_chromecasts()
cast = chromecasts[0]

def play_tts(text, lang='ja'):
   
    token = gtts_token.Token()
    tk = token.calculate_token(text)

    payload = {
        'ie' : 'UTF-8',
        'q' : text,
        'tl' : lang,
        'total' : 1,
        'idx' : 0,
        'textlen' : len(text),
        'tk' : tk,
        'client' : 't',
        'ttsspeed' : 1.0
    }

    params = urllib.parse.urlencode(payload, quote_via=urllib.parse.quote)
    url = 'https://translate.google.com/translate_tts?{}'.format(params)

    cast.wait()
    mc = cast.media_controller
    mc.play_media(url, 'audio/mp3')

if __name__=="__main__":
    text = "あいうえお"
    play_tts(text)