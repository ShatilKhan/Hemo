import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt

from langchain import PromptTemplate
import seaborn as sns
from transformers import pipeline
import pytesseract
from PIL import Image

# Set the path to the Tesseract OCR executable
pytesseract.pytesseract.tesseract_cmd = r'C:\msys64\mingw64\bin\tesseract.exe' 

st.set_page_config(page_title="💉 Hemo")
st.title('💉 Hemo')

# CSV file uploader in sidebar
uploaded_file = st.sidebar.file_uploader("Upload Blood Donor Dataset", type="csv")

# Medical Report Image
uploaded_image = st.sidebar.file_uploader("Upload Image", type=["png", "jpg", "jpeg"])

# Initialize the pipeline
pipe = pipeline("question-answering", model="impira/layoutlm-document-qa")

with st.form('myform'):
    query_text = st.text_input('Enter your question:', '')
    submitted = st.form_submit_button('Submit')

    if submitted and uploaded_image is not None:
        # Open the image file
        img = Image.open(uploaded_image)

        # Use pytesseract to convert the image to text
        text = pytesseract.image_to_string(img)

        # Use the pipeline to answer the question
        answer = pipe(question=query_text, context=text)

        # Display the answer
        st.write(answer['answer'])




if uploaded_file is not None:
    # Read the CSV file
    df = pd.read_csv(uploaded_file)

    # Set style and color palette
    sns.set_style('dark')
    sns.set_palette('icefire')

    # Set the background color to transparent
    plt.rcParams['figure.facecolor'] = 'none'
    plt.rcParams['axes.facecolor'] = 'none'

    # Set the text color to white
    plt.rcParams['text.color'] = 'white'
    plt.rcParams['axes.labelcolor'] = 'white'
    plt.rcParams['xtick.color'] = 'white'
    plt.rcParams['ytick.color'] = 'white'

    # Create a pairplot
    pairplot = sns.pairplot(df, hue='Class')

    # Reset the settings to default after creating the plot
    plt.rcParams.update(plt.rcParamsDefault)


    # Calculate & Display KPIs

    

    # Percentage of Not Donated

    # Define the dictionary
    class_dict = {'donated': 2, 'not donated': 1}

    # Replace the values
    df['Class'] = df['Class'].replace(class_dict)

    # Calculate the count of 'donated' and 'not donated'
    class_counts = df['Class'].value_counts()

    # Calculate the percentage of 'not donated'
    not_donated_percentage = (class_counts[1] / class_counts.sum()) * 100

    # Round to two decimal places
    not_donated_percentage = round(not_donated_percentage, 2)

    # Assuming not_donated_percentage is already calculated
    not_donated_percentage = not_donated_percentage / 100  # Convert the percentage to a fraction

    # Display the percentage as a progress bar
    st.progress(not_donated_percentage)

    # Display the percentage as text
    st.write(f"Percentage of not donated: {not_donated_percentage * 100}%")
    


    # Display the pairplot
    st.pyplot(pairplot.fig)


