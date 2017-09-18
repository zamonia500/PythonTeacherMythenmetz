flist = ['hello.py', 'ex01.py', 'ex02.py', 'ch02.py', 'intro.hwp']

new_flist = []
for file in flist:
    print(file.split('.')[0])
    new_flist.append(file.split('.')[0])
