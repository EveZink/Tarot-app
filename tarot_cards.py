import random
import textwrap

from PIL import Image, ImageDraw, ImageFont, ImageTk
import tkinter as tk
from tkinter import messagebox

tarot_cards_meanings = {
    'Juokdarys': {'reiksme': 'Nauja pradžia, naivumas.', 'aprasymas': 'tai tavo šansas gyvenime pardėti kažką naujo.',
                  'patarimas': 'Nebijok rizikuoti', 'paveikslelis': 'images/Juokdarys.jpg'},
    'Burtininkas': {'reiksme': 'Kūryba ir kontrolė', 'aprasymas': 'Jūs turite visas priemones savo tikslams pasiekti.',
                    'patarimas': 'Naudokite savo įgūdžius protingai ir pasitikėkite savo jėgomis.',
                    'paveikslelis': 'images/Burtininkas.jpg'},
    'Vyriausioji žynė': {'reiksme': 'Intuicija, įžvalgos', 'aprasymas': 'Tu tai turi- tikėk intuicija ir vidaus balsu.',
                         'patarimas': 'Sek savo vidiniu balsu', 'paveikslelis': 'images/Vyriausioji_zyne.jpg'},
    'Imperatorė': {'reiksme': 'Kūryba, vaisingumas, gausa', 'aprasymas': 'Galinga, įtakinga, mylinti ir besirūpinanti',
                   'patarimas': 'Rūpinkis savimi ir aplinkiniais', 'paveikslelis': 'images/Imperatore.jpg'},
    'Imperatorius': {'reiksme': 'Tvarka, struktūra, autoritetas',
                     'aprasymas': 'Autoriteteto ir galios žmogus/ valdžios atstovas',
                     'patarimas': 'Išlik stiprus ir disciplinuotas', 'paveikslelis': 'images/Imperatorius.jpg'},
    'Šventikas': {'reiksme': 'Tradiciškumas, išmintis, mokymas', 'aprasymas': 'Tavęs laukia apeigos arba mokymai',
                  'patarimas': 'Semkis išminties iš praeities', 'paveikslelis': 'images/Sventikas.jpg'},
    'Mylimieji': {'reiksme': 'Meilė, pasirinkimai, ryšiai.',
                  'aprasymas': 'Meilė ne tik džiaugsmas, tai ir atsakomybė bei pasirinkimai',
                  'patarimas': 'Atidžiai rinkis savo kelią.', 'paveikslelis': 'images/Mylimieji.jpg'},
    'Vežimas': {'reiksme': 'Kontrolė, valia, pergale.', 'aprasymas': 'Progresas tavo pusėje - viskas eina į gerą',
                'patarimas': 'Eik tiesiai į tikslą.', 'paveikslelis': 'images/Vezimas.jpg'},
    'Galia': {'reiksme': 'Jėga, kantrybė, drąsa.', 'aprasymas': 'Švelnuma ir atjauta, ne agresija nugalėsi sunkumus',
              'patarimas': 'Vidinė stiprybė nugali viską.', 'paveikslelis': 'images/Galia.jpg'},
    'Atsiskyrėlis': {'reiksme': 'meditacija, atsitraukimas, ieškojimas.',
                     'aprasymas': 'Atsakymus rasi atsiribojęs nuo visko.',
                     'patarimas': 'Neskubėk, apmąstyk.', 'paveikslelis': 'images/Atsiskyrėlis.jpg'},
    'Fortūnos ratas': {'reiksme': 'Sėkmė, pokytis, ciklai.',
                       'aprasymas': 'Pokyčiai jau tavo gyvenime - netikėtumai garantuoti.',
                       'patarimas': 'Viskas keičiasi – būk pasiruošęs.', 'paveikslelis': 'images/Fortunos_ratas.jpg'},
    'Teisingumas': {'reiksme': 'Pusiausvyra, tiesa, sąžiningumas.',
                    'aprasymas': 'Apie viską spręsk sąžinigai ir teisybė tavo pusėje.',
                    'patarimas': 'Elkis teisingai!', 'paveikslelis': 'images/Teisingumas.jpg'},
    'Pakabintasis': {'reiksme': 'Pauzė, auka, naujas požiūris.', 'aprasymas': 'Tu elgeisi neteisingai.',
                     'patarimas': 'Kartais reikia pasitraukti', 'paveikslelis': 'images/Pakabintasis.jpg'},
    'Mirtis': {'reiksme': 'Pabaiga, transformacija, nauja pradžia.',
               'aprasymas': 'Tavo gyvenime vyksta transformacijos.',
               'patarimas': 'Priimk pokyčius.', 'paveikslelis': 'images/Mirtis.jpg'},
    'Saikingumas': {'reiksme': 'Harmonija, kantrybė, pusiausvyra.',
                    'aprasymas': 'Harminongas žmogus ar subalansuotas periodas.',
                    'patarimas': 'Išlik ramus.', 'paveikslelis': 'images/Saikingumas.jpg'},
    'Velnias': {'reiksme': 'Priklausomybė, ribojimai, pagunda.', 'aprasymas': 'Daug pagundų ir neaiškių aplinkybių',
                'patarimas': 'Neapsiribok vien paviršiumi.', 'paveikslelis': 'images/Velnias.jpg'},
    'Bokštas': {'reiksme': 'Staigūs pokyčiai, griuvimas, tiesa.',
                'aprasymas': 'Netikėti griuvimai, tiesos atskleidimas',
                'patarimas': 'Kas griūna, padaro vietos naujam.', 'paveikslelis': 'images/Bokstas.jpg'},
    'Žvaigždė': {'reiksme': 'Viltis ir tikslai',
                 'aprasymas': 'Žvaigždė yra šviesos simbolis tamsoje, suteikiantis vilties ir aiškią kryptį.',
                 'patarimas': 'Pasitikėkite savo intuicija ir išlaikykite optimizmą.',
                 'paveikslelis': 'images/Zvaigzde.jpg'},
    'Mėnulis': {'reiksme': 'Paslaptingumas, iliuzija, emocijos.',
                'aprasymas': 'Nepastovios emocijos, iliuzijų periodas',
                'patarimas': 'Pasitikėk intuicija.', 'paveikslelis': 'images/Menulis.jpg'},
    'Saulė': {'reiksme': 'Džiaugsmas ir sėkmė',
              'aprasymas': 'Saulė simbolizuoja šviesią ateitį, laimę ir pilnatvę jūsų gyvenime.',
              'patarimas': 'Džiaukitės akimirka ir pasidalinkite savo laime su kitais.',
              'paveikslelis': 'images/Saule.jpg'},
    'Teismas': {'reiksme': 'Atsakomybė, vertinimas, pabudimas.',
                'aprasymas': 'Vyksta tavo vertinimas, atmokėjimas už darbus',
                'patarimas': 'Priimk savo sprendimus', 'paveikslelis': 'images/Teismas.jpg'},
    'Pasaulis': {'reiksme': 'Užbaigimas, pilnatvė, sėkmė.',
                 'aprasymas': 'Svajonių išsipildymas netoli, viską pasiekei!',
                 'patarimas': 'Viskas yra įmanoma.', 'paveikslelis': 'images/Pasaulis.jpg'},
}


