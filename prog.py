# Ave Cesare
eng = [chr(i) for i in range(97, 123)]
ENG = [chr(i) for i in range(65, 91)]
rus = [chr(i) for i in range(1040, 1104)]

way = input('Что хотите сделать с текстом (enc or dec):')
lan = input('Язык текста (eng or rus):')
step = int(input('Направление шифрования (l or r):'))
in_range = 25

def enc_eng(text):
    enc_arr = ''
    for i in range (len(text)):
        if text[i] in eng:
            if ord(text[i])+step > 123:
                enc_arr += chr(ord(text[i])+step-26)
            else:
                enc_arr += chr(ord(text[i])+step)
        elif text[i] in ENG:
            if ord(text[i])+step > 91:
                enc_arr += chr(ord(text[i])+step-26)
            else:
                enc_arr += chr(ord(text[i])+step)
        else:
            enc_arr += text[i]
    return enc_arr

def enc_rus(text):
    enc_arr = ''
    for i in range (len(text)):
        if text[i] in rus:
            enc_arr += chr(ord(text[i])+step)
        else:
            enc_arr += text[i]
    return enc_arr

def dec_rus(text):
    enc_arr = ''
    for i in range (len(text)):
        if text[i] in rus and 1040 <= ord(text[i]) <= 1072:
            if (ord(text[i])-step) <= 1040:
                enc_arr += chr(ord(text[i])-step+32)
            #elif (ord(text[i])-step) < 1072:
            #    enc_arr += chr(ord(text[i])-step+32)
            else:
                enc_arr += chr(ord(text[i])-step)
        elif text[i] in rus and 1073 <= ord(text[i]) <= 1104:  
            if (ord(text[i])-step) < 1072:
                enc_arr += chr(ord(text[i])-step+32)
            else:
                enc_arr += chr(ord(text[i])-step)
        else:
            enc_arr += text[i]
    return enc_arr

def dec_eng(text):
    enc_arr = ''
    step = 26
    while step != 0:
        for i in range (len(text)):
            if text[i] in eng:
                if ord(text[i])-step < 97:
                    enc_arr += chr(ord(text[i])-step+26)
                else:
                    enc_arr += chr(ord(text[i])-step)
            elif text[i] in ENG:
                if ord(text[i])-step < 65:
                    enc_arr += chr(ord(text[i])-step+26)
                else:
                    enc_arr += chr(ord(text[i])-step)
            else:
                enc_arr += text[i]
        print (enc_arr, sep= '\n')
        enc_arr = ''
        step -= 1

    #print (enc_arr)


while True:
    if way == 'enc':
        if lan == 'eng':
            print (enc_eng(input('Введите текст для шифрования:')))
        elif lan == 'rus':
            print (enc_rus(input('Введите текст для шифрования:')))
    else:
        if lan == 'eng':
            print (dec_eng(input('Введите текст для шифрования:')))
        elif lan == 'rus':
            print (dec_rus(input('Введите текст для шифрования:')))