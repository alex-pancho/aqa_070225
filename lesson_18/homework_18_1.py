"""
Є вiдкритий API NASA який дозволяє за певними параметрами отримати данi у виглядi JSON про фото зробленi ровером
“Curiosity” на Марсi. Серед цих даних є посилання на фото, якi потрiбно розпарсити i потiм за допомогою додаткових
запитiв скачати i зберiгти цi фото як локальнi файли mars_photo1.jpg , mars_photo2.jpg .
Завдання потрiбно зробити використовуючи модуль requests
"""
import requests
import os

url = 'https://api.nasa.gov/mars-photos/api/v1/rovers/curiosity/photos'
params = {'sol': 1000, 'camera': 'fhaz', 'api_key': 'DEMO_KEY'}


def get_nasa_data_json(url: str, params: dict):
    response = requests.get(url, params=params)
    if response.status_code == 200:
        response = response.json()
        return response
    else:
        print(f"Something wrong, status code: {response.status_code}\n"
              f"url: {response.url}\n"
              f"headers: {response.headers}\n"
              f"text: {response.text}\n")
        return None


def save_photos(url: str, params: dict):
    data = get_nasa_data_json(url, params=params)
    if data is None:
        print("Фотографії відсутні")
    else:
        photos = data['photos']
        os.makedirs('mars_photos', exist_ok=True)
        for id, photo in enumerate(photos):
            img_url = photo['img_src']
            img_data = requests.get(img_url).content  # Завантажуємо фото
            file_path = f'mars_photos/mars_photo_{id + 1}.jpg'
            with open(file_path, 'wb') as handler:
                handler.write(img_data)

            print(f'Фото збережено: {file_path}')


if __name__ == "__main__":
    save_photos(url, params)
