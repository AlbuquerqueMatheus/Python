#.keys() retorna todas as chaves do dicionário
#.values() retorna todos os valores.

dicionario = {'nome': 'matheus', 'idade': '26'}

print(f'as chaves são: {dicionario.keys()}')
print(f'os valores são {dicionario.values()}')

#adicionando um novo par chave-valor
dicionario['altura'] = 1.70
print(f'Dicionario atualizado: {dicionario}')

#removendo a chave 'nome' e seu valor do dicionário com .pop()
dicionario.pop('nome')
print(f'Dicionario atualizado: {dicionario}')

#Remoção do último par chave-valor com .popitem()
dicionario.popitem()
print(f'dicionario atualizado: {dicionario}')

#Atualização do dicionário com .update()
novoDicionario = {'basquete': 'quadra'}
dicionario.update(novoDicionario)
print(f'dicionario atualizado: {dicionario}')

#Iterar sobre um dicionário e acessar seus pares chave-valor 
for chave, valor in dicionario.items():
    print(f"{chave}: {valor}")

#{}.get saber se um elemento existe ou não no dicionarios
contatos = {
    "matheuskaral@gmail.com": {"nome": "matheus", "telefone": "8599646-2926"}
}
print(contatos.get("nome"))
print(contatos.get("chave", {}))
print(contatos.get("matheuskaral@gmail.com", {}))

#del
contatos = {
    "matheuskaral@gmail.com": {"nome": "matheus", "telefone": "8599646-2926"},
    "alisson@gmail.com": {"nome": "matheus", "telefone": "8599646-2926"}
}

del contatos["matheuskaral@gmail.com"]["nome"]
del contatos["alisson@gmail.com"]