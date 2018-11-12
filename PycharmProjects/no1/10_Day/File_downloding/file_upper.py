from ftplib import FTP
import logging
import re
import socket
import paramiko

class FtpUpper:

    LOG_FILENAME = 'logging_example.out'
    logging.basicConfig (
        filename=LOG_FILENAME ,
        level=logging.DEBUG ,
    )


    def downloadfile( self ):

      logging.info ( 'Enters to downloadfile()' )

      ftp = FTP('ftp.gnu.org')     # connect to host, default port
      ftp.login()
      logging.info ( 'logged in to ftp server' )

      lis = ftp.retrlines('LIST')
      print(lis)
      if not lis:
          logging.error ( 'no files' )
          return

      ftp.retrbinary('RETR README', open('README', 'wb').write)
      logging.info ( 'Downloaded the Readme.txt in the current directory' )

      ftp.quit()

      logging.info ( 'Exit from downloadfile()' )

    def w_readme( self ):
        stt = re.compile('the')
        f = open("/home/cisco/PycharmProjects/no1/10_Day/File_downloding/README")
        data = f.readlines()
        lis = []
        for d in data:
            if stt.search(d):
                lis.append(self.receive_from_server(d))
        self.w_file(lis)


    def receive_from_server( self,data):

        sock = socket.socket ( socket.AF_INET , socket.SOCK_STREAM )
        server_address = ('localhost' , 10000)
        sock.connect ( server_address )
        sock.send( bytes(data,"utf-8"))
        data , addr = sock.recvfrom ( 200 )
        data = data.decode("utf-8")
        return data

    def w_file( self ,d):
        f = open("the.txt",'w')
        addr = '127.0.0.1'
        for var in d:
            var = var.replace('127.0.0.1','')
            f.write(var+'\n')
        f.close()



    def send_file (self):

        ssh = paramiko.SSHClient ( )
        ssh.set_missing_host_key_policy ( paramiko.AutoAddPolicy ( ) )
        ssh.connect ( hostname='localhost' , username="cisco" , password="cisco" , port='22' )

        sftp = ssh.open_sftp ( )
        localpath = 'the.txt'
        remotepath = '/tmp/the1.txt'

        sftp.put(localpath,remotepath)
        sftp.close ( )
        ssh.close ( )

    def receive_file( self ):
        ssh = paramiko.SSHClient ( )
        ssh.set_missing_host_key_policy ( paramiko.AutoAddPolicy ( ) )
        ssh.connect ( hostname='localhost' , username="cisco" , password="cisco" , port='22' )

        sftp = ssh.open_sftp ( )
        localpath = '/home/cisco/PycharmProjects/no1/10_Day/File_downloding/the2.txt'
        remotepath = '/tmp/the1.txt'

        sftp.put ( remotepath , localpath )
        sftp.close ( )
        ssh.close ( )

if __name__ == '__main__':
    FtpUpper().downloadfile()
    FtpUpper().w_readme()
    FtpUpper().send_file()
    FtpUpper().receive_file()
