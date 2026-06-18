import csv, os, random
from datetime import datetime, date, timedelta

random.seed(42)
rows = []

dates = [date(2026, 5, 18) + timedelta(days=i) for i in range(7)]
weekdays = [d for d in dates if d.weekday() < 5]

def rt(d, h0, h1):
    return datetime(d.year, d.month, d.day,
                    random.randint(h0, h1 - 1),
                    random.randint(0, 59),
                    random.randint(0, 59))

def add(dt, acct, uid, store, role, op, res, result, ip):
    rows.append([dt.strftime('%Y-%m-%d %H:%M:%S'), acct, uid, store, role, op, res, result, ip])

# ── ST 渋谷店1047 (100001-100009) ────────────────────────
for i in range(9):
    acct, ip = 100001 + i, f'192.168.47.{101 + i}'
    uid = f'1047-{acct}'
    for d in weekdays:
        if random.random() < 0.82:
            add(rt(d, 9, 10), acct, uid, 1047, 'ST', 'LOGIN', '-', 'SUCCESS', ip)
            for _ in range(random.randint(1, 3)):
                add(rt(d, 10, 17), acct, uid, 1047, 'ST', 'ACCESS',
                    random.choice(['CONTRACT_DATA', 'TERMINAL_MGR']), 'SUCCESS', ip)
            add(rt(d, 17, 18), acct, uid, 1047, 'ST', 'LOGOUT', '-', 'SUCCESS', ip)

# ── ST 新宿店2089 (100010-100014) ────────────────────────
for i in range(5):
    acct, ip = 100010 + i, f'192.168.89.{110 + i}'
    uid = f'2089-{acct}'
    for d in weekdays:
        if random.random() < 0.82:
            add(rt(d, 9, 10), acct, uid, 2089, 'ST', 'LOGIN', '-', 'SUCCESS', ip)
            for _ in range(random.randint(1, 3)):
                add(rt(d, 10, 17), acct, uid, 2089, 'ST', 'ACCESS',
                    random.choice(['CONTRACT_DATA', 'TERMINAL_MGR']), 'SUCCESS', ip)
            add(rt(d, 17, 18), acct, uid, 2089, 'ST', 'LOGOUT', '-', 'SUCCESS', ip)

# ── ST 100023 渋谷店1047 (平日9-18 CONTRACT_DATA のみ) ──
for d in weekdays:
    add(rt(d, 9, 10), 100023, '1047-100023', 1047, 'ST', 'LOGIN', '-', 'SUCCESS', '192.168.47.123')
    for _ in range(random.randint(1, 2)):
        add(rt(d, 10, 17), 100023, '1047-100023', 1047, 'ST', 'ACCESS',
            'CONTRACT_DATA', 'SUCCESS', '192.168.47.123')
    add(rt(d, 17, 18), 100023, '1047-100023', 1047, 'ST', 'LOGOUT', '-', 'SUCCESS', '192.168.47.123')

# ── SM 800002 渋谷店1047 ─────────────────────────────────
for d in weekdays:
    add(rt(d, 9, 10), 800002, '1047-800002', 1047, 'SM', 'LOGIN', '-', 'SUCCESS', '192.168.47.202')
    for _ in range(random.randint(2, 4)):
        add(rt(d, 10, 18), 800002, '1047-800002', 1047, 'SM',
            random.choice(['ACCESS', 'MODIFY']),
            random.choice(['CONTRACT_DATA', 'SALES_DATA', 'TERMINAL_MGR']), 'SUCCESS', '192.168.47.202')
    add(rt(d, 18, 19), 800002, '1047-800002', 1047, 'SM', 'LOGOUT', '-', 'SUCCESS', '192.168.47.202')

# ── SM 800003 新宿店2089 ─────────────────────────────────
for d in weekdays:
    add(rt(d, 9, 10), 800003, '2089-800003', 2089, 'SM', 'LOGIN', '-', 'SUCCESS', '192.168.89.203')
    for _ in range(random.randint(2, 4)):
        add(rt(d, 10, 18), 800003, '2089-800003', 2089, 'SM',
            random.choice(['ACCESS', 'MODIFY']),
            random.choice(['CONTRACT_DATA', 'SALES_DATA', 'TERMINAL_MGR']), 'SUCCESS', '192.168.89.203')
    add(rt(d, 18, 19), 800003, '2089-800003', 2089, 'SM', 'LOGOUT', '-', 'SUCCESS', '192.168.89.203')

