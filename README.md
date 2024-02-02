![Hemo](https://github.com/ShatilKhan/Hemo/assets/52494840/0ec6a69e-6c42-41c3-b520-443ef132d507)


# Hemo🩸
*"A single drop of blood can make a huge difference."* 🩸  
Hemo is an AI Chatbot that helps Blood Donors learn more about Blood Donation &amp; predict Blood Donation Patterns.

[![GitHub stars](https://img.shields.io/github/stars/ShatilKhan/Hemo.svg)](https://github.com/Shatikhan/Hemo/stargazers)
[![GitHub watchers](https://img.shields.io/github/watchers/ShatilKhan/Hemo.svg)](https://github.com/Shatikhan/Hemo/watchers)
[![Pull Requests](https://img.shields.io/github/issues-pr/ShatilKhan/Hemo.svg)](https://github.com/Shatikhan/Hemo/pulls)
[![GitHub forks](https://img.shields.io/github/forks/ShatilKhan/Hemo.svg)](https://github.com/Shatikhan/Hemo/network/members)
[![Issues](https://img.shields.io/github/issues/ShatilKhan/Hemo.svg)](https://github.com/Shatikhan/Hemo/issues)
[![License](https://img.shields.io/github/license/ShatilKhan/Hemo.svg)](https://github.com/Shatikhan/Hemo/blob/main/LICENSE)

# Table of Contents
- [Hemo🩸](#hemo)
- [Table of Contents](#table-of-contents)
- [Scenario](#scenario)
- [Solution](#solution)
- [Sustainable Development Goals](#sustainable-development-goals)
- [Features](#features)
  - [Maps](#maps)
  - [Medical Report Chat](#medical-report-chat)
  - [Blood Donation Pattern Prediction](#blood-donation-pattern-prediction)
- [Demo](#demo-video)
- [Local Setup](#local-setup)

# Scenario
Every 2 seconds, someone in the U.S. needs blood, and more than 50,000 units of blood are needed each year at Cedars-Sinai alone.While 38% of the American population is eligible to give blood, only 2% actually donates. While this is just the condition of America, the scene is much worse in under-developed & developing countries like Rwanda , Bangladesh & many more. It's become so scarce to find blood donors that Rwanda is even using drones to supply blood from big cities to remote villages. In Bangladesh alone there's thousands of people that need blood everday. Most people lack the awarness about blood donation activities. So even if there are hundreds of blood donation camps, we still don't get blood donors. Hence the need for proper encouragement & information on blood donation. Hemo aims to encourage the young population through Generative AI to give proper assessment on the donors blood, manage thier donor information & also predict Blood Donation Patterns using Generative AI.  
Forecasting blood supply is a serious and recurrent problem for blood collection managers: in January 2019, "Nationwide, the Red Cross saw 27,000 fewer blood donations over the holidays than they see at other times of the year." Machine learning can be used to learn the patterns in the data to help to predict future blood donations and therefore save more lives.

# Solution
Hemo is an AI chatbot built for Social Good Purpose of encouraging blood donation activities. 
Hemo has the follwoing features:
- Getting Donors Blood Report as input (via pdf, txt file)
- Showing information about the donors blood type (which blood types are compatible, health advice for each blood type)
- Show nearby Blood Donation Centers where Donors can Register or Donate Blood
- Predicting Blood Donation Pattern by Analyzing Huge Amounts of Blood Donor Reports

# Sustainable Development Goals
![image](https://github.com/ShatilKhan/Hemo/assets/52494840/31bf9b26-a706-4a67-98a4-6d99884570f1)

# Features

## Maps
User can enter their current location & the web app will show nearby clinics/healthcare centers where they can donate blood.
API: Google Places API
![image](https://github.com/ShatilKhan/Hemo/assets/52494840/6d2a179c-0e69-4344-8dfb-908d354d25af)



## Medical Report Chat
Upload your Medical Report & Chat with it to understand & be informed as a blood donor. It's not perfect as I'm using an Open Source LLM at the moment  
Model: `impira/layoutlm-document-qa`  
type: `document-question-answering`  
Link to Model on Hugging Face: https:[//huggingface.co/impira/layoutlm-document-qa](https://huggingface.co/impira/layoutlm-document-qa)

You can upload & ask about you're blood test report now.
The goal is to automatically suggest the user about how & when they can donate blood based on their health report.  
***Note: most of all , using a smaller Open Source LLM makes the deployment process much easier & also uses less energy, hence also reducing CO2 emissions.***

## Blood Donation Pattern Prediction
You can upload a CSV data of blood donors & create a pattern prediction. This part uses the Pandas library & some python logic.
The web app creates a beautiful Pairplot & calculates the percentage of people who did not donate blood.
![image](https://github.com/ShatilKhan/Hemo/assets/52494840/75db5502-d2e1-411c-92b5-225ea473023a)

# Demo Video
This is the full demo of all the mentioned features.
First we see a location entered & immidiately nearby blood donation centers are shown.
Then We enter a CSV data of blood donors & a pattern is predicted through pairplot
Lastly we upload our Blood Test report & ask it general questions.


https://github.com/ShatilKhan/Hemo/assets/52494840/de2eda0e-2d74-4fdc-94ad-482cc91dea59



I'm using a fully open-source model instead of OpenAI because I'm lazy & don't want to create an API key everytime I run the app, plus I don't have any credits left :)

# Local Setup

## Prerequisites  
Install `PyTorch` , `Tesseract-OCR` on your device.

## Installation  

1.Install all the requirements  
```bash
pip install -r requirements.txt
```  
2. Rename `.env_sample` to `.env` & add your Google Places API KEY  
```
GOOGLE_API_KEY= "AI......"
```
3.Run the Web App   
```bash
streamlit run hemo.py
```

