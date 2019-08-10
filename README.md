# git-python
git operations using python ( Git class used for clone and push operations

# setup ( incase if you are using anaconda )
- conda create --name gitops  ( # create virtural env ex: gitops )
- conda activate gitops  ( # activate newly created virtual env )
- conda install pip ( # install pip onto new virtual env )

# Install gitpython using requirements.txt file
- pip install -r requirements.txt ( # install project specific python packages ex : gitpython )

# clone & push using our git class
- cwd = os.getcwd()
- gen_obj = Git(cwd)
- clone_url = "https://github.com/naninetwork/git-python.git"
- gen_obj.git_clone(clone_url) ( #clone any public with valid clone url )
- gen_obj.git_push(clone_url) ( #push to git repo with valid permissions )

