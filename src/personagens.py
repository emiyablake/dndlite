import random

from .dados import (
    ARMAS,
    POCAO_CURA_BONUS,
    POCAO_CURA_FACES,
    POCOES_INICIAIS,
    HP_POR_NIVEL,
    XP_INCREMENTO_POR_NIVEL,
    XP_PARA_NIVEL_2,
)


def rolar(n, faces):
    """Rola n dados de `faces` lados e retorna a soma."""
    return sum(random.randint(1, faces) for _ in range(n))


class Personagem:
    def __init__(self, nome, hp, ca, arma, atributos, mod_ataque):
        self.nome = nome
        self.hp_max = hp
        self.hp = hp
        self.ca = ca
        self.arma = ARMAS[arma]
        self.atributos = dict(atributos)
        self.mod_ataque = mod_ataque

    @property
    def vivo(self):
        return self.hp > 0

    def rolamento_ataque(self):
        """Retorna (d20 natural, total do ataque)."""
        natural = random.randint(1, 20)
        return natural, natural + self.mod_ataque

    def calcular_dano(self, critico=False):
        quantidade = 2 if critico else 1
        return rolar(quantidade, self.arma.faces) + self.mod_ataque

    def receber_dano(self, dano):
        self.hp = max(0, self.hp - dano)

    def __str__(self):
        return f"{self.nome}  HP: {self.hp}/{self.hp_max}  CA: {self.ca}"


class Jogador(Personagem):
    def __init__(self, nome, classe):
        super().__init__(
            nome=nome,
            hp=classe.hp,
            ca=classe.ca,
            arma=classe.arma,
            atributos=classe.atributos,
            mod_ataque=0,  # calculado dinamicamente, ver abaixo
        )
        self.classe = classe.nome
        self.nivel = 1
        self.xp = 0
        self.xp_proximo_nivel = XP_PARA_NIVEL_2
        self.pocoes = POCOES_INICIAIS

    @property
    def mod_ataque(self):
        return self.atributos[self.arma.atributo] // 2

    @mod_ataque.setter
    def mod_ataque(self, valor):
        pass  # mod é derivado dos atributos; ignora atribuição do __init__

    def ganhar_xp(self, quantidade):
        self.xp += quantidade
        print(f"Você ganhou {quantidade} XP! ({self.xp}/{self.xp_proximo_nivel})")
        while self.xp >= self.xp_proximo_nivel:
            self.subir_nivel()

    def subir_nivel(self):
        self.nivel += 1
        self.xp -= self.xp_proximo_nivel
        self.xp_proximo_nivel += XP_INCREMENTO_POR_NIVEL
        self.hp_max += HP_POR_NIVEL
        self.hp = self.hp_max
        print(f"\n*** LEVEL UP! Nível {self.nivel}! +{HP_POR_NIVEL} HP máx ***")
        self._distribuir_ponto()

    def _distribuir_ponto(self):
        opcoes = list(self.atributos)
        while True:
            print("Distribua +1 ponto de atributo:")
            for i, atributo in enumerate(opcoes, 1):
                print(f"  [{i}] {atributo.capitalize()} (atual: {self.atributos[atributo]})")
            escolha = input("> ").strip()
            if escolha.isdigit() and 1 <= int(escolha) <= len(opcoes):
                atributo = opcoes[int(escolha) - 1]
                self.atributos[atributo] += 1
                print(f"{atributo.capitalize()} agora é {self.atributos[atributo]}.")
                return
            print("Opção inválida!")

    def usar_pocao(self):
        if self.pocoes <= 0:
            print("Você não tem mais poções!")
            return False
        cura = rolar(1, POCAO_CURA_FACES) + POCAO_CURA_BONUS
        self.hp = min(self.hp_max, self.hp + cura)
        self.pocoes -= 1
        print(f"Você usou uma poção e recuperou {cura} HP! ({self.hp}/{self.hp_max})")
        return True

    def __str__(self):
        return (
            f"{self.nome} ({self.classe})  Nível: {self.nivel}  "
            f"HP: {self.hp}/{self.hp_max}  CA: {self.ca}  "
            f"For:{self.atributos['forca']} Int:{self.atributos['inteligencia']} "
            f"Des:{self.atributos['destreza']}  Poções: {self.pocoes}"
        )


class Inimigo(Personagem):
    def __init__(self, ficha):
        super().__init__(
            nome=ficha.nome,
            hp=ficha.hp,
            ca=ficha.ca,
            arma=ficha.arma,
            atributos={},
            mod_ataque=ficha.mod_ataque,
        )
        self.xp = ficha.xp
