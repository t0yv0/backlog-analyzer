from github import Auth, Github
from banal.mem import memory
import json
import os
import subprocess as sp


def client(token=None):
    if token is None:
        token = sp.check_output(["gh", "auth", "token"]).decode("utf-8").strip()
    return Github(auth=Auth.Token(token))


@memory.cache(ignore=["client"])
def open_issues(client, repository):
    repo = client.get_repo(repository)
    return [issue(client, repository, x.number) for x in repo.get_issues(state="open")]


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
