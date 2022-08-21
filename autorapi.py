import os
import shutil

downloaddir = 'C:/Users/fadli/Downloads/'
docdir = 'C:/Users/fadli/Downloads/Documents'
imgdir = 'C:/Users/fadli/Downloads/Pictures'
psddir = 'C:/Users/fadli/Downloads/Photoshop'
doctypes = ['docx', 'doc', 'xls', 'xlsx', 'pdf', 'rtf']
imgtypes = ['jpg', 'png', 'webp', 'jpeg']
psdfile = 'psd'

def main():
	files = os.listdir(downloaddir)
	for file in files:
		if file.split('.')[-1] in doctypes:
			move(file, docdir)
		if file.split('.')[-1] in imgtypes:
			move(file, imgdir)
		if file.split('.')[-1] == psdfile:
			move(file, psddir)


def move(file, dstdir):
	if os.path.exists(dstdir):
		print('memindahkan file {} '.format(file))
		shutil.move(downloaddir+file, dstdir)
	else:
		os.makedirs(dstdir)
		print('memindahkan file {} '.format(file))
		shutil.move(downloaddir+file, dstdir)

if __name__ == '__main__':
	main()