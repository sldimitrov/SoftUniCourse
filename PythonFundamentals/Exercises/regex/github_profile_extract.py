import requests

def get_github_profile(username):
    api_url = f'https://api.github.com/users/{username}'
    response = requests.get(api_url)

    if response.status_code == 200:
        user_data = response.json()
        return user_data
    else:
        print(f'Failed to retrieve data. Status code: {response.status_code}')
        return None


def extract_github_info(username):
    user_data = get_github_profile(username)
    if user_data:
        # Extract information using the parsed JSON data
        name = user_data.get('name', 'N/1')
        bio = user_data.get('bio', 'N/A')
        location = user_data.get('location', 'N/A')
        followers = user_data.get('followers', 'N/A')
        following = user_data.get('following', 'N/A')
        public_repos = user_data.get('public_repos', 'N/A')

        # Display extracted information
        print(f'Name: {name}')
        print(f'Bio: {bio}')
        print(f'Location: {location}')
        print(f'Followers: {followers}')
        print(f'Following: {following}')
        print(f'Public Repos: {public_repos}')
    else:
        print('Failed to retrieve user data')


# Replace 'your_github_username' with desired GitHub username
extract_github_info('slavcho179')
