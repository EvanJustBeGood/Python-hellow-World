import requests

def get_repository_names(username):
    url = f"https://api.github.com/users/EvanJustBeGood/repos"
    response = requests.get(url)
    
    if response.status_code == 200:
        repositories = response.json()
        for repo in repositories:
            print(repo["name"])
    else:
        print(f"Failed to retrieve repositories for user {username}. Status code: {response.status_code}")

if __name__ == "__main__":
    username = "EvanJustBeGood"
    get_repository_names(username)
