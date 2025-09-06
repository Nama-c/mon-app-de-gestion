# App de gestion du budget version 1 python

# --------------------------------
# enregistrement de l'utilisateur 
# --------------------------------
print("\n===== bienvenu sur budget+ =====")
print("\n1- s'inscrire ")
print("2- se connecter ")
choix=input("\nchoisir l'une des deux options : ")
while (not choix.isdigit()) or int(choix)<1 or int(choix)>2 :
    choix=input("choix incorrect, retapez votre choix : ")
choix=int(choix)

if choix == 1 :
    # inscription du client
    nom=input("\nsaisissez votre nom : ")
    while (not nom.isalpha()) or len(nom)==1 :
        nom=input("resaisissez votre nom : ")

    prenom=input("\nsaisissez votre prenom : ")
    while (not prenom.isalpha()) or len(prenom)==1 :
        prenom=input("resaisissez votre prenom : ")

    numero=input("\nsaisissez votre numero de telephone : ")
    while (not numero.isdigit()) or int(numero)<770000000 or int(numero)>=790000000:
        numero=input("numero de telephone saisi non valide veuillez retaper un numero valide : ")
    
    # mot de passe
    num=True
    while num==True:
        # premiere saisi
        mdp=input("\nenregistrer un mot de passe (uniquement des chiffres) : ")
        while not(mdp.isdigit()) or len(mdp)<4:
            mdp=input("mot de passe saisi non valide, retapez un mot de passe : ")
        mdp=int(mdp)
        # deuxieme saisi
        mdp2=input("\nsaisissez une deuxieme fois votre mot de passe : ")
        while not(mdp2.isdigit()):
            mdp2=input("retapez le mot de passe : ")
        mdp2=int(mdp2)
        if mdp != mdp2 :
            print("les mots de passe saisi ne correspondent pas !!!")
            num=True
        else:
            print("mot de passe enregistrer et compte creer !!!")
            num=False

client = {
    "numero":numero,
    "nom":nom.lower(),
    "prenom":prenom.lower(),
    "mot de passe":mdp,
}

if choix == 2 :
    # connexion du client
    nom_re=input("\nsaisissez votre nom : ")
    while (not nom_re.isalpha()) or len(nom_re)==1 :
        nom_re=input("resaisissez votre nom : ")

    numero_re=input("\nsaisissez votre numero de telephone : ")
    while (not numero_re.isdigit()) or int(numero_re)<770000000 or int(numero_re)>=790000000:
        numero_re=input("numero de telephone saisi non valide veuillez retaper un numero valide : ")

    mdp_re=input("\nsaisissez votre mot de passe : ")
    while not(mdp_re.isdigit()) or len(mdp_re)<4:
        mdp_re=input("mot de passe saisi non valide, retapez un mot de passe : ")

    client_re = {
        "numero":numero_re,
        "nom":nom_re.lower(),
        "mot de passe":mdp_re,
    }

# --------------------------------
# application de gestion du budget
# --------------------------------
