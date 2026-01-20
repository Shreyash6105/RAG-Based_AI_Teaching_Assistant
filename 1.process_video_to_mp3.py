#converts the videos to mp3
#we can do this process of converting mp4 to mp3 or any format to mp3 using ffmpeg
#just type in terminal say for video1.mp4 type "ffmpeg -i video1.mp4 -q:a 0 -map a output.mp3"
#we have to do simplar process in code format

import os
import subprocess

files=os.listdir("Videos_test")

for file in files:
    
    #for name in format <......................anything.......... tutoril 2.mp4>
    tutorial_number = file.split(".mp4")[0].split(" tutorial ")[1]
    tutorial_name = file.split(" tutorial ")[0]
    
    print(tutorial_number , tutorial_name)
    
    #convert it to format "ffmpeg -i video1.mp4 -q:a 0 -map a output.mp3"
    
    subprocess.run(["ffmpeg","-i",f"Videos_test/{file}",f"1.converted_audios/{tutorial_number}_{tutorial_name}.mp3"])