#import openai
import json

def main():
    f = open('data.json')
    data = json.load(f)
    f.close
    # Example OpenAI Python library request
    # openai.api_key = ""

    # MODEL = "gpt-3.5-turbo"
    # response = openai.ChatCompletion.create(
    #     model=MODEL,
    #     messages=[
    #         {
    #           "role": "system",
    #           "content": "You are a Java computer science teacher who is creating an online matching assignment for your students who are learning about nested iteration. You format your response in JSON based on the following array: " + data + "There should be 8 pairs of objects, each with a class that is the same as the matching objects class, and the actual data that will be the content of the matching game. The data should be in html format, be unique from other data, and test a students knowledge of Java nested for loops. The data must include Java code. Java variables should have generic names like: x, y, and z. You should only respond with the code, no other text."
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
new_data = [
    {
        "class": "1",
        "data": "data 1"
    },
    {
        "class": "1",
        "data": "data 2"
    },
    {
        "class": "2",
        "data": "data 3"
    },
    {
        "class": "2",
        "data": "data 4"
    },
    {
        "class": "3",
        "data": "data 5"
    },
    {
        "class": "3",
        "data": "data 6"
    }
]

def make_new_data(new_data):
    json_object = json.dumps(new_data, indent=4)

    with open("boxes.json", "w") as outfile:
        outfile.write(json_object)
    return
make_new_data(new_data)