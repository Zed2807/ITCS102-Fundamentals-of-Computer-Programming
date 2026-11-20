anime = ["Demon Slayer", "Jobless Reincarnation", "Haikyuu", "One punch man", "Boruto", "Attack on titan"]

Demon_Slayer = ["Tanjiro Kamado", "Zenitsu", "Inosuke"]
Jobless_Reincarnation = ["Rudeus Greyrat", "Roxy Migurdia", "Paul Greyrat"]
Haikyuu = ["Kenma", "Kageyama", "Hinata"]
One_Punch_Man = ["Saitama", "Genos", "Tatsumaki"]
Boruto = ["Boruto Uzumaki", "Uchiha Sarada", "Mitsuki"]
Attack_on_Titan = ["Eren Yeager", "Mikasa Ackerman", "Levi Ackerman"]

#Demonslayer
Tanjiro_Kamado = ['sense of smell', 'Water Breathing', 'Sun Breathing']
Zenitsu = ['sense of hearing', 'Thunder Breathing']
Inosuke = ['sense of touch', 'Beast Breathing']

#Jobless Reincarnation
Rudeus_Greyrat = ['without incantations', 'Water Magic', 'massive mana pool']
Roxy_Migurdia = ['King-tier Water Mage', 'Migurd demon', 'magic tutor']
Paul_Greyrat = ['Advanced three styles', 'former adventurer', 'flawed father']

#Haikyuu
Kenma = ['Nekoma setter', 'strategic mastermind', 'video gamer']
Kageyama = ['Karasuno setter', 'pinpoint accuracy', 'King of the Court']
Hinata = ['middle blocker', 'explosive jump', 'ultimate decoy']

#One punch man
Saitama = ['one-punch knockout', 'limitless strength', 'hero for fun']
Genos = ['Demon Cyborg', 'incineration cannons', 'Saitama disciple']
Tatsumaki = ['Tornado of Terror', 'S-Class Rank 2', 'supreme telekinesis']

#Boruto
Boruto_Uzumaki = ['Karma seal', 'Jougan eye', 'Vanishing Rasengan']
Sarada_Uchiha = ['Sharingan', 'superhuman strength', 'future Hokage']
Mitsuki = ['Sage Mode', 'synthetic human', 'stretching limbs']

#AOT
Eren_Yeager = ['Attack Titan', 'Founding Titan', 'relentless freedom']
Mikasa_Ackerman = ['Ackerman strength', 'red scarf', 'protects Eren']
Levi_Ackerman = ['humanity strongest soldier', 'ODM gear master', 'clean freak']

Demon_Slayer = {"Tanjiro Kamado": Tanjiro_Kamado, "Zenitsu": Zenitsu, "Inosuke": Inosuke}
Jobless_Reincarnation = {"Rudeus Greyrat": Rudeus_Greyrat, "Roxy Migurdia": Roxy_Migurdia, "Paul Greyrat": Paul_Greyrat}
Haikyuu = {"Kenma": Kenma, "Kageyama": Kageyama, "Hinata": Hinata}
One_Punch_Man = {"Saitama": Saitama, "Genos": Genos, "Tatsumaki": Tatsumaki}
Boruto = {"Boruto Uzumaki": Boruto_Uzumaki, "Sarada Uchiha": Sarada_Uchiha, "Mitsuki": Mitsuki}
Attack_on_Titan = {"Eren Yeager": Eren_Yeager, "Mikasa Ackerman": Mikasa_Ackerman, "Levi Ackerman": Levi_Ackerman}

Shounen = {"Demon Slayer": Demon_Slayer,"Haikyuu": Haikyuu,"Boruto": Boruto,"Attack on Titan": Attack_on_Titan}
Seinen = {"Jobless Reincarnation": Jobless_Reincarnation,"One Punch Man": One_Punch_Man}

acm ={"Shounen": Shounen, "Seinen": Seinen}

print("=== 1. Going down one level at a time ===")
print(acm["Shounen"]["Demon Slayer"]["Tanjiro Kamado"][1])

print()
print("=== 2. Loop level 1: categories ===")
for category in acm:
    print(category)

print()
print("=== 3. Loop levels 1-2: categories and titles ===")
for category, titles in acm.items():
    print(category)
    for title in titles:
        print(" -", title)

print()
print("=== 4. Loop ALL levels ===")
for category, titles in acm.items():
    print(category)
    for title, characters in titles.items():
        print("  " + title)
        for name, info in characters.items():
            print("    " + name)
            print("      Abilities:")
            for ability in info:
                print("       -", ability)

print()
print("=== 5. Count every character ===")
count = 0
for titles in acm.values():
    for characters in titles.values():
        for name in characters:
            count = count + 1
print("Total characters:", count)
