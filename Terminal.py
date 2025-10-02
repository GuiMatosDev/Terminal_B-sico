#Funções relativas aos comandos
def comando_teste():
    print('teste')

#Adicione a função correspondente ao comando


#Comandos Dicionário
comandos = {
    'teste': comando_teste,
    #Adicione aqui a palavra-chave e o nome da função
    }


#Checagem da entrada e ativação do comando
def leitura_entrada(entrada):

    comando = comandos.get(entrada)

    if comando:
        comando()
    else:
        print('Não reconheci seu comando')

def main():


    loop = True
    while loop:
        
        entrada = input('$: ')

        if entrada == 'exit':
            loop = False
        else:
            leitura_entrada(entrada)

#Execução
main()
