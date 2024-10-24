from banal.mem import memory
from banal import gh
from tqdm import tqdm
import numpy as np
import openai
import sys


def chat(repo, issues, query, progress_bar=False):
    client = openai.OpenAI()
    db = precomputed_db(client, issues, progress_bar=progress_bar)
    embedding = get_embedding(client, query)
    similar = find_similar_issues(db, embedding, n=20)
    messages = [f"Remember the GitHub issue {repo}#{s['number']}: {s['title']}\n\n{s['body']}" for s in similar]
    messages += [query]

    chat_completion = client.chat.completions.create(
        messages=[{
            "role": "user",
            "content": m
        } for m in messages],
        model="gpt-4o",
    )

    return chat_completion.choices[0].message.content


def get_embedding(client, text, model='text-embedding-3-small'):
    return client.embeddings.create(input=text[0:8192], model=model).data[0].embedding


@memory.cache(ignore=["client"])
def precomputed_db(client, issues, progress_bar=False):
    db = []
    if progress_bar:
        print("Computing embeddings..")
    wrap = tqdm if progress_bar else list
    for issue in wrap(issues):
        istr = f"{issue['title']}\n\n{issue['body']}\n\n{issue['labels']}"
        emb = get_embedding(client, istr)
        db.append({
            "number": issue["number"],
            "title": issue["title"],
            "body": issue["body"],
            "labels": issue["labels"],
            "embedding": emb,
        })
    return db


def find_similar_issues(db, embedding, n):
    sim = lambda datum: -cosine_similarity(datum['embedding'], embedding)
    return [datum for datum in sorted(db, key=sim)[0:n]]


def cosine_similarity(a, b):
    return np.dot(a, b) / (np.linalg.norm(a) * np.linalg.norm(b))
