#soal1
for i in range(1, 6):
    print(i)
#soal2
for i in range(2, 11, 2):
    print(i)
#soal3
hitung = 5
while hitung >=1:
    print(hitung)
    hitung -= 1
    
    #soal 1
nilai = [80, 75, 90, 85, 60]
for x in nilai:
    print(x)
#soal 2
total = 0
for x in nilai:
    total += x
print(total)
#soal 3
print(total/len(nilai))

#list dist
#soal1
mahasiswa = {
    'nama': 'dhanu',
    'umur': 19,
    'jurusan': 'sistem informasi'
}

#soal2
mahasiswa['ipk'] = '3.75'
print(mahasiswa)
#soal3
data = [
    {'nama': 'dhanu' , 'nilai': 80},
    {'nama': 'zaky', 'nilai': 75},
    {'nama': 'multzam', 'nilai': 90},
    {'nama': 'fahmi', 'nilai': 85},
    {'nama': 'dhanu', 'nilai': 60}
]
for i in data:
    print(i['nama'], i['nilai'])