import random

class Personagem:
    '''
    Classe de Personagem geral com métodos que ambos podem utilizar
    '''
    def __init__(self, nome, vida, nivel, ataque_basico):
        self.__nome = nome 
        self.__vida = vida
        self.__nivel = nivel
        self.__ataque_basico = ataque_basico

    def get_nome(self):
        return self.__nome
    
    def get_vida(self):
        return self.__vida
    
    def get_nivel(self):
        return self.__nivel
    
    def get_ataque_basico(self):
        return self.__ataque_basico
    
    def exibir_detalhes(self):
        return f"Nome: {self.get_nome()} - Vida: {self.get_vida()} - Nível: {self.get_nivel()} - Ataque básico: {self.get_ataque_basico()}"

    def receber_ataque(self, dano):
        self.__vida -= dano
        if self.__vida <= 0:
            self.__vida = 0

    def atacar(self, alvo):
        dano = random.randint(self.get_nivel() * 2, self.get_nivel() * 4) 
        alvo.receber_ataque(dano)
        print(f"\n{self.get_nome()} atacou {alvo.get_nome()} e causou {dano} de dano!")


class Heroi(Personagem):

    def __init__(self, nome, vida, nivel, ataque_basico, habilidade_especial):
        super().__init__(nome, vida, nivel, ataque_basico)
        self.__habilidade_especial = habilidade_especial

    def get_habilidade_especial(self):
        return self.__habilidade_especial
    
    def exibir_detalhes(self):
        return f"{super().exibir_detalhes()} - Habilidade: {self.get_habilidade_especial()}"
    
    def ataque_especial(self, alvo):
        dano = random.randint(self.get_nivel() * 5, self.get_nivel() * 24)
        alvo.receber_ataque(dano)
        print(f"\n{self.get_nome()} atacou {alvo.get_nome()} com o ataque especial {self.get_habilidade_especial()} e causou {dano} de dano!")
    

class Inimigo(Personagem):

    # ✅ corrigido: agora aceita o ataque_basico
    def __init__(self, nome, vida, nivel, ataque_basico, tipo):
        super().__init__(nome, vida, nivel, ataque_basico)
        self.__tipo = tipo

    def get_tipo(self):
        return self.__tipo
    
    def exibir_detalhes(self):
        return f"{super().exibir_detalhes()} - Tipo: {self.get_tipo()}"
    

class Jogo:

    Herois = {"Pirata":
              {"vida": 120, "nivel": 5,"habilidade comum": "golpe de espada", "habilidade extra": "Chuva de espadas"},

              "Mago(a)":
              {"vida": 90, "nivel": 7,"habilidade comum": "bola de fogo", "habilidade extra": "Bola de fogo gigante"},

              "Bárbaro(a)":
              {"vida": 180, "nivel": 7,"habilidade comum": "golpe com tacape", "habilidade extra": "Tacape giratório"},

              "Arqueiro(a)":
              {"vida": 100, "nivel": 7,"habilidade comum": "ataque a distância com flecha", "habilidade extra": "Flecha envenenada"},

              "Guerreiro(a)":
              {"vida": 170, "nivel": 6, "habilidade comum": "ataque com espada", "habilidade extra": "Espada giratória"}
              }
    
    Inimigos = {"Vampiro(a)":
                {"vida": 135, "nivel": 6, "tipo": "sangue", "ataque_basico": "mordida e roubo de vitalidade"},

                "Bruxo(a)":
                 {"vida": 90, "nivel": 6, "tipo": "mágico", "ataque_basico": "transforma em sapo"},

                "Zumbi":
                  {"vida": 100, "nivel": 6, "tipo": "morto-vivo", "ataque_basico": "mordida podre"},

                "Ogro":
                  {"vida": 180, "nivel": 6, "tipo": "Fera", "ataque_basico": "cascudo na cabeça"},

                "Palhaço":
                 {"vida": 120, "nivel": 6, "tipo": "mágico", "ataque_basico": "ilusão"}
                }
    
    def __init__(self):
        self.heroi = self.escolher_heroi()
        self.inimigo = self.sortear_inimigo()

    
    def escolher_heroi(self):
        print("\n=== Escolha seu herói ===\n")
    
        for i, (nome, dados) in enumerate(self.Herois.items(), start=1):
            print(f"{i}. {nome}")
            print(f"Vida: {dados['vida']}")
            print(f"Nível: {dados['nivel']}")
            print(f"Habilidade comum: {dados['habilidade comum']}")
            print(f"Habilidade especial: {dados['habilidade extra']}\n")
    
        while True:
            try:
                escolha_num = int(input("Digite o número do herói que deseja escolher: "))
                if 1 <= escolha_num <= len(self.Herois):
                    nome_escolhido = list(self.Herois.keys())[escolha_num - 1]
                    dados = self.Herois[nome_escolhido]
                    print(f"\nVocê escolheu {nome_escolhido}!")
                    print(f"Habilidade comum: {dados['habilidade comum']}")
                    print(f"Habilidade especial: {dados['habilidade extra']}\n")
                    return Heroi(
                        nome_escolhido,
                        dados["vida"],
                        dados["nivel"],
                        dados["habilidade comum"],
                        dados["habilidade extra"]
                    )
                else:
                    print("Número inválido! Tente novamente.\n")
            except ValueError:
                print("Por favor, digite um número válido.\n")
    
    def sortear_inimigo(self):
        nome_inimigo = random.choice(list(self.Inimigos.keys()))
        dados = self.Inimigos[nome_inimigo]
        print(f"\nUm {nome_inimigo} apareceu!")
        return Inimigo(nome_inimigo, dados["vida"], dados["nivel"], dados["ataque_basico"], dados["tipo"])

    def iniciar_batalha(self):
        print("Iniciando batalha !!!")

        while self.heroi.get_vida() > 0 and self.inimigo.get_vida() > 0:
            print("\n Detalhes dos personagens")
            print(self.heroi.exibir_detalhes())
            print(self.inimigo.exibir_detalhes())

            input("Pressione Enter para atacar...")
            escolha = input("Escolha 1 - Ataque básico | Escolha 2 - Ataque Especial: ")

            if escolha == "1":
                self.heroi.atacar(self.inimigo)
            elif escolha == "2":
                self.heroi.ataque_especial(self.inimigo)
            else:
                print("Escolha uma opção válida")

            if self.inimigo.get_vida() > 0:
                self.inimigo.atacar(self.heroi)
            
        if self.heroi.get_vida() > 0:
            print(f"\nO {self.heroi.get_nome()} ganhou a batalha! \nParabéns!")
        else:
            print(f"\nO {self.inimigo.get_nome()} ganhou a batalha! \nBoa sorte na próxima vez!")


jogo = Jogo()
jogo.iniciar_batalha()
