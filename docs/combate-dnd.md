# Decisão de Mecânica: Combate Baseado em D&D

> GDD — dndlite
> Status: **implementado** (ver `dndlite/`)

## Contexto

O sistema atual de combate é uma fórmula direta: `ataque base + Força + variação aleatória (−3 a +3) − defesa do inimigo`. Funciona, mas tem dois problemas:

1. **O jogador sempre acerta** — não existe chance de erro, esquiva ou crítico.
2. **Sem fundação pra expansão** — classes, armas e armaduras não têm onde se encaixar numa fórmula única.

Decisão: adotar um modelo inspirado em D&D, com **rolagem de dados por trás dos panos** (o jogador não rola nada manualmente — o jogo resolve).

## Mecânica Proposta

### 1. Rolamento de Acerto

```
total = 1d20 + modificador de ataque
acerto se total >= CA (Classe de Armadura) do inimigo
```

| Resultado do d20 | Efeito |
|---|---|
| 20 natural | **Crítico** — dano dobrado |
| 1 natural | **Erro crítico** — o ataque falha automaticamente |
| Demais | Compara `total` vs CA |

### 2. Modificador de Ataque

```
mod_ataque = bônus de atributo
```

- **Bônus de atributo**: derivado do atributo usado pela arma. Versão simplificada: usar atributo da arma ÷ 2 (arredondado pra baixo), ao invés da fórmula D&D de `(atributo − 10) / 2`.

### 3. Dano da Arma

Cada arma tem seu próprio dado de dano — a arma ganha "personalidade":

```
dano = rolagem_do_dado_da_arma + bônus de atributo
```

Exemplos (inspirado em D&D 5e):

| Arma | Dano |
|---|---|
| Adaga | 1d4 |
| Espada longa | 1d8 |
| Machado de batalha | 1d10 |
| Alabarda | 1d12 |
| Arco longo | 1d8 |

No crítico, a **rolagem do dado é dobrada** (ex: espada longa crítica = 2d8 + bônus).

## Adaptações pro Nosso Jogo

D&D completo é excessivo para um RPG de terminal. Pegamos o essencial:

| Conceito D&D | Versão do jogo |
|---|---|
| Mod. de atributo `(atributo − 10) / 2` | atributo da arma ÷ 2 (simplificado) |
| CA = 10 + mod. Destreza + armadura | CA fixa por inimigo, escala com a posição na lista de dificuldade |
| Vantagem/desvantagem | Futuro (ex.: ataque pelas costas, inimigo atordoado) |

## CA dos Inimigos (sugestão inicial)

Progressão alinhada à ordem de dificuldade atual:

| Inimigo | CA sugerida | Ataque |
|---|---|---|
| Goblin | 11 | Adaga 1d4 (+1) |
| Lobo Selvagem | 13 | Mordida 1d6 (+1) |
| Esqueleto | 12 | Espada curta 1d6 (+1) |
| Orc | 13 | Machado 1d8 (+3) |
| Troll | 14 | Clava 1d10 (+4) |
| Vex'thul, o Lich | 16 | Toque gélido 1d10 (+5) |

Inimigos rápidos (lobo) têm CA alta mas pouco HP; inimigos brutos (troll) têm CA média e muito HP. Números de dano/mods ainda serão calibrados — o HP do jogador agora é 13/10, então os danos precisam ser reescalados (ver seção de balanceamento).

## Ataque dos Inimigos

Inimigos seguem **exatamente as mesmas regras** dos jogadores:

```
acerto: 1d20 + mod do inimigo vs CA do jogador
dano:   rolagem do dado da arma do inimigo + mod
```

- Crítico no 20 natural (dado dobrado), erro automático no 1.
- O modificador do inimigo é fixo por tipo (na coluna "Ataque" acima) — inimigos não têm atributos visíveis, só o bônus final.
- A **CA do jogador** (16 Fighter / 14 Ranger, conforme armadura) é o que determina quanto os inimigos acertam. Fighter tanka mais, Ranger esquiva mais.

Exemplo: o Goblin rola 1d20+1 contra CA 16 do Fighter. Precisa tirar 15+ no dado (~30% de chance). Quando acerta, causa 1d4+1 (2 a 5 de dano).

Inimigos rápidos (lobo) têm CA alta mas pouco HP; inimigos brutos (troll) têm CA média e muito HP.

## Por Que Vale a Pena

1. **Combate menos previsível**: um goblin pode desviar de um golpe, um crítico pode virar uma luta perdida.
2. **Fundamento pra expansão**: classes (fighter → Força, ranger → Destreza), arsenal (cada arma com seu dado), armaduras (CA própria do jogador).
3. **Decisões de build**: level ups podem oferecer escolha ("+2 Força ou +10 HP máx?").

## Balanceamento / Reescala Necessária

A chegada das classes mudou a escala: o jogador agora tem **13 HP (Fighter) / 10 HP (Ranger)** e ganha **+5 HP por nível** — muito menos que os 50 HP atuais. Implicações:

- **Poções precisam ser reescaladas** — curar 20 num pool de 13 HP é cura total de graça. Sugestão: poção cura 1d8+2, ou um valor fixo baixo (4-5).
- **Dano dos inimigos** deve ficar na faixa de 2-8 nos primeiros combates, subindo gradualmente — um Orc acertando 1d8+3 pode derrubar um Fighter em 3 golpes, o que é aceitável como pico de dificuldade, não como regra.
- **XP/nível**: com +5 HP e +1 atributo por nível, chegar ao nível 4-5 antes de Vex'thul parece o alvo certo.

## Escopo do Primeiro Passo (quando implementar)

- Rolamento de acerto: **1d20 + mod vs CA** (jogador e inimigos)
- Dano: **dado da arma (1d8 inicial) + bônus do atributo da arma** (Força p/ Fighter, Destreza p/ Ranger)
- Crítico no 20, erro no 1
- **Com** as classes Fighter e Ranger (atributos, HP e CA fixos por classe)
- **Sem** múltiplas armas colecionáveis, armaduras trocáveis ou puzzles ainda — ficam para iterações futuras sobre esse esqueleto.
