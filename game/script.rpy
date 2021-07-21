
# Charrr
define a = Character("Mirai")
define b = Character("Ibu")
define anon = Character("???")
define mc = Character("[name]")
define c = Character("Pak Karwo")


# image charr mc
image mc kaget kasual = "mc kaget kasual.png"
image mc marah1 kasual = "mc marah1 kasual.png"
image mc ketawa kasual = "mc ketawa kasual.png"
image mc senyum3 kasual = "mc senyum3 kasual.png"
image mc senyum1 kasual = "mc senyum1 kasual.png"
image mc netral kasual = "mc netral kasual.png"
image mc ketawa spesial = "mc ketawa spesial.png"
image mc normal spesial = "mc normal spesial.png"
image mc senyum2 spesial = "mc senyum2 spesial.png"
image mc senyum3 spesial = "mc senyum3 spesial.png"
image mc senyum1 hodie = "mc senyum1 hodie.png"
image mc curiga hodie = "mc curiga hodie.png"
image mc senyum3 hodie = "mc senyum3 hodie.png"
image mc senyum2 hodie = "mc senyum2 hodie.png"
image mc sedih hodie = "mc sedih hodie.png"
image mc netral hodie = "mc netral hodie.png"
image mc ketawa hodie = "mc ketawa hodie.png"

# image charr Mirai
image Mirai jengkel kasual = "Mirai jengkel kasual.png"
image Mirai marah kasual = "Mirai marah kasual.png"
image Mirai netral hodie = "Mirai netral hodie.png"
image Mirai curiga hodie = "Mirai curiga hodie.png"
image Mirai delighted hodie = "Mirai delighted hodie.png"
image Mirai senyum hodie = "Mirai senyum hodie.png"
image Mirai senyum2 hodie = "Mirai senyum2 hodie.png"
image Mirai kaget hodie = "Mirai kaget hodie.png"
image Mirai jengkel hodie = "Mirai jengkel hodie.png"
image Mirai marah hodie = "Mirai marah hodie.png"


# image charr Ibukk
image ibuk ngomong = "ibuk ngomong.png"
image ibuk ngomong2 = "ibuk ngomong2.png"
image ibuk senyum = "ibuk senyum.png"

# char teuchi
image Teuchi = "Teuchi.png"

# bg
image bg dark = "dark.jpg"
image bg kamar = "room_morning_light_off.jpg"
image bg Rtengah = "livingroom.jpg"
image bg jalan = "streetbudal.jpg"
image bg pasar = "market.jpg"
image bg toko = "dalemtoko.jpg"
image bg jalan2 = "jalan.jpg"
image bg parkir = "parkir.jpg"
image bg eskrim1 = "icecream.jpg"
image bg eskrim2 = "toko_eskrim.jpg"


# items
image soal1 = "soal kecepatan.png"
image pilihan kecepatan1 = "pilihan kecepatan1.png"
image pilihan kecepatan2 = "pilihan kecepatan2.png"
image pilihan kecepatan3 = "pilihan kecepatan3.png"
image jawaban1 = "jawaban kecepatan.png"
image soal2 = "Soal pythagoras.png"
image jawaban2 = "Jawaban pythagoras.png"
image catatan belanja = "List belanja.png"
image hargakilo = "list belanja harga.png"
image eskrimtabung = "eskrimtabung.png"
image eskrimbulat = "eskrimbulat.png"
image eskrimkerucut = "eskrimkerucut.png"
image eskrimbalok = "eskrimbalok.png"
image eskrimgj = "eskrimgj.png"
image jawabbola= "jawabbola.jpg"
image jawabtabung = "jawabtabung.png"
image jawabkerucut = "jawabkerucut.jpg"
image jawaball = "jawaball.jpg"

# The game starts here.

