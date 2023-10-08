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
def main():
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

    print(names[0])
    pinecone.init(
    api_key=PINECONE_API_KEY,  # find at app.pinecone.io
    environment=PINECONE_API_ENV  # next to api key in console
    )
    index_name = "chatbot" 


    load_dotenv()
    st.set_page_config(page_title="Ask your PDF")
    st.header("chatbot-v000 💬")

    # upload file
    pdf = st.file_uploader("Upload your PDF (optional)", type="pdf")

    text = ""
    if pdf is not None:
        pdf_reader = PdfReader(pdf)
        for page in pdf_reader.pages:
            text += page.extract_text()

    # split into chunks if text is not empty
    if text:
        text_splitter = CharacterTextSplitter(
            separator="\n",
            chunk_size=1000,
            chunk_overlap=200,
            length_function=len
        )
        chunks = text_splitter.split_text(text)
        print (f'Now you have {len(chunks)} documents,done')
    else:
        chunks = []
    



    # create embeddings
    embeddings = OpenAIEmbeddings()
    docsearch = Pinecone.from_texts(chunks, embeddings, index_name=index_name,namespace="cryohub1")
    #docsearch = <langchain.vectorstores.pinecone.Pinecone object at 0x000001EA6638FD60>
    print(docsearch)
    print("sucess1")
    knowledge_base = FAISS.from_texts(chunks, embeddings) if chunks else None

    # show user input
    user_question = st.text_input("Please ask your question.")
    if user_question:
        # perform similarity search only if knowledge base exists
        # docsearch = Pinecone.from_existing_index(index_name, embeddings,namespace="666666")
        # print(docsearch)
        # print("sucess2")
        # docs2 = docsearch.similarity_search(user_question)
        # docs2 = []
#/////////////////////////////////////////////////////////////////////////////////////////////////
        docsearch1 = Pinecone.from_existing_index(index_name, embeddings,namespace="cryohub")
        # docsearch3 = Pinecone.from_existing_index(index_name, embeddings,namespace=names[3])
        # docsearch4 = Pinecone.from_existing_index(index_name, embeddings,namespace=names[4])
        # docsearch7 = Pinecone.from_existing_index(index_name, embeddings,namespace=names[7])
        # docsearch8 = Pinecone.from_existing_index(index_name, embeddings,namespace=names[8])
        # docsearch9 = Pinecone.from_existing_index(index_name, embeddings,namespace=names[9])

        tempanwer1 = docsearch1.similarity_search(user_question,k=10)
        # tempanwer3 = docsearch3.similarity_search(user_question,k=4)
        # tempanwer4 = docsearch4.similarity_search(user_question,k=4)
        # tempanwer7 = docsearch7.similarity_search(user_question,k=4)
        # tempanwer8 = docsearch8.similarity_search(user_question,k=4)
        # tempanwer9 = docsearch9.similarity_search(user_question,k=4)

        docs = knowledge_base.similarity_search(user_question) if knowledge_base else []

        output_parser = RegexParser(
          regex=r"(.*?)\nScore: (.*)",
          output_keys=["answer", "score"],
        )
        prompt_template = """Use the following pieces of context to answer the question at the end. If you don't know the answer, just say that you don't know, don't try to make up an answer.

        In addition to giving an answer, also return a score of how fully it answered the user's question. This should be in the following format:

        Question: [question here]
        Helpful Answer In English: [answer here]
        Score: [score between 0 and 100]

        Begin!

        Context:
        ---------
        {context}
        ---------
        Question: {question}
        Helpful Answer In English:"""
        PROMPT = PromptTemplate(
          template=prompt_template,
          input_variables=["context", "question"],
          output_parser=output_parser,
        )
#///////////////////////////////////////////////////

        llm = OpenAI()

        chain = load_qa_chain(OpenAI(temperature=0), chain_type="map_rerank",verbose=True, return_intermediate_steps=True)
        with get_openai_callback() as cb:

            response1=chain({"input_documents": tempanwer1, "question": user_question}, return_only_outputs=True)
            # response3=chain({"input_documents": tempanwer3, "question": user_question}, return_only_outputs=True)
            # response4=chain({"input_documents": tempanwer4, "question": user_question}, return_only_outputs=True)
            # response7=chain({"input_documents": tempanwer7, "question": user_question}, return_only_outputs=True)
            # response8=chain({"input_documents": tempanwer8, "question": user_question}, return_only_outputs=True)
            # response9=chain({"input_documents": tempanwer9, "question": user_question}, return_only_outputs=True)

        st.write(names[1])
        st.write(response1)
        # st.write(names[3])
        # st.write(response3)
        # st.write(names[4])
        # st.write(response4)
        # st.write(names[7])
        # st.write(response7)
        # st.write(names[8])
        # st.write(response8)
        # st.write(names[9])
        # st.write(response9)
    

if __name__ == '__main__':
    main()
