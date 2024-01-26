import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt
from langchain.llms import OpenAI
from langchain import PromptTemplate
import seaborn as sns

st.set_page_config(page_title="💉 Hemo")
st.title('💉 Hemo')
openai_api_key = st.sidebar.text_input('OpenAI API Key', type='password')

def generate_response(query):
  llm = OpenAI(model_name='text-davinci-003', openai_api_key=openai_api_key)
  # Prompt
  template = 'As an AI Phlebotomist, provide information on {query}.'
  prompt = PromptTemplate(input_variables=['query'], template=template)
  prompt_query = prompt.format(query=query)
  # Run LLM model and print out response
  response = llm(prompt_query)
  return st.info(response)

with st.form('myform'):
  query_text = st.text_input('Enter your question:', '')
  submitted = st.form_submit_button('Submit')
  if not openai_api_key.startswith('sk-'):
    st.warning('Please enter your OpenAI API key!', icon='⚠')
  if submitted and openai_api_key.startswith('sk-'):
    generate_response(query_text)

# CSV file uploader in sidebar
uploaded_file = st.sidebar.file_uploader("Choose a CSV file", type="csv")

if uploaded_file is not None:
    # Read the CSV file
    df = pd.read_csv(uploaded_file)

    # Create a pairplot
    pairplot = sns.pairplot(df)

    # Display the pairplot
    st.pyplot(pairplot.fig)