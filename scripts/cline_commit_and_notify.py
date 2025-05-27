import os
import subprocess
import requests
import json

def get_git_changes():
    """Get a summary of git changes"""
    return subprocess.check_output(['git', 'status', '--porcelain']).decode('utf-8')

def get_git_diff():
    """Get the git diff"""
    return subprocess.check_output(['git', 'diff']).decode('utf-8')

def create_summary(changes, diff):
    """Create a summary of changes"""
    summary = "Changes made:\n"
    summary += changes + "\n\n"
    summary += "Diff:\n"
    summary += diff[:1000] + "..." if len(diff) > 1000 else diff
    return summary

def send_to_slack(message):
    """Send message to Slack"""
    webhook_url = os.environ.get('SLACK_WEBHOOK_URL')
    if not webhook_url:
        print("SLACK_WEBHOOK_URL not set. Skipping Slack notification.")
        return

    payload = {
        "text": message,
        "channel": "cline-bot-git-action"
    }
    response = requests.post(webhook_url, data=json.dumps(payload),
                             headers={'Content-Type': 'application/json'})
    if response.status_code != 200:
        raise ValueError(f"Request to Slack returned an error {response.status_code}, "
                         f"the response is:\n{response.text}")

def commit_and_push():
    """Commit changes and push to repository"""
    branch_name = f"fix-{subprocess.check_output(['date', '+%Y%m%d-%H%M%S']).decode('utf-8').strip()}"
    
    subprocess.run(['git', 'checkout', '-b', branch_name])
    subprocess.run(['git', 'add', '.'])
    subprocess.run(['git', 'commit', '-m', 'Apply fixes'])
    subprocess.run(['git', 'push', 'origin', branch_name])

    return branch_name

def main():
    changes = get_git_changes()
    diff = get_git_diff()
    summary = create_summary(changes, diff)

    print("Summary of changes:")
    print(summary)

    send_to_slack(f"New changes ready for review:\n\n{summary}")

    branch_name = commit_and_push()
    print(f"Changes committed and pushed to branch: {branch_name}")

if __name__ == "__main__":
    main()
