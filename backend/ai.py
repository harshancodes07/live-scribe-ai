import requests 


def generate_answer(question : str):
        
    prompt = f"""
    You are LiveScribe, an AI learning assistant.

    Explain the main topic in the transcript to a student.

    Requirements:
    - Give 3 to 5 sentences.
    - Explain how the process works.
    - Include the important inputs and outputs.
    - Use simple language.
    - Do not describe who said what.
    - Do not invent details.
    - Return only the explanation.

    Transcript:
    {question}

    Explanation:
    """

    print("The prompt that being send to ollama ")
    print (prompt)
    try:
        response = requests.post(
        "http://localhost:11434/api/generate",
        json={
            "model": "gemma3:1b",
            "prompt": prompt,
            "stream": False,
            "options": {
    "temperature": 0.2
}
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