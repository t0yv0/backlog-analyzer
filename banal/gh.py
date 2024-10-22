from github import Auth, Github
from banal.mem import memory
import json
import os
import subprocess as sp
from tqdm import tqdm


def client(token=None):
    if token is None:
        token = sp.check_output(["gh", "auth", "token"]).decode("utf-8").strip()
    return Github(auth=Auth.Token(token))


@memory.cache(ignore=["client"])
def open_issues(client, repository, progress_bar=False):
    repo = client.get_repo(repository)
    all_issues = list(repo.get_issues(state="open"))
    if progress_bar:
        print("Downloading GitHub issues..")
    wrap = tqdm if progress_bar else list
    all_issues = wrap(all_issues)
    return [issue(client, repository, x.number) for x in all_issues]


@memory.cache(ignore=["client"])
def issue(client, repository, issue_number):
    repo = client.get_repo(repository)
    issue = repo.get_issue(number=issue_number)
    return {
        "number": issue_number,
        "title": issue.title,
        "body": issue.body,
        "labels": [x.name for x in issue.get_labels()],
    }
