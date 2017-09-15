from git import Repo
import os
import requests
import datetime


END_POINT = 'https://api.github.com/repos/'


def get_current_forks(git_url, base_url='https://github.com/'):
    """Get current number of forks
    Parameters:
        git_url (str): Github repo url.
        base_url (str): Base url of git repo.
    Returns:
        resp (int): Number of forks.

    """
    url = END_POINT + git_url.split(base_url)[1]
    resp = requests.get(url).json()
    return resp['forks_count']


def get_open_issues(git_url, base_url='https://github.com/'):
    """Get current number of open issues
    Parameters:
        git_url (str): Github repo url.
        base_url (str): Base url of git repo.
    Returns:
        resp (int): Number of issues.

    """
    url = END_POINT + git_url.split(base_url)[1]
    resp = requests.get(url).json()
    return resp['open_issues']


def get_current_stars(git_url, base_url='https://github.com/'):
    """Get current number of stars.
    Parameters:
        git_url (str): Github repo url.
        base_url (str): Base url of git repo.
    Returns:
        resp (int): Number of stars.

    """
    url = END_POINT + git_url.split(base_url)[1]
    resp = requests.get(url).json()
    return resp['stargazers_count']


def get_current_watchers(git_url, base_url='https://github.com/'):
    """Get current number of watchers.
    Parameters:
        git_url (str): Github repo url.
        base_url (str): Base url of git repo.
    Returns:
        resp (int): Number of watchers.

    """
    url = END_POINT + git_url.split(base_url)[1]
    resp = requests.get(url).json()
    return resp['subscribers_count']


def last_year_commit_frequency(git_url, base_url='https://github.com/'):
    """Get the commit frequency in every week of the last year.
    Parameters:
        git_url (str): Git repo url.
        base_url (str): Base url of git repo.
    Returns:
        resp (dict): Dictionary of 52 elements (1 per week) with the commits
                    every day (starting on Sunday), total commit sum and first
                    day of the week.

    """
    url = END_POINT + git_url.split('https://github.com/')[1]
    resp = requests.get(url + '/stats/commit_activity').json()
    for id, item in enumerate(resp):
        week_str = datetime.datetime.fromtimestamp(item['week']).strftime('%Y-%m-%d')
        resp[id]['week'] = week_str
    return resp


def clone_repo(url):
    """Clone a git repo.
    Parameters:
        url (str): Git repo url.
    Returns:
        repo_dir (str): Name of the folder name of the repo.

    """
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
    """Get total number of commits.
    Parameters:
        repo_dir (str): Repo directory.
    Returns:
        resp (int): Number of commits.

    """
    os.chdir(repo_dir)
    resp = os.popen('git rev-list HEAD --count').read()
    resp = int(resp.split('\n')[0])
    os.chdir('..')
    return resp


def get_number_branches(repo_dir):
    """Get total number of branches.
    Parameters:
        repo_dir (str): Repo directory.
    Returns:
        resp (int): Number of branches.

    """
    os.chdir(repo_dir)
    resp = os.popen('git branch -a | wc -l').read()
    os.chdir('..')
    resp = int(resp.split('\n')[0])
    resp = resp - 1 #there is always one repeated origin/HEAD
    return resp


def get_number_tags(repo_dir):
    """Get total number of tags.
    Parameters:
        repo_dir (str): Repo directory.
    Returns:
        resp (int): Number of tags.

    """
    os.chdir(repo_dir)
    resp = os.popen('git tag | wc -l').read()
    resp = int(resp.split('\n')[0])
    return resp


def get_number_contributors(repo_dir):
    """Get total number of contributors.
    Parameters:
        repo_dir (str): Repo directory.
    Returns:
        resp (int): Number of contributors.

    """
    os.chdir(repo_dir)
    resp = os.popen('git log --format="%aN" | sort -u | wc -l').read()
    resp = int(resp.split('\n')[0])
    return resp


def count_total_lines(repo_dir):
    """Get total number of lines.
    Parameters:
        repo_dir (str): Repo directory.
    Returns:
        resp (int): Number of lines.

    """
    os.chdir(repo_dir)
    resp = os.popen('git ls-files | xargs wc -l | grep total').read()
    resp = int(resp.split(' total')[0])
    return resp


def count_added_lines(repo_dir):
    """Get the number of added lines.
    Parameters:
        repo_dir (str): Repo directory.
    Returns:
        resp (int): Number of added lines.

    """
    os.chdir(repo_dir)
    resp = os.popen('git log  --pretty=tformat: --numstat | awk \'{ add += $1 } END { printf "%s",add }\'').read()
    resp = int(resp)
    return resp


def count_deleted_lines(repo_dir):
    """Get the number of deleted lines.
    Parameters:
        repo_dir (str): Repo directory.
    Returns:
        resp (int): Number of deleted lines.

    """
    os.chdir(repo_dir)
    resp = os.popen('git log  --pretty=tformat: --numstat | awk \'{ add += $1 ; subs += $2 } END { printf "%s",subs }\'').read()
    resp = int(resp)
    return resp

