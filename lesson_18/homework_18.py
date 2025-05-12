"""Є вiдкритий API NASA який дозволяє за певними параметрами отримати данi у виглядi JSON про фото зробленi ровером
“Curiosity” на Марсi. Серед цих даних є посилання на фото якi потрiбно розпарсити i потiм за допомогою додаткових
запитiв скачати i зберiгти цi фото як локальнi файли mars_photo1.jpg , mars_photo2.jpg . Завдання потрiбно зробити
використовуючи модуль requests"""

import requests
from pathlib import Path


def get_mars_photos(url, params):
    """Отримання JSON з фотографіями з NASA API."""
    response = requests.get(url, params=params)
    if response.status_code == 200:
        return response.json()
    else:
        print("Помилка при запиті:", response.status_code)
        return None


def save_all_photos(data, sol_number):
    """Збереження фото в окрему папку на основі номера sol."""
    photos = data.get("photos", [])
    save_path = Path("photos") / f"sol{sol_number}"
    save_path.mkdir(parents=True, exist_ok=True)

    for i, photo in enumerate(photos):
        img_url = photo.get("img_src")
        if img_url:
            img_response = requests.get(img_url)
            if img_response.status_code == 200:
                filename = save_path / f"mars_photo{i + 1}.jpg"
                with open(filename, "wb") as f:
                    f.write(img_response.content)
                    print(f"Збережено: {filename}")
            else:
                print(f"Помилка при завантаженні фото {i + 1}: {img_url}")


if __name__ == "__main__":
    # Основні параметри
    url = "https://api.nasa.gov/mars-photos/api/v1/rovers/curiosity/photos"
    params = {"sol": 1000, "camera": "fhaz", "api_key": "DEMO_KEY"}

    sol = params["sol"]
    mars_photos = get_mars_photos(url, params)
    if mars_photos and mars_photos.get("photos"):
        print(f"Знайдено {len(mars_photos['photos'])} фото для sol={sol}.")
        save_all_photos(mars_photos, sol)
    else:
        print("Фото не знайдено.")
