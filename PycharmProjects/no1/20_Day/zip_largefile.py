import zipfile
zip = zipfile.ZipFile('txtfiles.zip','w')

try:
    zip.write('one.txt')
    zip.write('two.txt')
finally:
    print('Reading files now.')
    zip.close()



zip=zipfile.ZipFile('txtfiles.zip','r')

print(zip)

for finfo in zip.infolist():
        if finfo.file_size == 0:
            print(finfo.filename ,'has',finfo.file_size)
