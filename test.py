from github import Github, Auth
import os
from dotenv import load_dotenv
from openai import OpenAI

# Load .env
load_dotenv()

# -------------------------
# Test GitHub
# -------------------------
GITHUB_TOKEN = os.getenv("GITHUB_TOKEN")
USERNAME = os.getenv("GITHUB_USERNAME")

assert GITHUB_TOKEN is not None, "GITHUB_TOKEN not set in .env"
assert USERNAME is not None, "GITHUB_USERNAME not set in .env"

g = Github(auth=Auth.Token(GITHUB_TOKEN))

# Get authenticated user
user = g.get_user()
print(f"👤 GitHub Authenticated as: {user.login}")

if user.login != USERNAME:
    print(
        f"⚠️ Warning: .env username ({USERNAME}) doesn't match actual login "
        f"({user.login})"
    )

print("\n📂 Your GitHub repos:")
for repo in user.get_repos():
    print("-", repo.name)

# -------------------------
# Test OpenAI
# -------------------------
OPENAI_API_KEY = os.getenv("OPENAI_API_KEY")
client = OpenAI(api_key=OPENAI_API_KEY)

try:
    response = client.models.list()
    print("\n✅ OpenAI Authenticated. Available models:")
    for m in response.data[:5]:
        print("-", m.id)
except Exception as e:
    print("\n❌ OpenAI API failed:", e)
