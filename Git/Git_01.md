# Git_01

## ✨ CLI(Command Line Interface)

- <-> GUI(Graphic User Interface)

* `~` : 사용자의 홈 디렉토리(폴더)

* `루트 디렉토리` : 이 머신의 가장 상위 디렉토리(폴더)

* 절대경로 : from `루트 디렉토리` to `목적 파일`까지의 모든 경로가 포함된 것.

  ```
  C:/users/SSAFY/a.txt
  ```

* 상대경로 : 현재 작업중인 디렉토리를 기준으로 계산한 상대적 위치

  * `./` :  현재 폴더
  *  `../` : 상위 폴더

  ``` bash
  C://users/SSAFY/sky/a.txt		# a 기준으로
  
  C://users/SSAFY/sky/b.txt		# b의 위치는 ./b.txt
  
  C://users/SSAFY/c.txt				# c의 위치는 ../c.txt
  
  C://users/SSAFY/kbk/k.txt		# k의 위치는 ../kbk/t.txt
  ```



## ✨ 기본적인 명령어

* `touch` : 파일을 생성하는 명령어, 띄어쓰기로 여러 파일을 한 번에 생성 가능

  ``` bash
  touch a.txt b.txt
  ```

* `start` : 폴더를 열어주는 명령어

  ```bash
  start .			# 현재 폴더를 엶.
  ```

* `mkdir` : *make directory.* 새 폴더를 만드는 명령어

  ``` bash
  mkdir folder_name
  mkdir 'folder name'
  ```

* `ls` : *list.* 현재 폴더의 리스트를 보여주는 명령어

  ```bash
  ls -a			# 숨겨놓은 파일까지 다 보여줌.
  ls -l			# 모든 파일의 정보를 자세히 보여줌.
  ```

* `pwd` : *print working directory.*  현재 위치를 알려주는 명령어

* `cd` : *change directory.* 폴더를 이동하는 명령어

  ```bash
  cd ..			# 상위 폴더로 이동
  cd test 	# test 폴더로 이동
  ```

* `mv` : *move.*

  ```bash
  mv a.txt b.txt			# a.txt를 b.txt로 rename (a.txt와 b.txt가 같은 폴더內이므로)
  mv a.txt ../test		# a.txt를 상위 폴더의 test 폴더로 이동
  ```

* `rm` : *remove.* 복구 안 됨.

  ```bash
  rm a.txt
  ```



## ✨ Git 기본기

* **커밋**은 `Working Directory`, `Staging Area`, `Repository` 의 3가지 영역을 바탕으로 동작
* `Repository` : 특정 디렉토리를 버전 관리하는 저장소

* `git init` : `Working Directory`에 프로젝트 생성하는 기능

  ```bash
  git init			# untracked file 상태
  ```

* `git config` : 사용자 설정

  ```bash
  git config --global user.name your_name
  git config --global user.email your_email
  git config --global --list			# 본인이 등록한 git 사용자 정보 확인
  ```

* `git add` : `Staging Area`에 untracked file 옮겨두는 기능

  ```bash
  git add ny_pjt.txt
  ```

* `git commit` : `Repository`에 version 확정하여 업로드하는 기능

  ```bash
  git commit -m "1st commit"			#'1st commit'이라는 메시지와 함께 커밋
  ```

* `git status` : 현재 git의 상태를 보여주는 명령어

  ```bash
  # 결과
  $ git status
  On branch master
  
  No commits yet								# Repository에 있는 파일
  
  Changes to be committed:			# Staging Area에 있는 파일
    (use "git rm --cached <file>..." to unstage)
          new file:   ny_pjt.txt
  
  Untracked files:							# Working Area에 있는 파일
    (use "git add <file>..." to include in what will be committed)
          a.txt
          b.txt
  ```

* `git log` : 커밋한 기록을 조회하는 명령어

  ```bash
  git log
  # 결과
  commit 498021ac1986f79b199fd34b675914efada3558f (HEAD -> master)
  Author: your_name <your_mail>
  Date:   Fri Jul 15 16:00:58 2022 +0900
  
      1st commit
  
  git log --oneline				# 커밋 기록을 한 줄로 보여줌.
  # 결과
  498021a (HEAD -> master) 1st commit
  ```



## ✨ GitHub

* git의 방식을 사용해서 파일을 관리하는 원격 관리 시스템

* `git push` : local PC의 git을 GitHub에 업로드

* `git clone` : **local PC에 git이 아무 것도 없을 때,** GitHub의 git을 local PC에 다운로드

  ```bash
  git clone https://github.com/your_name/folder_name.git receive_folder
  ```

* `git pull` : GitHub의 git을 local PC에 다운로드

  ```bash
  git pull origin master
  ```

* `git remote add` : local PC와 GitHub 사이에 다리를 놓는 명령어

  ```bash
  git remote add origin https://github.com/your_name/folder_name.git
  git remote -v					# remote 결과 확인
  git push -u origin master
  ```

  