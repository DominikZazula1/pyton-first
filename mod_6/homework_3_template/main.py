import requests as requests


def run_homework():
    try:
        response = requests.get("https://infoshareacademy.com")
    except requests.RequestException as error:
        print(f"Blad przy polaczeniu: {error}")
        return

    try:
        response.raise_for_status()
    except requests.HTTPError as error:
        print(f"zadanie zakończone niepowodzeniem {error}")
        return

    print(response.text.encode("utf-8"))


if __name__ == '__main__':
    run_homework()
