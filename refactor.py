import json
from pprint import pprint
from daxunctions import *

#this reads the input file into a list of dictionaries
more_messages = []
with open('/home/pi/Desktop/messages22.ldjson','r') as more_file:
   for line in more_file:
      more_messages.append(json.loads(line))

#this iterates through the messages in this example there are 10
#it uses absolute positioning

for counter in range(0,10):
        single_message = more_messages[counter]
        text_inside = single_message['text'] #just uses the text dictionary of the message
        mylist =text_inside.split('\r') #splits the text message by returns and places in a list

        #this could be a function to check that the message structure stays the same 
        naive_list_PID = mylist[1]
        naive_list_OBR = mylist[3]

        ID = naive_list_PID.split('|')[3].split('^')[0] #4th pipe bin 1st carat group in the PID 
        tyme =makedate(naive_list_OBR.split('|')[7]) #8th pipe bin in the OBR

        for counter in range(4,len(mylist)):
            #this prints out naive OBR messages until they run out
            segmented_message_result = solution_stapler(mylist[counter],ID,tyme)

            #adds the segmented observation into a file line by line as a json object
            #you could add a blank line or a comment to make the output file more readable
            with open("testfile.txt", "a") as the_file:
                the_file.write(segmented_message_result +'\n')


# if you picture the message as an array or grided map
# you can make some sort of crazy statement like this mylist[5].split('|')[3].split('^')[1]
# which drills down with the corridinates for each part of the message you wish to convert
# for clarity I divided the message up into a series of statements rather than one big gulp


