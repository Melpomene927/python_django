# python_django
實作RESTful API 並架設在Heroku

[測試網站](https://melpomene927.github.io/python_django/templates/test.html)

[Getting Started on Heroku with Python](https://devcenter.heroku.com/articles/getting-started-with-python)

### 使用工具
- [visual code](https://code.visualstudio.com/)
- [GIT](https://git-scm.com/)

### Markdown
- 參考資料
	- [語法說明](https://markdown.tw/#precode)
	- [線上編輯器](https://www.mdeditor.tw/)


```python
import pandas as pd
df=pd.read_clipboard()
df.to_csv('cathaybk.csv')
```



# GIT指令

```
1.版本號
git version


2.建立全域基本資訊
git config --global user.name jerry
git config --global user.email jerry@gmail.com

3.查詢資訊
git config --list

4.產生程式碼倉庫
git init


5.本地專案設定
git config user.name jerrychen
git config user.email jerrychen@gmail.com
git config --list
.git/config


6.工作區==>暫存區   
git add filename  # Untrack==>new file(U==>A)
git add .         # 一次全部加入

ps.產生對應的object(sha1編碼)


7.檢視(工作區/暫存區)狀態
git status	  # U/A/D/M



8.檢查sha-1格式的object
git cat-file -p sha-1 object

-t #型態
-p #內容
-s #大小


9.檢視在暫存區所有檔案
- git ls-file 
- git ls-file -s

10.進入暫存區後的修改
- git add ==>修改(modified)==>git add(確定修改) 
- git restore/checkout ==>恢復修改


11.準備commit(暫存區==>倉庫區)
- git commit -m "紀錄修改文案"


12.已經有進入倉庫區後的修改可以使用
- git commit -am "add 跟 commit一起)


13.修改上一次commit
- git commit --amend


ps.U=>A=>M 可以直接commit , 從倉庫區的修改都需要add


14.觀察commit log
- git log
- git log --oneline


15.git commit ==>進入vim模式
esc切換normal/insert
:w 	代表寫入 = 儲存
:q 	代表離開程式
:!  	代表強制執行
:q!	回到上一個動作
i	insert
a	append
o	new line



16.觀察檔案修改的差異
git diff filename
- 使用git restore/checkout 
- 使用git add 確定修改


17.刪除檔案

- 暫存區
	- git restore 恢復 
	- git add/rm  確認刪除	

- 倉庫區
	- git restore 恢復 
	- git add/rm  確認刪除
		- git commit 需要commit


18.git rm
暫存區
	- git rm --cached 恢復到工作區(U)
		- git add ==>暫存區
	- git rm -f 直接刪除檔案

倉庫區
	 git rm --cached 恢復到工作區(U)
		- git add ==>倉庫區

	 git rm/git rm -f
		- git commit ==>確認刪除 		
		- git restore --staged (unstage) ==>等同手動刪除
			- git add/rm  確認刪除
				- git commit 需要commit

18.git restore
	- 在暫存區/倉儲區刪除的檔案最後都可以使用git restore 進行恢復。
		- 倉庫區git rm時會比手動刪除時多一個git restore –staged指令(unstage)

19.分支操作
	-觀察目前分支
		-git branch		
	- 建立分支 git branch test
	- 切換分支 git checkout test
	- 刪除分支 git branch -D test
	- 合併分支 
		- git checkout master
		- git merge test

20.切換commit object 
	- 
	- 回到過去修正，需要新增branch
		-git checkout -b test		
	- git checkout master
		- git merge test
		- 衝突
	- git reflog 
		- git checkout commit object


21.git reset恢復到某一個commit object
	- 真正恢復到commit -->HEAD->master
	- git reset / git reset --soft 會保留之後的檔案
 	- git reset --hard 會刪除之後的檔案
	- git reset ORIG_HEAD
	
```

# 完成度
- [x] GIT基本指令
- [ ] GIT進階指令

# 繪製表格
### 繪製表格 Tables

| 專案        | 價格   |  數量  |
| --------   | -----:  | :----:  |
| 計算機      | $1600   |   5     |
| 手機        |   $12   |   12   |
| 管線        |    $1    |  234  |