import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt
import requests
import seaborn as sns
from transformers import pipeline
import pytesseract
from PIL import Image
from dotenv import load_dotenv
import os
import google.generativeai as ggi


st.set_page_config(page_title="💉 Hemo")
st.title('💉 Hemo')
st.subheader("Your AI Blood Health Expert")

# Set the path to the Tesseract OCR executable
# pytesseract.pytesseract.tesseract_cmd = r'C:\msys64\mingw64\bin\tesseract.exe' 

# Google Places API URL- Converts lat.lng into map data
url = "https://maps.googleapis.com/maps/api/place/nearbysearch/json"

# Google Geocoding API URL - converts text input into lat & lng
geocode_url = "https://maps.googleapis.com/maps/api/geocode/json"

# Load the environment variables from the .env file
load_dotenv()

# Get the API key from the environment variable
api_key = os.getenv("GOOGLE_API_KEY")


# Gemini
ggi.configure(api_key = api_key)

model = ggi.GenerativeModel("gemini-1.5-flash") 
chat = model.start_chat()

def LLM_Response(question):
    response = chat.send_message(question,stream=True)
    return response

user_quest = st.text_input("Ask a question:", key="chat")
btn = st.button("Ask")

if btn and user_quest:
    result = LLM_Response(user_quest)
    st.subheader("Response : ")
    for word in result:
        st.text(word.text)

# Disclaimer
st.markdown("""
*Disclaimer: The information provided by the AI assistant is for educational purposes only and should not be considered medical advice. Please consult a healthcare professional for personalized medical guidance.*
""")

# End Gemini


# Find Donors Based on Location & Blood Group
# Load donor data from the external file

# Direct download link for the file hosted on Google Drive
url = "https://drive.google.com/uc?export=download&id=1dHAnD4bIpIu6maRLFhA0OEw3zN2237dh"

@st.cache_data  # Cache the data so it doesn't reload every time
def load_donor_data():
    return pd.read_excel(url)

donor_data = load_donor_data()

# Function to filter donors by blood group and location
def filter_donors(blood_group, location):
    # Adjust column names to match the new DataFrame structure
    return donor_data[
        (donor_data['Blood Group'] == blood_group) & 
        (donor_data['Hometown'].str.contains(location, case=False))
    ]


# Sidebar inputs for blood group and location
st.sidebar.header("Find a Blood Donor")
blood_group = st.sidebar.selectbox("Select Blood Group:", ["A+", "A-", "B+", "B-", "AB+", "AB-", "O+", "O-"])
location = st.sidebar.text_input("Enter your current location:", key="donor_loc")

# Search button in sidebar
if st.sidebar.button("Search Donors"):
    if blood_group and location:
        filtered_donors = filter_donors(blood_group, location)
        if not filtered_donors.empty:
            st.subheader("Available Donors:")
            st.table(filtered_donors[['Name', 'Contact No.', 'Hometown']])
        else:
            st.write("No donors found for the specified blood group and location.")
    else:
        st.write("Please enter both a blood group and a location.")



# End of Donor Finding Feature



# Caching API requests
@st.cache_data
def geocode_location(location, api_key):
    geocode_params = {
        "address": location,
        "key": api_key,
    }
    response = requests.get(geocode_url, params=geocode_params)
    return response.json()

@st.cache_data
def get_nearby_clinics(lat, lng, api_key):
    places_params = {
        "location": f"{lat},{lng}",
        "radius": 5000,
        "type": "hospital",
        "key": api_key,
    }
    response = requests.get(url, params=places_params)
    return response.json()

# Location input
location = st.sidebar.text_input("Enter your current location:", key="location")

if location:
    geocode_data = geocode_location(location, api_key)
    if 'results' in geocode_data and len(geocode_data['results']) > 0:
        lat = geocode_data['results'][0]['geometry']['location']['lat']
        lng = geocode_data['results'][0]['geometry']['location']['lng']
        places_data = get_nearby_clinics(lat, lng, api_key)

        clinics = pd.DataFrame([{
            'lat': result['geometry']['location']['lat'],
            'lon': result['geometry']['location']['lng'],
        } for result in places_data.get('results', [])])

        st.subheader("Blood Donation Centers Near You")
        st.map(clinics)



# CSV file uploader in sidebar
uploaded_file = st.sidebar.file_uploader("Upload Dataset", type="csv")

# Medical Report Image
uploaded_image = st.sidebar.file_uploader("Upload Image", type=["png", "jpg", "jpeg"])

# Caching the pipeline initialization
@st.cache_resource
def load_pipeline():
    return pipeline("document-question-answering", model="impira/layoutlm-document-qa")


# Q&A form
if uploaded_image is not None:
    pipe = load_pipeline()

    with st.form('myform'):
        query_text = st.text_input('Enter your question:', '' , key="img_qna")
        submitted = st.form_submit_button('Submit')

        if submitted:
            # Open the image file
            img = Image.open(uploaded_image)

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
    # plt.rcParams['figure.facecolor'] = 'none'
    # plt.rcParams['axes.facecolor'] = 'none'

    # Set the text color to white
    plt.rcParams['text.color'] = 'red'
    plt.rcParams['axes.labelcolor'] = 'red'
    plt.rcParams['xtick.color'] = 'red'
    plt.rcParams['ytick.color'] = 'red'

# Replace data type to reduce memory
    if 'Class' in df.columns:
        df['Class'] = df['Class'].astype('category')

    # Calculate & Display KPIs
    if 'Class' in df.columns:
        # Define the dictionary
        class_dict = {'donated': 2, 'not donated': 1}
        df['Class'] = df['Class'].cat.rename_categories(class_dict)

        # Calculate the count of 'donated' and 'not donated'
        class_counts = df['Class'].value_counts()
        not_donated_percentage = round((class_counts[1] / class_counts.sum()) * 100, 2)
        not_donated_fraction = not_donated_percentage / 100

        st.subheader("Blood Donation Patterns")

        # Display the percentage as a progress bar
        st.progress(not_donated_fraction)

        # Display the percentage as text
        st.write(f"Percentage of not donated: {not_donated_percentage}%")
        # Display the percentage as text
        st.write(f"1=not donated , 2=donated")


        # Reduce sample size for plotting
        max_sample_size = 500  # Adjust this number based on resource limits
        if len(df) > max_sample_size:
            df_sampled = df.sample(n=max_sample_size, random_state=42)
        else:
            df_sampled = df

        # Create a pairplot
        pairplot = sns.pairplot(df_sampled, hue='Class')

        # Reset the settings to default after creating the plot
        plt.rcParams.update(plt.rcParamsDefault)

        # Display the pairplot
        st.pyplot(pairplot.fig)


