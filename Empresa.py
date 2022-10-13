import datetime
import abc
import random
from Classes import *

class Decore:
    def __init__(self):
        self._cnpj = '12345/001-23'
        self._contato = '89999-9999'
        self._endereco = ['rua 10','N° 350','Bairro: alvorecer']
        self._razao = 'Marmoraria'
        self.dicio_registro = {}
        self.dicio_servicos = {}
        self.dicio_cliente = {}
        self.dicio_funcionario = {}
        self.dicio_estoque = {}

        self.dicio_registro[self._cnpj] = [self._contato,self._endereco,self._razao]

    @property
    def cnpj(self):
        return self._cnpj
    
    @property
    def contato(self):
        return self._contato
    @contato.setter
    def contato(self,cll):
        self._contato = cll
    
    @property
    def endereco(self):
        return self._endereco
    @endereco.setter
    def endereco(self,end):
        self._endereco = end
    
    @property
    def razao(self):
        return self._razao
    @razao.setter
    def razao(self,rz):
        self._razao = rz

    def __repr__(self):
        return f'\tCNPJ: {self._cnpj}\n\tContato: {self._contato}\n\tEndereço: {self._endereco}\n\tRazão Social: {self._razao}'

    def cadastrar_cliente(self,nome,cpf,nascimento,contato,endereco):
        cliente = Cliente(nome,cpf,nascimento,contato,endereco)
        if cpf not in self.dicio_cliente.keys():
            self.dicio_cliente[cpf] = cliente
            return True, 'Cliente cadastrado com sucesso'
        else:
            print('Cliente já cadastrado')

    
    def cadastrarFuncionario(self,nome,cpf,nascimento,contato,cargo,salario):
        if cpf not in self.dicio_funcionario.keys():
            if cargo == 'gerente'.upper():
                senha = 9009
                gerente = Gerente(nome,cpf,nascimento,contato,cargo,salario,senha)
                self.dicio_funcionario[cpf] = gerente
                return 'Funcionário cadastrado com sucesso'
            else:
                funcionario = Funcionario(nome,cpf,nascimento,contato,cargo,salario)
                self.dicio_funcionario[cpf] = funcionario
        else:
            print('Funcionário já cadastrado')

    def adicionarServico(self,cpf,descricao,metragem,valor,cod,data_entrega):
        listaSer = []
        for i in self.dicio_estoque.values():
            aux,metro = i.verificarQ(metragem,cod)
            if aux == 0:
                return False,'O material disponiel não é sufuciente, aguarde reposição'
            if aux == 2:
                return False,'Material não disponivel'
            else:
                valor = metragem*metro
                servico = Servico(descricao,cod,metragem,valor,data_entrega)
                listaSer.append(servico)
                if cpf not in self.dicio_servicos.keys():
                    self.dicio_servicos[cpf] = listaSer
                    
                else:
                    self.dicio_servicos[cpf].append(listaSer)
                return True, 'Serviço adicionado'       

    def buscarServico(self,cpf):
        if cpf in self.dicio_servicos.keys():
            return self.dicio_servicos[cpf]
        else:
            return 'Cliente não cadastrado'

    def infoEstoque(self,cod,cor,met,preco_m):
        if cod not in self.dicio_estoque.keys():
            estoque = Estoque(cod,cor,met,preco_m)
            self.dicio_estoque[cod] = estoque
            return 'Material cadastrado com sucesso'
        else:
           return 'material já cadastrado'
    
    def imprimirEstoque(self):
        for i in self.dicio_estoque.values():
            print('\t',i)
    
    def estoqueBuscar(self,cod):
        if cod in self.dicio_estoque.keys():
            return self.dicio_estoque[cod]
        else:
            return 'Item não cadastrado no sistema'

    def verificar(self,cpf):
        if cpf in self.dicio_funcionario.keys():
            recebido = self.dicio_funcionario[cpf]
            if (isinstance(recebido,Validacao)):
                recebido.verificaLogin(recebido.senha)
                return 'Acesso permitido'
            else:
                return 'Funcionário não autorizado'

    def buscarPessoa(self,op,cpf):    
        if op == 1:
            if cpf in self.dicio_cliente.keys():
                return self.dicio_cliente[cpf]
            else:
                return 'Cliente não cadastrado no Sistema'
        if op == 2:
            if cpf in self.dicio_funcionario.keys():
                return self.dicio_funcionario[cpf]
            else:
                return 'Funcionário não cadastrado no Sistema'
       
    def imprimirEmpresa(self):
        c = len(self.dicio_cliente)
        f = len(self.dicio_funcionario)
        print('\tInformações Da Empresa:')
        print(f'Total de Clientes cadastrados: {c}')
        print(f'Total de Funcionários cadastrados: {f}')
        for i in self.dicio_registro.values():
            print(i)

    def imprimirFuncionários(self):
        print('\tFuncionários')
        for i in self.dicio_funcionario.values():
            print(i)

    def imprimirCliente(self):
        print('\tClientes')
        for i in self.dicio_cliente.values():
            print(i)
        


        
        





        
    

