# RAG-Based AI Teaching Assistant – Usage Guide

This project implements a step-by-step **Retrieval-Augmented Generation (RAG)** pipeline that converts **educational videos into a searchable knowledge base** and uses a Large Language Model (LLM) to answer user queries based on retrieved context.

The sections below describe the **exact workflow followed in this project**.

---

## Step 1: Collect Educational Videos

Move all educational video files into the following folder:
### Videos_test/
These videos act as the primary knowledge source for the assistant.

---

## Step 2: Convert Video to Audio (MP3)

Convert all video files into audio format by running:
#### "1.process_video_to_mp3.py"
The extracted audio files will be saved in the designated audio output folder.

---

## Step 3: Convert MP3 to JSON Chunks

Convert the audio files into text chunks stored as JSON by running:
#### "2.create_chunks.py"
This step splits long audio transcripts into smaller, manageable chunks to improve retrieval quality.

---

## Step 4: Convert JSON Chunks to Vector Embeddings

Generate vector embeddings from the JSON chunks by running:
#### "3.read_chunks.py"
These embeddings are later used for similarity-based retrieval during question answering.

---

## Step 5: Retrieval and Prompt Construction

To retrieve relevant chunks and prepare the LLM prompt:

- Load matching vector data using:
#### "4.pull_matching_chunks.py"
- Save the retrieved data as a DataFrame using:
#### "5.joblib_to_save_df.py"
- Construct a prompt using the user query and retrieved chunks
- Feed the constructed prompt to the LLM using:
#### "6.next_process.py"
#### "7.prompting_RAG_sys.py"

---

## Step 6: Generate the LLM Response

Run the following script:
#### "8.getting_llm_response.py"
This step:
- Generates a `prompt.txt` file containing the full prompt sent to the LLM
- Generates a `response.txt` file containing the final answer produced by the LLM

---

## Optional: Performance Tuning

To improve performance and reduce retrieval overhead:

- Merge smaller chunks by running:
#### "9.post-project_merge_chunks.py"
- This creates a `newjsons` folder which has new jsons which improved versions of `2.json_chunks` 
- Update the pipeline to use `newjsons/` instead of `2.json_chunks/`

---

## Important Setup Notes

Before running the pipeline, ensure the following are present:

1. A populated `Videos_test/` folder containing all video files  
2. The following empty folders:
##### 1.converted_audios/
##### 2.json_chunks/
3. For performance tuning, an empty:
##### newjsons/

---

## Author

**Shreyash More**
