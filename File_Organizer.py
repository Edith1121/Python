import os
import shutil


images ={".jpg",".jpeg",'.png','.gif','.webp',".bmp",".tiff",".tif",".svg",".ico"}
videos = {".mp4",".mkv",".avi",".mov",".wmv",".flv",".webm",".m4v",".mpeg",".mpg",".3gp",".ts"}
docs = {".pdf",".docx",".doc",".odt",".txt",".rtf",".tex",".md",".xls",".xlsx",".ppt",".pptx",".odt",".ods",".odp"}
music = {".mp3",".wav",".flac",".aac",".m4a",".ogg",".opus",".wma",".aiff",".alac"}
archives = {".zip",".rar",".7z",".tar",".gz",".bz2",".xz"}
code = {".py",".js",".html",".css", ".java", ".c",".cpp",".h",".hpp",".json",".xml",".sql", ".sh"}
path = "//home//joyalsaju//Pictures//Iphone"

for i in os.listdir(path):
    source = os.path.join(path,i)

    if not os.path.isfile(source):
        continue

    file_name = os.path.basename(source)
    name , extension = os.path.splitext(file_name)

    extension = extension.lower()

    if extension in images:  
        folder_name = "Images"
    elif extension in videos:
        folder_name = "Videos"
    elif extension in docs:
        folder_name = "Documents"
    elif extension in archives:
        folder_name = "Archives"
    elif extension in music:
        folder_name = "Music"
    elif extension in code:
        folder_name = "Code"
    else:
        folder_name = "Other"

    new_folder = os.path.join(path,folder_name)

    if not os.path.isdir(new_folder):
        os.mkdir(new_folder)

    shutil.move(source,new_folder)
    
print("Files Organized :)")     
        