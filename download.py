import os
import sys

if len(sys.argv) != 2:
  print 'usage: %s [filename]' % sys.argv[0]

lines = []

with open(sys.argv[1]) as fin:
  lines = fin.readlines()
  fin.close()

for url in lines:
  spl = url.split('/')
  fname = '%s-%s.wmv' % (spl[4], spl[6].split('-')[0])
  os.system('mimms -c %s %s' % (url, fname))
