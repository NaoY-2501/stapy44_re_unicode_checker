# stapy44_re_unicode_checker

## これは何

みんなのPython勉強会#44で発表した、正規表現の`\w`がマッチする範囲について確認するスクリプト

資料:[Pythonにおける正規表現の話
\wとUnicodeの意外な関係](https://gitpitch.com/NaoY-2501/GitPitch-Slides?p=stapy44_20190410#/)

### unicode_scraper.py

https://www.fileformat.info/info/unicode/category/をスクレイピングし、UnicodeカテゴリとUnicodeコードポイントの一覧を作成する。

対象のカテゴリは以下。


- Letter: Lu, Ll, Lo

- Number:Nd, Nl, No

- Punctuation: Pc, Pe, Pe

### any_word_char_check.ipynb

スクレイピングしたUnicodeカテゴリごとに `\w`にマッチする/しない文字をカウントする。

また、マッチしない文字の一覧を作成する。