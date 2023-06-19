import json
import openai
import os

def get_response(data_string):
  system_training = "You are a Java computer science teacher who is creating an online matching assignment for your students. Your job is to make a JSON 2D array similar to the following 2D array: "
  system_instructions = ". You should return an array with four arrays inside of it, each array you make has a code segment and the output to that code segment. You should replace \"code\" with a java code segment formatted in html inside of a string, and you should replace \"output\" with the output of the code segment inside of a string if it was to run. All of the code and outputs should be unique from each other. Java variables should have generic names like: x, y, and z. The Java must relate to for or while loops."

  # Example OpenAI Python library request
  openai.organization = "org-4syK5rpvVR7nABjSceLGim9e"
  openai.api_key = os.environ["OPENAI_API_KEY"]

  MODEL = "gpt-4"
  description = system_training + data_string + system_instructions
  response = openai.ChatCompletion.create(
      model=MODEL,
      messages = [
         {"role": "system", "content": description},
         {"role": "user", "content": "Make me a matching exercise that tests me over nested for and while loops"},
      ],
      temperature=0,
  )

  whole_message = response['choices'][0]['message']['content']
  
  print(whole_message)
  first_index = whole_message.find("```") + 3
  last_index = whole_message.find("```", first_index + 1)
  final_message = whole_message[first_index:last_index]
  print(f"\n\nFirst Index: {first_index}")
  print(f"Last Index: {last_index}")
  print(f"Final Message:\n\n\n" + final_message)
  print(type(final_message))
  new_data = json.loads(final_message)
  make_file(new_data)

def make_file(new_data):
  # Makes a JSON file called boxes.json which contains the response from GPT
  with open("boxes.json", "w") as outfile:
      json.dump(new_data, outfile)

def get_file():
  file = open('data.json')
  data = json.load(file)
  data_string = str(data)
  file.close
  get_response(data_string)

get_file()