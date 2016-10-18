#!/usr/bin/env python
# -*- coding: utf-8 -*-

import json
import subprocess

from flask import Flask, request
app = Flask(__name__)

def popen_jumanapp():
    p = subprocess.Popen(['/usr/local/bin/jumanpp'],
                         stdin=subprocess.PIPE,
                         stdout=subprocess.PIPE,
                         stderr=subprocess.PIPE)
    assert p is not None
    return p

jumanpp = popen_jumanapp()

@app.route("/jumanpp")
def _jumanpp():
    global jumanpp

    text = request.args.get('q')
    if text is None or len(text) == 0:
        return json.dumps({'text': None, 'jumanpp': None})

    (stdout_data, stderr_data) = jumanpp.communicate(text.encode('utf-8') + '\n')
    assert stdout_data is not None
    assert stderr_data is not None

    jumanpp = popen_jumanapp()

    tokens = stdout_data.split('\n')
    res = []
    for t in tokens:
        tt = t.split(' ')
        res.append(tt)
        if t == 'EOS':
            break

    return json.dumps({'text': text, 'jumanpp': res})

server_host = '0.0.0.0'
server_port = '5000'

if __name__ == "__main__":
    app.run(host=server_host, port=server_port)
