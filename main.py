from Empresa import *

def idade(nascimento):
    anoAtual = datetime.date.today()
    idade = anoAtual.year - nascimento.year
    if anoAtual.month < nascimento.month:
        idade-=1
    return idade

def buscar():
    op = int(input('\t1-Cliente\n\t2-Funcionário: '))
    cpf = str(input('Cpf: '))
    return decore.buscarPessoa(op,cpf)

def vizualizarServicos():
    cpf = str(input('CPF do titular'))
    retorno = decore.buscarServico(cpf)   
    print(retorno)
   
def adicionarServico():
    valor = 0
    cpf = str(input('Cpf do titular: '))
    descricao = str(input('Descrição do serviço: '))    
    metragem = float(input('Metragem total do serviço (m)'))
    cod = int(input('Codigo: '))
    data_entrega = input('Data de entrega').split(" ")
    return decore.adicionarServico(cpf,descricao,metragem,valor,cod,data_entrega)


def cadastrarCliente():
    contato=[]
    endereco = []
    nome = str(input('Nome: '))
    cpf = str(input('Cpf: '))
    contato.append(str(input('Contato: ')))
    dia, mes, ano = input('Nascimento: ').split(" ")
    dia = int(dia)
    mes = int(mes)
    ano = int(ano)
    nascimento = datetime.datetime(ano,mes,dia)
    id = idade(nascimento)
    if id < 18:
        print('Menores de idade não podem ser clientes titular')
    else:
        endereco.append(str(input('Endereco: ')))
    return decore.cadastrar_cliente(nome,cpf,nascimento,contato,endereco)   

    
def cadastrarFuncionario():
    contato = []
    nome = str(input('Nome: '))
    cpf = str(input('Cpf: '))
    contato.append(str(input('Contato: ')))
    dia, mes, ano = input('Nascimento: ').split(" ")
    dia = int(dia)
    mes = int(mes)
    ano = int(ano)
    nascimento = datetime.datetime(ano,mes,dia)
    id = idade(nascimento)
    if id < 18:
        print('Menores de idade não podem ser contrataos')
    else:
        cargo = str(input('Cargo: ')).upper()
        salario = float(input('Salario: '))
    return decore.cadastrarFuncionario(nome,cpf,nascimento,contato,cargo,salario)

#tá dando certo
def estoque():
    while True: 
        op = int(input('1-Adicionar\n2-4Buscar item\n3-Consultar Estoque\n4-Voltar ao Menu anterior: '))
        if op == 1:
            print('Cadastro de itens no estoque')
            cod = random.randint(100,999)
            print('cod: ',cod)
            cor = str(input('Cor associada ao codigo: '))
            met = float(input('Metragem Disponivel: '))
            preco_m = float(input('Preço do M²: '))  
            return decore.infoEstoque(cod,cor,met,preco_m)
        if op == 2:
            cod = int(input('Digite o código: \n'))
            return decore.estoqueBuscar(cod)
        if op == 3:
            return decore.imprimirEstoque()
        if op == 4:
            break      
# Tá dando certo
def empresaInfo():
    opc = int(input('\n\t1 -Empresa\n\t2 - Cadastrar Funcionário: '))
    try:
        if opc == 1:
            cpf = str(input('CPF: '))
            mensagem = decore.verificar(cpf)
            print(mensagem)
            op = int(input('\t1-Vizualizar Informações da Empresa\n\t2-Vizualizar Funcionário\n\t3-Vizualizar Clientes: '))
            if op == 1:
                decore.imprimirEmpresa()
            if op == 2:
                decore.imprimirFuncionários()
            if op == 3:
                    decore.imprimirCliente()
        if opc == 2:
            mensagem = cadastrarFuncionario()
            print(mensagem)          
    except:
        #no caso de digitar uma função inxistente, ele volta para o menu principal
       # print('Opção inválida. Digite uma das opções numéricas')
       pass
        
        
# Tá dando certo
def Menu():
    try:
        print(40*' ')
        print('\t\tDECORE MARMORARIA')
        print(40*' ')
        print('\t1-Cadastrar cliente\n\t2-Adicionar Serviço\n\t3-Buscar\n\t4-Estoque')
        print('\t5-Vizualizar Serviço\n\t6-Informações da Empresa\n\t7-Sair')
        esc = int(input('\tSelecione a opção desejada:  '))
        return esc
    except:
        print('Opção invpalida. Digite uma das opções numéricas.')
    
            
decore = Decore()
Validacao.register(Gerente)

while True:
    esc = Menu()
    if esc == 1:
        retorno,mensagem = cadastrarCliente()
        print(mensagem)
    if esc == 2:
         retorno,mensagem = adicionarServico()  
         print(mensagem) 
    if esc == 3:
        print('\t\tBUSCAR')
        mensagem = buscar()
        print(mensagem)
    if esc == 4:
       mensagem = estoque()
       print(mensagem)
    
    if esc == 5:#Corrigir as informações da empresa
       vizualizarServicos()
    if esc == 6:
        empresaInfo()
    if esc == 7:
        print('Sistema Finalizado')
        break


                          
   