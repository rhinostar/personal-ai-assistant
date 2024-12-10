from ollama import Client


# from ollama import chat
# from ollama import ChatResponse

# response: ChatResponse = chat(model='llama3', messages=[
#   {
#     'role': 'user',
#     'content': 'Why is the sky blue?',
#   },
# ])
# print(response['message']['content'])
# # or access fields directly from the response object
# print(response.message.content)


def ask_ollama(prompt):  
  client = Client(
    host='http://localhost:11434',
    headers={'x-some-header': 'some-value'}
  )
  response = client.chat(model='llama3', messages=[
    {
      'role': 'system',
      'content': '''You are an AI Personal Assistant, and your creator is Ryan. 
      You help in everyday tasks and tell some cool jokes. Give small response - short and crisp.
      Always ask for what can i help with at the end.
      ''',
    },
    {
      'role': 'user',
      'content': prompt,
    },
  ])
  resp = response.message.content
  print(resp)
  return resp

# print(response['message']['content'])
# # or access fields directly from the response object


