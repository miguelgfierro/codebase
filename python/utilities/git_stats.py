from git import Repo
import os
import requests
import datetime
from functools import lru_cache


END_POINT = "https://api.github.com/repos/"
BASE_URL = "https://github.com/"


class Github:
    def __init__(self, token, git_url):
        self.token = token
        self.url = END_POINT + git_url.split(BASE_URL)[1]

    @property
    @lru_cache()
    def general_stats(self):
        return requests.get(self.url).json()

    @property
    def forks(self):
        """Get current number of forks
        Returns:
            int: Number of forks.
        """
        return self.general_stats["forks_count"]

    @property
    def open_issues(self):
        """Get current number of open issues
        Returns:
            int: Number of issues.
        """
        return self.general_stats["open_issues_count"]

    @property
    def stars(self):
        """Get current number of stars.
        Returns:
            int: Number of stars.
        """
        return self.general_stats["stargazers_count"]

    @property
    def watchers(self):
        """Get current number of watchers.
        Returns:
            int: Number of watchers.
        """
        return self.general_stats["subscribers_count"]

    @property
    @lru_cache()
    def last_year_commit_frequency(self):
        """Get the commit frequency in every week of the last year.
        Returns:
            dict: Dictionary of 52 elements (1 per week) with the commits every day 
                (starting on Sunday), total commit sum and first day of the week.
        """
        resp = requests.get(self.url + "/stats/commit_activity").json()
        for id, item in enumerate(resp):
            week_str = datetime.datetime.fromtimestamp(item["week"]).strftime(
                "%Y-%m-%d"
            )
            resp[id]["week"] = week_str
        return resp

    @property
    def commits(self):
        # https://blog.notfoss.com/posts/get-total-number-of-commits-for-a-repository-using-the-github-api/
        pass

    @property
    @lru_cache()
    def branches(self):
        return requests.get(self.url + "/branches").json()

    @property
    def branches(self):
        return len(self.branches)

    @property
    def number_tags(self):
        pass

    @property
    def number_contributors(self):
        pass

    @property
    def repo_size(self):
        """Repo size in Mb
        Returns:
            int: Size.
        """
        return self.general_stats["size"]

    @property
    def creation_date(self):
        """Date of repository creation
        Returns:
            str: Date.
        """
        return self.general_stats["created_at"]

    @property
    @lru_cache()
    def languages(self):
        """Get the languages in the repo and the lines of code of each.
        Returns:
            dict: Dictionary of languages and lines of code.
        """
        return requests.get(self.url + "/languages").json()

    @property
    def number_languages(self):
        """Number of different languages
        Returns:
            int: Number
        """
        return len(self.languages)


def clone_repo(url):
    """Clone a git repo.
    Args:
        url (str): Git repo url.
    Returns:
        repo_dir (str): Name of the folder name of the repo.

    """
    repo_dir = url.split("/")[-1]
    if os.path.isdir(repo_dir):
        print("Repo {} already downloaded".format(repo_dir))
        return repo_dir
    Repo.clone_from(url, repo_dir)
    if os.path.isdir(repo_dir):
        return repo_dir
    else:
        raise Exception("Repo not downloaded correctly")


def get_number_commits(repo_dir):
    """Get total number of commits.
    Args:
        repo_dir (str): Repo directory.
    Returns:
        resp (int): Number of commits.

    """
    os.chdir(repo_dir)
    resp = os.popen("git rev-list HEAD --count").read()
    resp = int(resp.split("\n")[0])
    os.chdir("..")
    return resp


def get_number_branches(repo_dir):
    """Get total number of branches.
    Args:
        repo_dir (str): Repo directory.
    Returns:
        resp (int): Number of branches.

    """
    os.chdir(repo_dir)
    resp = os.popen("git branch -a | wc -l").read()
    os.chdir("..")
    resp = int(resp.split("\n")[0])
    resp = resp - 1  # there is always one repeated origin/HEAD
    return resp


def get_number_tags(repo_dir):
    """Get total number of tags.
    Args:
        repo_dir (str): Repo directory.
    Returns:
        resp (int): Number of tags.

    """
    os.chdir(repo_dir)
    resp = os.popen("git tag | wc -l").read()
    resp = int(resp.split("\n")[0])
    return resp


def get_number_contributors(repo_dir):
    """Get total number of contributors.
    Args:
        repo_dir (str): Repo directory.
    Returns:
        resp (int): Number of contributors.

    """
    os.chdir(repo_dir)
    resp = os.popen('git log --format="%aN" | sort -u | wc -l').read()
    resp = int(resp.split("\n")[0])
    return resp


def count_total_lines(repo_dir):
    """Get total number of lines.
    Args:
        repo_dir (str): Repo directory.
    Returns:
        resp (int): Number of lines.

    """
    os.chdir(repo_dir)
    resp = os.popen("git ls-files | xargs wc -l | grep total").read()
    resp = int(resp.split(" total")[0])
    return resp


def count_added_lines(repo_dir):
    """Get the number of added lines.
    Args:
        repo_dir (str): Repo directory.
    Returns:
        resp (int): Number of added lines.

    """
    os.chdir(repo_dir)
    resp = os.popen(
        "git log  --pretty=tformat: --numstat | awk '{ add += $1 } END { printf \"%s\",add }'"
    ).read()
    resp = int(resp)
    return resp


def count_deleted_lines(repo_dir):
    """Get the number of deleted lines.
    Args:
        repo_dir (str): Repo directory.
    Returns:
        resp (int): Number of deleted lines.

    """
    os.chdir(repo_dir)
    resp = os.popen(
        "git log  --pretty=tformat: --numstat | awk '{ add += $1 ; subs += $2 } END { printf \"%s\",subs }'"
    ).read()
    resp = int(resp)
    return resp

