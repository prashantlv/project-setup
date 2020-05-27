    import sys
    import os
    from github import Github
    path = "/path_to_project_directory"
    def create():
       folder_name = str(sys.argv[1])
       os.makedirs(path+folder_name)
       user = Github(username,password).get_user()
       repo = user.create_repo(folder_name)
       print(f"New Repository '{folder_name}' created successfully.")
    if __name__ == "__main__":
       create()
