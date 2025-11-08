class Personagem:
    def __init__(self, nome, vida, nivel):
        self.__nome = nome 
        self.__vida = vida
        self.__nivel = nivel

    def get_nome(self):
        return self.__nome
    
    def get_vida(self):
        return self.__vida
    
    def get_nivel(self):
        return self.__nivel
    
    def exibir_detalhes(self):
        return f"Nome: {self.get_nome()} - Vida: {self.get_vida()} - Nível: {self.get_nivel()}"

    def receber_ataque(self, dano):
        self.__vida -= dano
        if self.__vida <= 0:
            self.__vida = 0

    def atacar(self, alvo):
        dano = self.__nivel * 2 
        alvo.receber_ataque(dano)
        print(f"\n{self.get_nome()} atacou {alvo.get_nome()} e causou {dano} de dano!")


class Heroi(Personagem):
    def __init__(self, nome, vida, nivel, habilidade):
        super().__init__(nome, vida, nivel)
        self.__habilidade = habilidade

    def get_habilidade(self):
        return self.__habilidade
    
    def exibir_detalhes(self):
        return f"{super().exibir_detalhes()} - Habilidade: {self.get_habilidade()}"
    
    def ataque_especial(self, alvo):
        dano = self.get_nivel() * 5
        alvo.receber_ataque(dano)
        print(f"\n{self.get_nome()} atacou {alvo.get_nome()} com o ataque especial {self.get_habilidade()} e causou {dano} de dano!")
    

class Inimigo(Personagem):
    def __init__(self, nome, vida, nivel, tipo):
        super().__init__(nome, vida, nivel)
        self.__tipo = tipo

    def get_tipo(self):
        return self.__tipo
    
    def exibir_detalhes(self):
        return f"{super().exibir_detalhes()} - Tipo: {self.get_tipo()}"
    

class Jogo:
    def __init__(self):
        self.heroi = Heroi(nome="Pirata", vida=100, nivel=5, habilidade="Chuva de espadas")
        self.inimigo = Inimigo(nome="Vampiro", vida=130, nivel=6, tipo="sangue")

    def iniciar_batalha(self):
        print("Iniciando batalha !!!")

        while self.heroi.get_vida() > 0 and self.inimigo.get_vida() > 0:
            print("\n Detalhes dos personagens")
            print(self.heroi.exibir_detalhes())
            print(self.inimigo.exibir_detalhes())

            input("Pressione Enter para ataca...")
            escolha = input("Escolha 1 - Ataque básico | Escolha 2 - Ataque Especial")

            if escolha == "1":
                self.heroi.atacar(self.inimigo)
            if escolha == "2":
                self.heroi.ataque_especial(self.inimigo)
            else:
                print("Escolha uma opção válida")

            if self.inimigo.get_vida() > 0:
                
                self.inimigo.atacar(self.heroi)
            
        if self.heroi.get_vida() > 0:
            print(f"\nO {self.heroi.get_nome()} ganhou a batalha! \n Parabéns!")
        else:
            print(f"\nO {self.inimigo.get_nome()} ganhou a batalha! \n Boa sorte na próxima vez!")

jogo = Jogo()
jogo.iniciar_batalha()
