import subprocess
import sys

def display_notification(platform):
    header = "JustReleaseIt"
    message = f"{platform}: Release is uploaded successfully to App Center."
    
    # macOS system notification
    subprocess.run([
        "osascript", "-e", f'display notification "{message}" with title "{header}"'
    ])

if __name__ == "__main__":
    if len(sys.argv) != 2:
        print("Usage: python3 fileName.py <platform>")
    else:
        platform = sys.argv[1]
        display_notification(platform)
