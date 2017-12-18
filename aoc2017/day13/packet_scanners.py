from itertools import count

def caught(scanners, t, delta):
    if t-delta in scanners:
        length = (scanners[t-delta]-1)*2
        return t%length == 0
    return False

def severity(scanners, delta=0):
    severity = 0
    for t in range(delta, delta+max(scanners)+1):
        if caught(scanners, t, delta):
            severity += (scanners[t-delta]*t)
    return severity

def find_delta(scanners):
    return next(d for d in count() if not severity(scanners, d))

scanners = {} 
with open('input_short') as f:
    for line in f:
        line = line.replace(':', '')
        d, r = line.split()
        scanners[int(d)] = int(r)

print(severity(scanners))
print(find_delta(scanners))
