import requests

url = 'http://localhost:8000/predict'
image_path = 'test_img/image.png'  # Replace with the actual path

files = {'image': open(image_path, 'rb')}
response = requests.post(url, files=files)

print("Status Code:", response.status_code)
print("Response:", response.json())
