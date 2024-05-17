import ollama

response = ollama.chat(model="llama3",
                       messages=[
                           {
                                "role":"system",
                                "content":"Say only Hello, I'm good and you?"
                            },
                           {
                               "role":"user",
                               "content":"Hello, how are you?"
                           }
                        
                       ])
print(response["message"]["content"])