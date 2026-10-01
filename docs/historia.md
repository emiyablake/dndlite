# Decisão de Design: História e Narrativa por Fragmentos

> GDD — dndlite
> Status: **implementado** (ver `dndlite/dados.py` — lista `FRAGMENTOS`, e `main.py`)
> Relacionado: [combate](/combate-dnd.md), [personagens](/personagens-classes.md)

## Diretrizes Gerais

- A história não é contada de forma linear ou direta. Os fragmentos encontrados pelo caminho fazem o trabalho de deixar pistas para o jogador.
- Sem prazos ou explicações completas — mistério é a regra.
- **Como o jogador chegou na floresta fica propositalmente ambíguo.** As duas hipóteses coexistem como rumores contraditórios nos fragmentos (o contrato da taverna vs. um transporte misterioso). O jogador nunca recebe uma resposta definitiva.

## Introdução (impressa ao iniciar a jornada)

> Você acorda em uma clareira, com o sol forte queimando o seu rosto, mesmo com esforço não tem lembranças de como chegou ali. Quando levanta, tudo começar a rodar e sua cabeça está pesada, tocando o corpo procura seu cantil e sente um pergaminho amassado em seu bolso.

## Maelor, o Pálido 

Antes de sucumbir, Maelor foi um **grande mago pesquisador** do reino. Sua filha acometida por uma doença incuravel, fez com que o jovem mago elfico recorresse a métodos não tão ortodoxos. Apartir de seus estudos de necromancia ele desenvolveu um ritual de equivalencia vital para transferir parte de sua vida para a criança, usando como ponte um colar com pingente. Em vez de receber a vida de Maelor, o que restava no corpo da criança foi sugado para dentro do pingente de forma violenta, a magia havia saido completamento do controle do mago, destruindo seu corpo e aprisionando sua alma dentro do pingente. Inconformado com sua falha e cego pelo luto, Maelor continua ano após ano aprimorando o ritual, mantendo o corpo de sua querida filha com magia de preservação para que um dia ela possa retornar.

## Fragmentos 

Os fragmentos são pedaços da história que o jogador pode encontrar em momentos do jogo.

- `> [1] ler` — lê o fragmento na íntegra
- `> [2] guardar` — guarda sem ler

## Estrutura da Jornada 

>Como a história é contado e as batalhas acontecem?

Cena 01
O jogador acorda na clareira, é imprimido na tela a introdução, com as opções de escolha do jogador.
se ele escolhe ler o pergaminho -> imprime o que ta escrito no pergaminho
se ele escolhe pegar o cantil -> apenas bebe a agua enquanto olha ao redor 

ele encontra um caminho entre a arvores e resolve segui-lo para tentar sair da floresta, quando monstro aparece.

1. Goblin
2. Lobo Selvagem
3. Esqueleto
4. Orc
5. **Goblin Saqueador** (goblin reforçado)
6. **Esqueleto Antigo** (esqueleto reforçado)
7. Troll
8. **Vex'thul, o Lich** (chefe final — substitui o Dragão Sombrio)

## Por Que Não Mais um Dragão

O chefe original era um Dragão Sombrio, mas dragões são muito queridos — derrotá-los como vilão de rotina tira o encanto. O Lich carrega a história sozinho (motivação trágica, identidade com o tema de morte/ressurreição) e abre espaço pra um dragão aparecer no futuro como NPC, aliado ou masmorra opcional, sem precisar matá-lo.

## Em Aberto

- Final da história: o Lich morre grato ou amaldiçoa o jogador? (depende de como o desenvolvimento do final for implementado)
- NPCs, masmorras opcionais, dragão aliado
- Fragmentos podem ganhar efeitos mecânicos no futuro (ex.: ler todos desbloqueia algo)
