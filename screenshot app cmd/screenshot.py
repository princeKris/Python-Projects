import pyscreenshot as ps 
import time
import sys
time.sleep(int(sys.argv[1]))
img=ps.grab()
img.save("sample.png")
img.show()