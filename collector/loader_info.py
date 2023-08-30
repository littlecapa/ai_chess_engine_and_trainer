import logging
from libs.ip_lib import get_local_ip
import os

def get_out_dir_annotated_positions():
    #
    # To do: Implement a JSON File with Config
    #
    ip = get_local_ip()
    # If Windows 11
    if ip == "192.168.178.25":
        return r"G:\Meine Ablage\data\nn_chess\KRk"
    return "/Volumes/Data/DataLake/chess/filtered/eval/mate_included/"

def get_KRk_training_data_dir():
    #
    # To do: Implement a JSON File with Config
    #
    ip = get_local_ip()
    # If Windows 11
    if ip == "192.168.178.25":
        return r"C:\Users\littl\Documents\GIT\AI\ai_chess_engine_and_trainer\trainer\training_data"
    return "/Users/littlecapa/GIT/python/ai_chess_engine_and_trainer/trainer/training_data"

def get_KRk_training_data_file(k = 10):
    #
    # k = number of games to produce training data (in 1000 units)
    #
    filename = "train_KRk_" + str(k) + "k.csv"
    return os.path.join(get_KRk_training_data_dir(), filename)

def get_KRk_baseline_data_file():
    filename = "train_KRk_baseline.csv"
    return os.path.join(get_KRk_training_data_dir, filename)
