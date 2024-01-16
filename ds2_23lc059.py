import sqlite3

# 1. DB作成と接続
path = 'C:\Users\susie\Documents\ds2'
db_name = 'my_sleep_time.sqlite'
con = sqlite3.connect(path + db_name)
