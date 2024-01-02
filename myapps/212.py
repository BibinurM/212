import requests

def send_get_request(url):
    try:
        response = requests.get(url)
        response.raise_for_status()  # Проверка наличия ошибок в ответе
        return response.text
    except requests.exceptions.RequestException as e:
        return f"Error: {e}"

if __name__ == "__main__":
    server_url = input("Введите URL сервера: ")

    content = send_get_request(server_url)

    if "Error" in content:
        print(content)
    else:
        print("Ответ от сервера:")
        print(content)
