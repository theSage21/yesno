import os
import subprocess
import sys
print('In absence of <no of recordings> it passively records 5 second slices forever')
print('Usage: $python record.py <no of recordings>')

command = 'arecord -r 44000 {}.wav'
try:
    sys.argv[1]
except IndexError:
    i = list(filter(lambda x: 'wav' in x, os.listdir('.')))
    i = int(list(sorted(i))[-1].replace('.wav', ''))
    print('starting count at ', i)
    while True:
        i += 1
        with subprocess.Popen(command.format(i), shell=True) as process:
            try:
                process.wait(timeout=5)
            except subprocess.TimeoutExpired:
                print('timeout')
                process.send_signal(2)
else:
    for i in range(int(sys.argv[1])):
        quit = input('Press q to quit. Press Ctrl+c to stop recording. Press Enter to start recording: ')
        if quit.strip() == 'q':
            print('Quitting')
            sys.exit(0)
        os.system(command.format(i))
