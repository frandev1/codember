"""
Desafio 4: Evitando el caos en la red

ΩMEGA está destruyendo todas las redes que consten de 3 nodos o más conectados entre sí. 
¡Hay que descubrir qué nodos están a salvo de sus ataques!

¿Cómo funciona la red? 

La red se representa como una lista de pares de conexiones entre nodos. Por ejemplo:

Entrada: [[1, 2], [2, 3], [4, 5]]
Esto significa:

El nodo 1 está conectado al nodo 2.
El nodo 2 está conectado al nodo 3.
El nodo 4 está conectado al nodo 5.
En este caso:

Los nodos 1, 2 y 3 forman un grupo conectado.
Los nodos 4 y 5 forman otro grupo conectado.


"""


def isSafeNode(node: list, nodes: list):
    for num in node:
        count = 0
        for n in nodes:
            if num in n:
                count += 1
            if count > 1:
                return False
    return True


def safeNodes(nodes: list):
    res = []
    for node in nodes:
        if isSafeNode(node, nodes):
            for i in node:
                res.append(i)
    return res


if __name__ == "__main__":
    print("[[1, 2], [2, 3], [4, 5]] ->", safeNodes([[1, 2], [2, 3], [4, 5]]))
    print("\n[[1, 2], [2, 3], [3, 4]] ->", safeNodes([[1, 2], [2, 3], [3, 4]]))
    print(
        "\n[[4, 6], [7, 9], [10, 12], [12, 16]] ->",
        safeNodes([[4, 6], [7, 9], [10, 12], [12, 16]]),
    )
    with open("Codember-2024/Challenge03/network.txt") as file:
        for line in file:
            nodes = eval(line)
            getSafeNodes = safeNodes(nodes)
            print("\nsubmit " + ",".join(map(str, getSafeNodes)))
