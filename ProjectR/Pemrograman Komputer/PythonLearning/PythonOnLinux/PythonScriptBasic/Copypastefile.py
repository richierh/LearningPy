from shutil import copyfile

for i in range(3):
 i = i + 1
 src = "/home/richie/BH40-BaseHandbook.pdf"
 dst = "/home/richie/Downloads/BH40-BaseHandbook%d.pdf"%i
 copyfile(src, dst)
