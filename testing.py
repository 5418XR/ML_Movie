import openai
import os
import streamlit as st
from dotenv import load_dotenv, find_dotenv

from dotenv import load_dotenv, find_dotenv
_ = load_dotenv(find_dotenv()) # read local .env file
from dotenv import load_dotenv
# import streamlit as st
from PyPDF2 import PdfReader
from langchain.text_splitter import CharacterTextSplitter
from langchain.embeddings.openai import OpenAIEmbeddings
from langchain.vectorstores import FAISS
from langchain.chains.question_answering import load_qa_chain
from langchain.llms import OpenAI
from langchain.callbacks import get_openai_callback


from langchain.vectorstores import Chroma,Pinecone
from langchain.embeddings.openai import OpenAIEmbeddings
import pinecone
import os
from langchain.prompts import PromptTemplate

from langchain.embeddings.openai import OpenAIEmbeddings
from langchain.text_splitter import CharacterTextSplitter
from langchain.vectorstores import Chroma
from langchain.docstore.document import Document
from langchain.prompts import PromptTemplate
from langchain.indexes.vectorstore import VectorstoreIndexCreator

from langchain.output_parsers import RegexParser
from langchain.chains.question_answering import load_qa_chain
from dotenv import dotenv_values
from langchain.chains.summarize import load_summarize_chain
from langchain.document_loaders import TextLoader
from langchain.text_splitter import RecursiveCharacterTextSplitter
from langchain.llms import OpenAI

from pdfminer.high_level import extract_text
import webbrowser
import os

openai.api_key  = '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'
PINECONE_API_KEY = os.environ.get('PINECONE_API_KEY', 'bacc7a5f-0b08-4aae-8695-6fa9e0f458a9')
PINECONE_API_ENV = os.environ.get('PINECONE_API_ENV', 'us-west1-gcp-free')
pinecone.init(api_key=PINECONE_API_KEY,  # find at app.pinecone.io
    environment=PINECONE_API_ENV  # next to api key in console
)
index_name = "chatbot" 

def get_completion(prompt, model="gpt-3.5-turbo"):
    messages = [{"role": "user", "content": prompt}]
    response = openai.ChatCompletion.create(
        model=model,
        messages=messages,
        temperature=0,
    )
    return response.choices[0].message["content"]

# Streamlit App
st.title("Ask a Question")

# Initialize 'clicked_docs' and 'response_text' in session state if they don't exist
if 'clicked_docs' not in st.session_state:
    st.session_state.clicked_docs = []
if 'response_text' not in st.session_state:
    st.session_state.response_text = ""

user_input = st.text_area("Please provide your question:", "What pin is connected to the blue LED?")
submit_button = st.button("Submit")

if submit_button:
    text = """
    You are seeking advice for an undergraduate Embedded Systems course.
    In this course, students primarily use the MSP432 hardware.
    The MSP432 is a mixed-signal microcontroller family from Texas Instruments.
    They need to consult certain documents to help them address their questions and issues.
    Here are the documents that the students might refer to:

    "BoosterPack Quick Guide"
    "Launchpad User Guide"
    "Launchpad Quick Guide"
    "Graphics Library User Guide"
    "DriverLib User Guide"
    "Light Sensor"
    "Temperature Sensor"
    "MCU Technical Reference Manual"
    "MCU Datasheet"
    "BoosterPack User Guide"
    """
    prompt = f"{user_input}\n```{text}```"
    st.session_state.response_text = get_completion(prompt)

response = st.session_state.response_text
st.write(response)

names = [
    "BoosterPack Quick Guide",
    "Launchpad User Guide",
    "Launchpad Quick Guide",
    "Graphics Library User Guide",
    "DriverLib User Guide",
    "Light Sensor",
    "Temperature Sensor",
    "MCU Technical Reference Manual",
    "MCU Datasheet",
    "BoosterPack User Guide"
]

# Function to search the PDF and open in the default browser
def search_pdf_and_open(pdf_filename, sentence):
    try:
        content = extract_text(pdf_filename)
        pages = content.split('\f')
        for page_num, page_content in enumerate(pages):
            if sentence in page_content:
                st.write(f"Found sentence '{sentence}' in {pdf_filename} on page {page_num + 1}. Attempting to open in default browser...")
                webbrowser.open(f"file:///{os.path.abspath(pdf_filename)}")
                webbrowser.open(f'https://www.google.com/search?q={sentence}')
                st.write(f"You might need to manually navigate to page {page_num + 1}.")
                return
    except Exception as e:
        st.write(f"Error reading {pdf_filename}: {e}")

if 'clicked_docs' not in st.session_state:
    st.session_state.clicked_docs = []
if 'namespace_string' not in st.session_state:
    st.session_state.namespace_string = ""

selected_names = [name for name in names if name in response]

for name in selected_names:
    col1, col2, col3 = st.columns([4, 1, 1])

    with col1:
        if st.button(name):  # 保留文件名按钮
            st.write(f"You clicked on: {name}")

        embeddings = OpenAIEmbeddings()
        docsearch1 = Pinecone.from_existing_index(index_name, embeddings, namespace=name)
        tempanwer1 = docsearch1.similarity_search(user_input, k=4)
        llm = OpenAI()
        chain = load_qa_chain(OpenAI(temperature=0), chain_type="map_rerank", verbose=True, return_intermediate_steps=True)
        response1 = chain({"input_documents": tempanwer1, "question": user_input}, return_only_outputs=True)
        answer_score_pairs = [(step['answer'], step['score']) for step in response1['intermediate_steps']]
        for index, pair in enumerate(answer_score_pairs):
            answer = pair[0]
            score = pair[1]

            # 确保答案和其后的按钮在同一行，同时确保大拇指按钮靠右
            ans_col, thumbs_up_col, thumbs_down_col = st.columns([7, 1, 1])
            with ans_col:
                st.write(f"{answer} (Score: {score})")
            with thumbs_up_col:
                if st.button(f"👍", key=f"thumbs_up_answer_{index}_{name}"):
                    st.write(f"You clicked 👍 for answer: {answer}")
            with thumbs_down_col:
                if st.button(f"👎", key=f"thumbs_down_answer_{index}_{name}"):
                    st.write(f"You clicked 👎 for answer: {answer}")

    with col2:
        if st.button(f"👍", key=f"thumbs_up_{name}"):  # unique key based on name
            st.write(f"You clicked 👍 for: {name}")
            # Add any logic you want here for thumbs up

    with col3:
        if st.button(f"👎", key=f"thumbs_down_{name}"):  # unique key based on name
            st.write(f"You clicked 👎 for: {name}")
            # Add any logic you want here for thumbs down
# If the answer_score_pairs attribute exists in the session state, display those buttons
if 'answer_score_pairs' in st.session_state:
    for index, pair in enumerate(st.session_state.answer_score_pairs):
        answer = pair[0]
        score = pair[1]

        unique_key = f"answer_{index}_{answer}"

        if st.button(f"{answer} (Score: {score})", key=unique_key):
            st.write(f"You clicked on: {answer} with a score of {score}")

            pdf_filename = f"{st.session_state.namespace_string}.pdf"
            search_sentence = answer.strip()
            print(pdf_filename, search_sentence)
            # search_pdf_and_open(pdf_filename, search_sentence)
            abs_path = os.path.abspath(pdf_filename)
            print(f"Trying to open: {abs_path}")
            webbrowser.open(f"file:///{abs_path}")


