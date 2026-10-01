# dndlite

Uma campanha de RPG com mecânicas baseadas em DnD e Dark Souls para você jogar no terminal.

## Como jogar

Requer Python 3.8+.

```bash
python main.py
```

- Escolha entre **Fighter** (Força, espada longa, armadura pesada) e **Ranger** (Destreza, arco longo, armadura média)
- Combate por turnos: `1d20 + modificador vs CA`, crítico no 20, erro no 1 — iguais às regras clássicas de D&D
- Suba de nível, distribua pontos de atributo, gerencie poções
- Explore cenas interativas e decida se lê os fragmentos de história pelo caminho

## Estrutura

```
main.py      # ponto de entrada (menu, jornada, cenas)
src/         # código fonte
  dados.py        # tabelas: armas, classes, monstros, cenas, fragmentos
  personagens.py  # Personagem, Jogador, Inimigo
  combate.py      # rolagens e loop de batalha
docs/        # GDDs e documentação de design
```

## Documentação de design

As decisões de design (combate, classes, história) estão documentadas em [`docs/README.md`](docs/README.md), que serve como índice dos GDDs.
