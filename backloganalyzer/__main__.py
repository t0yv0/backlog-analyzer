import sys
import argparse

from .gh import authenticate, open_issues


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument('-r', '--repo', required=True, help='GitHub repository')
    ap.add_argument('-t', '--token', required=False, help='GitHub token')
    args = ap.parse_args()

    repo = args.repo
    token = args.token

    authenticate(token)

    issues = open_issues(repo)

    print("FOUND open issues: ", len(issues))
    print(issues[0])


if __name__ == '__main__':
    main()
