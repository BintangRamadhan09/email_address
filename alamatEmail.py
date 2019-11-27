## No. 2 Soal email


email = input('Silahkan Masukkan Email : ')

def tes(x):
    y = x.split('@')
    num = 0

    if '@' not in x or '.' not in x:
        out = 'TIDAK VALID'
    else:
        num = 0
        
        if y[0].isalnum() == True or '-' in y[0] or '_' in y[0]:
            num += 1
        z = y[1].split('.')

        if z[0].isalnum() == True:
            num += 1
        else:
            num = 0
        
        if z[1].isalpha() == True and len(z[1]) < 6:
            num += 1
        else:
            num = 0

        if num == 3:
            out = 'EMAIL VALID'
        else:
            out = 'TIDAK VALID'
    return out

hasil = tes(email)

print(f'HASIL : EMAIL INI {hasil}')