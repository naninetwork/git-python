import git
import os
from datetime import datetime

class Git():

    def __init__(self, cwd):
        self.cwd = cwd

    def git_clone(self, repo_url):
        out_dir = '/'.join(repo_url.split('/')[3:]).replace('.git','')
        cwd = os.getcwd()
        local_path = os.path.join(cwd, out_dir)
        if os.path.isdir(local_path):
            repo=git.Repo(local_path, search_parent_directories=True);
            repo.remotes.origin.pull()
        else:
            os.makedirs(local_path)
            git.Repo.clone_from(repo_url, local_path)

    def git_push(self, repo_url):
        try:
            
            out_dir = '/'.join(repo_url.split('/')[3:]).replace('.git','')
            
            local_folders = out_dir.split('/')
            local_git_path = os.path.join(cwd, local_folders[0])
            local_repo_path = os.path.join(local_git_path, local_folders[1])
            
            os.chdir(local_repo_path)
            repo = git.Repo(local_repo_path)
            repo.git.add(update=True)
            
            now = datetime.now()
            date_string = now.strftime("%d/%m/%Y %H:%M:%S")
            commit_msg = "Test commit message at {0}".format(date_string)
            
            repo.index.commit(commit_msg)
            origin = repo.remote(name='origin')
            origin.push()
        except:
            print('Some error occured while pushing the code')

if __name__ == '__main__':

    cwd = os.getcwd()
    gen_obj = Git(cwd)
    clone_url = "https://github.com/naninetwork/git-python.git"
    gen_obj.git_clone(clone_url)
    gen_obj.git_push(clone_url)
