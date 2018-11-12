from tqdm import tqdm
import sys
import paramiko

def viewBar(a,b):
    res = a/int(b)*100
    sys.stdout.write("\rComplete precent: %.2f %%" %(res))
    sys.stdout.flush()

def viewBar2(a,b):
    pbar = tqdm(total=int(b),ascii=True,unit='b',unit_scale=True)
    pbar.update(a)

t = paramiko.Transport(('localhost',22))
t.connect(username='cisco',password='cisco')

sftp = paramiko.SFTPClient.from_transport(t)
sftp.put("thebook.pdf",'/home/cisco/PycharmProjects/no1/10_Day/mcbook2.pdf',callback=viewBar2)
t.close()