import os, cv2, base64, requests, json, time, sys

# Get API key and secret
API_KEY = ""
API_SECRET = ""
# Replace these with your own API key and secret

# get url
http_url = 'https://api-us.faceplusplus.com/facepp/v3/detect'

# select the attributes you need
attributes = "gender,age,emotion,smiling,skinstatus"

# read image and convert it to base64 format (see Face++ documentation)
imgname = "politician2.jpg"
imgpath = os.path.join(imgname)
print(imgpath)

image_file = open(imgpath, "rb")
encoded_string = base64.b64encode(image_file.read())

# get response from Face++ API
r = requests.post(http_url,  data = {'api_key': API_KEY,
                             'api_secret': API_SECRET,
                             'image_base64': encoded_string,
                             'return_landmark': 0,
                             'return_attributes': attributes})

print(r.text)

js = json.loads(r.text)
print(json.dumps(js, indent=4))
