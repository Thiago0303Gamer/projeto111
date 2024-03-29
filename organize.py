import os
import shutil
from_dir = "C:/Users/thiag/Downloads"
to_dir = "C:/Users/thiag/OneDrive/Área de Trabalho/AulaC112/image"

listOfFiles = os.listdir(from_dir)
#print(listOfFiles)

for fileName in listOfFiles:
    name,extension=os.path.splitext(fileName)
    if extension == '':
        continue
    if extension in ['.txt','.pdf','.doc','.docx',]:
        
        path1=from_dir+'/'+fileName
        path2=to_dir+'/'+"image"
        path3=to_dir+'/'+"image"+'/'+fileName
        #print(path1)
        #print(path3)
        
        if os.path.exists(path2):
            print('move'+fileName+'...')
            shutil.move(path1,path3)
            
        else:
          os.makedirs(path2)
          print('move'+fileName+'...')
          shutil.move(path1,path3)