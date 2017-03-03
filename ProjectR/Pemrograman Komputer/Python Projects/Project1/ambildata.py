import http.client
import json
 
asal = input('Kota Asal : ')
tujuan = input('Kota Tujuan : ')
berat = int(input('Berat (Gram) : '))
jasa = int(input('1.TIKI 2.JNE 3.POS (Tekan Angka) :'))
 
list_kota = ["Aceh Barat","Aceh Barat Daya","Aceh Besar","Aceh Jaya","Aceh Selatan",
			 "Aceh Singkil","Aceh Tamiang","Aceh Tengah","Aceh Tenggara","Aceh Timur",
			 "Aceh Utara","Agam","Alor","Ambon","Asahan","Asmat","Badung","Balangan",
			 "Balikpapan","Banda Aceh","Bandar Lampung","Bandung","Bandung",
			 "Bandung Barat","Banggai","Banggai Kepulauan","Bangka","Bangka Barat",
			 "Bangka Selatan","Bangka Tengah","Bangkalan","Bangli","Banjar","Banjar",
			 "Banjarbaru","Banjarmasin","Banjarnegara","Bantaeng","Bantul",
			 "Banyuasin","Banyumas","Banyuwangi","Barito Kuala","Barito Selatan",
			 "Barito Timur","Barito Utara","Barru","Batam","Batang",
			 "Batang Hari","Batu","Batu Bara","Bau-Bau","Bekasi",
			 "Bekasi","Belitung","Belitung Timur","Belu","Bener Meriah",
			 "Bengkalis","Bengkayang","Bengkulu","Bengkulu Selatan","Bengkulu Tengah",
			 "Bengkulu Utara","Berau","Biak Numfor","Bima","Bima",
			 "Binjai","Bintan","Bireuen","Bitung","Blitar",
			 "Blitar","Blora","Boalemo","Bogor","Bogor",
			 "Bojonegoro","Bolaang Mongondow (Bolmong)","Bolaang Mongondow Selatan","Bolaang Mongondow Timur","Bolaang Mongondow Utara",
			 "Bombana","Bondowoso","Bone","Bone Bolango","Bontang",
			 "Boven Digoel","Boyolali","Brebes","Bukittinggi","Buleleng",
			 "Bulukumba","Bulungan (Bulongan)","Bungo","Buol","Buru",
			 "Buru Selatan","Buton","Buton Utara","Ciamis","Cianjur",
			 "Cilacap","Cilegon","Cimahi","Cirebon","Cirebon",
			 "Dairi","Deiyai (Deliyai)","Deli Serdang","Demak","Denpasar",
			 "Depok","Dharmasraya","Dogiyai","Dompu","Donggala",
			 "Dumai","Empat Lawang","Ende","Enrekang","Fakfak",
			 "Flores Timur","Garut","Gayo Lues","Gianyar","Gorontalo",
			 "Gorontalo","Gorontalo Utara","Gowa","Gresik","Grobogan",
			 "Gunung Kidul","Gunung Mas","Gunungsitoli","Halmahera Barat","Halmahera Selatan",
			 "Halmahera Tengah","Halmahera Timur","Halmahera Utara","Hulu Sungai Selatan","Hulu Sungai Tengah",
			 "Hulu Sungai Utara","Humbang Hasundutan","Indragiri Hilir","Indragiri Hulu","Indramayu",
			 "Intan Jaya","Jakarta Barat","Jakarta Pusat","Jakarta Selatan","Jakarta Timur",
			 "Jakarta Utara","Jambi","Jayapura","Jayapura","Jayawijaya",
			 "Jember","Jembrana","Jeneponto","Jepara","Jombang",
			 "Kaimana","Kampar","Kapuas","Kapuas Hulu","Karanganyar",
			 "Karangasem","Karawang","Karimun","Karo","Katingan",
			 "Kaur","Kayong Utara","Kebumen","Kediri","Kediri",
			 "Keerom","Kendal","Kendari","Kepahiang","Kepulauan Anambas",
			 "Kepulauan Aru","Kepulauan Mentawai","Kepulauan Meranti","Kepulauan Sangihe","Kepulauan Seribu",
			 "Kepulauan Siau Tagulandang Biaro (Sitaro)","Kepulauan Sula","Kepulauan Talaud","Kepulauan Yapen (Yapen Waropen)","Kerinci",
			 "Ketapang","Klaten","Klungkung","Kolaka","Kolaka Utara",
			 "Konawe","Konawe Selatan","Konawe Utara","Kotabaru","Kotamobagu",
			 "Kotawaringin Barat","Kotawaringin Timur","Kuantan Singingi","Kubu Raya","Kudus",
			 "Kulon Progo","Kuningan","Kupang","Kupang","Kutai Barat",
			 "Kutai Kartanegara","Kutai Timur","Labuhan Batu","Labuhan Batu Selatan","Labuhan Batu Utara",
			 "Lahat","Lamandau","Lamongan","Lampung Barat","Lampung Selatan",
			 "Lampung Tengah","Lampung Timur","Lampung Utara","Landak","Langkat",
			 "Langsa","Lanny Jaya","Lebak","Lebong","Lembata",
			 "Lhokseumawe","Lima Puluh Koto/Kota","Lingga","Lombok Barat","Lombok Tengah",
			 "Lombok Timur","Lombok Utara","Lubuk Linggau","Lumajang","Luwu",
			 "Luwu Timur","Luwu Utara","Madiun","Madiun","Magelang",
			 "Magelang","Magetan","Majalengka","Majene","Makassar",
			 "Malang","Malang","Malinau","Maluku Barat Daya","Maluku Tengah",
			 "Maluku Tenggara","Maluku Tenggara Barat","Mamasa","Mamberamo Raya","Mamberamo Tengah",
			 "Mamuju","Mamuju Utara","Manado","Mandailing Natal","Manggarai",
			 "Manggarai Barat","Manggarai Timur","Manokwari","Manokwari Selatan","Mappi",
			 "Maros","Mataram","Maybrat","Medan","Melawi",
			 "Merangin","Merauke","Mesuji","Metro","Mimika",
			 "Minahasa","Minahasa Selatan","Minahasa Tenggara","Minahasa Utara","Mojokerto",
			 "Mojokerto","Morowali","Muara Enim","Muaro Jambi","Muko Muko",
			 "Muna","Murung Raya","Musi Banyuasin","Musi Rawas","Nabire",
			 "Nagan Raya","Nagekeo","Natuna","Nduga","Ngada",
			 "Nganjuk","Ngawi","Nias","Nias Barat","Nias Selatan",
			 "Nias Utara","Nunukan","Ogan Ilir","Ogan Komering Ilir","Ogan Komering Ulu",
			 "Ogan Komering Ulu Selatan","Ogan Komering Ulu Timur","Pacitan","Padang","Padang Lawas",
			 "Padang Lawas Utara","Padang Panjang","Padang Pariaman","Padang Sidempuan","Pagar Alam",
			 "Pakpak Bharat","Palangka Raya","Palembang","Palopo","Palu",
			 "Pamekasan","Pandeglang","Pangandaran","Pangkajene Kepulauan","Pangkal Pinang",
			 "Paniai","Parepare","Pariaman","Parigi Moutong","Pasaman",
			 "Pasaman Barat","Paser","Pasuruan","Pasuruan","Pati",
			 "Payakumbuh","Pegunungan Arfak","Pegunungan Bintang","Pekalongan","Pekalongan",
			 "Pekanbaru","Pelalawan","Pemalang","Pematang Siantar","Penajam Paser Utara",
			 "Pesawaran","Pesisir Barat","Pesisir Selatan","Pidie","Pidie Jaya",
			 "Pinrang","Pohuwato","Polewali Mandar","Ponorogo","Pontianak",
			 "Pontianak","Poso","Prabumulih","Pringsewu","Probolinggo",
			 "Probolinggo","Pulang Pisau","Pulau Morotai","Puncak","Puncak Jaya",
			 "Purbalingga","Purwakarta","Purworejo","Raja Ampat","Rejang Lebong",
			 "Rembang","Rokan Hilir","Rokan Hulu","Rote Ndao","Sabang",
			 "Sabu Raijua","Salatiga","Samarinda","Sambas","Samosir",
			 "Sampang","Sanggau","Sarmi","Sarolangun","Sawah Lunto",
			 "Sekadau","Selayar (Kepulauan Selayar)","Seluma","Semarang","Semarang",
			 "Seram Bagian Barat","Seram Bagian Timur","Serang","Serang","Serdang Bedagai",
			 "Seruyan","Siak","Sibolga","Sidenreng Rappang/Rapang","Sidoarjo",
			 "Sigi","Sijunjung (Sawah Lunto Sijunjung)","Sikka","Simalungun","Simeulue",
			 "Singkawang","Sinjai","Sintang","Situbondo","Sleman",
			 "Solok","Solok","Solok Selatan","Soppeng","Sorong",
			 "Sorong","Sorong Selatan","Sragen","Subang","Subulussalam",
			 "Sukabumi","Sukabumi","Sukamara","Sukoharjo","Sumba Barat",
			 "Sumba Barat Daya","Sumba Tengah","Sumba Timur","Sumbawa","Sumbawa Barat",
			 "Sumedang","Sumenep","Sungaipenuh","Supiori","Surabaya",
			 "Surakarta (Solo)","Tabalong","Tabanan","Takalar","Tambrauw",
			 "Tana Tidung","Tana Toraja","Tanah Bumbu","Tanah Datar","Tanah Laut",
			 "Tangerang","Tangerang","Tangerang Selatan","Tanggamus","Tanjung Balai",
			 "Tanjung Jabung Barat","Tanjung Jabung Timur","Tanjung Pinang","Tapanuli Selatan","Tapanuli Tengah",
			 "Tapanuli Utara","Tapin","Tarakan","Tasikmalaya","Tasikmalaya",
			 "Tebing Tinggi","Tebo","Tegal","Tegal","Teluk Bintuni",
			 "Teluk Wondama","Temanggung","Ternate","Tidore Kepulauan","Timor Tengah Selatan",
			 "Timor Tengah Utara","Toba Samosir","Tojo Una-Una","Toli-Toli","Tolikara",
			 "Tomohon","Toraja Utara","Trenggalek","Tual","Tuban",
			 "Tulang Bawang","Tulang Bawang Barat","Tulungagung","Wajo","Wakatobi",
			 "Waropen","Way Kanan","Wonogiri","Wonosobo","Yahukimo",
			 "Yalimo","Yogyakarta"]
 
