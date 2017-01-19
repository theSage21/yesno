import os
import sys
print('Usage: $python record.py <non of recordings>')
for i in range(int(sys.argv[1])):
    quit = input('Press q to quit. Press Ctrl+c to stop recording. Press Enter to start recording: ')
    if quit in 'Qq':
        sys.exit(0)
    os.system('arecord -r 44000 {}.wav'.format(i))
