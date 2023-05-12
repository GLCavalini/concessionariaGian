from dataclasses import dataclass
import json

@dataclass
class Carro:
    nome:       str
    marca:      str
    ano:        int
    cor:        str
    preco:      int

    def criar_arquivo_txt(self):
        with open(f"{self.nome}.txt", "w") as file:
            json.dump(self.__dict__, file)

    @staticmethod
    def adicionar_carro_ao_arquivo(carro):
        arquivo_existente = True
        try:
            with open(f"{carro.nome}.txt", "r") as file:
                conteudo = json.load(file)
        except FileNotFoundError:
            arquivo_existente = False

        if arquivo_existente:
            # Adiciona o novo carro ao conteúdo existente
            conteudo.append(carro.__dict__)
        else:
            # Cria uma nova lista com apenas o novo carro
            conteudo = [carro.__dict__]

        # Escreve o conteúdo atualizado no arquivo
        with open(f"{carro.nome}.txt", "w") as file:
            json.dump(conteudo, file)


    @staticmethod
    def ler_arquivo_txt(nome_arquivo):
        with open(f"{nome_arquivo}.txt", "r") as file:
            conteudo = json.load(file)
        return Carro(**conteudo)

    def editar_carro(self):
        print("Digite as novas informações do carro:")
        novo_nome = input(f"Nome ({self.nome}): ")
        novo_marca = input(f"Marca ({self.marca}): ")
        novo_ano = input(f"Ano ({self.ano}): ")
        novo_cor = input(f"Cor ({self.cor}): ")
        novo_preco = input(f"Preço ({self.preco}): ")
        
        if novo_nome != '':
            self.nome = novo_nome
        if novo_marca != '':
            self.marca = novo_marca
        if novo_ano != '':
            self.ano = novo_ano
        if novo_cor != '':
            self.cor = novo_cor
        if novo_preco != '':
            self.preco = novo_preco
        
        with open(f"{self.nome}.txt", "w") as file:
            json.dump(self.__dict__, file)

#Criar Carro
meu_novo_carro = Carro(nome="Gol", marca="Volkswagen", ano=2015, cor="Branco", preco=35000)
Carro.adicionar_carro_ao_arquivo(meu_novo_carro)



#Ler Arquivo JSON
meu_carro = Carro.ler_arquivo_txt("Fiesta")
print(meu_carro)

#Editar arquivo JSON
meu_carro.editar_carro()
