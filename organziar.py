
# Automation 

import os
import shutil   # function to display what have we in one path 

folder_path = 'project1'
os.chdir(folder_path)
os.mkdir('imges')  # create folder with use :os.mkdir()
os.mkdir('docs')  # create folder with use :os.mkdir()
os.mkdir('audio_vedio')  # create folder with use :os.mkdir()



for file in os.listdir('.'):
    # now nedd to see the file has wich end jpg or mp3 or any end from this >> search in google
    # get file extention
    filename,file_extention = os.path.splitext(file)
   
    if file_extention in ['.jpg', '.png', '.gif', '.jpeg' ] :
        shutil.move(file,'imges')

    if file_extention in ['.pdf', '.epub', '.word', '.docs']:
        shutil.move(file, 'docs')
        
    if file_extention in ['.mp3', '.mp4', '.avi',  ] :
        shutil.move(file, 'audio_vedio')
        


   
