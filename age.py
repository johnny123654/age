drive = input ('請問您開過車嗎？')
if drive != '有' and drive != '沒有':
	print ('只能輸入有和沒有')

age = input ('請問您的年齡？')
age = int (age)
if drive == '有':
	if age >= 18 :
		print ('您可以開車')
	else:
		print ('您怎麼能夠開車')
elif drive == '沒有':
	if age >= 18:
		print ('您可以考駕照了')
	elif age < 18 :
		print ('需要再等等')




