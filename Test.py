print('Hoeveel maanden ben je voor plan om te sparen?')
maanden = int(input('Hoeveelheid maanden: '))


print('Hoeveel euro ben je voor plan elke maand te sparen?')
geldpermaand = int(input('Hoeveelheid in €: '))


print('Hoeveel euro heb je nu op je rekening staan?')
beginhoeveelheid = float(input('Hoeveelheid in €: '))

eindhoeveelheid = beginhoeveelheid + geldpermaand*maanden

eindhoeveelheid = '€' + str(beginhoeveelheid + maanden * geldpermaand)
print ('Je hebt in ' + str(maanden) + ' maanden ' + str(eindhoeveelheid) + ' op je rekening..')

