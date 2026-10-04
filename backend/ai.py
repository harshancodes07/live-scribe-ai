import requests 


def generate_answer(question : str):
    prompt = question 
    print("The prompt that being send to ollama ")
    print (prompt)
    try:
        response = requests.post(
        "http://localhost:11434/api/generate",
        json={
            "model": "gemma3:270m",
            "prompt": prompt,
            "stream": False
        },
        timeout = 60

    )
        response.raise_for_status()
        
        data = response.json()

        return data["response"]
    except requests.exceptions.ConnectionError:
        return "Could not connect to Ollama. Make sure Ollama is running."
    except requests.exceptions.Timeout:
        return "Ollama took long to respond"
    except Exception as e :
        return f"Something went wrong: {str(e)}"