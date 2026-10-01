"""Tabelas de dados do jogo — adicionar armas, classes ou monstros
novos aqui não exige mudar a lógica de personagens/combate."""

from dataclasses import dataclass


@dataclass(frozen=True)
class Arma:
    nome: str
    faces: int            # dado de dano: 1d<faces>
    atributo: str         # atributo que modifica acerto e dano


@dataclass(frozen=True)
class Classe:
    nome: str
    descricao: str
    atributos: dict       # {"forca": int, "inteligencia": int, "destreza": int}
    hp: int
    ca: int               # classe de armadura
    arma: str             # chave em ARMAS


@dataclass(frozen=True)
class FichaMonstro:
    nome: str
    ca: int
    hp: int
    arma: str             # chave em ARMAS
    mod_ataque: int       # bônus fixo de acerto/dano
    xp: int


ARMAS = {
    "adaga": Arma("Adaga", 4, "destreza"),
    "espada_curta": Arma("Espada curta", 6, "forca"),
    "espada_longa": Arma("Espada longa", 8, "forca"),
    "arco_longo": Arma("Arco longo", 8, "destreza"),
    "machado": Arma("Machado", 8, "forca"),
    "clava": Arma("Clava", 10, "forca"),
    "mordida": Arma("Mordida", 6, "forca"),
    "toque_gelido": Arma("Toque gélido", 10, "forca"),
}

CLASSES = {
    "1": Classe(
        nome="Fighter",
        descricao="Espada longa (1d8) e armadura pesada. Briga com Força.",
        atributos={"forca": 9, "inteligencia": 2, "destreza": 5},
        hp=13,
        ca=16,
        arma="espada_longa",
    ),
    "2": Classe(
        nome="Ranger",
        descricao="Arco longo (1d8) e armadura média. Atira com Destreza.",
        atributos={"forca": 4, "inteligencia": 3, "destreza": 9},
        hp=10,
        ca=14,
        arma="arco_longo",
    ),
}

# Ordem = progressão de dificuldade (o jogador enfrenta nessa sequência)
MONSTROS = [
    FichaMonstro("Goblin", ca=11, hp=7, arma="adaga", mod_ataque=1, xp=10),
    FichaMonstro("Lobo Selvagem", ca=13, hp=11, arma="mordida", mod_ataque=1, xp=15),
    FichaMonstro("Esqueleto", ca=12, hp=13, arma="espada_curta", mod_ataque=1, xp=20),
    FichaMonstro("Orc", ca=13, hp=15, arma="machado", mod_ataque=3, xp=25),
    FichaMonstro("Goblin Saqueador", ca=12, hp=14, arma="espada_curta", mod_ataque=2, xp=20),
    FichaMonstro("Esqueleto Antigo", ca=13, hp=16, arma="espada_curta", mod_ataque=2, xp=25),
    FichaMonstro("Troll", ca=15, hp=84, arma="clava", mod_ataque=4, xp=35),
    FichaMonstro("Vex'thul, o Lich", ca=16, hp=70, arma="toque_gelido", mod_ataque=5, xp=80),
]

