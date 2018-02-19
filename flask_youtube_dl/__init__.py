import subprocess
import os
import time
from flask import Flask, render_template, Response, request, send_file
from youtube_dl import YoutubeDL

app = Flask(__name__)

class Mylogger(object):
    def debug(self, msg):
        print (msg)
        pass

    def warning(self, msg):
        pass

    def error(self, msg):
        print(msg)

def my_hook(d):
    if d['status'] == 'finished':
        print('Done downloading, now converting ...')

ydl_opts = {
        'format': 'bestaudio',
        'postprocessors': [{
            'key': 'FFmpegExtractAudio',
            'preferredcodec': 'mp3',
            'preferredquality': '192',
            }],
            'logger': Mylogger(),
            'progress_hooks': [my_hook],
        }

@app.route('/')
def index():

    yt_url = request.args.get('url')
    filename = YoutubeDL({'forcefilename' : True,
        'quiet': True,
        'simulate': True})

    #output = subprocess.check_output(filename.download([yt_url]))

    #print(output)

    ydl = YoutubeDL(ydl_opts)

    ydl.download([yt_url])

    #filename =
    #script_dir = os.path.dirname(__file__)
    #os.path.join(script_dir, filename)

    #def generate_ytdl():
    #    x = 0
    #    while x <= 100:
    #        yield "data:" + str(x) + "\n\n"
    #        x = x + 10
    #        time.sleep(0.5)
    #    return

    return "ok"
    #return send_file('flask-youtube-dl.mp3', attachment_filename='flask-youtube-dl.mp3')
    #return Response(generate_ytdl(), mimetype= 'text/event-stream')
