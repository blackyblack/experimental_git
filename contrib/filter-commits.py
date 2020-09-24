#!/usr/bin/env python3

import subprocess, os

initialCommit = "HEAD~"
if "INITIAL_COMMIT" in os.environ:
    initialCommit = os.environ["INITIAL_COMMIT"]

subprocess.run(["git", "reset", "--soft", initialCommit])
subprocess.run(["git", "add", "--all", "."])
subprocess.run(["git", "rm", "--cached", "-r", "test_dir"])
subprocess.run(["git", "commit", "-m", "Auto squash commits from master since " + initialCommit])
subprocess.run(["git", "add", "test_dir"])
subprocess.run(["git", "commit", "-m", "Auxiliary changes"])
