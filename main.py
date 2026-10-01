import time

from src.combate import batalha, pausa
from src.dados import CENAS, CLASSES, FRAGMENTOS, MONSTROS
from src.personagens import Jogador

INTRODUCAO = (
    "\nVocê acorda em uma clareira, com o sol forte queimando o seu rosto,\n"
    "mesmo com esforço não tem lembranças de como chegou ali.\n"
    "Quando se levanta, tudo começa a rodar e sua cabeça está pesada.\n"
    "Tocando o corpo, procura seu cantil e sente um pergaminho amassado em seu bolso."
)


def executar_cena(cena, jogador):
    """Mostra a descrição do ambiente e resolve a escolha do jogador."""
    print()
    pausa(cena["descricao"], 1.5)
    print("\nO que você faz?")
    for i, escolha in enumerate(cena["escolhas"], 1):
        print(f"  [{i}] {escolha['texto']}")
    while True:
        comando = input("> ").strip()
        if comando.isdigit() and 1 <= int(comando) <= len(cena["escolhas"]):
            escolhida = cena["escolhas"][int(comando) - 1]
            break
        print("Opção inválida!")
    print(f"\n{escolhida['resultado']}")
    if "cura" in escolhida:
        jogador.hp = min(jogador.hp_max, jogador.hp + escolhida["cura"])
        print(f"(+{escolhida['cura']} HP — {jogador.hp}/{jogador.hp_max})")
    if "pocoes" in escolhida:
        jogador.pocoes += escolhida["pocoes"]
        print(f"(+{escolhida['pocoes']} poção — total: {jogador.pocoes})")
    input("\n(Enter para continuar)")


def criar_personagem():
    print("\nEscolha sua classe:")
    for chave, classe in CLASSES.items():
        atributos = " ".join(f"{nome[:3].capitalize()}:{valor}" for nome, valor in classe.atributos.items())
        print(f"  [{chave}] {classe.nome} — {classe.descricao} — {atributos}")
    while True:
        escolha = input("> ").strip()
        if escolha in CLASSES:
            break
        print("Opção inválida!")
    nome = input("Qual é o nome do seu herói? ").strip() or "Herói"
    return Jogador(nome, CLASSES[escolha])


def encontrar_fragmento(titulo, texto):
    print(f"\nFragmento encontrado: {titulo}")
    print("  >ler      Ler o fragmento")
    print("  >guardar  Guardar sem ler")
    while True:
        comando = input("> ").strip().lower()
        if comando == "ler":
            print(f"\n--- {titulo} ---")
            print(texto)
            input("\n(Enter para continuar)")
            return
        if comando == "guardar":
            print("Você guarda o fragmento sem ler.")
            return
        print("Comando inválido! Digite >ler ou >guardar.")


def jornada():
    """Roda uma jornada completa. Retorna True se o jogador venceu."""
    jogador = criar_personagem()
    pausa(f"\nBem-vindo, {jogador.nome}!", 0.8)
    pausa(INTRODUCAO, 1.5)

    for i, ficha in enumerate(MONSTROS):
        for cena in CENAS:
            if cena["antes_de"] == i:
                executar_cena(cena, jogador)
        if not batalha(jogador, ficha):
            return False
        if i < len(FRAGMENTOS):
            titulo, texto = FRAGMENTOS[i]
            encontrar_fragmento(titulo, texto)
        if i < len(MONSTROS) - 1:
            pausa("\nVocê segue mais fundo na floresta...", 1.2)
    return True


def menu_inicial():
    """Mostra o menu inicial. Retorna True para jogar, False para sair."""
    print("\nMenu Iniciar")
    print(" [1] > Iniciar jogo")
    print(" [2] > Sair do jogo")
    while True:
        comando = input("> ").strip().lower()
        if comando == "1":
            return True
        if comando == "2":
            return False
        print("Comando inválido! Digite > 1 ou > 2.")


def main():
    print("=" * 40)
    print("       dndlite — A JORNADA DO HERÓI")
    print("=" * 40)

    while True:
        if not menu_inicial():
            print("Até a próxima aventura!")
            return

        venceu = jornada()

        print("\n" + "=" * 40)
        if venceu:
            print("Vitória! Você libertou a floresta do luto de Vex'thul.")
        else:
            print("VOCÊ MORREU")
        print("=" * 40)

        print("\nDigite > 1 para jogar de novo ou > 2 para encerrar.")
        while True:
            comando = input("> ").strip().lower()
            if comando == "1":
                break
            if comando == "2":
                print("Até a próxima aventura!")
                return
            print("Comando inválido! Digite > 1 ou > 2.")


if __name__ == "__main__":
    main()
