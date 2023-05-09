#!/usr/bin/env python

import os.path
import re
import urllib.request

# fetch latest tlds file from iana
r = urllib.request.urlopen("https://data.iana.org/TLD/tlds-alpha-by-domain.txt")
assert r.status == 200
lines = r.read().decode("utf-8").split("\n")

# parse version and write it out
header = lines.pop(0)
if match := re.match("^# Version (?P<version>[0-9]+).*$", header):
    version = match.group("version")
    with open("./version", "w") as fd:
        fd.write(version)
else:
    raise RuntimeError("Failed to match version")

# format tlds and write them out
tlds = [line.lower() for line in lines if line and not line.startswith("#")]
target_dir = os.path.abspath("./tlds")
with open(os.path.join(target_dir, "_data.py"), "w") as fd:
    fd.write("tld_set = set(%s)\n" % (tlds,))
