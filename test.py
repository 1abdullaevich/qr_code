import requests
import io
from PIL import Image

url = "https://qrcode3.p.rapidapi.com/qrcode/text"

payload = {
    "data": "https://linqr.app",
    "image": {
        "uri": "icon://appstore",
        "modules": True
    },
    "style": {
        "module": {
            "color": "black",
            "shape": "default"
        },
        "inner_eye": {"shape": "default"},
        "outer_eye": {"shape": "default"},
        "background": {}
    },
    "size": {
        "width": 200,
        "quiet_zone": 4,
        "error_correction": "M"
    },
    "output": {
        "filename": "qrcode",
        "format": "png"
    }
}

headers = {
    "content-type": "application/json",
    "X-RapidAPI-Key": "22bbcfaf16msh6ff33c352478181p1d164djsn67b305c8fc5d",
    "X-RapidAPI-Host": "qrcode3.p.rapidapi.com"
}

response = requests.post(url, json=payload, headers=headers)

# Save the image as a file
image_path = "qrcode.png"
with open(image_path, "wb") as file:
    file.write(response.content)

# Open the image using the default image viewer
img = Image.open(io.BytesIO(response.content))
img.show()