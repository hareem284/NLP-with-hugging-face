from config import HF_API_KEY
#
#In this activity, you'll build a Python script that leverages the Hugging Face Inference API to perform sentiment analysis on text input. The script demonstrates how to securely import your API key, set up the necessary HTTP headers for authentication, and send a JSON payload containing your text to the Hugging Face API endpoint. Using a pre-trained DistilBERT model fine-tuned on sentiment analysis (SST-2), the API returns a JSON response with classification results, which the script then prints. This exercise reinforces essential concepts such as API integration, secure token handling, and processing JSON responses in Python.
#importing requests
import requests
def classify_text(text):
   API_URL="https://huggingface.co/distilbert/distilbert-base-uncased-finetuned-sst-2-english"
   headers={"Authorization":f"Bearer {HF_API_KEY}"}
   payload={"inputs":text}
   response=requests.post(API_URL,headers=headers,json=payload)
   return response.json()


if __name__=="__main__":
    sample_text="i love using api"
    results=classify_text(sample_text)
    print(results)