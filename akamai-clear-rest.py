#!/usr/bin/env python3

import sys
import urllib
import json
import argparse
import requests

ccu_base = "https://api.ccu.akamai.com"
ccu_endpoint = ccu_base+"/ccu/v2/queues/default"
headers = {'content-type': 'application/json'}

parser = argparse.ArgumentParser()
group = parser.add_mutually_exclusive_group(required=True)
group.add_argument("--cpcode", help="CP code to clear")
group.add_argument("--object", help="Object to clear (can specify multiple times)", action='append')
parser.add_argument("--user", help="Akamai user", required=True)
parser.add_argument("--passwd", help="Akamai password", required=True)
args = parser.parse_args()

if args.cpcode is not None:
    postdata = json.dumps({'type': 'cpcode', 'objects': [args.cpcode]})
else:
    postdata = json.dumps({'objects': args.object})

r = requests.post(ccu_endpoint, data=postdata, headers=headers, auth=(args.user, args.passwd))
if r.encoding is not None:
    print ("Error, unexpected data received:\n ",r.text)
    exit(1)
else:
    resp = json.loads(r.text)
    if resp['httpStatus'] < 200 or resp['httpStatus'] > 299:
        print ("Error, request not submitted\n\thttpStatus: ", resp['httpStatus'], "\n\ttitle: ", resp['title'], "\n\tdetail: ", resp['detail'], "\n\tdescribedBy: ", resp['describedBy'])
        exit(1)
    else:
        print ("Request submitted OK\n\tEstimated time to clear: ", resp['estimatedSeconds']/60, "minutes\n\tCheck URL: ", ccu_base+resp['progressUri'])
