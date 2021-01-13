import re
man = open('mbox-short.txt')
count = 0
# Búsqueda de líneas que contengan 'From'
for line in man:
    line = line.strip()

    if re.search('^From:', line):
        count +=1
        print(line)

print(count)


"""
    import re
    dir(re)
    help(re.search)

    ^   Coincide con el comienzo de la línea.
    $   Coincide con el final de la línea.
    .   Coincide con cualquier carácter (un comodín).
    \s  Coincide con un espacio en blanco.
    \S  Coincide con un carácter que no sea un espacio en blanco (el opuesto a \s).
    *   Se aplica al carácter o caracteres inmediatamente anteriores, indicando quepueden coincidir cero o más veces.
    *?  Se aplica al carácter o caracteres inmediatamente anteriores, indicando quecoinciden cero o más veces en modo “no ambicioso”.
    +   Se aplica al carácter o caracteres inmediatamente anteriores, indicando quepueden coincidir una o más veces
    +?  Se aplica al carácter o caracteres inmediatamente anteriores, indicando quepueden coincidir una o más veces en modo “no ambicioso”.
    ?   Se aplica al carácter o caracteres inmediatamente anteriores, indicando que puede coincidir cero o una vez.
    ??  Se aplica al carácter o caracteres inmediatamente anteriores, indicando quepuede coincidir cero o una vez en modo “no ambicioso
    ( ) Cuando se agregan paréntesis a una expresión regular, son ignorados para propósitos de encontrar coincidencias, pero permiten extraer un subconjunto de-terminado de la cadena en que se encuentra la coincidencia, en lugar de toda la cadena como cuando se utiliza findall()
    \b  Coincide con una cadena vacía, pero solo al comienzo o al final de una palabra.
    \B  Concide con una cadena vacía, pero no al comienzo o al final de una palabra.
    \d  Coincide con cualquier dígito decimal; equivalente al conjunto [0-9].
    \D  Coincide con cualquier carácter que no sea un dígito; equivalente al conjunto[ˆ0-9].
    [aeuoi] Coincide con un solo carácter, siempre que éste se encuentre dentro delconjunto especificado. En este caso, coincidiría con “a”, “e”, “i”, “o”, o “u”, perono con otros caracteres
    [a-z0-9]    Se pueden especificar rangos de caracteres utilizando el signo menos. Eneste caso, sería un solo carácter que debe ser una letra minúscula o un dígito    
    [ˆA-Za-z]   Cuando el primer carácter en la notación del conjunto es “ˆ”, inviertela lógica. En este ejemplo, habría coincidencia con un solo carácter queno seaunaletra mayúscula o una letra minúscula
    

"""
