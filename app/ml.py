from importlib.metadata import files
import pathlib
import time
import pickle
import os

BASE_DIR = pathlib.Path(__file__).resolve().parent.parent
MODEL_DIR = BASE_DIR / "models"
MODEL_RF = MODEL_DIR / 'random_forest.pkl'
PATH_EAST = MODEL_DIR / 'rf_east.pkl'
PATH_WEST = MODEL_DIR / 'rf_west.pkl'

sensors_paths = {'P39355': PATH_WEST,
                 'P39285': PATH_WEST,
                 'P93745': PATH_WEST,
                 'P39497': PATH_EAST,
                 'P93927': PATH_EAST,
                 'P96317': PATH_EAST}


def correct_rf(raw_purple_data=None, sensor_id=None, date_time=None):

    purple_data = format_purple_data(raw_purple_data)
    if sensor_id in sensors_paths.keys():
        model_path = sensors_paths[sensor_id]
    else:
        raise ValueError

    loaded_rf = pickle.load(open(model_path, 'rb') )
    correction = loaded_rf.predict(purple_data)
    return list(correction)


def correct_rf_2(raw_purple_data=None, sensor_id=None, date_time=None):
    loaded_rf = pickle.load(open(PATH_WEST, 'rb') )
    purple_data = [[10, 12, 20, 30, 40]]
    correction = loaded_rf.predict(purple_data)
    return list(correction)


def format_purple_data(raw_data):
    pm25_a = raw_data['PM25_A']
    pm25_b = raw_data['PM25_B']
    humedad = raw_data['Humedad']
    presion = raw_data['Presion']
    temperatura = raw_data['Temperatura']

    return [[pm25_a, pm25_b, humedad, presion, temperatura]]