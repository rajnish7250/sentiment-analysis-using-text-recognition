import os
HOME_DIR= os.path.abspath(os.pardir)
OldPath=HOME_DIR+"\\imageto text\\img2txt.txt" 
NewPath=HOME_DIR+"\\imageto text\\img2box.txt" 
print('hello')

if os.path.exists(OldPath) and os.path.exists(NewPath):
    OldFileObj=open(OldPath,mode='r')
    NewFileObj=open(NewPath,mode='r')

    OldList=OldFileObj.read().split('\n')
    NewList=NewFileObj.read().split('\n')

    OldList.sort()
    NewList.sort()

    if OldList==NewList:
        print("Files are same:")
    else:
        print('Files are not same')
else:
    print('files are not There')