label start:

    play sound "footstep_stairs.mp3"
    "......."
    "Suara langkah kaki terdengar di telingaku"
    play sound "room_door_O.mp3"
    play music "room.mp3"
    "Suara pintu terbuka"
    anon "..Ak.....Ngun..."
    anon "..Ak.....Bangun.."
    "Suara halus tersebut menyeru dengan semakin jelas"
    a "Kak...Bangun Kak!!!!"
    python:
        name = renpy.input("Masukkan Nama Anda")
        name = name.strip() or "Achsan"
    scene bg kamar
    show mc kaget kasual at left
    mc "UWAAH!!!"
    hide mc kaget kasual 
    "Dari suara tersebut aku pun hampir jatuh dari kasur"
    show mc marah1 kasual at left
    mc "Aduhhh.....deeek kalo mau bangunin jangan teriak di dekat telinga kakak juga dong"
    show Mirai jengkel kasual at right
    a "Yaaa habis kakak dibangunin ngga bangun bangun juga, kan adek sudah tidak ada cara lagi buat bangunin lagi"
    hide mc marah1 kasual
    show mc ketawa kasual at left
    mc "Memangnya jam berapa sih sekarang?"
    hide Mirai jengkel kasual
    show Mirai marah kasual at right
    a "Kakak liat sendiri aja disitu"
    hide Mirai marah kasual
    hide mc ketawa kasual
    "Akupun melihat jam yang ada di dinding"
    show mc kaget kasual at left
    mc " HAAAAAHHHHHHH!!!!"
    hide mc kaget kasual
    "Dan ternyata saat aku melihat jam di dinding waktu sudah menunjukkan pukul 11 siang"
    show Mirai marah kasual at right
    a "Hahhh....kakak bagaimana sihh di siang bolong begini masih tidur saja ayo turun sana sarapan dulu, yaa harusnya makan siang sihh"
    show mc senyum3 kasual at left
    mc "Ahh iya iyaa sebentar nanti kakak nyusul"
    hide mc senyum3 kasual
    hide Mirai marah kasual
    "Mirai pun menutup pintu kembali dan segera turun ke lantai bawah"
    show mc netral kasual at left
    mc "Hmm perasaan ku sudah menyalakan weker dehh...."
    hide mc netral kasual
    "Aku pun mengingat kembali hari kemarin sebelum tidur"
    show mc netral kasual at left
    mc "Yaa sudahlah saatnya ganti baju dan bersiap siap untuk turun"
    hide mc netral kasual
    play sound "scratching.mp3"
    "Akupun mengganti bajuku yang kotor"
    "Aku menuju pintu untuk keluar kamarku"
    play sound "room_door_O.mp3"
    "Suara pintu terbuka"
    play sound "room_door_C.mp3"
    "Pintu pun aku tutup kembali dan segera turun tangga untuk ke lantai bawah"
    "Dan ternyata dibawah sudah ada yang memanggil"
    stop music
    

    scene bg Rtengah
    
    play music "tengah.mp3"
    anon "Aduuuhh....kamu ini kemarin tidur jam berapa sih kok baru bangun sekarang?"
    "Dan baru bangun ini sudah terkena marahan dari Ibu"
    show mc ketawa spesial at left
    mc "iyaa maaf bu soalnya aku kemarin belajar, dan ternyata lupa waktu dan tidur sudah larut malam"
    show ibuk ngomong at right
    b "Yaa sudah kamu makan dulu sana nanti keburu tambah dingin lagi itu makanan"
    hide mc ketawa spesial
    hide ibuk ngomong
    play sound "pulling_back_a_chair.mp3"
    "Dan aku pun mulai meranjak ke meja makan dan menarik kursi makan tersebut"
    "Makanan yang ada di meja mulai aku santap"
    show ibuk ngomong at right
    b "Ahh sepertinya aku harus kepasar tapi sebentar lagi aku ada keperluan"
    hide ibuk ngomong 
    show ibuk senyum at right
    b "Kalo begitu, [name] tolong nanti belikan bahan bahan makanan yang kurang ini yaa... ibu sudah catat bahannya di buku daftar belanjaan diatas meja ruang keluarga"
    b "Nanti kamu ambil bukunya nahh uangnya sudah ada didalam bukunya yaa, nanti ajak adek juga ya kasian kalo sendirian dirumah"
    show mc ketawa spesial at left
    mc "Ahh memangnya nanti ibu mau kemana?"
    hide ibuk senyum
    show ibuk ngomong2 at right
    b "Ibu mau rapat sama warga warga perumahan sebentar saja"
    b "Kalo Adek kamu ikut beliin eskrim kesukaannya ya.. dari kemaren minta eskrim"
    mc "Baik bu, kalau begitu saya mau mandi dulu setelah itu saya akan berangkat ke pasar"
    hide mc ketawa spesial
    hide ibuk ngomong2
    "Setelah beberapa saat....."
    show Mirai netral hodie at right
    a "Kak, Ibu pergi kemana kok aku cariin tidak ada dirumah?"
    show mc normal spesial at left
    mc "Ohh, Ibu pergi rapat sama warga warga perumahan"
    a "yaahh, makanya aku cariin kok gaada.. "
    hide Mirai netral hodie
    show Mirai curiga hodie at right
    a "Eh, Kakak mau kemana? kok tumben rapi"
    hide mc normal spesial
    show mc senyum2 spesial at left
    mc "Ohhh, Kakak mau pergi ke pasar beliin daftar belanjanya mama, ayo adek ikut temenin kakak ke pasar.. nanti aku beliin eskrim deh.."
    hide Mirai curiga hodie
    show Mirai delighted hodie at right
    a "wahhh, eskrim???... "
    hide Mirai delighted hodie
    show Mirai senyum hodie at right
    a "Mau.... mau...."
    hide Mirai senyum hodie
    hide mc senyum2 spesial
    show Mirai senyum2 hodie at right
    show mc senyum3 spesial at left
    mc "Ayo kalo gitu kita berangkat sekarang..."
    stop music

