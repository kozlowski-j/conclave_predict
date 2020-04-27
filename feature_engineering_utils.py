def del_pope(x):
    """
    Function to delete pope's name from 'Consistory' variable.

    :param x: str
    :return: str
    """
    if x.find('Francis') != -1:
        return x.replace('Francis', '')
    elif x.find('Benedict\xa0XVI') != -1:
        return x.replace('Benedict\xa0XVI', '')
    elif x.find('John\xa0Paul\xa0II') != -1:
        return x.replace('John\xa0Paul\xa0II', '')
    else:
        return 999


def del_index(x):
    """
    Function to delete reduntant indices from 'Consistory' variable.

    :param x: str
    :return: str
    """
    if x.find('[') != -1:
        loc = x.find('[')
        return x[:loc]
    else:
        return x


def delete_latin_encoding(x):
    """
    Function to delete 'latin' encoded spaces from given variable

    :param x: 
    :return: 
    """
    if x.find("\xa0") != -1:
        return x.replace("\xa0", " ")
    else:
        return x
