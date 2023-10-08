# ML_Movie
## Installation & Setup

1. Clone the repository using git or GitHub.
2. Navigate to the project directory and install the dependencies:
   ```bash
   pip install -r requirements.txt
   ```
3. `app3.py` is Streamlit test versions. Start using:
   ```bash
   streamlit run app3.py
   ```
4. For a preliminary requirement document analysis demo, run:
   ```bash
   python main2.py
   ```
## Data set

Download the scripts, subtitles, and metadata from [Here](https://drive.google.com/file/d/1p6k1rW6XU-oR11LlKOBjqoiy44NmxKbg/view?usp=drive_link).

This zip file contains scripts (with .script extension), subtitles (with .srt extension), and metadata (in .json format) that all correspond to the same film titles. It also includes a list of films in a text file.

Because of the size of film frame scenes, you have to download it from [MovieNet](https://movienet.github.io/).

### Set-up for frame scene data

1. Change directory to where you have the below directory.
   ```bash
   movie1K.keyframes.240p.v1
   ```
2. Run the python code `moveFrameFiles.py`
   ```bash
   python ./moveFrameFiles.py
   ```
   Make sure you also have `film_list.txt` file on the same directory with `moveFrameFiles.py`
   File tree should be look like
- **project-root/**
   - `moveFrameFiles.py`
   - `file_list.txt`
   - **movie1K.keyframes.240p.v1/**
     - **240p/**   
   - **dataset/**
     - **framescene/**
   - **Other Files ...**

