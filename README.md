# spotify2applemusic

This script helps you to copy your Spotify songs to your Apple Music library.

# Instructions

Step 1 : Convert your spotify playlist to a text file with the names of the songs. You can use [Exporitfy](https://rawgit.com/watsonbox/exportify/master/exportify.html) to convert it to a csv file and then copy paste the song name field to a text file.

Step 2: Name the file **songlist.txt** and copy the file to the same location as the script.

Step 3: Take a screenshot of your Itunes screen and open it with paint. Find the X,Y coordinates of the add button(after searching a song) and the X button on the search fields.

Step 4: Put these coordinates into the script .

Step 5: Open Itunes, run the script `python add.py` with the Itunes window open in the same position when the coordinates were taken.

Step 6: Go grab a beer or coffee while your songs get added.

# Known Issues

After adding some songs, the library becomes unresponsive. Stop the script and delete the completed songs from songlist.py file.
