
per_cent={'ТКБ': 5.6, 'СКБ': 5.9, 'ВТБ': 4.28, 'СБЕР': 4.0}
a=(list(per_cent.values()))
money=int(input("Введите сумму вашего депозита, USD "))/100
deposit=(list(map((money).__mul__, a))) #функцию "mul" еще не изучали, однако подсказку нашел на https://question-it.com/questions/86250/kak-mne-umnozhit-kazhdyj-element-v-spiske-na-chislo
print(deposit)
print('Максимальная сумма, которую вы можете заработать',max(deposit), 'USD')

