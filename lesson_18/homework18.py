import requests


def download_mars_photos(sol=1000, camera='fhaz', api_key='DEMO_KEY', photo_names=None):
    url = 'https://api.nasa.gov/mars-photos/api/v1/rovers/curiosity/photos'
    params = {
        'sol': sol,
        'camera': camera,
        'api_key': api_key
    }

    response = requests.get(url, params=params)
    data = response.json()
    photos = data.get('photos', [])

    if not photos:
        print("Фото не знайдено за заданими параметрами.")
        return

    if photo_names is None:
        photo_names = [f'mars_photo{i + 1}.jpg' for i in range(min(2, len(photos)))]

    for photo, filename in zip(photos[:len(photo_names)], photo_names):
        image_url = photo['img_src']
        print(f"URL фото: {image_url}")
        image_data = requests.get(image_url).content

        with open(filename, 'wb') as f:
            f.write(image_data)

        print(f"Фото збережено як {filename}\n")


if __name__ == "__main__":
    download_mars_photos()