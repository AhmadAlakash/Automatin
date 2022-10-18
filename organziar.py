
# Automation 

import os   # function to display what have we in one path 

folder_path = 'project1'



for file in os.listdir(path=folder_path):
    # now nedd to see the file has wich end jpg or mp3 or any end from this >> search in google
    # get file extention
    filename,file_extention = os.path.splitext(file)

    if file_extention in ['.jpg', '.png', '.gif', '.jpeg' ] :
        print (file)


   
   
