

# Automation 

from distutils import extension
import os
import shutil   # function to display what have we in one path 

folder_path = 'project2'
os.chdir(folder_path)
os.mkdir('imges')  # create folder with use :os.mkdir()
os.mkdir('docs')  # create folder with use :os.mkdir()
os.mkdir('audio_vedio')  # create folder with use :os.mkdir()
os.mkdir('exe')  # create folder with use :os.mkdir()
os.mkdir('rar+zip')  # create folder with use :os.mkdir()

   # to know what from file we have can we this code using ' 
   # extention []
   # for file in os.listdir('.'):
#         filename,file_extension = os.path.spiltext(file)
   # '          extension.append(file_extension)
   # print (extension)




for file in os.listdir('.'):
    # now nedd to see the file has wich end jpg or mp3 or any end from this >> search in google
    # get file extention
    filename,file_extention = os.path.splitext(file)
   
    if file_extention in ['.jpg', '.png', '.gif', '.jpeg' ] :
        shutil.move(file,'imges')

    elif file_extention in ['.pdf', '.epub', '.word', '.docs']:
        shutil.move(file, 'docs')
        
    elif file_extention in ['.mp3', '.mp4', '.avi',  ] :
        shutil.move(file, 'audio_vedio')
        

        
    elif file_extention in ['.rar', '.zip'  ] :
        shutil.move(file, 'rar+zip')
        

        
    elif file_extention in ['.exe' ] :
        shutil.move(file, 'exe')


print ('done')


# to make the code more good we can 'istead of  ' file_extention in ' this write endswith but he take ()'


# new style from this code :

'''
def working_dir(path):
    os.chdir(path)
    print(f'moved to : {path}')


def check_folder():
    folders =['imges','docments','code','compressed','books']
    for folder in folders :
        if not os.path.exists(folder):
            os.mkdir(folder)

def get_extension():
    for file in os.listdir('.'):
        filename, file_extension = os.path.splitext(file)
        if file_extension not in extension:
            extension.append(file_extension)
    print(f'Avaliable Extention {extension}')
    pass


def organize():
    print('Start organizing Files')
    for file in os.listdir('.'):
        # now nedd to see the file has wich end jpg or mp3 or any end from this >> search in google
        # get file extention
   
        if file.endswith in ['.jpg', '.png', '.gif', '.jpeg']:
            shutil.move(file, 'imges')

        elif file.endswith in (('.pdf', '.epub', '.word', '.docs')):
            shutil.move(file, 'docs')

        elif file.endswith in (('.mp3', '.mp4', '.avi')):
            shutil.move(file, 'audio_vedio')

        elif file.endswith in (('.rar', '.zip')):
            shutil.move(file, 'rar+zip')

        elif file.endswith in (('.exe')):
            shutil.move(file, 'exe')
    print('Finish Organizing Files')

  
def main ():
    working_path = input ('Enter path :')
    print ('Start Working...')
    working_dir(working_path)
    check_folder()
    get_extension()
    organize()
    




if __name__ =='__main__':
    main()
'''

   
