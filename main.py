from tkinter import *
from tkinter.filedialog import askopenfilename
from tkinter.messagebox import showerror,showinfo


# from Liste import liste

class Personnage ():
    def __init__(self,first_name,name,born,born_place,address,type,email,nationality,phone,picture):
        self.first_name = first_name
        self.name = name
        self.born = born
        self.born_place = born_place
        self.address = address
        self.type = type
        self.email = email
        self.nationality = nationality
        self.phone = phone
        self.picture = picture

    def __eq__(self,other):
        return (self.first_name == other.first_name and self.name == other.name)


def parcourir():
    global image_names
    imn = askopenfilename (initialdir = "/",title = "Selectionner une image",
                           filetypes = (("png files","*.png"),("jpeg files","*.jpg")))
    if imn:
        image_names = imn
    if image_names:
        texte3 = image_names.split ("/")
        enter_picture.configure (text = ".../" + texte3[-1])


def appartient(list,val):
    for i in range (len (list)):
        if list[i].__eq__ (val):
            return 1
    return 0


def Valider():
    global liste_personne,image_names
    picture = image_names
    if enter_firstname.get () and enter_name.get () and picture:
        pn = Personnage (enter_firstname.get (),enter_name,picture)
        if appartient (liste_personne,pn):
            showerror (title = "Formulaire invalide",message = "Cet Utilisateur existe déja !")
        else:
            liste_personne.append (pn)
            showinfo (title = "Validation réussie",message = "{} a bien été ajouté".format (enter_firstname.get ()))

    else:
        showerror (title = "Formulaire invalide",message = "Toutes les champs doivent etre remplir")


def restart():
    global image_names
    enter_firstname.delete (0,END)
    enter_name.delete (0,END)
    enter_born.delete (0,END)
    enter_born_place.delete (0,END)
    enter_email.delete (0,END)
    enter_address.delete (0,END)
    enter_nationality.delete (0,END)
    enter_phone.delete (0,END)
    male.delete (0,END)
    female.delete (0,END)
    image_names = ''
    enter_picture.configure(text ="Aucune image sélectionner")


image_names, liste_personne = '',[]



formulary = Tk ()
formulary.geometry ("915x680")
formulary.title ("Formulaire")
formulary.config (bg = "#938C8C")



block1 = Canvas (formulary,bg = "#938C8C")



texte1 = Label (block1,text = 'Formulaire',font = ('Bank Gothic Medium BT',30),bg = '#FEFEFE',fg = 'black')
texte2 = Label (block1,text = '     Veuiller        saisir        vos        informatons      ',font = ('Bank Gothic Medium BT',20),bg = 'black',fg = '#FEFEFE')
texte1.grid (row = 1,column = 0,columnspan = 2)
texte2.grid (row = 2,column = 0,columnspan = 2)



first_name = Label (block1,text = "Prénom",font = ("MANDELA",15))
enter_firstname = Entry (block1)
first_name.grid (row = 3,column = 0,sticky = E,padx = 5,pady = 5)
enter_firstname.grid (row = 3,column = 1,padx = 5,pady = 5)



name = Label (block1,text = "Nom",font = ("MANDELA",15))
enter_name = Entry (block1)
name.grid (row = 4,column = 0,sticky = E,padx = 5,pady = 5)
enter_name.grid (row = 4,column = 1,padx = 5,pady = 5)



born = Label (block1,text = "Date de Naissance",font = ("MANDELA",15))
enter_born = Entry (block1)
born.grid (row = 5,column = 0,sticky = E,padx = 5,pady = 5)
enter_born.grid (row = 5,column = 1,padx = 5,pady = 5)



born_place = Label (block1,text = "Lieu de Naissance",font = ("MANDELA",15))
enter_born_place = Entry (block1)
born_place.grid (row = 6,column = 0,sticky = E,padx = 5,pady = 5)
enter_born_place.grid (row = 6,column = 1,padx = 5,pady = 5)



address = Label (block1,text = "Adresse",font = ("MANDELA",15))
enter_address = Entry (block1)
address.grid (row = 7,column = 0,sticky = E,padx = 5,pady = 5)
enter_address.grid (row = 7,column = 1,padx = 5,pady = 5)



type = Label (block1,text = "Genre",font = ("MANDELA",15))
value = StringVar ()
male = Radiobutton (block1,text = "Masculin",variable = value,value = 1)
female = Radiobutton (block1,text = "Féminin",variable = value,value = 2)
type.grid (row = 8,column = 0,sticky = E,padx = 5,pady = 5)
male.grid (row = 8,column = 1,padx = 5,pady = 5)
female.grid (row = 8,column = 2,padx = 5,pady = 5)



email = Label (block1,text = "E-Mail",font = ("MANDELA",15))
enter_email = Entry (block1)
email.grid (row = 9,column = 0,sticky = E,padx = 5,pady = 5)
enter_email.grid (row = 9,column = 1,padx = 5,pady = 5)



nationality = Label (block1,text = "Pays",font = ("MANDELA",15))
enter_nationality = Entry (block1)
nationality.grid (row = 10,column = 0,sticky = E,padx = 5,pady = 5)
enter_nationality.grid (row = 10,column = 1,padx = 5,pady = 5)



phone = Label (block1,text = "Téléphone",font = ("MANDELA",15))
enter_phone = Entry (block1)
phone.grid (row = 11,column = 0,sticky = E,padx = 5,pady = 5)
enter_phone.grid (row = 11,column = 1,padx = 5,pady = 5)



picture = Label (block1,text = "Photo",font = ("MANDELA",15))
enter_picture = Label (block1,text = "Aucune image sélectionner",font = ("MANDELA",10),fg = "#455D5A")
picture.grid (row = 12,column = 0,sticky = E,padx = 5,pady = 5)
enter_picture.grid(row = 12,column = 1,padx = 5,pady = 5,sticky = W)
parcourir = Button (block1,text = 'Parcourir',font = ('Bank Gothic Medium BT',10),bg = '#FEFEFE',fg = 'black',command = parcourir)
parcourir.grid (row = 12,column = 2,padx = 5,pady = 5,sticky = E)

valid = Button (formulary,text = 'Valider',font = ('Bank Gothic Medium BT',15),bg = '#FEFEFE',fg = 'black',command = Valider)
restart = Button (formulary,text = 'Annuler',font = ('Bank Gothic Medium BT',15),bg = '#FEFEFE',fg = 'black',command = restart)
list = Button (formulary,text = 'Voir la liste',font = ('Bank Gothic Medium BT',15),bg = '#FEFEFE',fg = 'black',command = "")

valid.grid (row = 11,column = 0,pady = 5)
restart.grid (row = 12,column = 0,pady = 5)
list.grid (row = 13,column = 0,pady = 5)

block1.grid (row = 0,column = 0,padx = 5,pady = 5)



formulary.mainloop ()
