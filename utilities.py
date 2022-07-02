#!/usr/bin/python3


def parser_list(lists):
    """this function parses a list that is of type string into a
    true list by decomposing each element and inserting
    into a new list
    Return: New List"""
    lista = lists[1:-1].replace("\"", "")
    lista = lista.split(", ")
    return lista


def isfloat(num):
    """This function evaluates if a number
    is a float or not a float and returns
    True if it is a float and False if not."""
    try:
        float(num)
        return True
    except ValueError:
        return False


def parser(lista):
    """This function parses the elements of a list if
    it is a string it removes the quotes and if it does
    not have quotes it keeps it the same, at the
    end it returns a parsed list"""
    final_list = []
    for i in lista:
        if (i[0] == '\"'):
            final_list.append(i[1:-1])
        else:
            final_list.append(i)
    return final_list


def validator(lists):
    """They are a valid function if what they are passing
    me is a list or has quotes to be able to parse it and
    return a set element with the correct type to be
    inserted in the dictionary later"""
    new_list = []
    lista_principal = []
    total = len(lists)
    new_member = lists[3]
    if (lists[3][0] == '\"' or lists[3][0] == '['):
        for i in range(total):
            if (lists[i][-1] == ']'):
                new_list.append(lists[i])
                break
            if (i > 3 and lists[i][-1] == '\"'):
                new_list.append(lists[i])
                break
            elif i >= 3:
                new_list.append(lists[i])
            else:
                lista_principal.append(lists[i])
        new_str = " ".join(new_list)
        lista_principal.append(new_str)
        lists = lista_principal
        if (lists[3][0] == '\"'):
            new_member = lists[3][1:-1]
        else:
            new_member = lists[3]
    return new_member
