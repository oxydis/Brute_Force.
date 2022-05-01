import random 

password = random.randint(1,100000)
print("Le code à trouver est :", password)

running = True

while running:

    brtf = random.randint(1, 100000)

    if(brtf == password):
        print("✅ | Le mot de passe à été trouver, c'était :", password)
        running = False
    else:
        print("❌ | Le mot de passe est incorecte ce n'est pas :", brtf)