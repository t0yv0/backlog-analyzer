import argparse
import gh
import ai


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument('-r', '--repo', required=True, help='GitHub repository')
    ap.add_argument('-t', '--token', required=False, help='GitHub token')
    ap.add_argument('-q', '--query', required=True, help='Question about the open issues')
    args = ap.parse_args()

    gh_client = gh.client(token=args.token)
    issues = gh.open_issues(gh_client, args.repo)
    response = ai.chat(args.repo, issues, args.query)
    print(response)


if __name__ == '__main__':
    main()