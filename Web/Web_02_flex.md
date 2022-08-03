# Web_02_flex

## ✨ Float

- 박스를 왼쪽 혹은 오른쪽으로 이동시켜 텍스트를 포함한 인라인 요소들이 주변을 wrapping하도록 함.
- 요소가 normal flow를 벗어나도록 함.
- **Float 속성**
    - `none` : 기본값
    - `left` : 요소를 왼쪽으로 띄움
    - `right` : 요소를 오른쪽으로 띄움

<br/>

## ✨ Flexbox

- 행과 열 형태로 아이템들을 배치하는 1차원 레이아웃 모델
- **축**
    - `main axis` (메인 축)                      *꼬치 방향*
    - `cross axis` (교차 축)                    *꼬치를 먹는 방향*
- **구성 요소**
    - `Flex Container` (부모 요소)        *부모 요소에 flex 적용*
    - `Flex Item` (자식 요소)
- **장점**
    - 수직 정렬 가능
    - 아이템의 너비와 높이 혹은 간격을 동일하게 배치

<br/>

## ✨ Flexbox 속성

- **배치 설정**
    - **flex-direction**            *reverse의 경우 HTML 태그 선언 순서와 시각적으로 다르니 유의! (웹 접근성에 영향)*
        - flex-direction: row : `main axis`  ➡️
        - flex-direction: row-reverse : `main axis` ⬅️
        - flex-direction: column : `main axis` ⬇️
        - flex-direction: column-reverse : `main axis` ⬆️
    - **flex-wrap**
        - 아이템이 컨테이너를 벗어나는 경우 해당 영역 내에 배치되도록 설정
        - 즉, 기본적으로 컨테이너 영역을 벗어나지 않도록 함.
        - flex-wrap: nowrap : flex item의 **크기를 조절**하여 한 줄에 배치
        - flex-wrap: wrap : flex item의 **크기를 조절하지 않고** 다음 줄에 배치
        - flex-wrap: wrap-reverse
    - **flex-flow**
        - flex-direction과 flex-wrap의 shorthand
        - fiex-direction과 flex-wrap에 대한 설정 값을 차례로 작성
        - flex-flow: row nowrap;
- **공간 나누기**
    - **justify-content** (`main axis`)
        - justify-content: flex-start : 아이템들을 axis 시작점으로
        - justify-content: flex-end : 아이템들을 axis 끝점으로
        - **justify-content: center** : 아이템들을 axis 중앙으로
        - justify-content: space-between : 여백을 균등하게 *(양 옆 미포함)*
        - justify-content: space-around : 각 flex-item의 양 옆 여백을 균등하게
        - justify-content: space-evenly : 여백을 균등하게 *(양 옆 포함)*
    - **align-content** (`cross axis`)              *아이템이 한 줄로 배치되는 경우 확인 불가*
        - align-content: flex-start
        - align-content: flex-end
        - align-content: center
        - align-content: space-between
        - align-content: space-around
        - align-content: space-evenly

- **정렬**

    - **align-items** (모든 아이템을 `cross axis` 기준으로)
        - align-items: stretch : 아이템을 flex-container 만큼 `cross axis` 방향으로 늘림
        - align-items: flex-start
        - align-items: flex-end
        - **align-items: center** : 세로 가운데 정렬
        - align-items: baseline : 아래 글자축 정렬
    - **align-self** (개별 아이템을 `cross axis` 기준으로)
        - align-self: stretch
        - align-self: flex-start
        - align-self: flex-end
        - align-self: center

- **기타**

    - **flex-grow** : 남은 영역을 아이템에 분배

        ```css
        .item1 {
          flex-grow: 1;
        }
        
        .item2 {
          flex-grow: 1;
        }
        
        .item3 {
          flex-grow: 2;
        }
        
        // item1, item2, item3에 남은 여백을 1:1:2 비율로 할당
        ```

    - **order** : 배치 순서