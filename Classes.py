import abc
class Pessoa(abc.ABC):
    def __init__(self,nome,cpf,nascimento,contato):
        self._nome = nome
        self._cpf = cpf
        self._nascimento = nascimento
        self._contato = contato

    @property
    def nome(self):
        return self._nome
    @nome.setter
    def nome(self,n):
        self._nome = n
    
    @property
    def cpf(self):
        return self._cpf
    @cpf.setter
    def cpf(self,id):
        self._cpf = id
    
    @property
    def nascimento(self):
        return self._nascimento
    @nascimento.setter
    def nascimento(self,data):
        self._nascimento = data
    
    @property
    def contato(self):
        return self._contato
    @contato.setter
    def contato(self,ctt):
        self._contato = ctt

    ''''@abc.abstractmethod
    def buscar(self,num):
        pass
  '''''
    def __repr__(self):
        return f'Nome: {self._nome}\nCPF: {self._cpf}\nData: {self._nascimento}\nContato: {self._contato}'


class Cliente(Pessoa):
    def __init__(self, nome, cpf, nascimento, contato,endereco):
        super().__init__(nome, cpf, nascimento, contato)
        self._endereco = endereco
       
   
    def listar(self):
        print(f'\tNome: {self._nome}\n\tCPF: {self._cpf}\n\tData: {self._nascimento}\n\tContato: {self._contato}\n\tEndereco: {self._endereco}\n')

    def __repr__(self):
        return f'\tNome: {self._nome}\n\tCPF: {self._cpf}\n\tData: {self._nascimento}\n\tContato: {self._contato}\n\tEnedreco: {self._endereco}'

class Funcionario(Pessoa):
    def __init__(self, nome, cpf, nascimento, contato,cargo,salario):
        super().__init__(nome, cpf, nascimento, contato)
        self._cargo = cargo
        self._salario = salario
    @property
    def cargo(self):
        return self._cargo
    @cargo.setter
    def cargo(self,c):
        self._cargo = c

    @property
    def salario(self):
        return self._salario
    @salario.setter
    def salario(self,sal):
        self._salario = sal
    

    def __repr__(self):
        return f'\tNome: {self._nome}\n\tCPF: {self._cpf}\n\tData: {self._nascimento}\n\tContato: {self._contato}\n\tCargo: {self._cargo}\n\tSalario: {self._salario}'

  
    def verificaSenha(self,senha):
       pass

#Vou usar essa classe para implementar a interface
class Gerente(Funcionario):
    def __init__(self, nome, cpf, nascimento, contato, cargo, salario,senha):
        super().__init__(nome, cpf, nascimento, contato, cargo, salario)
        self._senha = senha
    
    @property
    def senha(self):
        return self._senha
    
    def verificaLogin(self,senha):
        if senha == self._senha:
            return 'acesso permitido'
        else:
           return False
    def __repr__(self):
        return f'\tNome: {self._nome}\n\tCPF: {self._cpf}\n\tData: {self._nascimento}\n\tContato: {self._contato}\n\tCargo: {self._cargo}\n\tSalario: {self._salario}'

class Servico():
    def __init__(self,descricao,cod,metragem,valor,data_entrega):
        self._descricao = descricao
        self._metragem = metragem
        self._valor = valor
        self._cod = cod
        self._data_entrega = data_entrega
    @property
    def descricao(self):
        return self._descricao
    @descricao.setter
    def descricao(self,desc):
        self._descricao = desc
    
    @property
    def metragem(self):
        return self._metragem
    @metragem.setter
    def metragem(self, m):
        self._metragem = m
    
    @property
    def valor(self):
        return self._valor
    @valor.deleter
    def valor(self, v):
        self._valor = v
    
    @property
    def cod(self):
        return self._cod
    @cod.setter
    def cod(self, p):
        self._cpd = p
    
    @property
    def data_entrega(self):
        return self._data_entrega
    @data_entrega.setter
    def data_entrega(self,dt):
        self._data_entrega = dt

    def __repr__(self):
        return f'\n\tDescrição: {self._descricao}\n\tMetragem: {self._metragem}\n\tPedra: {self._cod}\n\tValor: {self._valor}\n\tData de entrega: {self._data_entrega}'

class Estoque:
    def __init__(self, cod, pedra, met,preco_m):
        self._cod = cod
        self._pedra = pedra
        self._met = met
        self._preco_m = preco_m
    
    @property
    def preco_m(self):
        return self._preco_m
    @preco_m.setter
    def preco_m(self,pr):
        self._preco_m = pr

    @property
    def cod(self):
        return self._cod
    @cod.setter
    def cod(self,c):
        self._cod = c
    
    @property
    def pedra(self):
        return self._pedra
    @pedra.setter
    def nome(self,n):
        self._pedra = n
    
    @property
    def met(self):
        return self._met
    @met.setter
    def met(self,m):
        self._met = m
    #metodo para verificar se tem material disponivel no estoque
    def verificarQ(self,metragem,cod):
        if cod == self._cod:
            if self._met < metragem:
                return 0
            else:
                self._met -= metragem
                return 1,self._preco_m
        else:
            return 2

    def __repr__(self):
        return f'\nCod: {self._cod} Cor: {self._pedra} Precço do m²: {self._preco_m} Metragem Diponivel: {self._met}'

class Validacao(abc.ABC):
    """essa classe verifica se o funcionário tem permissão para acessar o sistema interno da empresa
    """
    @abc.abstractmethod
    def verificaLogin(self,senha):
        if senha == self._senha:
            return 'acesso permitido'
        else:
            return False



