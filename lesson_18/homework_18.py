import requests

url = 'https://api.nasa.gov/mars-photos/api/v1/rovers/curiosity/photos'
params = {
    'sol': 1000,
    'camera': 'fhaz',
    'api_key': 'DEMO_KEY'
}

response = requests.get(url, params=params)
data = response.json()
photos = data.get('photos', [])

if not photos:
    print("Фото не знайдено за заданими параметрами.")
else:

    photo_names = ['mars_photo1.jpg', 'mars_photo2.jpg']

    for photo, filename in zip(photos[:2], photo_names):
        image_url = photo['img_src']
        print(f"URL фото: {image_url}")
        image_data = requests.get(image_url).content

        with open(filename, 'wb') as f:
            f.write(image_data)

        print(f"Фото збережено як {filename}\n")
