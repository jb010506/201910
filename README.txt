

20190908

show.py


ISSUE : 文檔格式讀取問題(UnicodeEncodeError)
Solution : encoding採取 utf-8 (變成一種限制，文檔須為utf-8才可讀取)

功能:
1) 將文檔做字串處理，並建立一個新的文檔
2) 讀取新的文檔，每行一個單字配一個中文意思 
3) 透過 PyQt5 函式庫並規範定時秀出各個單字，形成影片的感覺


20191010
解決超過一個的英文單字所產生的問題 如 department store