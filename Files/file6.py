f=open('file.txt', 'r')
data = f.read(12);
print('String is : ', data)
position = f.tell()
print('Current file position : ', position)
position = f.seek(0)
data = f.read()
print('String is : ', data)
f.close()