# Fragmentos de história encontrados após cada batalha.
# Cada entrada: (título, texto mostrado ao ler)
FRAGMENTOS = [
    ("Bilhete amassado no seu bolso",
     "Um contrato de compra. A floresta inteira, comprada por 'Vex'thul, Arquivista Real'.\n"
     "Na margem, a sua própria letra: 'Aceito os termos.'\n"
     "Você não se lembra de ter assinado nada."),
    ("Medalhão pendurado num galho",
     "Um medalhão de prata com o retrato de uma menina sorridente.\n"
     "No verso, gravado: 'Para a minha Elara — que o sol nunca se ponha pra você.'"),
    ("Página de diário rasgada",
     "'A febre não passa. Os curandeiros desistiram.\n"
     "Mas há uma cura proibida, registrada nos arquivos do reino...\n"
     "O que eu não faria por ela?'"),
    ("Grimório molhado de orvalho",
     "Anotações de pesquisa, cada vez mais desesperadas.\n"
     'Ritos de cura riscados, reescritos, riscados de novo.\n'
     'Na última página, apenas: "A cura e a necromancia usam a mesma porta."'),
    ("Carta selada, nunca enviada",
     "'Perdoe-me, Elara. Pai falhou.\n"
     "O ritual a mantém aqui, mas não é vida. Eu sei que não é vida.\n"
     "Ainda assim, não consigo deixá-la ir. Perdoe-me."),
    ("Boneca de pano apodrecida",
     "Uma boneca costurada à mão, com vestido azul desbotado.\n"
     "Está sobre uma pedra, como se alguém a tivesse colocado ali para descansar.\n"
     "A floresta inteira ficou quieta."),
    ("Última página do arquivista",
     "'Quem quer que esteja lendo: eu comprei esta floresta para guardá-la.\n"
     "Não para prendê-la.\n"
     "Se você chegou até aqui, termine o que eu não tive coragem de terminar.'"),
]

POCAO_CURA_FACES = 8
POCAO_CURA_BONUS = 2
POCOES_INICIAIS = 3
HP_POR_NIVEL = 5
XP_PARA_NIVEL_2 = 10
XP_INCREMENTO_POR_NIVEL = 10

# Cenas de exploração: descrição do ambiente + escolhas numeradas,
# tocadas antes da batalha de índice "antes_de" em MONSTROS.
# Efeitos opcionais por escolha: "pocoes" (ganha poções), "cura" (recupera HP).
CENAS = [
    {
        "antes_de": 0,  # Goblin
        "descricao": (
            "Você acorda em uma clareira, com o sol forte queimando o seu rosto.\n"
            "Mesmo com esforço, não tem lembranças de como chegou ali. Quando se levanta,\n"
            "tudo começa a rodar e sua cabeça está pesada. Tocando o corpo, procura seu\n"
            "cantil e sente um pergaminho amassado no seu bolso."
        ),
        "escolhas": [
            {
                "texto": "Pega o pergaminho",
                "resultado": (
                    "Um contrato de compra, assinado com a sua própria letra:\n"
                    "'Aceito os termos. — Vex'thul, Arquivista Real.'\n"
                    "Você não se lembra de ter assinado nada."
                ),
            },
            {
                "texto": "Pega o cantil",
                "resultado": "Ainda tem água. Você bebe e a cabeça clareia um pouco.",
                "cura": 3,
            },
        ],
    },
    {
        "antes_de": 3,  # Orc
        "descricao": (
            "A trilha se divide. À esquerda, marcas de botas na lama — alguém passou\n"
            "por aqui recentemente, arrastando algo pesado. À direita, a mata fechada,\n"
            "escura e silenciosa demais."
        ),
        "escolhas": [
            {
                "texto": "Seguir as marcas na lama",
                "resultado": "Você encontra uma mochila rasgada. Dentro, uma poção intacta.",
                "pocoes": 1,
            },
            {
                "texto": "Atravessar a mata fechada",
                "resultado": "Galhos arranham seu rosto, mas você atravessa. Algo observou você passar.",
            },
        ],
    },
    {
        "antes_de": 6,  # Troll
        "descricao": (
            "Um riacho corta o caminho. A água corre limpa sobre pedras cobertas de musgo,\n"
            "e do outro lado a trilha sobe até uma caverna. Há pegadas enormes na margem —\n"
            "recentes."
        ),
        "escolhas": [
            {
                "texto": "Descansar e beber água",
                "resultado": "A água é fria e boa. Você respira fundo e segue adiante.",
                "cura": 3,
            },
            {
                "texto": "Seguir imediatamente, sem parar",
                "resultado": "Você atravessa o riacho de uma vez, antes que o dono das pegadas volte.",
            },
        ],
    },
]
