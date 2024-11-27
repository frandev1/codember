'''
Desafío 2: Detectando acceso no deseado

- Sólo usa letras minúsculas y dígitos.
- Nunca usa dígitos después de una letra (Una vez aparecen letras, la contraseña debe continuar solo con letras)
- Si usa dígitos, siempre los usa de forma igual o creciente (si sale un 3, ya no usará después un número menor)
- Si usa letras, siempre las usa en orden alfabético igual o creciente (si sale una "b" ya no podrá usar una "a", por ejemplo)
  
Algunos ejemplos para que lo entiendas perfectamente:
1234     -> true
abc      -> true
aabbcc   -> true (repite pero siempre ascendente)
112233   -> true (repite pero siempre ascendente)
a123     -> false (un número después de una letra)
123abc   -> true
dbce     -> false (una "d" y después una "b")
'''

def unwantedAccess (password: str):
    for i in range(1, len(password)-1):
        if password[i].isdigit():
            if password[i-1].isalpha():
                return False
            elif (int(password[i]) < int(password[i-1])):
                return False 
        else:
            if password[i].isupper():
                return False
            elif (ord(password[i]) < ord(password[i-1])):
                return False
    return True;

def main ():
    with open("Codember-2024/Challenge01/log.txt", "r") as file:
        true = 0;
        false = 0;
        for linea in file:
            if (unwantedAccess(linea)):
                true += 1;
            else:
                false += 1;
        print(f'submit {true}true{false}false');


print('1234-> ',unwantedAccess('1234'));
print('abc-> ', unwantedAccess('abc'));
print('aabbcc-> ', unwantedAccess('aabbcc'));
print('112233-> ', unwantedAccess('112233'));
print('a123-> ', unwantedAccess('a123'));
print('123abc-> ', unwantedAccess('123abc'));
print('dbce-> ', unwantedAccess('dbce'));

main();