# ── SM 800001 5/18 (渋谷店1047 最終日) ───────────────────
d18 = date(2026, 5, 18)
add(rt(d18, 9, 10), 800001, '1047-800001', 1047, 'SM', 'LOGIN', '-', 'SUCCESS', '192.168.47.201')
for _ in range(random.randint(2, 3)):
    add(rt(d18, 10, 18), 800001, '1047-800001', 1047, 'SM',
        random.choice(['ACCESS', 'MODIFY']),
        random.choice(['CONTRACT_DATA', 'SALES_DATA', 'TERMINAL_MGR']), 'SUCCESS', '192.168.47.201')
add(rt(d18, 18, 19), 800001, '1047-800001', 1047, 'SM', 'LOGOUT', '-', 'SUCCESS', '192.168.47.201')

# ── AD 900001 5/18-5/19 (インシデント前・正常) ───────────
for d in [date(2026, 5, 18), date(2026, 5, 19)]:
    add(rt(d, 9, 10), 900001, '1047-900001', 1047, 'AD', 'LOGIN', '-', 'SUCCESS', '192.168.47.210')
    for _ in range(random.randint(2, 4)):
        add(rt(d, 10, 19), 900001, '1047-900001', 1047, 'AD',
            random.choice(['ACCESS', 'MODIFY']),
            random.choice(['CONTRACT_DATA', 'SALES_DATA', 'TERMINAL_MGR', 'ACCOUNT_MGR']), 'SUCCESS', '192.168.47.210')
    add(rt(d, 19, 20), 900001, '1047-900001', 1047, 'AD', 'LOGOUT', '-', 'SUCCESS', '192.168.47.210')

# ── AD 900002 新宿店2089 ─────────────────────────────────
for d in weekdays:
    add(rt(d, 9, 10), 900002, '2089-900002', 2089, 'AD', 'LOGIN', '-', 'SUCCESS', '192.168.89.211')
    for _ in range(random.randint(2, 4)):
        add(rt(d, 10, 19), 900002, '2089-900002', 2089, 'AD',
            random.choice(['ACCESS', 'MODIFY']),
            random.choice(['CONTRACT_DATA', 'SALES_DATA', 'TERMINAL_MGR', 'ACCOUNT_MGR']), 'SUCCESS', '192.168.89.211')
    add(rt(d, 19, 20), 900002, '2089-900002', 2089, 'AD', 'LOGOUT', '-', 'SUCCESS', '192.168.89.211')

# ── 退職者 (アクセス失敗) ────────────────────────────────
for acct, ip in [(700001, '172.16.31.101'), (700002, '172.16.31.102')]:
    uid = f'3124-{acct}'
    for d in random.sample(weekdays, 2):
        add(rt(d, 9, 17), acct, uid, 3124, 'EX', 'LOGIN', '-', 'FAILURE', ip)
        add(rt(d, 9, 17), acct, uid, 3124, 'EX', 'ACCESS', 'CONTRACT_DATA', 'FAILURE', ip)

# ══════════════════════════════════════════════════════════
# 不審パターン
# ══════════════════════════════════════════════════════════

# ── パターンA: 900001 権限自己復活・放置 (5/20) ──────────
d20 = date(2026, 5, 20)
# 昼間は通常アクセス
add(rt(d20, 9, 10),  900001, '1047-900001', 1047, 'AD', 'LOGIN',  '-',           'SUCCESS', '192.168.47.210')
add(rt(d20, 10, 18), 900001, '1047-900001', 1047, 'AD', 'ACCESS', 'ACCOUNT_MGR', 'SUCCESS', '192.168.47.210')
add(rt(d20, 10, 18), 900001, '1047-900001', 1047, 'AD', 'ACCESS', 'CONTRACT_DATA','SUCCESS', '192.168.47.210')
# 23時台: 自分のPERMISSION_CHANGEを実行 → 直後に機密データ連続アクセス
add(datetime(2026, 5, 20, 23, 14, 37), 900001, '1047-900001', 1047, 'AD', 'PERMISSION_CHANGE', 'ACCOUNT_MGR',  'SUCCESS', '192.168.47.210')
add(datetime(2026, 5, 20, 23, 18, 52), 900001, '1047-900001', 1047, 'AD', 'ACCESS',            'CONTRACT_DATA','SUCCESS', '192.168.47.210')
add(datetime(2026, 5, 20, 23, 22, 11), 900001, '1047-900001', 1047, 'AD', 'ACCESS',            'SALES_DATA',   'SUCCESS', '192.168.47.210')
add(datetime(2026, 5, 20, 23, 25, 44), 900001, '1047-900001', 1047, 'AD', 'ACCESS',            'SALES_DATA',   'SUCCESS', '192.168.47.210')
add(datetime(2026, 5, 20, 23, 48,  3), 900001, '1047-900001', 1047, 'AD', 'LOGOUT',            '-',            'SUCCESS', '192.168.47.210')
# 翌日以降: 権限を戻さず継続アクセス (5/21, 5/22)
for d in [date(2026, 5, 21), date(2026, 5, 22)]:
    add(rt(d, 9, 10),  900001, '1047-900001', 1047, 'AD', 'LOGIN',   '-',            'SUCCESS', '192.168.47.210')
    add(rt(d, 10, 18), 900001, '1047-900001', 1047, 'AD', 'ACCESS',  'CONTRACT_DATA','SUCCESS', '192.168.47.210')
    add(rt(d, 10, 18), 900001, '1047-900001', 1047, 'AD', 'ACCESS',  'SALES_DATA',   'SUCCESS', '192.168.47.210')
    add(rt(d, 10, 18), 900001, '1047-900001', 1047, 'AD', 'MODIFY',  'SALES_DATA',   'SUCCESS', '192.168.47.210')
    add(rt(d, 19, 20), 900001, '1047-900001', 1047, 'AD', 'LOGOUT',  '-',            'SUCCESS', '192.168.47.210')

