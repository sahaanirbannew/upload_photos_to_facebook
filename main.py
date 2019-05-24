########################################################################################################################
# Improvements on previous version main_1.py
# What version 1.000 did:
#   It took one folder as an input. It uploaded photographs from that one folder at every point in time.
# What does version 1.001 do?
#   a. First "sequence.py" is executed:
#       i. Takes more than one folder as input.
#      ii. Creates two files:
#           > folder_rec.csv
#               Contains the following fields: folder_no | folder_path | long_link | bit.ly_link
#           > schedule.csv
#               Contains the following fields: number | folder_no | file_path
#               The files are arranged randomly.
#   b. Then "main.py" is executed:
#       i. Takes the file_path from the schedule.csv
#      ii. Fetches long link and bit.ly link from folder_rec.csv
#     iii. Creates description using the long link. Adds the bit.ly link to description.
#      iv. Uploads the photograph with description to Facebook page.
# Developer: Anirban Saha.
########################################################################################################################
# Version   Status  Date        Comments
#   1.001   Draft   23.05.2019  Added sequencer, randomises description to an extent, uploads it.
#   1.002   Draft   23.05.2019  Files upload to Twitter once a day.
########################################################################################################################

import g_
import f_
import pandas as DataFrame
import summarise
import datetime as dt
import upload_twitter

##################################################################
# This is the count, the file number which needs to be uploaded.
# Count = 0  | The upload data is not prepared.
# Count = -1 | Data is prepared and upload has not started.
# Count > 0  | Upload has started and interrupted midway.
##################################################################
count = int(f_.get_count(), 10)
print(count)

##################################################################
# Fetches data from :
#   a.  the database where the chosen folder details are saved.
#   b.  the database where the files are sequenced and stored.
##################################################################
sequence_path = g_.root + g_.folder_db + 'schedule.csv'
folder_path = g_.root + g_.folder_db + 'folder_rec.csv'
folder_db_details = open(folder_path, 'r', encoding='utf-8')
sequence_db_details = open(sequence_path, 'r', encoding='utf-8')
folder_db = DataFrame.read_csv(folder_path)
sequence_db = DataFrame.read_csv(sequence_path)

##################################################################
# Final count of the number of files in the pipeline.
##################################################################
final_count = sequence_db.size

##################################################################
if count == -1:
    count = 0
##################################################################

##################################################################
# This is the main block.
# This does the following steps:
#   a. Get the next file to upload [from sequence_db]
#   b. Finds which folder it is from [from sequence_db]
#   c. Fetches the link and the shortened link [from folder_db]
#   d. Fetches a description randomly created from blog post.
#   e. Uploads to the Facebook page.
##################################################################
while count < final_count:
    curr_time = str(dt.datetime.now().hour) + ":" + str(dt.datetime.now().minute)
    if curr_time in g_.selected_fb_time:
        file_path = str(sequence_db.loc[count, 'file_path'])
        folder_no = str(sequence_db.loc[count, 'folder_no'])
        rows = folder_db.loc[folder_db['folder_no'] == int(folder_no)]
        link = rows.iloc[0]['link']
        short_link = rows.iloc[0]['short_link']
        description = summarise.get_summary_description(link, 'fb')
        description = description + " Check out more at " + short_link
        page_graph = f_.fb_page_graph_build(g_.page_id, g_.client_token)
        count = f_.fb_page_post_image(file_path, page_graph, description, count)

    if curr_time in g_.selected_tw_time:
        file_path = str(sequence_db.loc[count, 'file_path'])
        folder_no = str(sequence_db.loc[count, 'folder_no'])
        rows = folder_db.loc[folder_db['folder_no'] == int(folder_no)]
        link = rows.iloc[0]['link']
        short_link = rows.iloc[0]['short_link']
        description = summarise.get_summary_description(link, 'tw')
        description = description + " Check out more at " + short_link
        description = description + '\n#photographoftheday #photography #traveller'
        done = upload_twitter.upload(file_path, description)

##################################################################
# Terminating condition.
##################################################################
if count == final_count:
    print("Finishing execution.")
    f_.reset_count()
