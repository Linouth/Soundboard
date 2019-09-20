import os
from flask import Flask, render_template
import mpv


app = Flask(__name__, instance_relative_config=True)
player = mpv.MPV()

BASE_DIR = 'sounds'


@app.route('/hello')
def hello():
    return 'Hello World!'


@app.route('/')
def root():
    return listing('')

@app.route('/favicon.ico')
@app.route('/favicon.ico/')
def favico():
    return ''


@app.route('/play/<path:filename>', methods=(['GET']))
def play(filename):
    path = os.path.join(BASE_DIR, filename)
    if os.path.exists(path):
        player.play(path)
        print(f'Playing file: {path}')
        return 'OK'
    return 'File Not Found'


@app.route('/<path:directory>/')
def listing(directory):
    files = []
    dirs = []
    path = os.path.join(os.path.relpath(BASE_DIR), directory)
    for c in os.listdir(path):
        cpath = os.path.join(path, c)
        if os.path.isdir(cpath):
            dirs.append(os.path.relpath(cpath, path))
        else:
            files.append(os.path.relpath(cpath, path))

    return render_template('index.html', current_dir=directory, files=sorted(files), dirs=sorted(dirs))


if __name__ == '__main__':
    if os.path.isdir(BASE_DIR):
        app.run(host='0.0.0.0')
    else:
        print(f'Directory {BASE_DIR} not found')
