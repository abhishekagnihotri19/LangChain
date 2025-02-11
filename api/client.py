import requests
import streamlit as st

def get_OpenAi_response(input_text):
    response= requests.post("http://localhost:8000/essay/invoke", 
                            json={'input': {'topic': input_text}})
    
    return response.json()['output']['content']


def get_Ollama_response(input_text):
    try:
        url = "http://localhost:8000/poem/invoke"  # Ensure this is correct
        payload = {"input": {"topic": input_text}}
        
        response = requests.post(url, json=payload)
        
        print("Status Code:", response.status_code)  # Print status code
        print("Response Text:", response.text)      # Print raw response
        
        response.raise_for_status()  # Raise an error for bad responses
        
        return response.json().get("output", "No output found")
    
    except requests.exceptions.JSONDecodeError:
        print("❌ JSON Decode Error: The response is not in JSON format.")
        return "Invalid JSON response from the server."
    except requests.exceptions.ConnectionError:
        print("❌ Connection Error: Is the server running?")
        return "Server not reachable."
    except requests.exceptions.RequestException as e:
        print("❌ Error:", e)
        return "Request error."

st.title("Demo of LangChain with Olamma API and ChatGPT API")
input_text=st.text_input("Write an Essay on")
input_text1= st.text_input("Write an Poem on")

if input_text:
    st.write(get_OpenAi_response(input_text))

if input_text1:
    st.write(get_Ollama_response(input_text1))