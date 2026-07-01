import json
import urllib.request
import urllib.error
import argparse

SUPPORTED_EVENTS = [
    "PushEvent",
    "PullRequestEvent",
    "WatchEvent",
    "IssuesEvent",
    "ForkEvent",
]

BASE_URL = "https://api.github.com/users/{username}/events"


def fetch_events(username: str):
    url = BASE_URL.format(username=username)
    try:
        with urllib.request.urlopen(url, timeout=10) as response:
            body = response.read()
            return json.loads(body)
    except urllib.error.HTTPError as e:
        if e.code == 404:
            raise SystemExit(f"Error: User '{username}' not found.")
        raise SystemExit(f"Error: GitHub returned status {e.code}.")
    except urllib.error.URLError as e:
        if "timed out" in str(e.reason).lower():
            raise SystemExit("Error: GitHub is taking too long. Try again in a moment.")
        raise SystemExit("Error: No internet connection. Check your network and try again.")
    except json.JSONDecodeError:
        raise SystemExit("Error: GitHub sent back a response we couldn't understand. Try again.")


def format_event(event: dict):
    """Return a human-readable string for a single event, or None if unsupported."""
    event_type = event["type"]
    repo_name = event["repo"]["name"]

    # PushEvent
    if event_type == "PushEvent":
        return f"Pushed to {repo_name}."

    # PullRequestEvent
    if event_type == "PullRequestEvent":
        action = event["payload"].get("action", "")
        if action == "opened":
            return f"Opened a new PR in {repo_name}."
        if action == "merged":
            return f"Merged a PR in {repo_name}."
        if action == "closed":
            return f"Closed a PR in {repo_name}."

    # WatchEvent
    if event_type == "WatchEvent":
        action = event["payload"].get("action", "")
        if action == "started":
            return f"Starred {repo_name}."

    # IssuesEvent
    if event_type == "IssuesEvent":
        action = event["payload"].get("action", "")
        if action == "opened":
            return f"Opened a new issue in {repo_name}."
        if action == "closed":
            return f"Closed an issue in {repo_name}."

    # ForkEvent
    if event_type == "ForkEvent":
        action = event["payload"].get("action", "")
        forkee = event["payload"].get("forkee", {})
        fork_name = forkee.get("full_name", repo_name)
        if action == "forked":
            return f"Forked {repo_name} to {fork_name}."
        
    return None


def main():
    parser = argparse.ArgumentParser(description="Fetch recent GitHub activity for a user.")
    parser.add_argument("username", help="GitHub username")
    args = parser.parse_args()

    username = args.username.strip()
    if not username:
        raise SystemExit("Error: Username cannot be empty.")

    events = fetch_events(username)

    if not events:
        print(f"No public recent activity found for {username}.")
        return

    print(f"Recent activity for {username}:\n")
    for event in events:
        message = format_event(event)
        if message:
            print(f"  - {message}")

if __name__ == "__main__":
    main()
