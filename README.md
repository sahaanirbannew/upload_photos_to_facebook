# upload_photos_to_facebook
Problem statement: I'm too lazy to remember and upload photographs to my page regularly. <br>
Result: My page is not updated. People do not go to my blog via my page.<br>
Solution proposed: One program will run in the background which will take photographs from a folder in the hard disk and upload it to my page at regular interval. <br><br>
Considerations:<br>
a. My laptop remains on all the time during working hours. <br>
b. I have active internet during the working hours. <br>
c. Photographs are arranged in sub-folders. Sub folders are in one specified folder.<br> 
<br>
What's my process? <br>
I photograph only during travel using my DSLR. I shoot RAW. I edit in Adobe LightRoom. <br>
I export to a folder "../LightRoomEdits" and it is my standard practise for the last 6 years. <br> 
I name the folders based on what the event is about. Example: "../LightRoomEdits/walpurgisnacht"<br> 
The folder has all the photographs. 
<br><br>
What does the program do?<br>
Task A: It asks the user (only me) to choose folder(s).<br>
Task B: It tries to suggest which link (from anirbansaha.com) should go with the photographs. <br>
Task B.a: Asks for confirmation. If confirmed, it creates the Bit.ly link to track clicks. <br>
Task B.b: If suggested link fails, it asks the user to give the link explicitly.<br>
Task C: It tries to summarise the blog post content in a few words. <br> 
Task D: Once agreed upon, it starts uploading the images to my FB page at 5:30 hours, 10:30 hours, 15:30 hours, 20:00 hours German time. (Indian time = German time + 3.5 hours) <br>
Task E: Saves the settings in file system, which the otherwise non technical or lazy me can open and see. <br>
<br><br>
Future work:<br>
a. Write some program (I do not know what/how) that will run this python code each time my laptop starts.<br>
b. Currently I have a "suggested link" option. Based on the folder name, it tries to search for the most relevant blog post on my blog. <br> We can make this suggesting option more interesting. <br>
c. Description of the photograph is automated. But it needs developments!<br> 
<br>
Maybe future work: <br>
a. Upload to Personal profile! (because if I log in, I waste a lot of time. And there are around 4000 friends and 4500+ subscribers). So some amount of people should go to my blog! <br> 
b. Upload to Twitter profile. Automate description and hashtags before uploading. <br>
<br>
<br>
Stay connected to www.anirbansaha.com
