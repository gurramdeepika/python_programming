import os
import subprocess
import sys
import paramiko

def sendfile(file):
    ssh=paramiko.SSHClient ( )
    ssh.set_missing_host_key_policy ( paramiko.AutoAddPolicy ( ) )
    ssh.connect ( hostname='localhost' , username="cisco" , password="cisco" , port='22' )

    sftp=ssh.open_sftp ( )
    localpath=file
    remotepath='/tmp/largefile.txt'

    sftp.put ( localpath , remotepath )
    sftp.close ( )
    ssh.close ( )

r,w = os.pipe()
pid=os.fork()  # which is a system call which is creating the one more process in the memory
if pid:
    os.wait()
    #this is the parent process
    #closes file descriptor
    os.close(w)
    r= os.fdopen(r)
    print("parent reading")
    mstr = r.read()
    print("text =",mstr)
    completed=subprocess.run ( [ 'ls' , '-1' ] ,
                               stdout=subprocess.PIPE )

    lis=completed.stdout.decode ( 'utf-8' ).strip ( ).split ( '\n' )
    dic={}
    lis1=[ ]
    for var in lis:
        details=os.stat ( var )
        dic[ details[ 6 ] ]=var
        lis1.append ( details[ 6 ] )
    print ( lis )

    print ( dic )
    lis1.sort ( reverse=True ) #max(lis1)
    file = dic[ lis1[ 0 ] ]
    print ( 'Largest file:' , dic[ lis1[ 0 ] ] , 'Size:' , lis1[ 0 ] )
    sendfile(file)
    sys.exit(0)

else:
    #this is the child process
    os.close(r)
    w = os.fdopen(w,'w')
    print('child writing')
    w.write("text written by child")
    w.close()
    print("child closing")
    sys.exit(0)

