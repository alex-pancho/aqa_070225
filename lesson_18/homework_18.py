import requests

url = 'https://api.nasa.gov/mars-photos/api/v1/rovers/curiosity/photos'
params = {'sol': 1000, 'camera': 'fhaz', 'api_key': 'DEMO_KEY'}
response = requests.get(url, params=params)
data = response.json()

photos = data['photos']
for index, photo in enumerate(photos):
    img_url = photo['img_src']
    img_data = requests.get(img_url).content
    with open(f"mars_photo{index + 1}.jpg", "wb") as file:
        file.write(img_data)
        



    