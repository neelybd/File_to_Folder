import os
import shutil
from file_handling import *
from selection import *


# Folder Location
file_pth_in = select_multiple_files("Select files to make folders")

# Split Path from file
file_pth = list()
for i in file_pth_in:
    file_pth.append(os.path.split(i))

# Output Folder Location
fldr_out = select_folder(title="Select folder for output", initialdir=file_pth[0][0])

# Not allowed characters
dsllwd_char = ['<', '>', ':', '"', '/', '\\', '|', '?', '*']

# Input if Main Folder separated by '-' is desired
main_separated = y_n_question('Separate Folders by Main Folder using {-}? (yes/no): ')

# Make list of new folder paths
nw_fldr_pth_lst = list()

# Make Directory and Move File
for i in file_pth:
    # New Folder Name
    nw_fldr_nm = os.path.splitext(i[1])[0]

    # Strip Disallowed Characters
    for char in dsllwd_char:
        nw_fldr_nm = nw_fldr_nm.replace(char, '_')

    # New Folder path
    nw_fldr_pth = os.path.join(fldr_out, nw_fldr_nm)

    # Append new folder paths to list
    nw_fldr_pth_lst.append(nw_fldr_pth)

    # Make Directory
    try:
        os.mkdir(nw_fldr_pth)
    except:
        print('Folder {} already exists...'.format(nw_fldr_pth))

    # Old File
    old_fl_pth = os.path.join(i[0], i[1])

    # New File
    nw_fl_pth = os.path.join(nw_fldr_pth, i[1])

    # Move File
    print('Moving: {} to {}'.format(old_fl_pth, nw_fl_pth))
    shutil.move(old_fl_pth, nw_fl_pth)

# List of new folders to make
nw_fldr_lst = list()

# If Main Separated is selected
if main_separated:
    # Iterate through list of final directories
    for i in nw_fldr_pth_lst:
        try:
            # Folder Path Base
            fldr_pth_base = os.path.basename(os.path.normpath(i))

            # Split header of '-'
            nw_fldr_head = fldr_pth_base.split('-')[0]

            # Append new folder to list
            nw_fldr_lst.append(nw_fldr_head)

            # One directory up
            flder_up = os.path.dirname(os.path.normpath(i))

            # Append new folder to base path
            nw_fldr = os.path.join(flder_up, nw_fldr_head)

            # Try to make new folder
            if not os.path.exists(nw_fldr):
                os.makedirs(nw_fldr)

            # Make destination path
            dest_pth = os.path.join(nw_fldr, fldr_pth_base)

            # Move Directory
            print('Moving: {} to {}'.format(i, dest_pth))
            shutil.move(i, dest_pth)
        except:
            print("Could not move or create: {}...".format(fldr_pth_base))
