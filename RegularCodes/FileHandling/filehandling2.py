import os
print(os.getcwd())
f=open('testfile1.txt','w')#current folder mai bnegi ye file, aap currenlty jis folder mai hoge
f.write("hello how are you, I am fine and hope the same for you")

list=["a\n","b\n","c\n","d\n"]
f.writelines(list)

f.close()

f=open('testfile1.txt','r')
data=f.read()
print(data)

f1=open('testfile1copy.txt','w')
f1.write(data)

f.close()
f1.close()
