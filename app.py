import streamlit as st
from config import load_llm
from core.data_loader import load_csv
from core.retriever import create_vector_store,retrieve_context
from core.prompt import build_prompt
from core.code_gen import generate_code
from core.code_exe import execute_code


st.set_page_config(page_title="RAG DATA ANALYST",layout="wide")
st.title("RAG ASSISTANT ANNALYST")
uploaded_file=st.file_uploader("upload csv",type=["csv"])

if uploaded_file:
    df=load_csv(uploaded_file)
    st.write("preview dataset")
    st.dataframe(df.head())

    vectorstore=create_vector_store(df)

    query=st.text_input("ask a question about your data")

    if query:
        llm=load_llm()

        context=retrieve_context(vectorstore,query)
        prompt=build_prompt(context,query)
        code=generate_code(llm,prompt)
        st.subheader("Generated code")
        st.code(code)
        result=execute_code(code,df)
        st.subheader("Result")
        st.write(result)