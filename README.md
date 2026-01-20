# How to use this RAG Based AI teaching assistant.

## step-1 : collect videos
Move all your video files to Videos_test folder

## step-2 : Convert video to mp3
convert all video files to mp3 by running 1.process_video_to_mp3.py

## step-3 : convert mp3 to json
convert all mp3 files to json by running 2.create_chunks.py

## step-4 : Convert the json files to Vectors
convert all json files to vectors by running 3.read_chunks.py

## step-5 : Prompt generation and feeding to LLM
Read the joblib file and load it to memory using 4.;ulling_matching_chunks.py and saving it as df using 5.joblib_to_save_df.py. Then create a relevant prompt as per the user query and Feed it to the LLM using 6.next_process.py and 7.prompting_RAG_sys.py.

## step-6 : Getting LLM's Response
Our code creates an prompt.txt showing prompt and response.txt showing LLM's response to query using 8.getting_llm_response.py

## Optional Tuning to make code faster:
use 9.post-project_merge_chunks.py to merge chunks which will create folder newjsons and now refer this in codes instead of 2.jsons_chunks

### It Must be kept in mind that you have to manually provide 
1. Videos_test folder with all the videos.
2. empty folder named 1.converted_audios and 2.json_chunks.
3. for tuning, provide folder newjsons.

### Author
### *Shreyash More*
