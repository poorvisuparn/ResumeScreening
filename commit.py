from git import Repo
#commit count
repo = Repo()

print(len(list(repo.iter_commits())))