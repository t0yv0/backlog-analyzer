import ollama
import random


def summarize_issues(issues):
    stuff = issues
    random.shuffle(stuff)

    c = f'Please group these issues into related clusters, and for the largest clusters print the summary of themes and the number of issues in them: <issues>{stuff}</issues>'

    print("PROMPT LENGTH", len(c))

    response = ollama.chat(model='mistral', messages=[
        {
            'role': 'user',
            'content': c,
        },
    ])

    print(response['message']['content'])