# ── パターンB: 800001 異動後権限残存 (5/19-5/24) ─────────
# 5/19-5/22: 新店舗2089に正常ログイン + 旧店舗1047に不正アクセス継続
for d in [date(2026, 5, 19), date(2026, 5, 20), date(2026, 5, 21), date(2026, 5, 22)]:
    add(rt(d, 9, 10), 800001, '2089-800001', 2089, 'SM', 'LOGIN', '-', 'SUCCESS', '192.168.89.201')
    for _ in range(random.randint(1, 3)):
        add(rt(d, 10, 17), 800001, '2089-800001', 2089, 'SM', 'ACCESS',
            random.choice(['CONTRACT_DATA', 'SALES_DATA', 'TERMINAL_MGR']), 'SUCCESS', '192.168.89.201')
    # 削除漏れ: 2089のIPから1047へアクセス (user_idは旧1047-800001が生存)
    add(rt(d, 11, 16), 800001, '1047-800001', 1047, 'SM', 'ACCESS',
        random.choice(['SALES_DATA', 'CONTRACT_DATA']), 'SUCCESS', '192.168.89.201')
    add(rt(d, 18, 19), 800001, '2089-800001', 2089, 'SM', 'LOGOUT', '-', 'SUCCESS', '192.168.89.201')
# 5/23-5/24 (週末): 引き続き1047アクセス
add(datetime(2026, 5, 23, 14,  8, 55), 800001, '1047-800001', 1047, 'SM', 'ACCESS', 'SALES_DATA',    'SUCCESS', '192.168.89.201')
add(datetime(2026, 5, 24, 11, 31, 22), 800001, '1047-800001', 1047, 'SM', 'ACCESS', 'CONTRACT_DATA', 'SUCCESS', '192.168.89.201')

# ── パターンC: 100023 深夜不審アクセス (5/20 02:xx, 外部IP) ─
sus_ip = '203.0.113.45'
add(datetime(2026, 5, 20,  2,  7, 14), 100023, '1047-100023', 1047, 'ST', 'LOGIN',             '-',         'SUCCESS', sus_ip)
add(datetime(2026, 5, 20,  2,  9, 33), 100023, '1047-100023', 1047, 'ST', 'PERMISSION_CHANGE', 'ACCOUNT_MGR','SUCCESS', sus_ip)
add(datetime(2026, 5, 20,  2, 11, 45), 100023, '1047-100023', 1047, 'ST', 'ACCESS',            'SALES_DATA', 'SUCCESS', sus_ip)
add(datetime(2026, 5, 20,  2, 13, 22), 100023, '1047-100023', 1047, 'ST', 'ACCESS',            'SALES_DATA', 'SUCCESS', sus_ip)
add(datetime(2026, 5, 20,  2, 15,  8), 100023, '1047-100023', 1047, 'ST', 'ACCESS',            'SALES_DATA', 'SUCCESS', sus_ip)
add(datetime(2026, 5, 20,  2, 17, 31), 100023, '1047-100023', 1047, 'ST', 'LOGOUT',            '-',          'SUCCESS', sus_ip)

# ── ソート & 書き出し ────────────────────────────────────
rows.sort(key=lambda x: x[0])

out = r'C:\portfolio\access-analyzer-poc\logs.csv'
with open(out, 'w', newline='', encoding='utf-8') as f:
    w = csv.writer(f)
    w.writerow(['datetime', 'account_id', 'user_id', 'store_code', 'role',
                'operation', 'resource', 'result', 'ip_address'])
    w.writerows(rows)

print(f'Generated {len(rows)} rows -> {out}')
