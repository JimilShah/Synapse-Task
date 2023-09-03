jumbled_names = ['DocToR_STRAngE', 'sPidERmaN', 'MOON_KnigHT', 'caPTAIN_aMERIca', 'hULK']

indices = []
decoded_names = []

for index, name in enumerate(jumbled_names):
    indices.append(index)
    decoded_names.append(name.lower().replace('_', ' '))

name_lengths = list(map(lambda x: len(x), decoded_names))

indices.sort(key=lambda x: name_lengths[x])

sorted_superheroes = [decoded_names[i].title() for i in indices]

for index, superhero in enumerate(sorted_superheroes, start=1):
    print(f'{index}. {superhero}')