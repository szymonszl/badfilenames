#!/usr/bin/env python3
for i in range(1,32):
    f = open(chr(i),'w')
    f.write(chr(i))
    f.close()
