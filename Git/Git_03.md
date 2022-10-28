# Git_03

## ✨ Git Undoing

- **Working Directory 작업 단계**
  - Working Directory에서 수정한 파일 내용을 이전 커밋 상태로 되돌리기
  - `git restore`
    - 이미 버전 관리가 되고 있는 파일만 관리 가능
- **Staging Area 작업 단계**
  - Staging Area에 반영된 파일을 Working Directory로 되돌리기
  - `git rm --cached`
    - root-commit이 없는 경우
  - `git restore --staged`
    - root-commit이 있는 경우
- **Repository 작업 단계**
  - 커밋을 완료한 파일을 Staging Area로 되돌리기
  - `git commit --amend`
    - Staging Area에 새로 올라온 내용이 없다면, 직전 커밋의 메시지만 수정
    - Staging Area에 새로 올라온 내용이 있다면, 직전 커밋을 덮어 씀.
    - 이전 커밋을 완전히 고쳐서 커밋을 변경하므로, 이전 커밋은 일어나지 않은 일이 되며 히스토리

<br/>

## ✨ Git Reset

- 시계를 마치 과거로 돌리는 듯한 행위로, 프로젝트를 특정 커밋(버전) 상태로 되돌림.
- 특정 커밋으로 되돌아 갔을 때, 해당 커밋 이후로 쌓았던 커밋들은 전부 사라짐.
- `git reset [옵션] {커밋 ID}`
  - 옵션
    - `soft` : 되돌아간 커밋 이후의 파일들은 Staging Area로 감.
    - `mixed` : 되돌아간 커밋 이후의 파일들은 Working Directory로 감. *(default)*
    - `hard` : 되돌아간 커밋 이후의 파일들은 모두 Working Directory에서 삭제
  - 커밋 ID
    - 되돌아가고 싶은 시점의 커밋 ID

<br/>

## ✨ Git Revert

- 과거를 없었던 일로 만드는 행위로, 이전 커밋을 취소한다는 새로운 커밋을 생성
- `git revert {취소할 커밋 ID}`
- git reset과의 차이점
  - reset은 커밋 내역을 삭제하는 반면 revert는 새로운 커밋을 생성
  - 깃헙을 이용해 협업할 때 커밋 내역의 차이로 인한 충돌 방지 가능

<br/>

## ✨ Git Branch

- 여러 갈래로 작업 공간을 나누어 독립적으로 작업할 수 있도록 도와주는 git의 도구
- 장점
  - 독립 공간을 형성하기 때문에 원본에 대해 안전
  - 하나의 작업은 하나의 브랜치로 나누어 진행되므로 체계적인 개발이 가능
  - git은 브랜치를 만드는 속도가 굉장히 빠르고 적은 용량을 소모

<br/>

## ✨ Git Branch 명령어

- 조회
  - `git branch` : 로컬 저장소의 브랜치 목록 확인
  - `git branch -r` : 원격 저장소의 브랜치 목록 확인
- 생성
  - `git branch {브랜치 이름}` : 새로운 브랜치 생성
  - `git branch {브랜치 이름} {커밋 ID}` : 특정 커밋 기준으로 브랜치 생성
- 삭제
  - `git branch -d {브랜치 이름}` : 병합된 브랜치만 삭제 가능
  - `git branch -D {브랜치 이름}` : 강제 삭제
- 다른 브랜치로 이동
  - `git switch {브랜치 이름}` : 다른 브랜치로 이동
  - `git switch -c {브랜치 이름}` : 브랜치를 새로 생성 및 이동
  - `git switch -c {브랜치 이름} {커밋 ID}` : 특정 커밋 기준으로 브랜치 생성 및 이동
  - **switch하기 전에 해당 브랜치의 변경 사항을 반드시 커밋해야 함을 주의!**
  - 다른 브랜치에서 파일을 만들고 커밋하지 않은 상태에서 switch하면
    브랜치를 이동했음에도 불구하고 해당 파일이 그대로 남아 있게 됨.

<br/>

## ✨ Git Merge

- 분기된 브랜치들을 하나로 합치는 명령어
- master 브랜치가 상용이므로 주로 master 브랜치에 병합
- `git merge {합칠 브랜치 이름}`
- 병합하기 전에 브랜치를 합치려고 하는 main branch로 switch 해야 함.
- 병합이 완료된 브랜치는 삭제
- 종류
  1. Fast-Forward
     - 마치 빨리감기처럼 브랜치가 가리키는 커밋을 앞으로 이동시키는 방법
     - 커밋의 수가 늘어나지 않음.
  2. 3-way Merge
     - 각 브랜치의 커밋 두 개와 공통 조상 하나를 사용하여 병합하는 방법
     - 커밋의 수가 늘어남. (새로운 커밋이 생김.)
  3. Merge Conflict

<br/>

## ✨ Git Workflow

- Branch와 원격 저장소를 이용해 협업을 하는 두 가지 방법

  1. 원격 저장소 소유권이 있는 경우 ➡ `Shared Repositroy Model`

  2. 원격 저장소 소유권이 없는 경우 ➡ `Fork & Pull Model`

<br/>

## ✨ Shared Repository Model

- 원격 저장소가 자신의 소유이거나 콜라보레이터로 등록되어 있는 경우
- master branch에 직접 개발하는 것이 아니라 **기능별로 브랜치를 따로 만들어 개발**
- pull request를 통해 팀원 간 변경 내용에 대한 소통 진행

<br/>

## ✨ Fork & Pull Model

- 자신의 소유가 아닌 원격 저장소인 경우 원본 원격 저장소를 그대로 내 원격 저장소에 복제 (Fork)
- 기능 완성 후 복제한 내 원격 저장소에 push
- 이후 pull request를 통해 원본 원격 저장소에 반영될 수 있도록 요청