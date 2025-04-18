import requests 

def get_mars_photos():
    url = 'https://api.nasa.gov/mars-photos/api/v1/rovers/curiosity/photos'
    params = {
        'sol': 1000,            
        'camera': 'fhaz',       
        'api_key': 'DEMO_KEY'   
    }

    response = requests.get(url, params=params)
    
    if response.status_code == 200:
        data = response.json()         
        photos = data.get('photos', [])  

        if len(photos) > 0:
            for i in range(min(5, len(photos))):
                photo = photos[i]
                image_url = photo['img_src']  

                image_response = requests.get(image_url)

                if image_response.status_code == 200:
                    file_name = f"mars_photo{i+1}.jpg"
                    with open(file_name, 'wb') as file:
                        file.write(image_response.content)
                    print(f"Фото збережено: {file_name}")
                else:
                    print("Не вдалося завантажити фото:", image_url)
        else:
            print("Фото не знайдено.")
    else:
        print("Помилка при запиті до API:", response.status_code)

if __name__ == "__main__":
    get_mars_photos()