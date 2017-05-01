# Prettify JSON

Данный скрипт принимает на вход путь до файла, в котором хранится json и выводит его содержимое в консоль в удобном для чтения виде. 

# Quickstart

Example of script launch on Linux, Python 3.5:

```#!bash

$ python pprint_json.py <path to file> 

#[
#    {
#        "Address": "Нижний Кисельный переулок, дом 3, строение 1",
#        "AdmArea": "Центральный административный округ",
#        "District": "Мещанский район",
#        "ID": "000069302",
#        "IsNetObject": "нет",
#        "Latitude_WGS84": "55.7653669567739740",
#        "Longitude_WGS84": "37.6215879462381080",
#        "Name": "Юнион Джек",
#        "PublicPhone": [
#            {
#                "PublicPhone": "(495) 621-19-63",
#                "global_id": 21025.0,
#                "global_object_id": 20660594.0,
#                "system_object_id": "000069302_1"
#            }
#        ],
#        "SeatsCount": 30,
#        "SocialPrivileges": "нет",
#        "TypeObject": "бар",
#        "geoData": {
#            "coordinates": [
#                37.62158794615201,
#                55.76536695660836
#            ],
#            "type": "Point"
#        },
#        "global_id": 20660594,
#        "system_object_id": "000069302"
#    },
#    {
#        "Address": "проспект Мира, дом 91, корпус 1",
#        "AdmArea": "Северо-Восточный административный округ",
#        "District": "Останкинский район",
#        "ID": "000058901",
#        "IsNetObject": "нет",
#        "Latitude_WGS84": "55.8055749999999000",
#        "Longitude_WGS84": "37.6357100000000000",
#        "Name": "Бар «Джонни Грин Паб»",
#        "PublicPhone": [
#            {
#                "PublicPhone": "(495) 602-45-85",
#                "global_id": 21059.0,
#                "global_object_id": 20660628.0,
#                
#
#Количество страниц в базе:  335 
#Введите номер интересующей страницы: 
#

```

# How to Help

```bash
python pprint_json.py --help
```

# Project Goals

The code is written for educational purposes. Training course for web-developers - [DEVMAN.org](https://devman.org)
