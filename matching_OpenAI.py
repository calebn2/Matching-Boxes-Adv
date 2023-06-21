import json
import openai
import os

# Calls GPT-4
def get_response(data_string, user):
  # Messages I give to GPT-4
  system_training = "You are a teacher who is creating an online matching assignment for your students. Your job is to make a JSON 2D array similar to the following 2D array: "
  system_instructions = ". You should return an array with four arrays inside of it. You should not make JSON objects named 'content' and 'output', but rather replace 'content' and 'output' in the array with the content and output that you make. You should replace 'content' with content that relates to the school topic formatted in html inside of a string, and you should replace 'output' with the output answer to the question. All of the content should be generic to make the questions harder. The arrays should be inside of three backticks like so: ```[[code, output],[code, output]]```. Do not use any html tags except for <sub> and <sup>. Just put the content in a string."
  user_content = insert_topic("calling static methods", user)
  # OpenAI Keys
  openai.organization = "org-4syK5rpvVR7nABjSceLGim9e"
  openai.api_key = os.environ["OPENAI_API_KEY"]

  # OpenAI request
  MODEL = "gpt-4"
  description = system_training + data_string + system_instructions
  response = openai.ChatCompletion.create(
      model=MODEL,
      messages = [
         {"role": "system", "content": description},
         {"role": "user", "content": user_content},
      ],
      temperature=0,
  )
  # The response
  whole_message = response['choices'][0]['message']['content']
  
  first_index = whole_message.find("```") + 3
  last_index = whole_message.find("```", first_index + 1)
  final_message = whole_message[first_index:last_index]
  new_data = json.loads(final_message)
  make_file(new_data)

def make_file(new_data):
  # Makes a JSON file called boxes.json which contains the response from GPT
  with open("boxes.json", "w") as outfile:
      json.dump(new_data, outfile)

def get_user_content(topic, data):
    if topic == "calc":
      file = 'APCalcABBCPrompt.txt'
    if topic == "chemistry":
      file = 'APChemistryPrompt.txt'
    if topic == "CSA":
      file = 'APComputerScienceAPrompt.txt'
    if topic == "world":
      file = 'APWorldHistoryPrompt.txt'
    with open(file, "r") as f:
      lines = f.readline()
    f.close
    get_response(data, lines)

def get_file():
  file = open('data.json')
  data = json.load(file)
  data_string = str(data)
  file.close
  get_user_content("CSA", data_string)

def insert_topic(text, prompt):
  index = prompt.find("[TOPIC]")
  new_prompt = prompt[:index] + text + prompt[(index + 7):]
  return new_prompt
get_file()