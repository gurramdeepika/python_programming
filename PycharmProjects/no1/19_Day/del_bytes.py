import os
import subprocess


# completed = subprocess.run('cd /home/cisco/PycharmProjects/no1/19_Day/del_files')
completed=  subprocess.run(['ls','-1'],
    stdout=subprocess.PIPE)


lis  = completed.stdout.decode('utf-8').strip().split('\n')
for var in lis:
    details=os.stat ( var )
    if details[6] == 0:
        os.unlink(var)
    print(details[6])

print(lis)