import os
import sys

if len(sys.argv) != 2:
  print 'usage: %s [filename]' % sys.argv[0]
  exit(0)

lines = []

with open(sys.argv[1]) as fin:
  lines = [l.strip() for l in fin.readlines()]
  fin.close()

for url in lines:
  spl = url.split('/')
  fname = '"%s-%s.wmv"' % (spl[4], spl[6].split('-')[0])
  os.system('mimms -c %s tmp' % url)
  os.system('mv tmp %s' % fname)

print 'done'
