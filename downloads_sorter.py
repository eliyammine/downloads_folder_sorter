"""
This simple script allows all files in the current users downloads folder to be sorted based on file extension. 

This tool creates a new folder for each file extension and moves all files to that folder, creating an
organized place to look for specific files by extension.

"""
import os

old_path = os.path.expanduser("~")+"/Downloads/"
os.chdir(old_path)

for item in os.listdir('.'):
	name, ext = os.path.splitext(item)
	
	if ext != '':
		new_path = old_path + "\\" + ext[1:] + "\\" +  name + ext
		old_name = r'%s\%s%s' % (old_path, name, ext)
		print(old_name)
		print(new_path)
		try:
			os.mkdir(ext[1:])
			os.rename(old_name, new_path)
		except FileExistsError:
			os.rename(old_name, new_path)

