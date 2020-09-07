# Algorithm-Study



## :books: 알고리즘 사이트

프로그래머스 : https://programmers.co.kr/learn/challenges?tab=all_challenges

백준 온라인 저지 : https://www.acmicpc.net/

codeground : https://www.codeground.org/practice

삼성 SW 아카데미 : https://swexpertacademy.com/main/main.do



## 알고리즘 공부 방법

### 먼저 본인에게 부족한 스킬이 무엇인지 파악하기

- **구현력**
  - 본인이 생각한 알고리즘을 그대로 소스코드로 구현하는 능력
  - 프로그램 순서도, 사용할 변수나 함수의 데이터 타입 등을 올바르게 정하는 과정
  - 이 스킬을 향상시키려면 **어떤 프로그램을 만들고자 하는지**를 명확히 해야한다
  - 무엇을 입력받아 어디에 저장하고 어떤 과정을 거쳐 중간 결과로 무엇을 얻고 최종적으로 어떤 결과물을 출력하는지 순서도를 적은 후 데이터 타입 또는 자료구조에 저장할지 생각하는 연습을 하자.
- **문제해결능력**
  - 알고있는 알고리즘, 자료구조, 테크닉을 당면한 문제에 맞게 변형 적용하는 것
  - 문제를 창의적인 시각에서 접근해 해결하는 능력이 필요
  - 중위권에서 상위권으로 갈 때 발목잡는 스킬
  - 이 능력이 부족하면 **어떻게 접근해야 할지**, **막상 솔루션은 내가 아는 알고리즘,자료구조** 인 상황이 연출된다
  - 이 스킬을 향상시키려면 **양질의 문제를 풀기**, **이전에 본인이 접근한 다양한 방법**을 잘 정리 해두는 것이 좋다
- **배경지식**
  - 기초적인 프로그래밍 문법, 알고리즘, 자료구조, 선형대수나 확률 등 기본적인 수학적 지식 (가끔 하드웨어, OS 지식)
  - 이 능력이 부족하면 **솔루션을 열었을때 외계어**를 마주하게 된다.
- 정해진 시간내에 문제풀때 문제 이해시간/풀이 생각시간/코딩시간/디버깅시간을 기록하며 어떤 부분이 구체적으로 부족한지 인지해서 부족한 부분에 더 노력을 들이기로



### 공부 순서

1. 알고리즘 관련 이론 공부하고 이해한다!
   * 자신이 이해할 수 있는 방식으로 이론을 정리
   * 정리한 이론을 github에 공유
2. 공부한 이론과 관련된 알고리즘 문제를 푼다.
   * 예시) Greedy 정리 -> Greedy 문제
   * 자신의 눈높이, 적당한 시간을 맞추어 푼다
   * 60~120분 내에 풀지 못하면 답을 본다
     * 비슷한 유형을 마주쳤을 때 풀 수 있도록 이해하자!!!
3. 이해가 안되는 문제는 질문하거나 자세한 풀이를 본다.
   * PS는 오랜 시간동안 고민하는 것 보다는 답을 보고 이해하고 비슷한 유형의 문제를 여러 문제 푸는 것이 더 좋다.
   * 쉬운 문제도 Okay
   * github에 Issue를 등록하거나 Pull Request를 날려서 질문!
     * 자신이 어디에 막혔는지, 무엇을 모르고 있는지 **명확히** 알아야 상대방도 답변이 가능하다.
4. 알고리즘 이해 후 코드 수정 or 다시 풀기
   * 자신이 접근한 방법을 README.md에 적는다.
     * 더 좋은 방법을 찾았다거나, 옳바른 접근에 대해서 README.md에 똑같이 적어둔다.

* 자신의 공부법 찾기!



## 스터디 진행 방식

### 공통문제

* 주에 1~2문제 예상
* 시간 정해두고 문제 풀기 (특정 시간)
  * 실제 코딩테스트 대비를 위해 시간을 정해두고 푸는 것을 권장 (최대 2시간 이내)
* 문제풀이 마크다운 작성 후 업로드
  * 개인 폴더/문제 폴더/README.md
  * 문제풀이 양식
    * https://github.com/TheCopiens/algorithm-study/blob/master/source/lee/team/200325_dp.md 참조!

**개인문제는 언제나 업로드 가능**

## Git 저장소 이용하는 방법

- 저장소 : https://github.com/LeeJeongHwi/Algorithm-Study

### 폴더 설명

- contents: 공동폴더. 알고리즘 관련 이론을 정리해서 업로드하는 폴더
- source: 개인 폴더. 필요한 개인폴더를 생성하고 알고리즘 풀이를 업로드하는 폴더



### GitBash 명령어 사용 방법

- [원격저장소의 브랜치를 생성하는 방법](https://github.com/TheCopiens/algorithm-study/blob/master/docs/github/howToCreate_branch.md#원격저장소의-브랜치를-생성하는-방법)
- [원격저장소의 브랜치를 로컬로 가져오는 방법](https://github.com/TheCopiens/algorithm-study/blob/master/docs/github/bring_remote_branch.md)
- [fork한 저장소 최신으로 동기화하는 방법](https://github.com/TheCopiens/algorithm-study/blob/master/docs/github/update_forkedRepo_from_originRepo.md#fork-한-repository-최신으로-동기화-하는-방법)

#### 원격저장소 로컬에 가져오기

```
git clone https://github.com/LeeJeongHwi/Algorithm-Study
```

#### 로컬에서 개인 브랜치 생성하기

local workspace에 'LeeJeongHwi'라는 이름으로 브랜치 생성
`git branch LeeJeongHwi`

#### 로컬에서 브랜치 작업후 원격저장소에 반영하기

로컬 브랜치가 있는 폴더에서 개인작업을 마친 후 공동 저장소에 반영한다.

1. `**git checkout LeeJeongHwi** `- master에서 LeeJeonghwi 브랜치로 전환
2. workspace에서 작업
3. `**git add .**`
4. `**git commit -m "message"**`
5. `**git push origin LeeJeongHwi** `- 원격저장소 LeeJeonghwi 브랜치에 반영
6. `**git checkout master** `- 브랜치 전환
7. `**git pull** `- 원격저장소 master의 최신 정보를 로컬에 업데이트 시키기
8. `**git merge LeeJeongHwi** `- master에 LeeJeonghwi 브랜치 작업 반영
9. `**git push origin master** `- 원격저장소 master에 반영

### 주의할 점

* `git checkout 브랜치이름` 을 수행 후 작업 하는 것이 마음에 편한다..!
* 위에 원격 저장소의 브랜치 생성,로컬가져오기 등 게시글을 확인하자!



## 참고 사이트

* https://github.com/TheCopiens/algorithm-study