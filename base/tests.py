import requests

def get_github_user_info(username):
    base_url = f"https://api.github.com/users/{username}"
    
    try:
        # Make a GET request to the GitHub API for the user
        response = requests.get(base_url)
        response.raise_for_status()  # Raise an exception if there's an HTTP error
        
        user_data = response.json()
        
        total_contributions = user_data.get("contributions")
        total_repos = user_data.get("public_repos")
        followers = user_data.get("followers")
        
        return total_contributions, total_repos, followers
    
    except requests.exceptions.RequestException as e:
        print(f"Error: {e}")
        return None

# GitHub username for which you want to get information
github_username = "NagiPragalathan"

# Get GitHub user information
user_info = get_github_user_info(github_username)

if user_info:
    total_contributions, total_repos, followers = user_info
    print(f"GitHub User: {github_username}")
    print(f"Total Contributions: {total_contributions}")
    print(f"Total Public Repositories: {total_repos}")
    print(f"Followers: {followers}")
else:
    print(f"User information not found for {github_username}")
