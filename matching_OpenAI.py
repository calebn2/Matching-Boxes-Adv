import json
import openai
import os

# Calls GPT-4
def get_response(system_prompt, user_prompt):
  # Messages I give to GPT-4
  system_training = system_prompt
  # OpenAI Keys
  openai.organization = "org-4syK5rpvVR7nABjSceLGim9e"
  openai.api_key = os.environ["OPENAI_API_KEY"]

  # OpenAI request
  MODEL = "gpt-4"
  description = system_training
  response = openai.ChatCompletion.create(
      model=MODEL,
      messages = [
         {"role": "system", "content": description},
         {"role": "user", "content": user_prompt},
      ],
      temperature=0,
  )
  # The response
  whole_message = response['choices'][0]['message']['content']

  first_index = whole_message.find("```") + 7
  last_index = whole_message.find("```", first_index + 1)

  final_message = whole_message[first_index:last_index]
  print(f"Final message: \n{final_message}")
  new_data = json.loads(final_message)
  make_file(new_data)

def make_file(new_data):
  # Makes a JSON file called boxes.json which contains the response from GPT
  with open("boxes.json", "w") as outfile:
      json.dump(new_data, outfile)

def get_user_content(topic):
    if topic == "calc":
      file = 'APCalcABBCPrompt.txt'
    if topic == "lang":
      file = 'APLangPrompt.txt'
    if topic == "CSA":
      file = 'APComputerScienceAPrompt.txt'
    if topic == "world":
      file = 'APWorldHistoryPrompt.txt'
    if topic == "chem":
      file = 'APChemistryPrompt.txt'
    if topic == "bio":
      file = 'APBiologyPrompt.txt'
    if topic == "csa2":
      file = 'APComputerScienceAPrompt2.txt'
    with open(file, "r") as f:
      user_prompt = f.readline()
    with open('SystemPrompt.txt', "r") as s:
      system_prompt = s.readline()
    f.close
    s.close
    get_response(system_prompt, user_prompt)

get_user_content("bio")