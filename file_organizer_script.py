import os
# os module is used to interact with Operating System
import shutil
# Used to perform operations with files like copy, move, delete, archieve files and directories

DIR_PATH='C:/Users/HP/Documents/Notes/'

dictionary = {
    '.pdf':'PDF',
    '.docx':'DOCX',
    '.txt':'DOCX',
    '.png':'Images',
    '.jpg':'Images',
    '.mp4':'Videos',
    '.mp3':'Songs'
}

def file_organizer():
    # Get list of all files in directory
    all_files = os.listdir(DIR_PATH)
    try:
        for file in all_files:
            if not os.path.isfile(os.path.join(DIR_PATH,file)):
                continue
            _,extension = os.path.splitext(file)
            if extension in dictionary:
                if not os.path.exists(os.path.join(DIR_PATH,dictionary[extension])):
                    os.mkdir(os.path.join(DIR_PATH,dictionary[extension]))
                shutil.move(os.path.join(DIR_PATH,file),os.path.join(DIR_PATH,dictionary[extension]))
        print('File Organization Complete')
    except Exception as e:
        print('Error:',e)
    
file_organizer()