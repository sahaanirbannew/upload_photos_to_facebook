import randomise_f_

########################################################################################################################
# Part 1: Take user input. Save it to the file.
########################################################################################################################
message = randomise_f_.build_folder_record()

########################################################################################################################
# Part 2: Take the file names, randomise them.
########################################################################################################################
if message == 'proceed':
    randomise_f_.generate_schedule_draft_1()
else:
    print(message)

########################################################################################################################
# Output: A csv file with randomised file sequences.
########################################################################################################################