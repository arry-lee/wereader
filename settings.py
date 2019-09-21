# COOKIE = "pgv_pvid=7374219385; eas_sid=6175O539f9W9q4K3z4h8q0N1n4; pgv_pvi=9972147200; RK=cwxsV8DNYF; ptcz=1c48ec83775bbe0dde88a324355e6965c6a45d4581a86cd3c0c0a8e0c07efaa8; ptui_loginuin=1396783423; pgv_si=s881334272; ptisp=ctc; uin=o1396783423; wr_name=Arry; wr_logined=1; wr_vid=23859891; wr_skey=qKgUEr9m; wr_avatar=http%3A%2F%2Fthirdwx.qlogo.cn%2Fmmopen%2Fvi_32%2FQ0j4TwGTfTJfGIgYkJcsJibm6phYRwS74eRQdHLPxR4Cqqt43oBg1W62Xb1aSicR1vvR3BYoAlRmJgMsviclBDkDQ%2F132"

COOKIE ="pgv_pvid=7374219385; eas_sid=6175O539f9W9q4K3z4h8q0N1n4; pgv_pvi=9972147200; RK=cwxsV8DNYF; ptcz=1c48ec83775bbe0dde88a324355e6965c6a45d4581a86cd3c0c0a8e0c07efaa8; ptui_loginuin=1396783423; pgv_si=s881334272; ptisp=ctc; uin=o1396783423; wr_name=Arry; wr_logined=1; wr_vid=23859891; wr_skey=8kBuZPG4; wr_avatar=http%3A%2F%2Fthirdwx.qlogo.cn%2Fmmopen%2Fvi_32%2FQ0j4TwGTfTKpLmUZ9ZwQEhQC1ibeMkKFGuBpRPbh7243JhHUMiaibf3QdVkT98g8QvTDcmicjTnuq51mTLav1VyFoA%2F132"


for c in COOKIE.split(';'):
	k,v = c.strip().split('=')
	if k == 'wr_vid':
		break

USERVID = int(v)
