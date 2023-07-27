import requests

url = "https://qrcode3.p.rapidapi.com/qrcode/wifi"

payload = "-----011000010111000001101001\r\nContent-Disposition: form-data; name=\"metadata\"\r\n\r\n{\"data\":{\"ssid\":\"My WiFi network name\",\"password\":\"Pass!&#^@#*@\",\"security\":\"WPA\",\"hidden\":false},\"image\":{\"modules\":true},\"style\":{\"module\":{\"color\":\"black\",\"shape\":\"default\"},\"inner_eye\":{\"shape\":\"default\"},\"outer_eye\":{\"shape\":\"default\"},\"background\":{}},\"size\":{\"width\":200,\"quiet_zone\":4},\"output\":{\"filename\":\"qrcode\",\"format\":\"svg\"}}\r\n-----011000010111000001101001\r\nContent-Disposition: form-data; name=\"image\"\r\n\r\n\r\n-----011000010111000001101001--\r\n\r\n"
headers = {
	"content-type": "multipart/form-data; boundary=---011000010111000001101001",
	"X-RapidAPI-Key": "13e39cd008msh404313621a0ff4fp148846jsn0156d96a8ef1",
	"X-RapidAPI-Host": "qrcode3.p.rapidapi.com"
}

response = requests.post(url, data=payload, headers=headers)

print(response.json())