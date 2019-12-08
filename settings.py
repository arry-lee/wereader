# COOKIE = "pgv_pvid=7374219385; eas_sid=6175O539f9W9q4K3z4h8q0N1n4; pgv_pvi=9972147200; RK=cwxsV8DNYF; ptcz=1c48ec83775bbe0dde88a324355e6965c6a45d4581a86cd3c0c0a8e0c07efaa8; ptui_loginuin=1396783423; pgv_si=s881334272; ptisp=ctc; uin=o1396783423; wr_name=Arry; wr_logined=1; wr_vid=23859891; wr_skey=qKgUEr9m; wr_avatar=http%3A%2F%2Fthirdwx.qlogo.cn%2Fmmopen%2Fvi_32%2FQ0j4TwGTfTJfGIgYkJcsJibm6phYRwS74eRQdHLPxR4Cqqt43oBg1W62Xb1aSicR1vvR3BYoAlRmJgMsviclBDkDQ%2F132"

COOKIE ="pgv_pvi=6568148992; pgv_pvid=1431408232; RK=gcw0Xbd8fj; ptcz=48f4782127aee2bc917305a8f5209f387ff806f900b4afec0232746101429183; tvfe_boss_uuid=51b88b6d3554bb21; gid=c93b64d1-8094-473f-9d22-df83cbac3118; eas_sid=11e5O589i897d5s9C630O1v159; o_cookie=727057301; pac_uid=1_727057301; ptui_loginuin=727057301; pgv_si=s7981846528; wr_logined=1; uin=o0727057301; skey=@BhMUR5PMa; ptisp=cm; pgv_info=ssid=s7443794080; wr_logined=1; wr_gid=273958241; wr_vid=377902464; wr_skey=lOrqjZ0E; wr_pf=1; wr_rt=web%40ujroDlvBy02hhZPOD2m_WL; wr_localvid=737326508168655808d7e45; wr_name=%E9%99%88%E9%B2%81%E5%8B%87; wr_avatar=http%3A%2F%2Fwx.qlogo.cn%2Fmmhead%2F12hqpQxZbWqS7AGhuL8u3hsDXFqQwk7wLA0ppW61o7w%2F0; wr_gender=1"

for c in COOKIE.split(';'):
	try:
		k,v = c.strip().split('=')
		if k == 'wr_vid':
			break
	except Exception as e:
		print(e)

USERVID = int(v)
