# Decisão de Design: Personagens, Atributos e Classes

> GDD — dndlite
> Status: **implementado** (ver `dndlite/`)
> Relacionado: [mecânica combate](/combate-dnd.md)

## Contexto

Com o combate sendo reformulado para o modelo D&D-like, o próximo passo é definir quem é o personagem do jogador: atributos e classes. Decisão de escopo: **3 atributos, 2 classes**, sem distribuição livre de pontos na criação.

## Atributos

De Força, Inteligência, Carisma e Destreza, escolhemos os três com impacto direto em mecânicas de jogo:

| Atributo | Afeta |
|---|---|---|
| **Força** | Ataques corpo a corpo (espadas, machados) | 
| **Inteligência** | Puzzles e enigmas no mundo (ver seção abaixo) |
| **Destreza** | Chance de esquiva, acerto com armas leves/ranged |

São 16 pontos de atributo distribuídos.

## Classes

### Fighter

| Atributo | Valor inicial |
|---|---|
| Força | 9 |
| Inteligência | 2 |
| Destreza | 5 |

13 HP
16 CA

Começa com espada longa (1d8) e armadura pesada. 
Habilidade usada Força.

### Ranger

| Atributo | Valor inicial |
|---|---|
| Força | 4 |
| Inteligência | 3 |
| Destreza | 9 |

10 HP
14 CA

Começa com um Arco Longo (1d8) e uma armadura média. 
Habilidade usada Destreza.

## Criação de Personagem

1. Jogador escolhe a **classe** (Fighter ou Ranger).
2. Jogador escolhe o **nome**.

## Progressão: Level Up

Ao subir de nível, o jogador ganha:

1. **+1 ponto de atributo**, distribuído à escolha entre Força, Inteligência ou Destreza.
2. **Pontos de vida máximo** — 5 pontos.

## Puzzles e Inteligência (TBD)

Inteligência é o atributo de fora de combate: puzzles e enigmas espalhados pelo mundo entre as batalhas. Ideias iniciais, ainda não fechadas:

- **Enigma do guardião**: um NPC ou inscrição faz uma pergunta de lógica/adivinha — acertar destrava o caminho (errar talvez dispare uma luta).
- **Armadilhas em masmorras**: uma checagem de Inteligência para perceber/desarmar antes de tomar dano.
- **Runas/estátuas com ordem**: sequência correta abre uma porta; dicas espalhadas no cenário.

Mecânica sugerida: `1d20 + Inteligência ÷ 2 vs CD (Classe de Dificuldade)` — o mesmo espírito do combate. Falhas podem ter custo (dano, luta extra), não apenas "tente de novo".

Não definido ainda: quantos puzzles, se são opcionais (recompensas) ou obrigatórios (progressão), e se falhas são permanentes.

