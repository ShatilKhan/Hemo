import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt
import requests
from langchain import PromptTemplate
import seaborn as sns
from transformers import pipeline
import pytesseract
from PIL import Image
from dotenv import load_dotenv
import os



st.set_page_config(page_title="💉 Hemo")
st.title('💉 Hemo')
st.subheader("Your AI Blood Health Expert")

# Set the path to the Tesseract OCR executable
pytesseract.pytesseract.tesseract_cmd = r'C:\msys64\mingw64\bin\tesseract.exe' 

# Google Places API URL- Converts lat.lng into map data
url = "https://maps.googleapis.com/maps/api/place/nearbysearch/json"

# Google Geocoding API URL - converts text input into lat & lng
geocode_url = "https://maps.googleapis.com/maps/api/geocode/json"

# Load the environment variables from the .env file
load_dotenv()

# Get the API key from the environment variable
api_key = os.getenv("GOOGLE_API_KEY")

# Create a text input field for the location
location = st.sidebar.text_input("Enter your current location:")

# Search & Display nearby clinics
if location:
    # Parameters for the geocoding API request
    geocode_params = {
        "address": location,  # Location name
        "key": api_key,  # Your Google Places API key
    }

    # Send the geocoding API request
    geocode_response = requests.get(geocode_url, params=geocode_params)

    # Parse the geocoding response
    geocode_data = geocode_response.json()

    # Extract the latitude and longitude from the geocoding response
    lat = geocode_data['results'][0]['geometry']['location']['lat']
    lng = geocode_data['results'][0]['geometry']['location']['lng']

    # Parameters for the Places API request
    places_params = {
        "location": f"{lat},{lng}",  # Latitude and longitude
        "radius": 5000,  # Search radius in meters
        "type": "hospital",  # Type of place to search for
        "key": api_key,  # Your Google Places API key
    }

    # Send the Places API request
    places_response = requests.get(url, params=places_params)

    # Parse the Places response
    places_data = places_response.json()

    # Extract the clinic locations from the Places response
    clinics = pd.DataFrame([{
        'lat': result['geometry']['location']['lat'],
        'lon': result['geometry']['location']['lng'],
    } for result in places_data['results']])

    # Display the clinics on a map
    st.subheader("Blood Donation Centers Near You")
    st.map(clinics)




# CSV file uploader in sidebar
uploaded_file = st.sidebar.file_uploader("Upload Dataset", type="csv")

# Medical Report Image
uploaded_image = st.sidebar.file_uploader("Upload Image", type=["png", "jpg", "jpeg"])

# Initialize the pipeline
pipe = pipeline("document-question-answering", model="impira/layoutlm-document-qa")


# Q&A form
with st.form('myform'):
    query_text = st.text_input('Enter your question:', '')
    submitted = st.form_submit_button('Submit')

    if submitted and uploaded_image is not None:
        # Open the image file
        img = Image.open(uploaded_image)

        # Use pytesseract to convert the image to text
        # text = pytesseract.image_to_string(img)

        # Use the pipeline to answer the question
        answer = pipe(question=query_text, image=img)

        # Get the best answer
        best_answer = answer[0]['answer']

        # Display the best answer
        st.write(best_answer)



# CSV Data Analysis
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

    st.subheader("Blood Donation Patterns")

    # Display the percentage as a progress bar
    st.progress(not_donated_percentage)

    # Display the percentage as text
    st.write(f"Percentage of not donated: {not_donated_percentage * 100}%")
    


    # Display the pairplot
    st.pyplot(pairplot.fig)


