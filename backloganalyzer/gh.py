from github import Auth
from github import Github
from joblib import Memory
import subprocess as sp
import json
import os


TOKEN = None
CACHEDIR = os.path.expanduser("~/.backloganalyzer/memory")


memory = Memory(CACHEDIR, verbose=0)


def authenticate(token=None):
    if token is None:
        token = sp.check_output(["gh", "auth", "token"]).decode("utf-8").strip()
    global TOKEN
    TOKEN = token


@memory.cache
def open_issues(repository):
    g = client()
    repo = g.get_repo(repository)
    return [issue(repository, x.number) for x in repo.get_issues(state="open")]


@memory.cache
def issue(repository, issue_number):
    print(f"Fetching issue {issue_number} from {repository}")
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
