import os
import sys
print('Usage: $python record.py <non of recordings>')
for i in range(int(sys.argv[1])):
    input('>')
    os.system('arecord -r 44000 {}.wav'.format(i))
