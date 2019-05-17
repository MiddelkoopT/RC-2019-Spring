#!/usr/bin/python3

import re
import sys

debug=False

if debug: print("Filter phone numbers>")

# Timothy Middelkoop (314)300-9999
# 573-882-2320 Tim Middelkoop
# Test 1 +1-555-1212
#12345678901234567890123456789012345678901234567890
#              (1         ) (2    )     (3    )
p1=re.compile('(\d{3})[-. )](\d{3})[-. ](\d{4})')

for l in sys.stdin:
    l=l[:-1]
    if debug: print("+++",l)
    m=p1.search(l)
    if m is None:
        print(",,,")
        continue
    #print(m)
    print("%s,%s,%s" % (m.group(1),m.group(2),m.group(3)))
    


