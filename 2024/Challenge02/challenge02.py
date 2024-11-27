'''
Desafío 3: ¡Siguiendo la pista de la IA ΩMEGA!

- Número positivo: ΩMEGA avanza ese número de posiciones.
- Número negativo: Retrocede ese número de posiciones.
- Cero: Se queda en la misma posición (pero cuenta como movimiento).

**Importante**: Cada vez que ΩMEGA lee una instrucción, incrementa el valor de esa instrucción en 1 después de usarla.

- Si encuentra un 2, avanza 2 posiciones y luego esa instrucción se convierte en 3.
- Si encuentra un 0, se queda en su posición y luego esa instrucción se convierte en 1.
- Si encuentra un -3, retrocede 3 posiciones y luego esa instrucción se convierte en -2.
'''

def stepsCounter(instruction: list):
    pos = 0;
    steps = 0;
    while (pos >= 0 and pos <= len(instruction)-1):
        actualPos = pos
        pos += instruction[pos];
        instruction[actualPos] += 1;
        steps += 1;
    return steps

def main():
    totalSteps = 0;
    finalSteps = 0;
    with open("Codember-2024/Challenge02/trace.txt", "r") as file:
        for line in file:
            line = line.strip();
            instructions = [int(x) for x in line.split(' ')];
            steps = stepsCounter(instructions);
            totalSteps += steps;
            finalSteps = steps;
    print(f'submit {totalSteps}-{finalSteps}');
    return


print("1 2 4 1 -2 ->", stepsCounter([1, 2, 4, 1, -2]))
print("0 1 2 3 -1 ->", stepsCounter([0, 1, 2, 3, -1]))
print("1 -2 5 ->", stepsCounter([1, -2, 5]))
main()