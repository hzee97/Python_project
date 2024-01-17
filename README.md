# 이러닝캠퍼스 UI 개선하기

### 💡프로젝트 배경

기존의 이러닝캠퍼스의 경우에는, 수강과목에 하나하나 들어가 개별적으로 정보를 확인했어야해서 비효율적이였고, 출석여부를 한눈에 파악하기 어려웠습니다. 
그러다보니 출석을 놓치는 경우가 생기는 경우가 많아, 이를 바탕으로 기존의 프로그램에 추가 기능을 구현하여 학생들이 좀 더 편하게 사용할 수 있는 이러닝캠퍼스를 개선하는 프로젝트를 진행하게 되었습니다.

### ✨동작구조
1. Session을 통한 이러닝 캠퍼스 로그인
2. BeautifulSoup을 이용해 페이지 html 파싱
3. href 태그를 이용해 각 과목 페이지 접근
4. 출석 현황 html 코드 파싱
5. 메인페이지 html에 삽입
6. webbrowser 모듈을 이용해 수정된 html을 크롬으로 동작

### 📌사용모듈
* Webbrowser
* BeautifulSoup
* Requests
* Platform

### ⭐사용방법
main.py를 실행하고 콘솔창에 학번과 비밀번호를 입력하면 'reformPage.html' 파일이 생기고 크롬에서 열리게 됩니다.

</br>

<img src="https://github.com/hzee97/Python_project/assets/136284855/23426328-9e65-44f9-8e11-257bba440632.png" width="800" height="400"/>


### 🌈결과 (Before)

</br>

<img src="https://github.com/hzee97/Python_project/assets/136284855/71f42d01-5296-4d09-8958-80357a2bbdc2.png" width="800" height="400"/>

### 🌈결과 (After)

</br>

<img src="https://github.com/hzee97/Python_project/assets/136284855/6f04f20b-d713-4176-91c8-d675b96c7229.png" width="800" height="400"/>



