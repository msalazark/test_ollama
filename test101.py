import ollama

model = "llama3"
response = ollama.chat(
    model=model,
    messages=[
        {"role": "user", "content": "What's the capital of Poland?"}
    ]
)
print(response["message"]["content"])

## Prints: The capital of Poland is Warsaw (Polish: Warszawa).