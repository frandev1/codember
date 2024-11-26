"""
Desafio 4: Evitando el caos en la red
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

def main():
    with open("Codember-2024/Challenge03/network.txt") as file:
        for line in file:
            nodes = eval(line);
            getSafeNodes = safeNodes(nodes)
            print("\nsubmit " + ",".join(map(str, getSafeNodes)))

print("[[1, 2], [2, 3], [4, 5]] ->", safeNodes([[1, 2], [2, 3], [4, 5]]))
print("\n[[1, 2], [2, 3], [3, 4]] ->", safeNodes([[1, 2], [2, 3], [3, 4]]))
print(
    "\n[[4, 6], [7, 9], [10, 12], [12, 16]] ->",
    safeNodes([[4, 6], [7, 9], [10, 12], [12, 16]]),
)

main()
