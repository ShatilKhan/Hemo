import streamlit as st
from langchain.llms import OpenAI
from langchain import PromptTemplate

st.set_page_config(page_title="💉 AI Blood Donation Expert")
st.title('💉 AI Blood Donation Expert')
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
