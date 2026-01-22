# for sikilini o'tamiz nima ma'nosi aylanma, ishlatilishi ketma-ketligi takrorlash ayanama deyiladi. for xuddi shu vazifani bajaradi
# for bizada funksiya hisoblanadi, bu funksiya ma'lum bir qiynatlarni o'zida saqliydi. hozirgi paytgachon misollarni
# for ichida misollar bajarilgani yaxshi chunki sifat oshadi va tezroq chiqarib beradi, xatolar darajasini pasaytirib beradi
# for shartni ham tekshiradi. isalgan saytdan ro'yxatdan o'tish qismida bu funksiyadan foydalaniladi
# misol parol kiritdiz lekin muammo bo'ldi funksiya nima qiladi qayta tepaga chiqadi yana boshqatdan yozishni boshliydi
# if elif else shartli operatorlarni yozganmiz "buna raqam chiqsa xatolik chiqsin" " agar bunaqa bo'lsa xatolik chiqsin", " bu ham xato"
# shunaqa yozuv qayta qayta chiqishi misol takrorlanishini bajaradi.
# MISOL

# noms = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]   #list ichida son kiritish, obyekt bo'yicha 1 dan boshlab saniydi. index bo'yicha 0 dan
#                                          #qo'shtirnoqqa olsam string bo'lib qoladi yani qiymati oddiy teksga aylanib qoladi. forda sikilda aylantitib ko'riladi
#
# for i in noms:
#     print(i * 2)                        #har bitta listga kiritilingan soni 2 ga ko'paytirdi. for funksiyasi hisoblash uchun bittadan borib kelib amaliyotni davom ettiradi
#                                         #nomsni i qiymatiga o'zgartirib olindi nega? sikilda o'zgartirish kerak ekanda, bu boshqa holatga o'tdi. fordan keyin yozilgan o'zgaruvchi forga teg bo'ladi. yani aylanadi. noms oddiy list ichida ma'lumoti bor halos
# range - bu qiymatni aylantirib beradi, xuddi gacha shundan shu gachon degan narsani beradi u faqat for bilan keladi.
# range faqat indeksda hisoblaydi. 10 hachon misolida ko'rishimiz mumkin.
# for i in range(10):
#     print(i)
# range endi  2 qiladigan ishini ko'rishimiz mumkin. 1 qadam beriladi va gachon son kiritilinadi va misol 2 ta qadamdan deb kiritamiz vergullar bilan
# ranga boshlanish nuqtasi tugash nuqtasi va nechi qadamdan yurish mumkin bo'lhan nuqtasi bor.

#
# for i in range(5, 20, 2):
#      print(i)


# listga toq va juft sonlarni yeg'amiz buning uchun toq deb list ochamiz va juft deb list ochamiz appendan yanai oxiriga qoshib ketish metodidan foydalanmiz
#
# juft = []       # buni ham bosh qoladiramiz bularni ichiga yeg'amiz
# toq = []    # deymiza listni bosh qolaidramiz
#
# for i in range(20):     #juft va toqni aniqlash o'zgarmas formulasi bor if i % 2 == 0: bu bizada juftniki
#      if i % 2 == 0:
#          juft.append(i)
#
#      else:
#          toq.append(i)     #Bu joyda bitta holat bo'yicha tekshirdik. yani juftni qildim  avtomat tarzda toq o'zi chiqadi, bu juda qulay bo'lishi mumkin ayrim holatlarda xatolik berishi mumkin
#                             # chunki ikkinchi holatni tekshirmadik shunchaki berib ketdik. jarayon ketmoqda biz esa shunchaki chiqarib qo'ydik
# print("Juft:", juft)
# print("Toq:", toq)
# Boshqa variantlarini ham ko'ramiz yuqoridagi ham xato emas

#
# juft = []
# toq = []
# #range bilan juft va toqni ajratish mumkin
# # printni ichkariga ozgina olib kelsa boshqacha ko'rinishida  javob chiqar ekan
#
# for i in range(0, 30, 2):
#     juft.append(i)
# print(juft)
#
# for i in range(1, 30, 2):
#     toq.append(i)
# print(toq)

# deksherin
# generatsiya for ga aloqador bo'lgan narsa  listni ichida generatsiya qilib ketsa bo'ladi. Bira to'la listni ichiga yeg'amiz
# list ichida yeg'ishi yani forni listga olamiz buni generatsiya deyiladi. Buni yozilishi 1 bo'lib qiymatni holatga keltirish
# ya'ni jarayonga keladi


# list1 = [i*2 for i in range(10)]
# print(list1)

