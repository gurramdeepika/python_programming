import ftplib

f = ftplib.FTP('ftp.gnu.org','anonymous','abcdef@alphabets.com')
files = []
#ftp.oreilly.com
print(f.retrlines('LIST',files.append))
print(len(files))
print(files[0])

