#!/usr/bin/python3
"""
    A python scripts taking a command line argument using
    REPOSITORY NAME and USERNAME
    get a LIST of the LAST 10 COMMITS from recent to oldest
    using GITHUBAPI and displaying the result in a manner
    THIS IS A BACKEND INTERVIEW QUESION!!!
"""
import sys
import requests


if __name__ == '__main__':

    repo_name = sys.argv[1]
    owner = sys.argv[2]
    url = f'https://api.github.com/repos/{owner}/{repo_name}/commits'
    response = requests.get(url)
    # save the commits as json
    commits = response.json()
    # iterate through all to get the last 10
    for i, last_ten in enumerate(commits):
        if i >= 10:
            break
        print(F"{last_ten['sha']}: {last_ten['commit']['author']['name']}")
