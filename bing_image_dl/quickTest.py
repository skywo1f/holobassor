from bing_image_downloader import downloader
import os
from PIL import Image 
query_string='frog on mountain'
thisDir = os.getcwd()

downloader.download(query_string, limit=1, adult_filter_off=False, force_replace=False, timeout=60, output_dir="")
fileName = thisDir + "/" + query_string +"/Image_1.jpg"
im = Image.open(fileName)
im.show()
