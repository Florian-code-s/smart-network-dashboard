import requests


def main():
    response = requests.get("https://api.github.com")
    print("Status Code: ", response.status_code)

if __name__ == "__main__":
    main()
