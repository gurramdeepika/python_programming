import os
import paramiko

def printTotals(transferred, toBeTransferred):
    print("transferred: {0}\tOut of: {1}".format(transferred, toBeTransferred))

ssh = paramiko.SSHClient()
ssh.set_missing_host_key_policy(paramiko.AutoAddPolicy())
ssh.connect(hostname='localhost',username="cisco",password="cisco",port='22')

sftp = ssh.open_sftp()
localpath = 'hello.py'
remotepath = '/tmp/urname.py'

#sftp.put(localpath,remotepath)
sftp.put(localpath,remotepath,callback=printTotals)
sftp.close()
ssh.close()