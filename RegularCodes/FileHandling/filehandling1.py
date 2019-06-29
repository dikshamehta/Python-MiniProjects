import os
print(os.getcwd())
os.chdir('/home/tonystark')
print(os.getcwd())

#os.makedirs(os.path.join('/home/tonystark/Documents/Python Programs/testfolder'))
print(os.path.abspath('..'))
print(os.path.isabs('/home/tonystark'))

p= '/home/tonystark/Documents/Python Programs'
print(os.path.basename(p))

print(os.path.dirname(p))

print(os.path.split(p))

print(os.sep)
print(p.split(os.sep))
