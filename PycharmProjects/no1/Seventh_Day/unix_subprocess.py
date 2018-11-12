
#subprocess_os_system.py

import subprocess
import os
#
# completed = subprocess.run(['ls', '-1'])
# print('returncode:', completed.returncode)


#subprocess_shell_variables.py


# completed = subprocess.run('echo $HOME', shell=True)
# print('returncode:', completed.returncode)

#capturing the o/p

completed = subprocess.run(
    ['ls','-1'],
    stdout=subprocess.PIPE,
)


# print('returncode:', completed.returncode)
# print('Have {} bytes in stdout:\n{}'.format(
#     len(completed.stdout),
#     completed.stdout.decode('utf-8'))
# )
sum = 0
lis  = completed.stdout.decode('utf-8').strip().split('\n')

for var in lis:
    details = os.stat(var)
    sum+=details[6]

kb = sum/1024
print(str(kb)+'KB')

#os
#sys
#shutil
#subprocess
#logging
#time
#pickle
#re
#signal