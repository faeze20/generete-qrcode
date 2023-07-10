import pyqrcode
from pyqrcode import QRCode
github="https://github.com/faeze20"
myQR=QRCode(github)
myQR.show()
myQR.png("qrcode github",scale=8)