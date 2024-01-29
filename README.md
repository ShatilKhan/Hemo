![Modern Logo for Blood Donation, cool, AI-type (1)](https://github.com/ShatilKhan/Hemo/assets/52494840/6f3953f4-4596-41b4-aed9-8dfc2aae1ed7)

# Hemo🩸
*"A single drop of blood can make a huge difference."* 🩸  
Hemo is an AI Chatbot that helps Blood Donors learn more about Blood Donation &amp; predict Blood Donation Patterns.

# Table of Contents
1. [Hemo🩸](#hemo)
2. [Scenario](#scenario)
3. [Solution](#solution)
4. [SDG](#sustainable-development-goals)
5. [Features](#features)
6. [Demo](#demo-video)
7. [Setup](#local-setup)

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

## Medical Report Chat
Upload your Medical Report & Chat with it to understand & be informed as a blood donor. It's not perfect as I'm using an Open Source LLM at the moment  
Model: `impira/layoutlm-document-qa`  
type: `document-question-answering`  
Link to Model on Hugging Face: https:[//huggingface.co/impira/layoutlm-document-qa](https://huggingface.co/impira/layoutlm-document-qa)

It can only answer from a very clear pdf without watermark & all. Since most medical reports contain some form of WaterMark. We may need to use a more advance Open Source LLM. How ever installing & configuring larger Open Source LLMs takes a lot of time & internet speed. None of which I have at the moment. So currently I'll supply some sample Blood Test formats that users can use to test.
The goal is to automatically suggest the user about how & when they can donate blood based on their health report.
***Note: most of all , using a smaller Open Source LLM makes the deployment process much easier & also uses less energy, hence also reducing CO2 emissions.***

# Demo Video

Check out the Video of how the web app creates a beautiful Pairplot & calculates the percentage of people who did not donate blood:

https://github.com/ShatilKhan/Hemo/assets/52494840/886d656f-2afd-4a3c-8ba1-9c6372ba2e7f

I'm planning on using a fully open-source model instead of OpenAI because I'm lazy & don't want to create an API key everytime I rune the app, plus I don't have any credits left :)

# Local Setup

1.Install all the requirements
``` pip install -r requirements.txt```

2.Run the Web App
``` streamlit run hemo.py```

***Note*** ***: You will need Teseract-OCR & Pytorch installed on your device.***

### **`Currently Hemo can generate Pairplot from Blood Transfusion CSV data to predict Blood Donation Patterns.I'm currently working on adding the nearby blood donation center feature & automatic suggestion feature for different blood types`**
