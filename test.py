import facebook as fb
import datetime as dt


page_id = '118243818253158'
client_token_ = 'EAAna9amya9QBAK3ySs3P5diapHz2b5ZCikIHsQ2X3b7jlk3uo0Qmn6CdZCZCjcca55IQXn6bAuHUApZAEI80N7pHb48GOVTjd6SZA9ie4zD2NZBR4yx0bjUcepxverrkjb70rulYlgIZCgvlmwA1SgfdiVybqOS7YEHoeZAL5vVG8NC5LaOEbIVwb3iZBnT5ZAmKFOvRdCeqKMkAZDZD'
app_id = '2019459095028570'  # changed to new
client_token = 'EAAcsrZCXZCY1oBAD0V3hIhNV3ZBowN0nzLq9WjxvQFh5NZC2Y9YPXkr3SdM3XbGzAsACCIdERv87HnYq77kPVCWYIE0xf7pMwB8F27NQ6faCI7NYgot7TxmVhcGAmQaNeorbwN1nFtDWe6LKyZAF2iZAa669DxXm5rMwB5D5pK6SSMqQNkgaGZAajLTwM7gDWGRlnY0CbFvdwZDZD'
# app_token = '2774023439281108|9P_wSoacNzk6vd7R1tnwGSNdP6E'

cfg = {
    "page_id": page_id,
    "access_token": client_token
}

graph = fb.GraphAPI(cfg['access_token'], version='3.1')
resp = graph.get_object('me/accounts')
page_access_token = None
for page in resp['data']:
    if page['id'] == cfg['page_id']:
        page_access_token = page['access_token']
graph = fb.GraphAPI(page_access_token)

# ------------------------------------------
folder_path = 'D:/Photographs/LightRoom Edits/'
specific_folder_name = 'more birds/'
file_name = 'sea gull.jpg'
# ------------------------------------------
description = 'This is the description.'
disclaimer = '#automatedPost #testing'
# ------------------------------------------

file = folder_path + specific_folder_name + file_name
description = description + '\n'+ disclaimer
# ------------------------------------------

count = 0
done = 0
while count < 1:
    time1 = dt.datetime.now()
    if str(time1.hour) == '10' and str(time1.minute) == '15' and done == 0:
        print("came till here.")
        with open(file, "rb") as image:
            graph.put_photo(image=image, message=description)
        print("Processed.")
        done = 1
    if str(time1.minute) == '6' and done == 1:
        done = 0.
