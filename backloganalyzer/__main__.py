import sys
import argparse

from .gh import authenticate, issue
from .funcmodule import my_function

def main():
    ap = argparse.ArgumentParser()
    ap.add_argument('-r', '--repo', required=True, help='GitHub repository')
    ap.add_argument('-t', '--token', required=False, help='GitHub token')
    ap.add_argument('-i', '--issue', required=True, help='Issue number')
    args = ap.parse_args()

    repo = args.repo
    token = args.token
    issue_number = int(args.issue)

    authenticate(token)
    print(issue(repo, issue_number))


if __name__ == '__main__':
    main()
