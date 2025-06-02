import requests
import os

def get_photos_by_sol(sol):
    api_url = f'https://api.nasa.gov/mars-photos/api/v1/rovers/curiosity/photos?sol={sol}&api_key=DEMO_KEY'
    response = requests.get(api_url)

    if response.status_code == 200:
        return response.json()['photos']
    else:
        print("Ошибка при получении данных.")
        return []

def choose_camera(photos):
    cameras = set(photo['camera']['name'] for photo in photos)
    print("Доступные камеры:")
    for i, camera in enumerate(cameras, start=1):
        print(f"{i}. {camera}")

    choice = int(input("Выберите камеру по номеру: "))
    selected_camera = list(cameras)[choice - 1]


    filtered_photos = [photo for photo in photos if photo['camera']['name'] == selected_camera]

    print(f"Фотографии с камеры {selected_camera}:")
    for i, photo in enumerate(filtered_photos, start=1):
        print(f"{i}. {photo['img_src']}")

    # Выбор фотографии
    photo_choice = int(input("Выберите фотографию по номеру: "))
    selected_photo = filtered_photos[photo_choice - 1]

    return selected_photo['img_src']


def download_image(image_url, filename):
    file_extension = os.path.splitext(image_url)[1]
    full_filename = f"{filename}{file_extension}"

    response = requests.get(image_url)
    if response.status_code == 200:
        with open(full_filename, 'wb') as file:
            file.write(response.content)
        print(f"Фото успешно скачано: {full_filename}")
    else:
        print("Ошибка при скачивании изображения.")

def main():
    sol = int(input("Введите sol (например, 1900): "))


    photos = get_photos_by_sol(sol)

    if photos:
        photo_url = choose_camera(photos)
        filename = input("Введите имя файла для сохранения (например, photo.jpg): ")
        download_image(photo_url, filename)
    else:
        print("Не удалось найти фотографии для данного sol.")

if __name__ == "__main__":
    main()