def draw_card():
    selected_card = random.choice(list(tarot_cards_meanings.keys()))
    details = tarot_cards_meanings[selected_card]

    try:
        img = Image.open(details['paveikslelis'])
    except FileNotFoundError:
        messagebox.showerror('Klaida', f'Paveikslėlis nerastas: {details['paveikslelis']}')
        return

    width, height = img.size
    new_height = height + 200
    combined_img = Image.new('RGB', (width, new_height), color='white')
    combined_img.paste(img, (0, 0))
    draw = ImageDraw.Draw(combined_img)
    font = ImageFont.truetype('arial.ttf', size=18)

    text_content = (
        f'Korta: {selected_card}\n'
        f'Reikšmė: {textwrap.fill(details['reiksme'], width=25)}\n'
        f'Aprašymas: {textwrap.fill(details['aprasymas'], width=25)}\n'
        f'Patarimas: {textwrap.fill(details['patarimas'], width=25)}\n'
    )
    draw.text((0, height + 10), text_content, fill='black', font=font)

    combined_img.thumbnail((400, 600))
    img_tk = ImageTk.PhotoImage(combined_img)
    canvas.image = img_tk
    canvas.create_image(200, 300, anchor='center', image=img_tk)

root = tk.Tk()
root.title('Taro Burimas')

canvas = tk.Canvas(root, width=400, height=600, background='white')
canvas.pack()

btn_draw = tk.Button(root, text='Sugalvok klausimą ir versk kortą', command=draw_card)
btn_draw.pack(pady=10)

btn_exit = tk.Button(root, text='Išeiti', command=root.destroy)
btn_exit.pack(pady=5)

root.mainloop()
