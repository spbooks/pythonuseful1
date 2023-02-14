import glob
import os
from PIL import Image, IptcImagePlugin

# https://iptc.org/std/photometadata/specification/IPTC-PhotoMetadata#title
IPTC_Title = (2, 120)

# Work through all of the images that match *.jpg
for image_filename in glob.glob("*.jpg"):
    # Open the image with Pillow
    im = Image.open(image_filename)
    # Get the IPTC metadata for this image
    iptc = IptcImagePlugin.getiptcinfo(im)
    im.close()
    # In the IPTC metadata, look up the title
    title = iptc[IPTC_Title].decode("utf-8")
    # rename the image file based on the title from the metadata
    destination_filename = f"{title}.jpg"
    print(f"Renaming {image_filename} -> {destination_filename}")
    os.rename(image_filename, destination_filename)
