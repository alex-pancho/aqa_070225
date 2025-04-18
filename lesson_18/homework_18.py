"""
Є вiдкритий API NASA який дозволяє за певними параметрами отримати данi 
у виглядi JSON про фото зробленi ровером “Curiosity” на Марсi. Серед цих 
даних є посилання на фото якi потрiбно розпарсити i потiм за допомогою 
додаткових запитiв скачати i зберiгти цi фото як локальнi файли mars_photo1.jpg , 
mars_photo2.jpg . Завдання потрiбно зробити використовуючи модуль requests
"""
import json
import requests
from pathlib import Path
from requests.exceptions import HTTPError, ConnectionError, Timeout


def get_data_in_json(url, params):
    """ Getting data... """
    try:
        response = requests.get(url, params, timeout=30)
        response.raise_for_status()
        try:
            data = response.json()
            return data
        except json.JSONDecodeError as e:
           print('Помилка при серіалізації JSON:', e)
       
    except HTTPError as e:
        print('HTTP Помилка:', e)
    
    except ConnectionError as e:
        print('Помилка з\'єднання:', e)
    except Timeout as e:
        print('Часова помилка:', e)
    except Exception as e:
        print('Невідома помилка:', e)

"""{'photos': 
    [
        {
         'id': 102693, 
         'sol': 1000,
         'camera': {'id': 20, 'name': 'FHAZ', 'rover_id': 5, 'full_name': 'Front Hazard Avoidance Camera'}, 
         'img_src': 'http://mars.jpl.nasa.gov/msl-raw-images/proj/msl/redops/ods/surface/sol/01000/opgs/edr/fcam/FLB_486265257EDR_F0481570FHAZ00323M_.JPG', 
         'earth_date': '2015-05-30', 
         'rover': {'id': 5, 'name': 'Curiosity', 'landing_date': '2012-08-06', 'launch_date': '2011-11-26', 'status': 'active'}
         },
          
         {'id': 102694, 'sol': 1000, 
          'camera': {'id': 20, 'name': 'FHAZ', 'rover_id': 5, 'full_name': 'Front Hazard Avoidance Camera'},
           'img_src': 'http://mars.jpl.nasa.gov/msl-raw-images/proj/msl/redops/ods/surface/sol/01000/opgs/edr/fcam/FRB_486265257EDR_F0481570FHAZ00323M_.JPG', 
           'earth_date': '2015-05-30', 
           'rover': {'id': 5, 'name': 'Curiosity', 'landing_date': '2012-08-06', 'launch_date': '2011-11-26', 'status': 'active'}
           }
    ]
}"""

def save_pic(json_data):
    
    directory = Path(r'C:\Users\dmytr\OneDrive\Desktop\LYUBA\Hillel\aqa_070225\lesson_18\Mars photos')
    if directory.exists():
        pass
    else:
        directory.mkdir()
    
    pic_number = 1
    try:
        if json_data["photos"]:
            for photo in json_data['photos']:
                link = photo['img_src']
                response = requests.get(link)
                with open(directory / f"mars_photo{pic_number}.jpg", 'wb') as file:
                    file.write(response.content)
                print(f"Picture mars_photo{pic_number}.jpg is downloaded")
                pic_number+=1
                print(f"Picture link {link}")
        else:
            print("No pictures found")

    except TypeError as e:
        print(f"Type error occured: {e}")
    except Exception as e:
        print(f"Error occured: {e}")


if __name__ == "__main__":
    url = 'https://api.nasa.gov/mars-photos/api/v1/rovers/curiosity/photos'
    params = {'sol': 1000, 'camera': 'fhaz', 'api_key': 'DEMO_KEY'}
    json_data_test = get_data_in_json(url, params)
    #print(json_data_test)
    save_pic(json_data_test)
