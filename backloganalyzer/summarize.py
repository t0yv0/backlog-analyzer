import ollama


def summarize_issues(issues):
    stuff = issues
    response = ollama.chat(model='mistral', messages=[
        {
            'role': 'user',
            'content': f'Please group these issues into related clusters, and for the largest clusters print the summary of themes and the number of issues in them: <issues>{stuff}</issues>',
        },
    ])

    print(response['message']['content'])
