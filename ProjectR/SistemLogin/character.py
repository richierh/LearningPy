def count():
    file = input('masukkan file ber-ekstensi txt yang ingin dibuka: ')


    try:
        with open(file) as o:
            text = o.read()
            print(text)
            char = input('masukkan char yang ingin dihitung: ')
            hitung = 0

            for i in text:
                if i == char:
                    hitung += 1
            print('jumlah huruf {0} pada {1} adalah {2}'.format(char, file, hitung))
    except:
        print('file text tidak ada didalam folder')


count()