# generatsiya forda listni ichida qilinadi. faqat fordami generatsiya deyilsa hozircha forda
# for ni juda ko'p maqsadda ishlatsa bo'ladi forni vazifasi bo'lmaa ham zor narsa ya'ni ajratib turadi holat ketma- ketligini ajratib turadi. birinchi funksiyani ikkinchi funksiyadan ajratib turadi

# list ichida son va yozib birga kelsa uni ajratish uchun ham fordan foydalansak bo'ladi

# sozlar = [1, 25, 435,"olma","Python", 4353, "MISHKA"]
# int_list = [i for i in sozlar if type(i)==int]
# str_list = [i for i in sozlar if type(i)==str]
#
# print(int_list)
# print(str_list)

# list ichida generatsiya ko'rib ketamiz. 2 xil usulda generatsiya qilish mumkin birinchisi range qadamlar bilan ko'ramiz

# juft = [i for i in range(0, 20, 2)]  #bu juftni ajratish bo'ladi
# toq = [i for i in range(1,20,2)]    #bu toq sonlarni 20 magachon indexda chiqarib beradi

# generatsiya qilib if bilan ikkinchi usulda ko'rdik juft toqni topishda o'zgarmas qiymat  i % 2 == 0. i % 2 == 1

# juft = [i for i in range(20) if  i % 2 == 0]
# toq = [i for i in range(20) if  i % 2 == 1]
#
# print("JUFT:", juft)
# print("TOQ:", toq)

# sum, min, max larni o'tamiz

# nums = [i for i in range(50)]  #bunda 10 gachon bo'lgan sonlarni yeg'indisini topib berdi
# print(sum(nums))
# print(min(nums))      # bu eng kichik son ko'rsatadi qadam bersak ham bo'ladi
# misol
# nums = [i for i in range(4, 10)]
# # print(min(nums))          #eng kichkina qiymatni chiqarib berdi
# print(max(nums))    #max  eng yuqori soni chiqarib beradi. kiritilingan sonlarning ichida emg yuqorisini chiqarib beradi

# #qadamlar bo'yicha holatni belgilash
# print(nums[0:20])   #bu ham indexda hisonlaydi. qadamlarda ya'ni range qavus ichida 50 gachon kiritgan bolsakda printda list ochilganda  ma'lum bir songachon belgilasak bo'ladi. range faqat for bilan birga keladi

# print(nums[20:])  # 20 va undan yuqori bo'lgan sonlar 50 gachon chiqadi
# print(nums[::-1])  # orqadan  boshlab boshiga sanaydi
# print(nums[3:30:2])  #3 dan 30ga qadar 2 qadamdan

# toq juftni sikilda va generatsiyada chiqarishni o'rgandik va undanda oson yo'li bor
# print(nums[::2]) # juft sonlarni ajratib beradi
# print(nums[1::2]) # toq sonlarni ajratib beradi
#  listni ichida qadamlash deyiladi yuqoridagi misollar yana bitta misol


# nums = [i for i in range(10) ]
# for i in nums:
#     print(i)
#     if i == 5:
#         print("Topildi!")
#         break

# break dasturni to'xtatishga ishlatilinadiu


# Uyga vazifa a = [1, 1, 2, 3, 5, 8, 13, 21, 34, 55, 89] roʻyxati mavjud.
# Alohida ro'yxatda 5 dan kichik yoki unga teng va 5 dan katta raqamlarni chop eting.

# royxat = [1, 1, 2, 3, 5, 8, 13, 21, 34, 55, 89]
#
# a = []
# b = []
# for i in royxat:
#     if i <= 5:
#         a.append(i)
#     elif 5 <= i:
#         b.append(i)
#
# print(
#     f'5dan kichik sonlar: {a}\n'
#     f'5dan yuqori sonlar: {b}'
# )

#Foydalanuvchidan ADD misolini qabul qiladigan dasturni yozing va natijani chop eting.

# sonlar1 = (input("Sonlarni bosh joy tashab kirting: ")).split(' ')
# sonlar2 = []
#
# for i in sonlar1:
#     sonlar2.append(int(i))
#
# print(sum(sonlar2))


# Nikolay ro‘yxat asosida “foydasiz” raqam topish haqida o‘yladi. Buning mohiyati quyidagicha:
# u raqamlarning ixtiyoriy ro'yxatini oladi, ularning eng kattasini topadi va keyin uni ro'yxat uzunligiga bo'linadi.
# Talaba bunday qiymat qayerda foydali bo(')lishi mumkinligini hali aniqlamadi,
# lekin bunday funktsiyani amalga oshirishda sizning yordamingizni kutmoqda.)


# raqam = input("raqam kiritng vergul bilan : ").split(',')
# raqam2 = []
# for i in raqam:
#     raqam2.append(int(i))
# print(max(raqam2)/len(raqam2))






