########################################################################################################################
# This program takes photographs from a folder
# and posts it on fb.com/anirbansahablog.
# Developer: Anirban Saha.
########################################################################################################################
# Version   Status  Date        Comments
#   0.001   Draft   14.05.2019  Just uploads the images
#   0.002   Draft   16.05.2019  Asks for user input; Saves the last upload details.
########################################################################################################################

import facebook as fb
import datetime as dt
import g_
import f_
import glob


########################################################################################################################
# Setting time:
########################################################################################################################
t1 = '5:30'
t2 = '14:50'
t3 = '15:30'
t4 = '22:30'

# This would soon be user input or data driven.
selected_time = [t1, t2, t3, t4]
########################################################################################################################

##################################################################
# This is the count, the file number which needs to be uploaded.
# Count = 0  | The upload data is not prepared.
# Count = -1 | Data is prepared and upload has not started.
# Count > 0  | Upload has started and interrupted midway.
##################################################################
count = int(f_.get_count(), 10)

##################################################################
# Prepares the FB graph for page.
##################################################################
page_graph = f_.fb_page_graph_build(g_.page_id, g_.client_token)
profile_graph = f_.fb_user_profile_graph_build(g_.user_id, g_.user_token) #This has errors
##################################################################

##################################################################
# Finds Folder details
##################################################################
folder_path = g_.root
if count == 0:
    specific_folder_name = input("Name of the folder : ")
    specific_folder_name = specific_folder_name + '/'
    f_.save_foldname(specific_folder_name)
    f_.set_count(-1)
else:
    specific_folder_name = f_.get_foldname()

##################################################################
# Finds file details
##################################################################
file_paths = glob.glob(folder_path + specific_folder_name + "*.jpg") + glob.glob(folder_path + specific_folder_name + "*.png")
num_of_files = len(file_paths)

##################################################################
# Creates description
# This should be automated.
##################################################################
if count == 0:
    text = input("Please enter description") + '\n'
    link = f_.create_link(specific_folder_name)
    # Saves the current description in local memory and in file.
    description = f_.save_description(text, link)

else:
    description = f_.get_description()

##################################################################
if count == -1:
    count = 0
##################################################################
##################################################################
print("Current count: " + str(count))
print("Next file: " + file_paths[count])
##################################################################

while count < num_of_files:
    curr_time = str(dt.datetime.now().hour)+":"+str(dt.datetime.now().minute)
    if curr_time in selected_time:
        file = file_paths[count]
        count = f_.fb_page_post_image(file, page_graph, description, count)

##################################################################
# Terminating condition.
##################################################################
if count == num_of_files:
    print("Finishing execution.")
    f_.reset_count()
