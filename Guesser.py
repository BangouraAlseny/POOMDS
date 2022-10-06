from re import A


nom = "Jac"

leet = ["a","e","i","o","l","s","b","t","z","g"]

def positon(liste, mot):
    tab = []
    for i in range(len(liste)):
        for j in range(len(mot)):
            if (liste[i] == mot[j]):
                tab.append({mot[j]: j})
    return tab

print(positon(leet, "jacela"))

def toTab(mot):
    tab = []
    for i in range(len(mot)):
        tab.append(mot[i])
    return tab
    
toTab(nom)

# nom[0] = "a"
print(toTab(nom))

tab = [nom.upper()]
tab.append(nom.title())
tab.append(nom.lower())

print(tab)



