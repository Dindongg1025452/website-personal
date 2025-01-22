print("Zombie apocalypse \ngame pemilihan ending \nperingatan : pilih opsinya saja")
print("Telah terjadi zombie apocalypse di dunia! \nkamu sedang berada di rumah, apa yang akan kamu lakukan?")
print("a.tetap mengunci diri di rumah dan menunggu bantuan datang dengan suplai yang tersisa \nb.memberanikan diri untuk keluar, kita tak bisa bergantung pada bantuan yang tak pasti!")
a = (input("Kamu sedang berada dirumah, apa yang akan kamu lakukan? masukan opsimu : "))
if a == "a" :
    print("suplai kian hari makin habis, apa yang akan kamu lakukan?")
    print("a.berteriak meminta bantuan dari jendela \nb.tetap menunggu bantuan")
    v = (input("pilih opsi :"))
    if v == "a" :
        print("oh tidak, para zombie malah mendatangi sumber suaramu")
        print("para zombie menggedor pintumu")
        print("a.menangis dan bersembunyi dilemari \nb.mengambil pisau dapur")
        x = (input("masukan opsi :"))
        if x == "a" :
            print("panik tak membantu, zombie menemukanmu dan kamu menjadi salah satu dari mereka")
        elif x == "b" :
            print("kamu bersiap membantai zombie-zombie itu dengan pisaumu")
            print("zombie masuk dan bersiap menerkammu!!")
            print("a.tetap bersikap tenang dan mencari titik lemah zombie \nb.sadar diri dengan kalah jumlah lalu pergi ke luar jendela dan memanjat balkon tetangga")
            y = (input("masukan opsimu :"))
            if y == "a" :
                print("serang bagian \na.leher \nb.kepala")
                o = (input("masukan opsi :"))
                if o == "a" :
                    print("kamu mengenai nadi zombie, zombie mengalami pendarahan parah dan mati")
                elif o == "b" :
                    print("pisaumu hanya menyangkut ke kepala si zombie dan kamu kehilangan senjatamu. para zombie mulai menggigit tubuhmu")
                else :
                    print("kamu terlalu bimbang dan zombie mulai menggigiti seluruh tubuhmu")
            elif y == "b" :
                print("kamu berhasil melompat ke balkon tetangga dan kabur dari ruanganmu yang penuh zombie")
            else :
                print("kamu terlalu bimbang mengambil keputusan sampai zombie datang mendobrak masuk dan memakanmu")
    elif v == "b" :
        print("suplaimu menghabis dan kamu mulai kelaparan")
    else :
        print("kamu menyerah pada takdirmu")
elif a == "b" :
    print("kamu akan keluar rumah, apa yang akan kamu bawa sebagai perlengkapan? \na.pakaian-pakaian dan makanan ringan, minuman perisa dan air, dan tongkat baseball \nb.kain secukupnya, makanan ringan, air putih, dan pisau")
    q = (input("apa yang akan kamu bawa? "))
    print("kamu pergi membawa suplai pilihanmu")
    print("setelah beberapa waktu kamu mengembara bertahan hidup. suatu hari, kamu melihat ada seseorang yang terpojokkan oleh para zombie. \na.bantu dia \nb.menyelamatkan diri")
    z = (input("pilih opsi anda: "))
    if z == "a" :
        print("kamu menggunakan senjatamu untuk menyerang zombie, orang itu ikut membantumu dalam penyerangan. Kalian pun menjadi sahabat / partner in crime")
    elif z == "b" :
        print("dari kejauhan, kamu bisa melihat orang itu telah dicabik-cabik oleh zombie")
    else : 
        print("kamu hanya melongo menatap dia tercabik-cabik zombie")
else :
    print("kamu kebingungan sampai akhirnya hanya mati membusuk di dalam rumah")