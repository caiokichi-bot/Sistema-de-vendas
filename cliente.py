class Cliente:

    def __init__(self, id, nome, cpf, email, telefone, endereco, cidade, estado, cep):
        self.__id = id
        self.__nome = nome
        self.__cpf = cpf
        self.__email = email
        self.__telefone = telefone
        self.__endereco = endereco
        self.__cidade = cidade
        self.__estado = estado
        self.__cep = cep

    @property
    def id(self):
        return self.__id
    
    @id.setter
    def id(self, valor):
        if valor is None or isinstance(valor, int):
            self.__id = valor
        else:
            raise ValueError("ID deve ser inteiro ou None")

    @property
    def nome(self):
        return self.__nome
    
    @nome.setter
    def nome(self, valor):
        if isinstance(valor, str) and len(valor.strip()) > 0 and len(valor) <= 100:
            self.__nome = valor.strip()
        else:
            raise ValueError("Nome deve ser string não vazia (máx. 100 caracteres)")

    @property
    def cpf(self):
        return self.__cpf
    
    @cpf.setter
    def cpf(self, valor):
        if isinstance(valor, str) and len(valor.strip()) > 0 and len(valor) <= 100:
            self.__cpf = valor.strip()
        else:
            raise ValueError("CPF deve ser string não vazia (máx. 100 caracteres)")

    @property
    def email(self):
        return self.__email
    
    @email.setter
    def email(self, valor):
        if isinstance(valor, str) and len(valor.strip()) > 0 and len(valor) <= 100:
            self.__email = valor.strip()
        else:
            raise ValueError("Email deve ser string não vazia (máx. 100 caracteres)")

    @property
    def telefone(self):
        return self.__telefone
    
    @telefone.setter
    def telefone(self, valor):
        if isinstance(valor, str) and len(valor.strip()) > 0 and len(valor) <= 100:
            self.__telefone = valor.strip()
        else:
            raise ValueError("Telefone deve ser string não vazia (máx. 100 caracteres)")

    @property
    def endereco(self):
        return self.__endereco
    
    @endereco.setter
    def endereco(self, valor):
        if isinstance(valor, str) and len(valor.strip()) > 0 and len(valor) <= 100:
            self.__endereco = valor.strip()
        else:
            raise ValueError("Endereco deve ser string não vazia (máx. 100 caracteres)")

    @property
    def cidade(self):
        return self.__cidade
    
    @cidade.setter
    def cidade(self, valor):
        if isinstance(valor, str) and len(valor.strip()) > 0 and len(valor) <= 100:
            self.__cidade = valor.strip()
        else:
            raise ValueError("Cidade deve ser string não vazia (máx. 100 caracteres)")

    @property
    def estado(self):
        return self.__estado
    
    @estado.setter
    def estado(self, valor):
        if isinstance(valor, str) and len(valor.strip()) > 0 and len(valor) <= 100:
            self.__estado = valor.strip()
        else:
            raise ValueError("Estado deve ser string não vazia (máx. 100 caracteres)")

    @property
    def cep(self):
        return self.__cep
    
    @cep.setter
    def cep(self, valor):
        if isinstance(valor, str) and len(valor.strip()) > 0 and len(valor) <= 100:
            self.__cep = valor.strip()
        else:
            raise ValueError("Cep deve ser string não vazia (máx. 100 caracteres)")

    def __str__(self):
        return f"id:{self.id}, nome:{self.nome}, cpf:{self.cpf}, email:{self.email}, telefone:{self.telefone}, endereco:{self.endereco}, cidade:{self.cidade}, estado:{self.estado}, cep:{self.cep}"