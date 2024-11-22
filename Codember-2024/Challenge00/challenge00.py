'''
Desafío 1: ¡Consigue acceso a la terminal!

El número de la izquierda es la combinación inicial y las cadenas
de texto de la derecha son los movimientos que debes hacer.

Siempre empezamos del primer número de la izquierda. Los movimientos son:

R (Right)  movernos al siguiente dígito
L (Left)   desplazarnos al dígito anterior
U (Up)     incrementar ese dígito
D (Down)   decrementar el dígito actual

Si llegamos a la derecha del todo y recibimos un R, volvemos al
primer dígito. Si recibimos L y estamos en el primero, vamos al 
último. En el caso de que el dígito actual sea 9 y recibamos 
una U, pasará a 0. Y si es D y ese dígito es 0, pasará a ser 9.

000 URURD -> 119
1111 UUURUUU -> 4411
9999 LULULULD -> 8000

528934712834 URDURUDRUDLLLLUUDDUDUDUDLLRRRR
'''


def descifrar(num : str, code: str):
    res = list(num);
    pos = 0;
    act = int(res[pos]);
    for i in code:
        act = int(res[pos]);
        match i:
            case 'R':
                pos += 1;
            case 'L':
                pos -= 1;
            case 'U':
                act += 1;
                act %= 10;
                res[pos] = str(act)
            case 'D':
                if act == 0:
                    act = 9
                else:
                    act -= 1;
                res[pos] = str(act)
    return "".join(res)

print('000 URURD -> ',descifrar('000', 'URURD'))
print('1111 UUURUUU -> ',descifrar('1111', 'UUURUUU'))
print('9999 LULULULD -> ',descifrar('9999', 'LULULULD'))
print('528934712834 URDURUDRUDLLLLUUDDUDUDUDLLRRRR -> ', descifrar('528934712834', 'URDURUDRUDLLLLUUDDUDUDUDLLRRRR'))
