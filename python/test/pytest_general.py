import os
import sys
import pytest
from python.utilities.git_stats import Github


@pytest.mark.system
@pytest.mark.skipif("sys.version_info >= (3,7)")
def test_github_metrics():
    g = Github(os.environ["GITHUB_TOKEN"], "https://github.com/miguelgfierro/codebase")
    g.clean()
    assert g.forks >= 3
    assert isinstance(g.open_issues, int)
    assert isinstance(g.open_pull_requests, int)
    assert g.stars >= 8
    assert g.watchers >= 2
    # assert len(g.last_year_commit_frequency)
    assert g.top_ten_referrers is not None
    assert g.number_total_referrers >= 1
    assert g.number_unique_referrers >= 1
    assert g.top_ten_content is not None
    assert g.views is not None
    assert g.number_total_views >= 10
    assert g.number_unique_views >= 10
    assert g.clones is not None
    assert g.number_total_clones >= 1
    assert g.number_unique_clones >= 1
    assert g.repo_size >= 2
    assert g.creation_date == "2016-12-27T13:23:55Z"
    assert sorted(g.languages.keys()) == [
        "C++",
        "CMake",
        "CSS",
        "Dockerfile",
        "HTML",
        "JavaScript",
        "Jupyter Notebook",
        "MATLAB",
        "PHP",
        "PLpgSQL",
        "Python",
        "SQL",
        "Shell",
    ]
    assert g.number_languages >= 12
    assert g.number_commits > 600
    assert g.number_contributors >= 1
    assert g.number_branches >= 1
    assert g.number_tags >= 0
    assert g.number_total_lines > 300000
    assert g.number_added_lines > 15000
    assert g.number_deleted_lines > 3000
