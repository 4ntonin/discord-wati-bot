from random import randint


def roulette(liste):
    r = []
    w = ''
    for i in range(len(liste)):
        if liste[i] != ',':
            if liste[i] == ' ':
                if liste[i-1] != ',':
                    w += liste[i]
            else:
                w += liste[i]
        else:
            r.append(w)
            w = ''
    r.append(w)
    if len(r) > 1:
        res = r[randint(0, len(r)-1)]
        return res
