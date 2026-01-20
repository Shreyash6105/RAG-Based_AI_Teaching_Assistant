# How to Use the RAG-Based AI Teaching Assistant

This project follows a step-by-step pipeline to convert **educational videos into a searchable knowledge base** and then use an LLM to answer user queries using retrieved context.

Below are the exact steps used in this project.

---

## Step 1: Collect Videos
Move all your educational video files into the folder:
### Videos_test/
These videos act as the knowledge source for the assistant.

---

## Step 2: Convert Video to MP3
Convert all video files into audio format by running:
#### "1.process_video_to_mp3.py"
The extracted audio files will be saved in the audio output folder.

---

## Step 3: Convert MP3 to JSON Chunks
Convert the audio files into text chunks stored as JSON by running:
#### "2.create_chunks.py"
This step breaks long audio transcripts into smaller, manageable chunks.

---

## Step 4: Convert JSON Files to Vectors
Generate vector embeddings from the JSON chunks by running:
#### "3.read_chunks.py"
These vectors are later used for similarity matching during retrieval.

---

## Step 5: Prompt Generation and Feeding to LLM
- Load the stored vector data using:
#### "4.pull_matching_chunks.py"
- Save it as a DataFrame using:
#### "5.joblib_to_save_df.py"
- Create a relevant prompt based on the user query and retrieved chunks
- Feed the prompt to the LLM using:
#### "6.next_process.py"
#### "7.prompting_RAG_sys.py"

---

## Step 6: Getting the LLM Response
Run:
#### "8.getting_llm_response.py"
This step:
- Generates a `prompt.txt` file showing the full prompt
- Generates a `response.txt` file containing the LLM’s final answer

---

## Optional Tuning (Performance Improvement)
To make the system faster:
- Merge smaller chunks using:
#### "9.post-project_merge_chunks.py"
- This creates a `newjsons` folder
- Update the code to use this folder instead of `2.json_chunks`

---

## Important Notes
You must manually provide:
1. `Videos_test/` folder containing all video files  
2. Empty folders:
 - `1.converted_audios/`
 - `2.json_chunks/`
3. For tuning, an empty `newjsons/` folder  

---

## Author
**Shreyash More**
