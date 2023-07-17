from PIL import Image
import sys
img=Image.open(str(sys.argv[1]))
img.save(str(sys.argv[2]))