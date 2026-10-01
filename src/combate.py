import random
import time

from .personagens import Inimigo


def pausa(msg="", seg=0.6):
    if msg:
        print(msg)
    time.sleep(seg)


def _atacar(atacante, defensor):
    """Resolve um ataque completo. Retorna True se acertou."""
    natural, total = atacante.rolamento_ataque()
    critico = natural == 20

    if natural == 1:
        pausa(f"{atacante.nome} rolou 1 no d20 — erro crítico! O ataque falha.", 0.8)
        return False

    if critico or total >= defensor.ca:
        dano = atacante.calcular_dano(critico)
        defensor.receber_dano(dano)
        msg = f"{atacante.nome} acerta (rolou {natural}+{atacante.mod_ataque} vs CA {defensor.ca})"
        if critico:
            msg += " — CRÍTICO!"
        pausa(f"{msg} e causa {dano} de dano!", 0.8)
        return True

    pausa(f"{atacante.nome} errou (rolou {natural}+{atacante.mod_ataque} vs CA {defensor.ca}).", 0.8)
    return False


def batalha(jogador, ficha):
    """Roda uma batalha. Retorna True se o jogador sobreviveu (vitória ou fuga)."""
    inimigo = Inimigo(ficha)
    pausa(f"\nUm {inimigo.nome} apareceu! {inimigo}", 1.0)

    while jogador.vivo and inimigo.vivo:
        print("\n" + "-" * 40)
        print(jogador)
        print(inimigo)
        print("-" * 40)
        print("[1] Atacar   [2] Poção   [3] Fugir")

        escolha = input("O que você faz? ").strip()

        if escolha == "1":
            _atacar(jogador, inimigo)
        elif escolha == "2":
            if not jogador.usar_pocao():
                continue
        elif escolha == "3":
            if random.random() < 0.5:
                pausa("Você conseguiu fugir!", 0.8)
                return True
            pausa("Você tentou fugir, mas falhou!", 0.8)
        else:
            print("Opção inválida!")
            continue

        if inimigo.vivo:
            _atacar(inimigo, jogador)

    if not jogador.vivo:
        return False

    pausa(f"\nVocê derrotou o {inimigo.nome}!", 1.0)
    jogador.ganhar_xp(inimigo.xp)
    if random.random() < 0.4:
        jogador.pocoes += 1
        pausa("O inimigo dropou uma poção!", 0.8)
    return True
