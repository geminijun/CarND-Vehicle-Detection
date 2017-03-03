import os
import glob

def get_file_list(basedir):
  filelist = []
  image_types = os.listdir(basedir)
  for imtype in image_types:
    filelist.extend(glob.glob(basedir+imtype+'/*'))
  return filelist

cars = get_file_list('vehicles/')
notcars = get_file_list('non-vehicles/')

print('Number of Vehicle Images found:', len(cars))
print('Number of Non-Vehicle Images found:', len(notcars))

