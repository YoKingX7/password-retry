# 密碼重試程式
# password = "a12345"
# 讓使用者重複輸入密碼
# 最多輸入 3 次
# 如果正確 就印出 “登入成功！”
# 如果不正確 就印出 “密碼錯誤！ 還有＿次機會！”

password = "a12345" # 儲存正確密碼
i = 3 # 剩餘機會

while True:
	pwd = input("請輸入密碼：") # 儲存使用者輸入
	if pwd == password:
		print("登入成功！")
		break # 逃出迴圈
	else:
		i = i - 1 # 剩餘次數 - 1 後再存回去 i
		print("密碼錯誤！ 還有 ", i, " 次機會！")
		if i == 0: # 剩餘機會是 0 次
			break # 逃出迴圈
