from git import Repo
from git.exc import GitCommandError
from vela.processors.repo_processor import process_repos
import os

def clone_repository(repo_url):
    try:
        # Determine the name of the repository by splitting the URL
        repo_name = repo_url.split('/')[-1]
        if repo_name.endswith('.git'):
            repo_name = repo_name[:-4]

        # Path where the repository will be cloned
        vela_path = os.path.abspath(os.path.join(os.getcwd()))
        repos_path = os.path.join(vela_path, 'repos')
        repo_path = os.path.join(repos_path, repo_name)

        # Create the directory if it doesn't exist
        os.makedirs(repos_path, exist_ok=True)

        # Clone the repository
        print(f"Cloning repository {repo_url} into {repo_path}...")
        Repo.clone_from(repo_url, repo_path)
        print("Repository cloned successfully.")
        print("Processing Repos")
        code_chunks = process_repos()

        print(code_chunks)

    except GitCommandError as e:
        print(f"An error occurred while cloning the repository: {e}")

# Test the function

