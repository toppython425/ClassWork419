import json

import requests


class GitHubAPI:
    def __init__(self):
        self.base_url = 'https://api.github.com'

    def get_user_repos(self, username):
        url = f'{self.base_url}/users/{username}/repos'
        try:
            response = requests.get(url)
            response.raise_for_status()
            repos = response.json()
            return GitHubAPI._parse_repos(repos)
        except requests.exceptions.RequestException as rex:
            print(f'Ошибка при запросе к GitHub API: {rex}')
            return None

    @staticmethod
    def _parse_repos(repos_data):
        repos_info = []
        for repo in repos_data:
            if not repo['description']:
                description = 'No description'
            else:
                description = repo['description']
            repo_info = {
                'name': repo['name'],
                'description': description,
                'language': repo.setdefault('language', 'Not specified'),
                'stars': repo['stargazers_count'],
            }
            repos_info.append(repo_info)
        return repos_info

    @classmethod
    def save_to_json(cls, data, filename='github_repos.json'):
        with open(filename, 'w', encoding='utf-8') as fp:
            json.dump(data, fp, ensure_ascii=False, indent=4)
        print(f'Данные сохранены в {filename}')


if __name__ == "__main__":
    github = GitHubAPI()
    username = "toppython425"
    my_repos = github.get_user_repos(username)

    if my_repos:
        print(f"Репозитории пользователя {username}:")
        for my_repo in my_repos:
            print(f"Название репозитория: {my_repo['name']}")
            print(f"Описание репозитория: {my_repo['description']}")
            print(f"Язык репозитория: {my_repo['language']}")
            print(f"Звёзд: {my_repo['stars']}")
            print()

        GitHubAPI.save_to_json(my_repos)
    else:
        print("Не удалось получить данные.")
