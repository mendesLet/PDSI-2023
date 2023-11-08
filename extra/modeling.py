from sklearn.linear_model import LinearRegression
from myAudioProcessingLib import *

SOUND_PATH = "sounds/"
SOUND_FILE = "train.wav"

def prepare_data(sound_path):
    pass
    # loop through sound_path

    # read sound_file

    # save sound, label

def get_data(data_path):
    pass
    # get train/test data

def main():

    # get train/test data
    X, X_test, y = get_data(SOUND_PATH)

    # train model with data
    model = LinearRegression().fit(X, y)

    # validate model

    # test model
    model.predict(X_test)