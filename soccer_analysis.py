import glob
import os
import sys
import subprocess
import pkg_resources
import pip

def import_or_install(package):
    try:
        __import__(package)
    except ImportError:
        pip.main(['install', package])   

import_or_install('pandas')

import pandas as pd

dir_path = os.path.dirname(os.path.realpath(__file__))
os.chdir(dir_path)
filepath = glob.glob('soccer.csv')
soccer_data = pd.read_csv(filepath[0])
soccer_data['goal_difference'] = abs(soccer_data['Goals'] - soccer_data['Goals Allowed'])
lowest_GD_Team = soccer_data[soccer_data['goal_difference'] == min(soccer_data['goal_difference'])]['Team'].to_list()[0]
soccer_data['win_percentage'] = soccer_data['Wins']/soccer_data['Games']
win_percentage_teams = soccer_data.sort_values(by='win_percentage').head(10)['Team'].to_list()
print(lowest_GD_Team)
print(win_percentage_teams)
soccer_data = soccer_data.drop(['goal_difference','win_percentage'],axis=1)
print(soccer_data.sort_values(by='Draws').head(1))