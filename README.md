# use-case-gen

## Overview
This project features a chatbot designed to provide expert advice on leveraging Generative Artificial Intelligence (Generative AI) in businesses to enhance revenue and productivity. The chatbot simulates interaction with a Generative AI expert, offering brainstorming sessions and practical use case suggestions tailored to specific business contexts.

## Features
- Generative AI Expertise: The chatbot acts as a virtual consultantspecializing in Generative AI technologies.
- Use Case Generation: Provides creative and practical use cases where Generative AI can be applied to boost business operations.
- Holistic Planning: Guides users through step-by-step plans for implementing Generative AI solutions in their businesses.
- Contextual Understanding: Able to process business context provided via URL or text to tailor advice accordingly.
- Focused Expertise: Responds only to queries related to Generative AI applications; redirects non-relevant queries politely.

## Prerequisites

- Ensure you have Python 3.8 or later installed.
- Install dependencies using `pip`:
  ```bash
  pip install -r requirements.txt


## Setup

### Configure Google API Key

To enable functionality that requires a Google API key, set your key as an environment variable. Replace `YOUR_GOOGLE_API_KEY` with your actual API key

#### Add Folllowing Api keys to your .env file

```bash
GOOGLE_API_KEY = "GOOGLE_API_KEY"

USER_AGENT = "Search on google whats my user agent key and paste here"

LANGCHAIN_TRACING_V2 = true

LANGCHAIN_API_KEY = "Its Actually optional to put key but useful if you want to trace using langsmith" 
```


## Run the application 

```powershell
uvicorn app.main:app --reload
```