label berangkat:
    play music "mbaleh.mp3"
    scene bg jalan
    show mc senyum1 hodie at left
    mc "Ayo dek sini aku boncengin make sepedamotor ya.."
    show Mirai delighted hodie at right
    a "Iya kak.." 
    hide Mirai delighted hodie
    show Mirai netral hodie at right
    a "tapi kalo berangkat sekarang lalu sampe pasar kira-kira jam berapa ya?"
    hide Mirai netral hodie
    show soal1:
        xalign 0.8 yalign 0.3
    hide mc senyum1 hodie

    show mc senyum1 hodie at left
    mc "eh iya, sekarang jam 11.30 kakak biasanya mengendarai di kecepatan 60 Km/Jam dan jarak dari rumah ke pasar 15Km, kira-kira jam berapa ya sampai pasar?"
    hide mc senyum1 hodie
    show mc curiga hodie at left
    mc "hmmm sebaiknya kuhitung dulu.."
    
    hide soal1
    menu:
        #insert soal kecepatan
        "sekarang jam 11.30 kalo berkendara 60 Km/Jam dan jarak dari rumah ke pasar 15Km, kira-kira jam berapa ya sampai pasar?"
        
        "Kurang lebih jam 11.40 sih dek.\n{image=pilihan kecepatan1.png}":
            jump jawabanjalan1_salah    

        "Kurang lebih jam 11.45 sih dek.\n{image=pilihan kecepatan2.png}":
            jump jawabanjalan1_benar
        
        "Kurang lebih jam 11.50 sih dek.\n{image=pilihan kecepatan3.png}":
            jump jawabanjalan1_salah


    label jawabanjalan1_benar:

        $ menu_flag = True
        hide mc curiga hodie
        show mc senyum3 hodie at left
        show jawaban1:
            xalign 0.8 yalign 0.3
    
        "Yaa benar aku ingat ini salah satu pelajaran di matematika sekolahku, ini memakai rumus t= S/v "
        "Waktu = Jarak / Kecepatan"
        mc "Kira-kira kita sampai sana jam 11.15 dek.."

        hide jawaban1
        jump jawabanjalan1_selesai

    label jawabanjalan1_salah:

        $ menu_flag = False
        show mc sedih hodie at left
        "Hmmm sepertinya salah deh ini,, coba ku hitung lagi dengan lebih teliti.. Ini kan seperti pelajaran disekolahku.."
        hide mc sedih hodie
        show mc curiga hodie at left
        menu:
            
            "sekarang jam 11.30 kakak biasanya mengendarai di kecepatan 60 Km/Jam dan jarak dari rumah ke pasar 15Km, kira-kira jam berapa ya sampai pasar?"
        
            "Kurang lebih jam 11.40 sih dek.\n{image=pilihan kecepatan1.png}":
                jump jawabanjalan1_salah    

            "Kurang lebih jam 11.45 sih dek.\n{image=pilihan kecepatan2.png}":
                jump jawabanjalan1_benar
            
            "Kurang lebih jam 11.50 sih dek.\n{image=pilihan kecepatan3.png}":
                jump jawabanjalan1_salah



    label jawabanjalan1_selesai:
    hide mc senyum3 hodie
    show mc senyum2 hodie at left
    mc "Baik dek ayo naik..."
    show Mirai senyum2 hodie at right
    a "Iya kak..."
    hide Mirai senyum2 hodie
    hide mc senyum2 hodie
    scene dark
    stop music

