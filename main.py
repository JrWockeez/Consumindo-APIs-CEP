import requests

print('###CONSUMINDO APIs###')

cep_input = input("Digite o CEP para a consulta: ")
if len(cep_input) != 8:
    print('Quantidade de dígitos inválida!')
    exit()

requests = requests.get('https://viacep.com.br/ws/{}/json/'.format(cep_input))

address_data = requests.json()

if 'erro' not in address_data:
    print()
    print('CEP encontrado:')
    print('Endereço: {}'.format(address_data['logradouro']))
    print('Bairro: {}'.format(address_data['bairro']))
    print('UF: {}'.format(address_data['uf']))
    print('CEP: {}'.format(address_data['cep']))

else:
    print('{}: CEP inválido!'.format(cep_input))




