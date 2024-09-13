import single_linked_list as lt
def rotate_right(lst, n):
    """
    Rota una lista enlazada un número dado de posiciones hacia la derecha.
    Rota la lista 'n' posiciones a la derecha, teniendo en cuenta el dato de entrada.
    Se ajustan los apuntadores del primer y último elemento de la lista según el número de rotaciones.

    Args:
        lst:  La lista a rotar a la derecha.
        n:  Número de posiciones a rotar la lista.

    Returns:
        La lista rotada a la derecha el número de posiciones dado.
    """
    while n != 0:
        last_og = lst["last"]
        remove_last(lst)
        add_first(lst, last_og)
        n -= 1
    return lst