label perjalanan:
    play music "perjalanan.mp3"
    "Lalu kami pun berangkat ke pasar dengan berboncengan"
    scene bg jalan2
    "Tiba-tiba di perjalanan adekku bertanya.."
    show Mirai netral hodie at right
    show soal2:
        xalign 0.5 yalign 0.2 
    a "Kak, kira-kira jarak antara rumah langsung dengan pasar kalau tidak melewati jalan raya berapa ya?"
    hide Mirai netral hodie

    "Aku pun sempat berpikiran,ternyata adek saya kelewat pintar . Pertanyaannya pun bukan kaleng-kaleng "
    "Lalu karena dijalan raya harus fokus maka aku hanya mengingat materi matematika yang cocok untuk pertanyaan adekku tersebut"
    show mc senyum3 hodie at left
    mc "Sebentar ya dek, nanti kalau di parkiran pasar aku jawab yaa"
    hide mc senyum3 hodie
    hide soal2
    scene dark
    "saat sampai diparkiran pasar"
    scene bg parkir
    
    show mc curiga hodie at left
    show soal2:
        xalign 0.5 yalign 0.2 
    mc "hmmmm... berapa ya?"

    menu:
        #insert soal kecepatan
        "kira-kira jarak antara rumah langsung dengan pasar kalau tidak melewati jalan raya berapa ya?"
        
        "Kurang lebih 7.5 Km sih dek.":
            jump jawabanjalan2_salah    

        "Kurang lebih 9 Km sih dek.":
            jump jawabanjalan2_salah
        
        "Kurang lebih 11 km sih dek.":
            jump jawabanjalan2_benar

        "Tetap 15 Km sih dek.":
            jump jawabanjalan2_salah

    label jawabanjalan2_benar:

        $ menu_flag = True
        hide mc curiga hodie
        show mc senyum3 hodie at left
        show jawaban2:
            xalign 0.5 yalign 0.0
    
        "Yaa benar aku ingat ini salah satu pelajaran di matematika sekolahku, ini memakai Teorema Pythagoras."
        "Seharusnya memakai vektor, tapi karena kebetulan sudut antar rumahku dan pertigaan ujung pasar siku-siku jadi bisa memakai Teorema Pythagoras"

        hide jawaban2
        jump jawabanjalan2_selesai

    label jawabanjalan2_salah:

        $ menu_flag = False
        show mc sedih hodie at left
        "Hmmm sepertinya salah deh ini,, coba ku hitung lagi dengan lebih teliti.. Ini kan seperti pelajaran disekolahku.."
        hide mc sedih hodie
        show mc curiga hodie at left
        menu:
            "kira-kira jarak antara rumah langsung dengan pasar kalau tidak melewati jalan raya berapa ya?"
            "Kurang lebih 7.5 Km sih dek.":
                jump jawabanjalan2_salah    

            "Kurang lebih 9 Km sih dek.":
                jump jawabanjalan2_salah
            
            "Kurang lebih 11 km sih dek.":
                jump jawabanjalan2_benar

            "Tetap 15 Km sih dek.":
                jump jawabanjalan2_salah


    label jawabanjalan2_selesai:
    hide soal2
    show mc netral hodie at left
    mc "Ehh iya dek adek tadi kan tanya yaa jarak antara rumah langsung dengan pasar kalau tidak melewati jalan raya berapa..."
    hide mc netral hodie
    show mc senyum3 hodie at left
    mc "Nahh.. jadi jarak antara rumah langsung dengan pasar kalau tidak melewati jalan raya itu kurang lebih 11 Km"
    hide mc senyum3 hodie
    show Mirai delighted hodie at right
    a "Wahh kakak pinter banget yaa bisa hitung hitung seperti itu.."
    show mc ketawa hodie at left
    mc "yahh makanya kalo sekolah belajar yang rajin yaa biar bisa seperti kakak"
    show Mirai senyum2 hodie at right
    a "Wahh iya kak, aku jadi semakin semangat sekolah"
    hide mc ketawa hodie
    show mc senyum3 hodie at left
    mc "Hehe.. iya deh,, ayo sekarang beli yang disuruh mama tadi.."
    hide Mirai senyum2 hodie
    show Mirai senyum hodie at right
    a "Iya kak"
    hide Mirai senyum hodie
    hide mc senyum3 hodie
    scene dark
    "Setelah itu aku pun mengunci sepedamotor di parkiran pasar dan menuju ke wilayah pasar"
    stop music

