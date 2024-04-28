
participantes_list = []

def inserir_participante_clojure(x):
    participantes_list.append(x)

def print_participantes():
    print("Participantes:")
    for p in participantes_list:
        (nome, matricula) = p()
        print(matricula + " " + nome)