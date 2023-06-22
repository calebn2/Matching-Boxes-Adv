import json
import openai
import os

# Calls GPT-4
def get_response(user_prompt):
  # Messages I give to GPT-4
  system_training = "I am making a matching exercise for students and you are making the things that are being matched. A student will be working on a school subject and topic that they will tell to you. It is your job to come up with four pairs of items that match to each other and relate to the subject and topic that they tell you. The pairs you come up with should be easy enough for a high school student to understand; however, they should also be generic and different from each other to make the exercise more challenging for a student. Unless told otherwise, make the pairs be base level understanding. The pairs you make should be formatted into a JSON file. First make an array, and then put arrays of pairs inside the initial array. It should be formatted like this: {0: {term: term, output: output}}. Surround the JSON file with three back-ticks like so: ```{0: {term: term, output: output}}```."
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

  first_index = whole_message.find("```") + 3
  last_index = whole_message.find("```", first_index + 1)

  final_message = whole_message[first_index:last_index]

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
    with open(file, "r") as f:
      user_prompt = f.readline()
    f.close
    get_response(user_prompt)

get_user_content("lang")