from PIL import Image
from pyzbar.pyzbar import decode
data=decode(Image.open("qrcoded.png"))
print(data)