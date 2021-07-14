# 猜密碼程式

password = input('設定英文+數字7碼密碼： ')
chance = int(input('你想猜幾次： '))
remain_chance = chance

while remain_chance > 0:
	guess_password = input('請輸入7碼密碼，英文+數字： ')
	if password != guess_password:
		remain_chance -= 1
		if remain_chance == 0:
			print('密碼錯誤！你已經試了', chance, '次，請1天後再試')
		else:
			print('密碼錯誤！還有', remain_chance, '次機會')
	else:
		print('登入成功！')
		break

