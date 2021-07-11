  
import os
statinfo = os.stat('test.txt')
print(statinfo.st_size, 'bytes')