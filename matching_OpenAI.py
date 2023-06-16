#import openai
import json

file = open('data.json')
data = json.load(file)
file.close

system_training = "You are a Java computer science teacher who is creating an online matching assignment for your students. Your job is to make java code segments and outputs that is structured in a JSON 2D array like the following."
system_instructions = "You should make 4 arrays, each with a code segment, and the output to that code segment. The code and output should be in html format, and unique from each other. Java variables should have generic names like: x, y, and z. The content of the array should be related to Java classes and objects. The content should be generic to make the questions harder."
# Example OpenAI Python library request
# openai.api_key = ""

# MODEL = "gpt-4"
# response = openai.ChatCompletion.create(
#     model=MODEL,
#     messages=[
#         {
#           "role": "system",
#           "content": system_training + " " + data + " " + system_instructions
#         },
#         {
#           "role": "user", 
#           "content": "Make me a matching game that tests me over nested for loops and String outputs"
#         },
#     ],
#     temperature=0,
# )

# response

#new_data = response['choices'][0]['message']['content']

# Dummy data
new_data = [
    [
        "code",
        "output"
    ],
    [
        "code",
        "output"
    ]
]

# Makes a JSON file called boxes.json which contains the response from GPT
with open("boxes.json", "w") as outfile:
    json.dump(new_data, outfile)