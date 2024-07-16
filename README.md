# use-case-gen

**gen ai use cases**

## Description

`use-case-gen` is a tool designed to generate AI use cases. This repository provides the necessary code and instructions to set up and run the application.

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
