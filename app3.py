from dotenv import load_dotenv
import streamlit as st
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
import os

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
    # load_dotenv()
    # st.set_page_config(page_title="Ask your PDF")
    # st.header("Ask your PDF 💬")
    
    # # upload file
    # pdf = st.file_uploader("Upload your PDF", type="pdf")
    
    # # extract the text
    # if pdf is not None:
    #   pdf_reader = PdfReader(pdf)
    #   text = ""
    #   for page in pdf_reader.pages:
    #     text += page.extract_text()
        
    #   # split into chunks
    #   text_splitter = CharacterTextSplitter(
    #     separator="\n",
    #     chunk_size=1000,
    #     chunk_overlap=200,
    #     length_function=len
    #   )
    #   chunks = text_splitter.split_text(text)
      
    #   # create embeddings
    #   embeddings = OpenAIEmbeddings()
    #   knowledge_base = FAISS.from_texts(chunks, embeddings)
      
    #   # show user input
    #   user_question = st.text_input("Give me a response when I am a high school student with absolutely no hardware knowledge.")
    #   if user_question:
    #     docs = knowledge_base.similarity_search(user_question)
        
    #     llm = OpenAI()
    #     chain = load_qa_chain(llm, chain_type="stuff")
    #     with get_openai_callback() as cb:
    #       response = chain.run(input_documents=docs, question=user_question)
    #       print(cb)
           
    #     st.write(response)
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
    docsearch = Pinecone.from_texts(chunks, embeddings, index_name=index_name,namespace="TT")
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
        docsearch1 = Pinecone.from_existing_index(index_name, embeddings,namespace=names[1])
        docsearch3 = Pinecone.from_existing_index(index_name, embeddings,namespace=names[3])
        docsearch4 = Pinecone.from_existing_index(index_name, embeddings,namespace=names[4])
        docsearch7 = Pinecone.from_existing_index(index_name, embeddings,namespace=names[7])
        docsearch8 = Pinecone.from_existing_index(index_name, embeddings,namespace=names[8])
        docsearch9 = Pinecone.from_existing_index(index_name, embeddings,namespace=names[9])

        tempanwer1 = docsearch1.similarity_search(user_question,k=4)
        tempanwer3 = docsearch3.similarity_search(user_question,k=4)
        tempanwer4 = docsearch4.similarity_search(user_question,k=4)
        tempanwer7 = docsearch7.similarity_search(user_question,k=4)
        tempanwer8 = docsearch8.similarity_search(user_question,k=4)
        tempanwer9 = docsearch9.similarity_search(user_question,k=4)

        docs = knowledge_base.similarity_search(user_question) if knowledge_base else []



#//////////////////////////////////////////////////

    #     refine_prompt_template = (
    # "The original question is as follows: {question}\n"
    # "We have provided an existing answer: {existing_answer}\n"mka
    # "We have the opportunity to refine the existing answer"
    # "(only if needed) with some more context below.\n"
    # "------------\n"
    # "{context_str}\n"
    # "------------\n"
    # "Given the new context, refine the original answer to better "
    # "answer the question. "
    # "If the context isn't useful, return the original answer. Reply in English."
    #   )
    #     refine_prompt = PromptTemplate(
    #     input_variables=["question", "existing_answer", "context_str"],
    #     template=refine_prompt_template,
    #   )


    #     initial_qa_template = (
    #     "Context information is below. \n"
    #     "---------------------\n"
    #     "{context_str}"
    #     "\n---------------------\n"
    #     "Given the context information and not prior knowledge, "
    #     "answer the question: {question}\nYour answer should be in English.\n"
    #   )
    #     initial_qa_prompt = PromptTemplate(
    #     input_variables=["context_str", "question"], template=initial_qa_template
    #   )
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
        # chain = load_qa_chain(OpenAI(temperature=0), chain_type="refine", return_refine_steps=True,
        #              question_prompt=initial_qa_prompt, refine_prompt=refine_prompt)

        chain = load_qa_chain(OpenAI(temperature=0), chain_type="map_rerank",verbose=True, return_intermediate_steps=True)

        # print(docs2)
        # print(docs)
        # input_variables= ["comument1:"+docs, "comument2:"+docs2]
        # input_variables= ["comument1:" + " ".join(docs), "comument2:" + " ".join(docs2)]
        # input_variables= ["comument1:" + " ".join(doc.content for doc in docs), "comument2:" + " ".join(doc.content for doc in docs2)]
        # prompt = PromptTemplate(
        # input_variables=["docs", "docs2"],
        # template="The document answer the question {docs} and {docs2}",
        # )
        # # documents = [Document(page_content=text) for text in prompt]
        with get_openai_callback() as cb:
            # response = chain.run(input_documents=docs, question=user_question)
            # response = chain.run(input_documents=docs2, question=user_question)
            #print(docs2)
            response1=chain({"input_documents": tempanwer1, "question": user_question}, return_only_outputs=True)
            response3=chain({"input_documents": tempanwer3, "question": user_question}, return_only_outputs=True)
            response4=chain({"input_documents": tempanwer4, "question": user_question}, return_only_outputs=True)
            response7=chain({"input_documents": tempanwer7, "question": user_question}, return_only_outputs=True)
            response8=chain({"input_documents": tempanwer8, "question": user_question}, return_only_outputs=True)
            response9=chain({"input_documents": tempanwer9, "question": user_question}, return_only_outputs=True)
            # print(response1)
            # print(cb)
            # print(tempanwer1)

        #text = '\n'.join(doc.page_content for doc in docs2)
        # Open the file with write permission
        # with open("output.txt", "w",encoding='utf-8') as file:
          # Write the text to the file
          # file.write(text)

        st.write(names[1])
        st.write(response1)
        st.write(names[3])
        st.write(response3)
        st.write(names[4])
        st.write(response4)
        st.write(names[7])
        st.write(response7)
        st.write(names[8])
        st.write(response8)
        st.write(names[9])
        st.write(response9)
    

if __name__ == '__main__':
    main()

