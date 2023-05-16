from PIL import Image
def proc81():


    im = Image.open('9may.jpg')
    im_crop = im.crop((10, 10, 300, 400))
    im_crop.save('otkrytka.jpg')
    im_crop.show()



def proc82():
    spisok = {"День победы": "9may.jpg", "Праздник всех женщин":"8-marta.jpg", "Новый год": "Happy_new_year.jpg", "День рождение": "birthday.jpg"}
    polzavatel =input("Какой сейчас праздник? ")
    if polzavatel in spisok:
        image = Image.open(spisok[polzavatel])
        image.show()
    else:
        print("Такой открытки нет")

def proc83():
    from PIL import Image, ImageDraw, ImageFont

    name = input("Введите имя получателя: ")
    filename = "birthday.jpg"
    with Image.open(filename) as img:
        img.load()
    font = ImageFont.truetype("arial.ttf", 30)
    draw_text = ImageDraw.Draw(img)
    draw_text.text(
        (img.width // 2 - 100, 15),
        name + ", поздравляю!",
        font=font,
        fill=('red')
    )
    img.show()
    img.save(name + "birthday_2.png")




