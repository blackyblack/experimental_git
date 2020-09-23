#!/usr/bin/env python3

import subprocess

subprocess.run(["git", "config", "--local", "user.name", "blackyblack"])
subprocess.run(["git", "reset", "--soft", "58dc14c148f481a6ad48119825f1f0e78339e17b"])
subprocess.run(["git", "add", "--all", "."])
subprocess.run(["git", "rm", "--cached", "-r", "test_dir"])
subprocess.run(["git", "commit", "-m", "First commit"])
subprocess.run(["git", "add", "test_dir"])
subprocess.run(["git", "commit", "-m", "Second commit"])
