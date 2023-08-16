"""
Exercício Python 114: Crie um código em Python que teste se o site pudim está acessível pelo computador usado.
"""

import requests


def verificar_acessibilidade(site_url):
    try:
        response = requests.get(site_url, timeout=10)

        # Verificar o código de status da resposta
        if response.status_code == 200:
            return True, "Site acessível"
        else:
            return False, f"Código de status: {response.status_code}"
    except requests.ConnectionError:
        return False, "Falha na conexão"
    except requests.Timeout:
        return False, "Tempo limite excedido"
    except Exception as e:
        return False, f"Erro: {str(e)}"


# URL do site que você deseja verificar
site_url = "https://www.facebook.com"

# Verificar a acessibilidade do site
acessivel, mensagem = verificar_acessibilidade(site_url)

if acessivel:
    print(f"O site {site_url} está acessível.")
else:
    print(f"O site {site_url} não está acessível. Razão: {mensagem}")
