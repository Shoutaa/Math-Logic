import itertools

def nilai(kata, substitusi):
    s = 0
    faktor = 1
    for huruf in reversed(kata):
        s += faktor * substitusi[huruf]
        faktor *= 10
    return s

def penyelesaian(persamaan):
    kiri, kanan = persamaan.lower().replace(' ', '').split('=')
    kiri = kiri.split('+')
    huruf_huruf = set(kanan)
    for kata in kiri:
        for huruf in kata:
            huruf_huruf.add(huruf)
    huruf_huruf = list(huruf_huruf)
    digit = range(10)
    
    for perm in itertools.permutations(digit, len(huruf_huruf)):
        solusi = dict(zip(huruf_huruf, perm))
        if sum(nilai(kata, solusi) for kata in kiri) == nilai(kanan, solusi):
            if solusi[kanan[0]] != 0:
                print(' + '.join(str(nilai(kata, solusi)) for kata in kiri) + " = {} (Penjelasan : {})".format(nilai(kanan, solusi), solusi))
if __name__ == '__main__':
    penyelesaian('BA + AB = AAC')#Soal
