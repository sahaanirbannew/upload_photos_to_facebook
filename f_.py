import datetime as dt
import glob
import time
from googlesearch import search
import facebook as fb
import g_


def fb_page_graph_build(page_id, client_token):
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
    return graph


def fb_user_profile_graph_build(user_id, user_access_token):
    cfg = {
        "user_id": user_id,
        "access_token": user_access_token
    }
    graph = fb.GraphAPI(cfg['access_token'], version='3.1')
    return graph


def fb_page_post_image(file, graph, description, count):
    print(str(dt.datetime.now()) + " Uploading ...")
    with open(file, "rb") as image:
        graph.put_photo(image=image, message=description)
    print(str(dt.datetime.now()) + " Uploaded " + str(file))

    # Update the log
    log = g_.root + g_.folder_db + 'db.csv'
    log_content = open(log, 'a', encoding='utf-8')
    log_content.write(str(dt.datetime.now()) + ',' + "Uploaded" + ',' + str(file) + '\n')
    log_content.close()

    # Update count number.
    count = count + 1
    counter = g_.root + g_.folder_db + 'count.txt'
    counter_content = open(counter, 'w', encoding='utf-8')
    counter_content.write(str(count))
    counter_content.close()

    time.sleep(60)
    return count


def get_count():
    counter = g_.root + g_.folder_db + 'count.txt'
    counter_content = open(counter, 'r')
    count = counter_content.read()
    counter_content.close()
    return count


def reset_count():
    counter = g_.root + g_.folder_db + 'count.txt'
    counter_content = open(counter, 'w', encoding='utf-8')
    counter_content.write("0")
    counter_content.close()


def set_count(val):
    counter = g_.root + g_.folder_db + 'count.txt'
    counter_content = open(counter, 'w', encoding='utf-8')
    counter_content.write(str(val))
    counter_content.close()


def save_description(text, link):
    link = 'You can read more by clicking on this link: ' + link + '\n'
    description = text + link
    desc_path = g_.root + g_.folder_db + 'Description.txt'
    desc_content = open(desc_path, 'w', encoding='utf-8')
    desc_content.write(description)
    desc_content.close()


def get_description():
    desc_path = g_.root + g_.folder_db + 'Description.txt'
    desc_content = open(desc_path, 'r')
    return desc_content.read()


def save_foldname(text):
    fold_path = g_.root + g_.folder_db + 'folder.txt'
    fold_content = open(fold_path, 'w', encoding='utf-8')
    fold_content.write(text)
    fold_content.close()


def get_foldname():
    fold_path = g_.root + g_.folder_db + 'folder.txt'
    fold_content = open(fold_path, 'r')
    return fold_content.read()


def get_suggested_link(specific_folder_name):
    query = specific_folder_name + ' + anirbansaha'
    for j in search(query, tld="com", num=1, stop=1, pause=10):
        return j

    return 0