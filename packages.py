import requests


def cep_info(cep):
    r = requests.get('https://viacep.com.br/ws/{}/json'.format(cep))

    print(r.status_code)
    print(r.json())
    print(r.text)

    data = r.json()

    print(data.get('cep'))
    print(data.get('logradouro'))
    print(data.get('bairro'))
    print(data.get('localidade'))
    print(data.get('uf'))


if(__name__ == '__main__'):
    cep_info('18700010')
