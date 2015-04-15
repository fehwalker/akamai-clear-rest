#!/usr/bin/env python

import json
import argparse
import requests
import time

ccu_base = "https://api.ccu.akamai.com"
ccu_endpoint = ccu_base+"/ccu/v2/queues/default"
headers = {'content-type': 'application/json'}

parser = argparse.ArgumentParser()
group = parser.add_mutually_exclusive_group(required=True)
group.add_argument("--cpcode", help="CP code to clear")
group.add_argument("--object", help="Object to clear (can specify multiple times)", action='append')
parser.add_argument("--user", help="Akamai user", required=True)
parser.add_argument("--passwd", help="Akamai password", required=True)
parser.add_argument("--timemult", help="Muliplier for Akamai estimated clear time (optional, default 1.5)", required=False)
args = parser.parse_args()

if args.cpcode is not None:
    postdata = json.dumps({'type': 'cpcode', 'objects': [args.cpcode]})
else:
    postdata = json.dumps({'objects': args.object})

r = requests.post(ccu_endpoint, data=postdata, headers=headers, auth=(args.user, args.passwd))
if r.encoding is not None:
    print "Error, unexpected data received:\n ",r.text
    exit(1)
else:
    resp = json.loads(r.text)
    if resp['httpStatus'] < 200 or resp['httpStatus'] > 299:
        print "Error, request not submitted\n\thttpStatus: ", resp['httpStatus'], "\n\ttitle: ", resp['title'], "\n\tdetail: ", resp['detail'], "\n\tdescribedBy: ", resp['describedBy']
        exit(1)
    else:
        print "Request submitted OK\n\tEstimated time to clear: ", resp['estimatedSeconds']/60, "minutes\n\tCheck URL: ", ccu_base+resp['progressUri']

	status_uri = ccu_base + resp['progressUri']
	if args.timemult > 0:
		duration = resp['estimatedSeconds'] * args.timemult
        else:
		duration = resp['estimatedSeconds'] * 1.5
	end_time = time.time() + duration
	print "\t++ Sleeping 60 seconds..."
	time.sleep(60)
	while end_time > time.time():
		r = requests.get(status_uri, headers=headers, auth=(args.user, args.passwd))
		resp_status = json.loads(r.text)
		if resp_status['purgeStatus'] == 'Done':
			print "Purge complete!"
			exit(0)
		else:
			print "\t++ purge still running, sleeping 60 seconds..."
			time.sleep(60)
	print "Clear did not complete within ", duration/60, " minutes!"
	exit(1)
