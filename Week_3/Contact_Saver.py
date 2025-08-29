from pathlib import Path
import csv

# name = input('Enter your name here: ')
# age = int(input('Enter your age here: '))
# phone = input('Enter your phone number here: ')
# track = input('Enter your track here: ')

folder = Path('participant_pkg')
# folder.mkdir(exist_ok=True)
# folder_init = folder / '__init__.py'

# folder_help = folder / 'file_ops.py'

# open(folder_init, 'w')
# open(folder_help, 'w')

folder_main = folder / 'main.py'
open(folder_main, 'w')
