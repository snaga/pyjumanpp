#!/usr/bin/env python
# -*- coding: utf-8 -*-

import json
import requests
import sys

import zenhan

server_host = 'localhost'
server_port = '5000'

if len(sys.argv) <= 1:
    print "Usage: %s <text>" % sys.argv[0]
    sys.exit(0)

text = zenhan.h2z(sys.argv[1].decode('utf-8'))

r = requests.get('http://%s:%s/jumanpp?q=%s' % (server_host, server_port, text))
assert r.status_code == 200

d = json.loads(r.text)

print d['text']
for j in d['jumanpp']:
    print "['" + "','".join(j) + "']"
