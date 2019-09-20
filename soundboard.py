import os
from flask import Flask, render_template
import mpv

app = Flask(__name__, instance_relative_config=True)
player = mpv.MPV()

try:
    os.makedirs(app.instance_path)
except OSError:
    pass

@app.route('/hello')
def hello():
    return 'Hello World!'


@app.route('/')
def root():
    return listing('')


@app.route('/play/<path:filename>', methods=(['GET']))
def play(filename):
    print(filename)
    path = os.path.join(app.instance_path, filename)
    if os.path.exists(path):
        # player.play(path)
        return 'OK'
    return 'File Not Found'


@app.route('/<path:directory>/')
def listing(directory):
    files = []
    dirs = []
    path = os.path.join(os.path.relpath(app.instance_path), directory)
    for c in os.listdir(path):
        cpath = os.path.join(path, c)
        if os.path.isdir(cpath):
            dirs.append(os.path.relpath(cpath, path))
        else:
            files.append(os.path.relpath(cpath, path))

    return render_template('index.html', files=sorted(files), dirs=sorted(dirs))
