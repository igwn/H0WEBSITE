# -*- coding: utf-8 -*-
#!/usr/bin/env python

"""
Filename        = test_git_push.py
Description     = Check for successful git push from event updates

Created on Wed Jan 24 10:15:55 2024

__author__      = nnarenraju
__copyright__   = Copyright 2024, h0-website
__credits__     = nnarenraju
__license__     = ???
__version__     = 0.0.1
__maintainer__  = nnarenraju
__email__       = nnarenraju@gmail.com
__status__      = [*inProgress*, 'Archived', 'inUsage', 'Debugging']


Github Repository: https://github.com/igwn/h0-website/tree/continuous-integration
Changes have not been merged into main yet.

Documentation:
    When paired when CI, checks are run when merging with main branch
    1. Changes from grace-db can come in via periodic bg processes (without PR)
        a. Check event updates (potential/GW) in events-list.json
    2. Changes can be made manually to events-list.json with EM counterparts (with PR)
        a. Check if EM counterpart have been added to events-list.json
        b. If EM counterpart, check if sky position is the same as associated GW event

"""

## Packages
## TODO: Need to update requirements.txt
import os
import re
import json
import difflib
# Limitations: Cannot be used in daemon-like processes
from git import Repo

# Get working repository
repo = Repo('.', search_parent_directories=True)
# Set working_tree_dir and working_branch as global
working_tree_dir = repo.working_tree_dir
working_branch = "continuous-integration"


def test_bare_repo():
    # Check if repo is not bare
    assert not repo.bare


def test_checkout_exists_branch():
    # Check if branch exists within repo
    assert working_branch in repo.references
    # Checkout branch if exists_branch does not fail
    repo.git.checkout(working_branch)


def test_attached_head():
    # Check if HEAD is still attached
    assert not repo.head.is_detached


def test_event_updates():
    # Check if automagic event update has occurred from grace-db bg process
    hcommit = repo.head.commit
    #print(hcommit.diff())  # diff tree against index
    # diff tree against previous tree
    # Traverse added Diff objects only
    for diff_item in hcommit.diff("HEAD~1").iter_change_type("M"):
        a_blob = diff_item.a_blob.data_stream.read().decode('utf-8')
        b_blob = diff_item.b_blob.data_stream.read().decode('utf-8')

    print(len(a_blob[:]))
    print(len(b_blob[:]))

    log = repo.git.diff('--numstat', 'HEAD~1')
    for line in log.split('\n'):
        is_added = re.match(r"(\d+)\s+(\d+)\s+(.+)", line)[1]

    matcher = difflib.SequenceMatcher(a=a_blob, b=b_blob)
    diff = []

    if is_added:
        for match in matcher.get_matching_blocks():
            print(a_blob[match.a: match.size])


def test_git_push():
    # Check if a successful git push occurred
    check_file = os.path.join(working_tree_dir, "events-list.json")
    # Get files that appear in git diff
    # NOTE: Use None for unstaged files, use HEAD for staged files
    changed = [item.a_path for item in repo.index.diff("Head")]
    # Check if file has been changed
    if check_file in repo.untracked_files:
        pass
    elif check_file in changed:
        pass
    else:
        pass


def test_whatever():
    assert 37 in {
        num
        for num in range(2, 50)
        if not any(num % div == 0 for div in range(2, num))
    }