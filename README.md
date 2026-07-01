# GH-USER-ACTIVITY

A command-line tool that fetches the recent public activity of a GitHub user and displays it in the terminal.

## Table of Contents
- [Feature Overview](#feature-overview)
- [Installation](#installation)
- [Usage](#usage)
- [Commands](#commands)
- [Project Source](#project-source)

## Feature Overview

- Accepts a GitHub username as a command-line argument
- Fetches the user's recent public events via the GitHub REST API
- Displays a human-readable summary of each event in the terminal
- Handles the following event types:
  - `PushEvent` — commits pushed to a repository
  - `PullRequestEvent` — PRs opened, closed, or merged
  - `WatchEvent` — repositories starred
  - `IssuesEvent` — issues opened or closed
  - `ForkEvent` — repositories forked
- Handles errors gracefully: unknown users, network failures, timeouts, and malformed responses
- No external dependencies — uses Python's standard library only

## Installation

To install this program, use the commands below:

```bash
git clone https://github.com/fmax-dev/GH-USER-ACTIVITY.git
cd GH-USER-ACTIVITY
```

No packages to install.

## Usage

```bash
python gh_user_activity.py <username>
```

**Example:**

```bash
python gh_user_activity.py torvalds
```

**Output:**

```
Recent activity for fmax-dev:

  - Pushed to fmax-dev/TASK-TRACKER
  - Starred tinyfish-io/bigset.
  - Starred anomalyco/opencode.
  - ...
```

## Commands

| Argument | Description |
|---|---|
| `username` | The GitHub username to look up (required) |

## Project Source

This project is from [roadmap.sh](https://roadmap.sh). Click [here](https://roadmap.sh/projects/github-user-activity) to check it out.
