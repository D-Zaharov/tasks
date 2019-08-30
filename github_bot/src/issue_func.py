from github import Github

g = Github("65e74c6d0cf79e382a5905284870e5745bc62d27")
repo = g.get_repo("D-Zaharov/tasks")

message = str(input())
def issue(text):
    repo.create_issue(title=text)

issue(message)