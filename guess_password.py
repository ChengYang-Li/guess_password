# 猜密碼程式

password = 'a123456'
chance = 2

while chance >= 0:
	guess_password = input('請輸入7碼密碼，英文+數字： ')
	if password != guess_password:
		if chance == 0:
			print('密碼錯誤！你已經試了3次了，請1天後再試')
			break
		print('密碼錯誤！還有', chance, '次機會')
		chance -= 1
	else:
		print('登入成功！')
		break