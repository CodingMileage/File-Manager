import os
import shutil
import getpass
from pathlib import Path

audio = (".3ga", ".aac", ".ac3", ".aif", ".aiff",
         ".alac", ".amr", ".ape", ".au", ".dss",
         ".flac", ".flv", ".m4a", ".m4b", ".m4p",
         ".mp3", ".mpga", ".ogg", ".oga", ".mogg",
         ".opus", ".qcp", ".tta", ".voc", ".wav",
         ".wma", ".wv")

video = (".webm", ".MTS", ".M2TS", ".TS", ".mov",
         ".mp4", ".m4p", ".m4v", ".mxf")

img = (".jpg", ".jpeg", ".jfif", ".pjpeg", ".pjp", ".png",
       ".gif", ".webp", ".svg", ".apng", ".avif")

doc = (".docx", ".txt", ".doc", ".csv")

pdf = (".pdf", ".rqq")

zipp = (".rar", ".zip", ".7z", ".iso")

exe = (".exe", ".msi")

code = (".java", ".class")

mem = 0

user = getpass.getuser()

def is_audio(file):
	return os.path.splitext(file)[1] in audio

def is_image(file):
	return os.path.splitext(file)[1] in img

def is_video(file):
	return os.path.splitext(file)[1] in video

def is_Doc(file):
	return os.path.splitext(file)[1] in doc

def is_zip(file):
	return os.path.splitext(file)[1].lower() in zipp

def is_resume(file):
    name, ext = os.path.splitext(file)
    return (ext in doc) and "resume" in name.lower()

def is_pdf(file):
    return os.path.splitext(file)[1] in pdf

def is_exe(file):
	return os.path.splitext(file)[1] in exe

def is_Java(file):
	return os.path.splitext(file)[1] in code

os.chdir(f"C:/Users/{user}/Downloads")

#Build Folders
# if not os.path.exists("Zip"):
#     os.mkdir("Zip")
# if not os.path.exists("Audio"):
#     os.mkdir("Audio")
# if not os.path.exists("Images"):
#     os.mkdir("Images")
# if not os.path.exists("Videos"):
#     os.mkdir("Videos")
# if not os.path.exists("Doc"):
#     os.mkdir("Doc")
# if not os.path.exists("Exe"):
#     os.mkdir("Exe")
# if not os.path.exists("Pdf"):
#     os.mkdir("Pdf")
# if not os.path.exists("Resume"):
#     os.mkdir("Resume")

for file in os.listdir():

	mem += os.stat(file).st_size

	if is_audio(file):
		Path("Audio").mkdir(exist_ok=True)
		shutil.move(file, f"C:/Users/{user}/Downloads/Audio")

	elif is_zip(file):
		Path("Zip").mkdir(exist_ok=True)
		shutil.move(file, f"C:/Users/{user}/Downloads/Zip")

	elif is_video(file):
		Path("Videos").mkdir(exist_ok=True)
		shutil.move(file, f"C:/Users/{user}/Downloads/Videos")

	elif is_image(file):
		Path("Images").mkdir(exist_ok=True)
		shutil.move(file, f"C:/Users/{user}/Downloads/Images")

	elif is_resume(file):
		Path("Resume").mkdir(exist_ok=True)
		shutil.move(file, f"C:/Users/{user}/Downloads/Resume")

	elif is_pdf(file):
		Path("Pdf").mkdir(exist_ok=True)
		shutil.move(file, f"C:/Users/{user}/Downloads/Pdf")

	elif is_exe(file):
		Path("Exe").mkdir(exist_ok=True)
		shutil.move(file, f"C:/Users/{user}/Downloads/Exe")

	elif is_Doc(file):
		Path("Doc").mkdir(exist_ok=True)
		shutil.move(file, f"C:/Users/{user}/Downloads/Doc")

	elif is_Java(file):
		Path("Java").mkdir(exist_ok=True)
		shutil.move(file, f"C:/Users/{user}/Downloads/Java")

print(round(mem / (1024 * 1024)) , "MB left in the " , os.getcwd()[-1])



print(os.getcwd())

# print(os.getcwd())

# # os.rename('Resume-Engineering.docx', 'RE.docx')

# Path("I_Made_A_New_Folder").mkdir(exist_ok=True)

# #MOVE
# # shutil.move('RE.docx', 'C:/Users/B/Desktop')

# #COPY
# shutil.copy("C:/Users/B/Downloads/Resume-Engineering.docx", os.getcwd())