origin_id = list_kota.index(asal) + 1;
dest_id = list_kota.index(tujuan) + 1;
str_jasa = ""
 
if jasa == 1:
	str_jasa = "tiki"
elif jasa == 2:
	str_jasa = "jne"
elif jasa == 3:
	str_jasa = "pos"
 
 
conn = http.client.HTTPConnection("rajaongkir.com")
 
payload = "origin="+str(origin_id)+"&amp;destination="+str(dest_id)+"&amp;weight="+str(berat)+"&amp;courier="+str_jasa
 
headers = {
    'key': "ca818097e5881aea40a3f8cffbd07a52",
    'content-type': "application/x-www-form-urlencoded"
    }
 
conn.request("POST", "/api/starter/cost", payload, headers)
 
rawreply = conn.getresponse().read()
reply = json.loads(rawreply.decode())
 
hasil = reply['rajaongkir']['results']
print("Pengiriman Dari :",reply['rajaongkir']['origin_details']['city_name'],
	  " Ke :",reply['rajaongkir']['destination_details']['city_name'],
	  " Berat :",reply['rajaongkir']['query']['weight'],"Gram")
for item1 in hasil:
	print("JASA :",item1['name'])
	hasil2 = item1['costs']
	for item2 in hasil2:
		str_out = 'Layanan : '
		str_out += item2['service']
		hasil3 = item2['cost']
		for item3 in hasil3:
			str_out += ' Harga : Rp.'
			str_out += str(item3['value'])
			print(str_out)
