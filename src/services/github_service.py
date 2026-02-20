import requests

def github_status():
    resp = requests.get("https://api.github.com", timeout=5)
    return {"status_code": resp.status_code}