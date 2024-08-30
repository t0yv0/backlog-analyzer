from github import Auth
from github import Github
import subprocess as sp
import json


TOKEN = None


def authenticate(token=None):
    if token is None:
        token = sp.check_output(["gh", "auth", "token"]).decode("utf-8").strip()
    global TOKEN
    TOKEN = token


def issue(repository, issue_number):
    g = client()
    repo = g.get_repo(repository)
    issue = repo.get_issue(number=issue_number)
    return json.dumps({
        "labels": [x.name for x in issue.get_labels()],
        "body": issue.body,
        "title": issue.title,
    }, indent=True)


def client():
    auth = Auth.Token(TOKEN)
    return Github(auth=auth)
