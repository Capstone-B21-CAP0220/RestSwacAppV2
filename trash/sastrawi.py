# import Sastrawi package
from Sastrawi.Stemmer.StemmerFactory import StemmerFactory

# create stemmer
factory = StemmerFactory()
stemmer = factory.create_stemmer()

# stem
sentence = 'Perekonomian Indonesia sedang dalam pertumbuhan yang membanggakan'
output   = stemmer.stem(sentence)

print(output)
# ekonomi indonesia sedang dalam tumbuh yang bangga

# print(stemmer.stem('Mereka meniru-nirukannya'))
# mereka tiru
(["foo", "bar", "baz"])
print(stemmer.stem('Aku anak tunggal. Ibu dan ayah berpisah ketika umur saya 4 tahun. Ibu menikah dengan laki-laki yang perkerjaannya notaris. Aku dipaksa ibu memanggil ayah baru dengan sebutan "daddy". Sejak saat itu juga daddy memperlakukanku tidak enak. Aku nggak ingat pas umur berapa, tapi aku udah diperkosa daddy selama bertahun-tahun. Aku juga disiksa sebelum aku diperkosa. Ibu enggak tau kejadian ini karena daddy punya kekuasaan tinggi di rumah. Tolong bantu aku, aku tidak tau harus mengadu kesiapa'))


# print(sentence.split(' '))
# print(sentence.lower().split(' '))

