print("سلام به برنامه ما خوش آمدید؛ جهت تمام شدن کار برنامه کلمه تمام را وارد کنید.\n\n")
def number(text):
    numbers = set() #جلوگیری از چاپ شماره های تکراری
    print("شماره های استخراج شده از این متن:\n")
    for i in text.split():
        if len(i) == 11 and i[0:2] == "09":
            numbers.add(i)
    for num in numbers:
        if num[:3] == "093":
            print(f"{num} ایرانسل \n")
        elif num[:3] == "091":
            print(f"{num} همراه اول \n")
        elif num[:3] == "092" :
            print(f"{num} رایتل\n")
        else:
            print(f"{num} اپراتور تشخیص داده نشد\n")
    if numbers == set():
        print("موردی برای نمایش پیدا نشد")
while(True):
    matn = input("\n جهت شناسایی شماره های موجود در متن، متن خود را وارد کنید: \n")
    if matn == "تمام":
       break
    number(matn)

print("برنامه تمام شد.")