label pasar:
    play music "shop.mp3"
    "Saat sampai di pasar"

    scene bg pasar
    show Mirai kaget hodie at right
    a "Wahh kakak liat besar banget ya pasarnya.."
    hide Mirai kaget hodie
    show Mirai jengkel hodie at right
    a "Kakak jangan lupa sama eskrimku yaa"
    show mc senyum3 hodie at left
    mc "iya dek, tenang saja pasti kakak beliin kok"
    hide mc senyum3 hodie
    hide Mirai jengkel hodie
    "Lalu akupun melihat daftar belanja dari Ibuku"

    show catatan belanja:
        xalign 0.5 yalign 0.4

    show mc netral hodie at left
    mc "Hmmm ternyata cuma bawa uang 100Ribu, kira kira cukup gk ya?.. nanti juga beliin adek Eskrim 5ribu"
    hide mc netral hodie
    show mc curiga hodie at left
    mc "Wahh ini seperti matematika yang diajarkan di sekolah"
    mc "hmmm pertama... kita harus ke penjualnya dulu untuk tanya harga"
    hide mc curiga hodie

    "Setelah sampai dilapak Pak karwo..."
    
    scene bg toko
    show Teuchi at right
    c "Wahh adek-adek ke pasar mau beli apa nih?"
    show mc ketawa hodie at left
    mc "Anu pak mau nanya harga dulu"
    c "Oohh begituu.. oke deh silahkan tanya harga dulu..."
    hide mc ketawa hodie
    show mc senyum3 hodie at left
    mc "Baik Pak, ini Harga Gula 1kg brp ya.."
    c "Ohh harga Gula 1kg nya Rp 13.000,00"
    hide mc senyum3 hodie
    show mc ketawa hodie at left
    mc "Kalau harga Telur 1kg berapa pak?"
    c "Kalau Telur 1kg nya Rp 24.000,00"
    hide mc ketawa hodie
    show mc senyum3 hodie at left
    mc "oke pak, kalau Apel merah nya 1kg berapa?"
    c "Apel merahnya 1kg Rp 40.000,00"
    hide mc senyum3 hodie
    show mc ketawa hodie at left
    mc "sebentar ya pak, saya hitung dulu takutnya uangnya kurang..."
    c "Ohh, kalau gitu saya tunggu ya dek"
    mc "iya pak, sebentar yaa.."
    hide mc curiga hodie at left
    hide Teuchi
    show hargakilo
    "Hmmm saya harus hitung nih... jadi totalnya..."

    menu:
        "Gula 1kg = Rp 13.000,00 \nTelur 1kg = Rp 24.000,00   \nApel merah 1kg = Rp 40.000,00"
        "Jadi totalnya Rp 72.000,00 ":
            jump jawabanpasar1_salah

        "Jadi totalnya Rp 82.000,00":
            jump jawabanpasar1_salah

        "Jadi totalnya Rp 92.000,00":
            jump jawabanpasar1_benar

        "Uangnya kurang.":
            jump jawabanpasar1_salah
        
    label jawabanpasar1_benar:

        $ menu_flag = True
        hide mc curiga hodie
        show mc senyum3 hodie at left
        hide hargakilo
        show catatan belanja:
            xalign 0.7 yalign 0.4
        "Jadi totalnya Rp 92.000,00"
        
        mc "Iya pak ini sesuai catatan yaa.."
        hide mc senyum3 hodie

        jump jawabanpasar1_selesai

    label jawabanpasar1_salah:
        
        
        $ menu_flag = False
        show mc sedih hodie at left
        "Hmmm sepertinya salah deh ini,, coba ku hitung lagi dengan lebih teliti.. Ini kan seperti pelajaran disekolahku.."
        hide mc sedih hodie
        
        menu:
            "Gula 1kg = Rp 13.000,00 \nTelur 1kg = Rp 24.000,00   \nApel merah 1kg = Rp 40.000,00"
            "Jadi totalnya Rp 72.000,00 ":
                jump jawabanpasar1_salah

            "Jadi totalnya Rp 82.000,00":
                jump jawabanpasar1_salah

            "Jadi totalnya Rp 92.000,00":
                jump jawabanpasar1_benar

            "Uangnya kurang.":
                jump jawabanpasar1_salah


    label jawabanpasar1_selesai:

        # ... the game continues here.
    "Setelah beberapa saat"
    show mc senyum3 hodie at left
    mc "Wahh iya pak, jadi beli sesuai catetan lalu lomboknya Rp 3.000,00 ya pak.."
    hide mc senyum3 hodie
    show Teuchi at right
    c "Oke siapp dek.."
    hide Teuchi
    show mc senyum2 hodie at left
    mc "Ok pak, sudah semua nih, Terimakasih ya pak.."
    hide mc senyum2 hodie
    show Teuchi at right
    c "Iya sama-sama dek [name]"
    hide Teuchi
    "Setelah kami membeli sayur dan buah, kami pun berjalan menuju toko eskrim untuk membeli eskrim adek"
    stop music
