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

t1 = '5:30'
t2 = '10:30'
t3 = '15:30'
t4 = '22:30'

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
profile_graph = f_.fb_user_profile_graph_build(g_.user_id, g_.user_token)
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
    suggested_link = f_.get_suggested_link(specific_folder_name)
    confirm = input("Is this link correct? [Y/N] Link: " + suggested_link + " :")
    if confirm == 'Y':
        link = suggested_link
    else:
        link = input("Please enter the link: ")
    link = 'You can read more by clicking on this link: ' + link + '\n'
    disclaimer = '#automated #test\n'
    description = text + link + disclaimer
    f_.save_description(text, link)

else:
    description = f_.get_description()

##################################################################
if count == -1:
    count = 0
##################################################################
##################################################################
# For the sake of moner shanti: #experiments
print("Current count: " + str(count))
print("Next file: " + file_paths[count])
##################################################################
#The time part will change.
while count < num_of_files:
    file = file_paths[count]
    time1 = dt.datetime.now()
    if str(time1.hour) == '11' and str(time1.minute) == '53':
        print("Count: " + str(count))
        print("Next photo: " + file)
        count = f_.fb_page_post_image(file, profile_graph, description, count)
    if str(time1.hour) == '5' and str(time1.minute) == '30':
        print("Count: " + str(count))
        print("Next photo: " + file)
        count = f_.fb_page_post_image(file, page_graph, description, count)
    if str(time1.hour) == '10' and str(time1.minute) == '58':
        print("Count: " + str(count))
        print("Next photo: " + file)
        count = f_.fb_page_post_image(file, page_graph, description, count)
    if str(time1.hour) == '15' and str(time1.minute) == '0':
        print("Count: " + str(count))
        print("Next photo: " + file)
        count = f_.fb_page_post_image(file, page_graph, description, count)
    if str(time1.hour) == '22' and str(time1.minute) == '0':
        print("Count: " + str(count))
        print("Next photo: " + file)
        count = f_.fb_page_post_image(file, page_graph, description, count)

##################################################################
# Terminating condition.
##################################################################
if count == num_of_files:
    print("Finishing execution.")
    f_.reset_count()
