from git import Repo
import os
import requests


def get_current_forks(url):
    resp = requests.get(url).json()
    return resp['forks_count']


def get_open_issues(url):
    resp = requests.get(url).json()
    return resp['open_issues']


def get_current_stars(url):
    resp = requests.get(url).json()
    return resp['stargazers_count']


def get_current_watchers(url):
    resp = requests.get(url).json()
    return resp['subscribers_count']


def clone_repo(url):
    repo_dir = url.split('/')[-1]
    if os.path.isdir(repo_dir):
        print('Repo {} already downloaded'.format(repo_dir))
        return repo_dir
    Repo.clone_from(url, repo_dir)
    if os.path.isdir(repo_dir):
        return repo_dir
    else:
        raise Exception('Repo not downloaded correctly')


def get_number_commits(repo_dir):
    os.chdir(repo_dir)
    resp = os.popen('git rev-list HEAD --count').read()
    resp = int(resp.split('\n')[0])
    os.chdir('..')
    return resp


def get_number_branches(repo_dir):
    os.chdir(repo_dir)
    resp = os.popen('git branch -a | wc -l').read()
    os.chdir('..')
    resp = int(resp.split('\n')[0])
    resp = resp - 1 #there is always one repeated origin/HEAD
    return resp


def get_number_tags(repo_dir):
    os.chdir(repo_dir)
    resp = os.popen('git tag | wc -l').read()
    resp = int(resp.split('\n')[0])
    return resp


def get_number_contributors(repo_dir):
    os.chdir(repo_dir)
    resp = os.popen('git log --format="%aN" | sort -u | wc -l').read()
    resp = int(resp.split('\n')[0])
    return resp


def count_total_lines(repo_dir):
    os.chdir(repo_dir)
    resp = os.popen('git ls-files | xargs wc -l | grep total').read()
    resp = int(resp.split(' total')[0])
    return resp


def count_added_lines(repo_dir):
    os.chdir(repo_dir)
    resp = os.popen('git log  --pretty=tformat: --numstat | awk \'{ add += $1 } END { printf "%s",add }\'').read()
    resp = int(resp)
    return resp


def count_deleted_lines(repo_dir):
    os.chdir(repo_dir)
    resp = os.popen('git log  --pretty=tformat: --numstat | awk \'{ add += $1 ; subs += $2 } END { printf "%s",subs }\'').read()
    resp = int(resp)
    return resp