label eskrimm:
    play music "Cream.mp3"
    scene bg eskrim1
    "Saat di depan toko eskrim"
    show Mirai delighted hodie at right 
    a "Wahh nyampek juga kak di toko eskrim "
    show mc ketawa hodie at left
    mc "Hehe iya dek.."
    hide mc ketawa hodie
    show mc netral hodie at left
    mc "Oh iya ngomong ngomong nanti kamu pengen eskrim yang kayak apa?"
    hide Mirai delighted hodie
    show Mirai netral hodie at right
    a "liat liat dulu deh kak"
    hide Mirai netral hodie
    show Mirai senyum2 hodie at right
    a "ayo masuk saja biar bisa milih"
    hide mc netral hodie
    show mc senyum1 hodie at left
    mc "Baik dek"
    hide mc senyum1 hodie
    hide Mirai senyum2 hodie
    
    scene bg eskrim2
    show mc senyum3 hodie at left
    mc "Nahh ayo pilih rasa apa dek?"
    show Mirai senyum2 hodie at right
    a "hmmm... Terserah.."
    hide mc senyum3 hodie
    hide Mirai senyum2 hodie
    "Haduh dasar cewek selalu terserah"
    show mc senyum1 hodie at left
    mc "Oke dehh, kalo gitu pertama.. bentuknya pengen apa?"
    show Mirai netral hodie at right
    a "hmm.. apa yaa"
    hide mc senyum1 hodie
    show mc senyum2 hodie at left
    mc "Gini deh.. aku sebutin bentuk-bentuk eskrimnya..."
    hide mc senyum2 hodie
    hide Mirai netral hodie 
    "Ini seperti bentuk bangun ruang di matematika"
    "Mana Eskrim yang berbentuk Bola?"
    menu:
        "{image=eskrimbulat.png}":
            jump jawabaneskrim1_benar
        "{image=eskrimtabung.png}":
            jump jawabaneskrim1_salah
        "{image=eskrimkerucut.png}":
            jump jawabaneskrim1_salah
    
    label jawabaneskrim1_benar:

        $ menu_flag = True
        hide mc curiga hodie
        show mc senyum3 hodie at left
        show jawabbola:
            xalign 0.8 yalign 0.1
    
        "Benar,, eskrim ini berbentuk Bola"
        hide jawabbola
        "Baik, sekarang eskrim mana yang berbentuk tabung? "
        menu:
            
            "{image=eskrimbalok.png}":
                jump jawabaneskrim2_salah
            "{image=eskrimkerucut.png}":
                jump jawabaneskrim2_salah
            "{image=eskrimtabung.png}":
                jump jawabaneskrim2_benar
        
        label jawabaneskrim2_benar:

        $ menu_flag = True
        hide mc curiga hodie
        show mc senyum3 hodie at left
        show jawabtabung:
            xalign 0.8 yalign 0.1
    
        "Benar,, eskrim ini berbentuk Tabung"

        hide jawabtabung
        "Baik, sekarang eskrim mana yang berbentuk Kerucut? "
        menu:
                
            "{image=eskrimbalok.png}":
                jump jawabaneskrim3_salah
            "{image=eskrimkerucut.png}":
                jump jawabaneskrim3_benar
            "{image=eskrimgj.png}":
                jump jawabaneskrim3_salah


        label jawabaneskrim3_salah:

        $ menu_flag = False
        show mc sedih hodie at left
        "Hmmm sepertinya salah deh ini,,  eskrim ini bukan berbentuk Kerucut"
        hide mc sedih hodie
        show mc curiga hodie at left
        menu:
                    
            "{image=eskrimbalok.png}":
                jump jawabaneskrim3_salah
            "{image=eskrimkerucut.png}":
                jump jawabaneskrim3_benar
            "{image=eskrimgj.png}":
                jump jawabaneskrim3_salah
                    
                    
        label jawabaneskrim3_benar:

        $ menu_flag = True
        hide mc curiga hodie
        show mc senyum3 hodie at left
        show jawabkerucut:
            xalign 0.8 yalign 0.1
                
        "Benar,, eskrim ini berbentuk Kerucut"

        hide jawabkerucut
        "Baik, Semua bentuk eskrim sudah selesai"
        
                    
        jump jawabaneskrim_selesai
        
        label jawabaneskrim2_salah:

        $ menu_flag = False
        show mc sedih hodie at left
        "Hmmm sepertinya salah deh ini,,  eskrim ini bukan berbentuk tabung"
        hide mc sedih hodie
        show mc curiga hodie at left
        menu:
            
            "{image=eskrimbalok.png}":
                jump jawabaneskrim2_salah
            "{image=eskrimkerucut.png}":
                jump jawabaneskrim2_salah
            "{image=eskrimtabung.png}":
                jump jawabaneskrim2_benar
        

    label jawabaneskrim1_salah:

        $ menu_flag = False
        show mc sedih hodie at left
        "Hmmm sepertinya salah deh ini,,  eskrim ini bukan berbentuk bola"
        hide mc sedih hodie
        show mc curiga hodie at left
        menu:
            
            "{image=eskrimbulat.png}":
                jump jawabaneskrim1_benar
            "{image=eskrimtabung.png}":
                jump jawabaneskrim1_salah
            "{image=eskrimkerucut.png}":
                jump jawabaneskrim1_salah

    label jawabaneskrim_selesai:
    hide mc senyum3 hodie
    show mc senyum2 hodie at left
    show jawaball:
        xalign 0.8 yalign 0.1
    mc "Baik dek jadi bentuknya eskrim disini ada 3 jenis, yakni Bola,Tabung dan Kerucut."
    show Mirai delighted hodie at right
    hide jawaball
    a "Wahh jadi ada tiga ya..."
    hide Mirai delighted hodie
    show Mirai senyum2 hodie at right
    a "Milih yang kerucut aja deh.."
    hide mc senyum2 hodie
    show mc senyum3 hodie at left
    mc "Okee, aku beliin dulu ya.. kamu tunggu disini"
    hide Mirai senyum2 hodie
    show Mirai senyum hodie at right
    a "Baik kak.."
    hide mc senyum3 hodie
    hide Mirai senyum hodie 

    scene dark
    "Setelah beberapa saat keluar dari toko.."
    scene bg eskrim1
    show mc senyum3 hodie at left
    mc "Ini dek, satu untuk adek, satu untuk kakak"
    show Mirai curiga hodie at right
    a "Lahh.. Katanya uangnya tadi cuma Rp.5000,00 ?"
    hide mc senyum3 hodie
    show mc ketawa hodie at left
    mc "Iya, tapi karena hari ini hari Valentine beli sama pasangan jadi beli 1 gratis 1"
    hide Mirai curiga hodie
    show Mirai jengkel hodie at right
    a "Lahh kan kita kakak sama adekkk.."
    hide mc ketawa hodie
    show mc senyum3 hodie at left
    mc "Jangan marah gitu dongg, kan lumayan gratis 1"
    hide Mirai jengkel hodie
    show Mirai marah hodie at right
    a "Iiihhh Kakak malu maluinn"
    hide mc senyum3 hodie
    show mc ketawa hodie at left 
    mc "Hahahahaha..."
    hide Mirai marah hodie
    hide mc ketawa hodie
    scene bg dark
    "Setelah itu Mirai pun keluar toko eskrim dengan kesal dan jalan di depanku"

    stop music
    call credits
    
    # This ends the game.

    label credits:
    $ credits_speed = 25 #scrolling speed in seconds
    scene black #replace this with a fancy background
    with dissolve
    show theend:
        yanchor 0.5 ypos 0.5
        xanchor 0.5 xpos 0.5
    with dissolve
    with Pause(3)
    hide theend
    show cred at Move((0.5, 5.0), (0.5, 0.0), credits_speed, repeat=False, bounce=False, xanchor="center", yanchor="bottom")
    with Pause(credits_speed)
    show thanks:
        yanchor 0.5 ypos 0.5
        xanchor 0.5 xpos 0.5
    with dissolve
    with Pause(3)
    hide thanks


    init python:
        credits = ('Pembuat :', 'Achsanudin Nursy'), ('Nim :', '19030174097'), ('Kelas :', '2019A'), ('Dosen Pengampu :', 'Cuddlywad'), ('Cerita :', 'Karangan Pembuat'), ('Programming :', 'Python')
        credits_s = "{size=80}Credits\n\n"
        z1 = ''
        for z in credits:
            if not z1==z[0]:
                credits_s += "\n{size=40}" + z[0] + "\n"
            credits_s += "{size=60}" + z[1] + "\n"
            z1=z[0]
        credits_s += "\n{size=40}Engine\n{size=60}Ren'py\n6.15.7.374" #Don't forget to set this to your Ren'py version
        
    init:
    #    image cred = Text(credits_s, font="myfont.ttf", text_align=0.5) #use this if you want to use special fonts
        image cred = Text(credits_s, text_align=0.5)
        image theend = Text("{size=80}To be Continue...", text_align=0.5)
        image thanks = Text("{size=80}Terimakasih! Jika ada perlu silahkan email: yggdra203@gmail.com ", text_align=0.5)

    return
