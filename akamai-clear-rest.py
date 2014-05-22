#!/usr/bin/env python3

import sys
import urllib
import urllib3
import json
import argparse


parser = argparse.ArgumentParser()
group = parser.add_mutually_exclusive_group(required=True)
group.add_argument("--cpcode", help="CP code to clear")
group.add_argument("--object", help="Object to clear")
parser.add_argument("--user", help="Akamai user", required=True)
parser.add_argument("--pass", help="Akamai password", required=True)
args = parser.parse_args()

if args.cpcode is not None:
    postdata = json.dumps({'type': 'cpcode', 'objects': [args.cpcode]})
    print (postdata)
else:
    postdata = json.dumps({'objects': [args.object]})
    print (postdata)
