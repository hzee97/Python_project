import platform
import requests
import webbrowser
from bs4 import BeautifulSoup
URL = 'https://ecampus.kangnam.ac.kr/'
LOGIN_URL = 'https://ecampus.kangnam.ac.kr/login/index.php'
LOGIN_HEADER = {
    'Referer': 'https://ecampus.kangnam.ac.kr/login.php',
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) '
                  'AppleWebKit/537.36 (KHTML, like Gecko) '
                  'Chrome/90.0.4430.85 Safari/537.36'
}
CSS_URL = 'https://ecampus.kangnam.ac.kr/theme/styles.php?theme=coursemosv2&rev=1620358043&type=all'
LOGIN_DATA = {
    'username': input("username : "),
    'password': input("password : ")
}

# #*** 테스트용 ***#
# LOGIN_DATA = {
#     'username': '201704049',
#     'password': '****'
# }

# Session 생성, with 구문 안에서 세션 유지, with 를 벗어나면 자동으로 세션 종료
with requests.Session() as s:
    # index.php에 로그인 요청
    response = s.post(LOGIN_URL, headers=LOGIN_HEADER, data=LOGIN_DATA)
    # 200이 나오면 정상 응답
    print("response.status_code :", response.status_code)
    # 이러닝홈페이지를 GET방식으로 가져옵니다.
    print("*** 이러닝홈페이지를 GET방식으로 가져옵니다. ***")
    page = s.get(URL)
    # 로그인이 정상적으로 되었는지 확인용도
    print("*** 로그인 성공 여부(-1은 실패) ***")
    print(page.text.find('로그아웃'))
    # 기존 메인 페이지 soup 만들기
    print("*** 기존 메인 페이지 soup 만들기 ***")
    soup = BeautifulSoup(page.text, 'html.parser')

    # f = open("originPage.html", "w", encoding="utf-8")
    # f.write(page.text)
    # f.close()

    # a태그 찾기
    print("*** a태그 찾기 ***")
    courseLinkTag = soup.select('.course_label_re_03 a')
    coursePageList = list()
    # attendCountList = list()
    attendTableList = list()
    # a태그 속 href 로 세션만들기
    print("*** a태그 속 href 로 세션만들기 ***")
    for courseLink in courseLinkTag:
        print(courseLink.get('href'))
        coursePageList.append(s.get(courseLink.get('href')))
    # 교과목 페이지에서 진도 현황 가져오기
    print("*** 교과목 페이지에서 진도 현황 가져오기 ***")
    for page in coursePageList:
        print(page.text.find('허지욱'))
        html = BeautifulSoup(page.text, 'html.parser')
        # attendCountList.append(html.select('.att_count'))
        attendTableList.append(html.select('.user_attendance_table'))
    # 진도 현황 가져와졌는지 출력해보기
    print("*** 진도 현황 가져와졌는지 출력해보기 ***")
    for div in attendTableList:
        print(div)

    # CSS 가져와서 css.text 에 저장
    # print("*** CSS 가져와서 css.text 에 저장 ***")
    # css = s.get(CSS_URL)
    # f = open("css.txt", "w", encoding="utf-8")
    # f.write(css.text)
    # f.close()

    # attendCountList 를 attendCountList.txt 파일로 저장
    # print("*** attendCountList 를 attendCountList.txt 파일로 저장 ***")
    # f = open("attendCountList.txt", "w", encoding="utf-8")
    # f.write("")
    # f = open("attendCountList.txt", "a", encoding="utf-8")
    # for div in attendCountList:
    #     f.write(str(div))
    # f.close()

    # attendTableList 를 attendTableList.txt 파일로 저장
    print("*** attendTableList 를 attendTableList.txt 파일로 저장 ***")
    f = open("attendTableList.txt", "w", encoding="utf-8")
    f.write("")
    f = open("attendTableList.txt", "a", encoding="utf-8")
    for div in attendTableList:
        f.write(str(div))
    f.close()

    # attendCountList.txt 파일을 soup 으로 만듬
    # print("*** attendCountList.txt 파일을 soup 으로 만듬 ***")
    # f = open("attendCountList.txt", "r", encoding="utf-8")
    # soupAttendCountList = BeautifulSoup(f.read(), 'html.parser')
    # f.close()

    # attendTableList.txt 파일을 soup 으로 만듬
    print("*** attendTableList.txt 파일을 soup 으로 만듬 ***")
    f = open("attendTableList.txt", "r", encoding="utf-8")
    soupAttendTableList = BeautifulSoup(f.read(), 'html.parser')
    f.close()
    # css 적용하기
    div_table_css = "box-sizing : border-box; color : rgb(51, 51, 51); " \
                    "font-family : NanumGothic; font-size : 14px; " \
                    "line-height : 20px; text-size-adjust : 100%; width : 100%;"
    ul_css = "border-top-color : rgb(235, 235, 235); " \
             "border-top-style : solid; border-top-width : 1px; " \
             "border-bottom-color : rgb(235, 235, 235); " \
             "border-bottom-style : solid; border-bottom-width : 1px; " \
             "box-sizing : border-box; color : rgb(51, 51, 51); " \
             "line-height : 20px; list-style-image : none; " \
             "list-style-position : outside; list-style-type : none;"
    li_active01_css = "box-sizing : border-box; display : list-item; " \
                      "float : left; height : 80px; width : 38.75px; " \
                      "font-size : 12px; font-weight : 600; line-height : 17.1429.px; " \
                      "text-align : center; text-size-adjust : 100%; " \
                      "color : rgb(42, 123, 205); background-color : rgb(255, 255, 255); " \
                      "border-right-color : rgb(235, 235, 235); border-right-style : solid; " \
                      "border-right-width : 1px; list-style-image : none; list-style-position : outside;" \
                      "-webkit-tap-highlight-color : rgba(0, 0, 0, 0); "
    li_active02_css = "box-sizing : border-box; display : list-item; " \
                      "float : left; height : 80px; width : 38.75px; " \
                      "font-size : 12px; font-weight : 600; line-height : 17.1429.px; " \
                      "text-align : center; text-size-adjust : 100%; " \
                      "color : rgb(220, 86, 72); background-color : rgb(255, 255, 255); " \
                      "border-right-color : rgb(235, 235, 235); border-right-style : solid; " \
                      "border-right-width : 1px; list-style-image : none; list-style-position : outside;" \
                      "-webkit-tap-highlight-color : rgba(0, 0, 0, 0); "
    li_inactive_css = "box-sizing : border-box; display : list-item; " \
                      "float : left; height : 80px; width : 38.75px; " \
                      "font-size : 12px; font-weight : 600; line-height : 17.1429.px; " \
                      "text-align : center; text-size-adjust : 100%; " \
                      "color : rgb(153, 153, 153); background-color : rgb(245, 245, 246); " \
                      "border-right-color : rgb(235, 235, 235); border-right-style : solid; " \
                      "border-right-width : 1px; list-style-image : none; list-style-position : outside;" \
                      "-webkit-tap-highlight-color : rgba(0, 0, 0, 0); "
    p_active01_css = "descript : active01; "\
                     "background-color : rgb(51, 140, 204); " \
                     "border-bottom-color : rgb(51, 140, 204); " \
                     "border-bottom-left-radius : 50%; " \
                     "border-bottom-right-radius : 50%; " \
                     "border-bottom-style : solid; " \
                     "border-bottom-width : 1px; " \
                     "border-image-outset : 0; " \
                     "border-image-repeat : stretch; " \
                     "border-image-slice : 100%; " \
                     "border-image-source : none; " \
                     "border-image-width : 1; " \
                     "border-left-color : rgb(51, 140, 204); " \
                     "border-left-style : solid; " \
                     "border-left-width : 1px; " \
                     "border-right-color : rgb(51, 140, 204); " \
                     "border-right-style : solid; " \
                     "border-right-width : 1px; " \
                     "border-top-color : rgb(51, 140, 204); " \
                     "border-top-left-radius : 50%; " \
                     "border-top-right-radius : 50%; " \
                     "border-top-style : solid; " \
                     "border-top-width : 1px; " \
                     "box-sizing : border-box; " \
                     "color : rgb(255, 255, 255); " \
                     "cursor : pointer; " \
                     "font-size : 16px; " \
                     "font-weight : 600; " \
                     "height : 32px; " \
                     "line-height : 32px; " \
                     "list-style-image : none; " \
                     "list-style-position : outside; " \
                     "list-style-type : none; " \
                     "margin-block-end : 10px; " \
                     "margin-block-start : 13px; " \
                     "margin-bottom : 10px; " \
                     "margin-inline-end : 2.875px; " \
                     "margin-inline-start : 2.875px; " \
                     "margin-left : 2.875px; " \
                     "margin-right : 2.875px; " \
                     "margin-top : 13px; " \
                     "text-align : center; " \
                     "text-size-adjust : 100%; " \
                     "width : 32px;" \
                     "-webkit-tap-highlight-color : rgba(0, 0, 0, 0); "
    p_active02_css = "descript : active02; "\
                     "background-color : rgb(220, 86, 72); " \
                     "border-bottom-color : rgb(220, 86, 72); " \
                     "border-bottom-left-radius : 50%; " \
                     "border-bottom-right-radius : 50%; " \
                     "border-bottom-style : solid; " \
                     "border-bottom-width : 1px; " \
                     "border-image-outset : 0; " \
                     "border-image-repeat : stretch; " \
                     "border-image-slice : 100%; " \
                     "border-image-source : none; " \
                     "border-image-width : 1; " \
                     "border-left-color : rgb(220, 86, 72); " \
                     "border-left-style : solid; " \
                     "border-left-width : 1px; " \
                     "border-right-color : rgb(220, 86, 72); " \
                     "border-right-style : solid; " \
                     "border-right-width : 1px; " \
                     "border-top-color : rgb(220, 86, 72); " \
                     "border-top-left-radius : 50%; " \
                     "border-top-right-radius : 50%; " \
                     "border-top-style : solid; " \
                     "border-top-width : 1px; " \
                     "box-sizing : border-box; " \
                     "color : rgb(255, 255, 255); " \
                     "cursor : pointer; " \
                     "font-size : 16px; " \
                     "font-weight : 600; " \
                     "height : 32px; " \
                     "line-height : 32px; " \
                     "list-style-image : none; " \
                     "list-style-position : outside; " \
                     "list-style-type : none; " \
                     "margin-block-end : 10px; " \
                     "margin-block-start : 13px; " \
                     "margin-bottom : 10px; " \
                     "margin-inline-end : 2.875px; " \
                     "margin-inline-start : 2.875px; " \
                     "margin-left : 2.875px; " \
                     "margin-right : 2.875px; " \
                     "margin-top : 13px; " \
                     "text-align : center; " \
                     "text-size-adjust : 100%; " \
                     "width : 32px;" \
                     "-webkit-tap-highlight-color : rgba(0, 0, 0, 0); "
    p_inactive_css = "descript : inactive; "\
                     "box-sizing : border-box; " \
                     "display : block; " \
                     "height : 32px; " \
                     "margin-bottom : 10px; " \
                     "margin-left : 2.875px; " \
                     "margin-right : 2.875px; " \
                     "margin-top : 13px; " \
                     "width : 32px; " \
                     "font-size : 16px; " \
                     "font-weight : 600; " \
                     "line-height : 32px; " \
                     "text-align : center; " \
                     "text-size-adjust : 100%; " \
                     "color : rgb(153, 153, 153); " \
                     "border-bottom-color : rgb(204, 204, 204); " \
                     "border-bottom-style : solid; " \
                     "border-bottom-width : 1px; " \
                     "border-image-outset : 0; " \
                     "border-image-repeat : stretch; " \
                     "border-image-slice : 100%; " \
                     "border-image-source : none; " \
                     "border-image-width : 1; " \
                     "border-left-color : rgb(204, 204, 204); " \
                     "border-left-style : solid; " \
                     "border-left-width : 1px; " \
                     "border-right-color : rgb(204, 204, 204); " \
                     "border-right-style : solid; " \
                     "border-right-width : 1px; " \
                     "border-top-color : rgb(204, 204, 204); " \
                     "border-top-style : solid; " \
                     "border-top-width : 1px; " \
                     "cursor : pointer; " \
                     "border-bottom-left-radius : 50%; " \
                     "border-bottom-right-radius : 50%; " \
                     "border-top-left-radius : 50%; " \
                     "border-top-right-radius : 50%; " \
                     "list-style-image : none; " \
                     "list-style-position : outside; " \
                     "list-style-type : none; " \
                     "margin-block-end : 10px; " \
                     "margin-block-start : 13px; " \
                     "margin-inline-end : 2.875px; " \
                     "margin-inline-start : 2.875px; "
    # att_count 하위 css 필요
    div_count_css = "text-size-adjust: 100%; " \
                    "-webkit-tap-highlight-color: rgba(0,0,0,0); " \
                    "line-height: 1.42857143; " \
                    "color: #333; " \
                    "box-sizing: border-box; " \
                    "font-family: NanumGothic, dotum, sans-serif; " \
                    "font-size: 12px; " \
                    "margin-top: 10px; "
    p_count01_css = "text-size-adjust: 100%; " \
                    "-webkit-tap-highlight-color: rgba(0,0,0,0); " \
                    "line-height: 1.42857143; " \
                    "font-size: 12px; " \
                    "box-sizing: border-box; " \
                    "margin: 0 0 10px; " \
                    "font-family: NanumGothic,dotum,Helvetica,sans-serif,AppleGothic; " \
                    "float: left; " \
                    "color: #999; " \
                    "padding: 0 15px; "
    p_count02_css = "box-sizing: border-box; " \
                    "color: #999; " \
                    "display: block; " \
                    "float: left; " \
                    "font-family: NanumGothic,dotum,Helvetica,sans-serif,AppleGothic; " \
                    "font-size: 12px; " \
                    "line-height: 1.42857143; " \
                    "margin-block-end: 10px; " \
                    "margin-block-start: 0px; " \
                    "margin-bottom: 10px; " \
                    "margin-inline-end: 0px; " \
                    "margin-inline-start: 0px; " \
                    "margin-left: 0px; " \
                    "margin-right: 0px; " \
                    "margin-top: 0px; " \
                    "padding-bottom: 0px; " \
                    "padding-left: 15px; " \
                    "padding-right: 15px; " \
                    "padding-top: 0px; " \
                    "text-size-adjust: 100%; " \
                    "-webkit-tap-highlight-color: rgba(0,0,0,0); "
    span_count01_css = "text-size-adjust: 100%; " \
                       "-webkit-tap-highlight-color: rgba(0,0,0,0); " \
                       "line-height: 1.42857143; " \
                       "font-size: 12px; " \
                       "box-sizing: border-box; " \
                       "font-family: NanumGothic,dotum,sans-serif; " \
                       "color: #333; "
    span_count02_css = "box-sizing: border-box; " \
                       "color: #333; " \
                       "font-family: NanumGothic,dotum,sans-serif; " \
                       "font-size: 12px; " \
                       "line-height: 1.42857143; " \
                       "text-size-adjust: 100%; " \
                       "-webkit-tap-highlight-color: rgba(0,0,0,0); "
    before_count01_css = ""
    before_count02_css = ""
    print("*** css 적용하기 ***")
    for div in soupAttendTableList.select(".user_attendance_table"):
        div['style'] = div_table_css
    for ul in soupAttendTableList.select(".attendance"):
        ul['style'] = ul_css
    for li in soupAttendTableList.select(".attendance > li"):
        # class명에 공백이 있어 list형태로 들어와서 1번째와 비교 (아래 형태)
        # ['attendance_section', 'active', 'name_text1', 'piece_16']
        if str(li['class'][1]) == "active":
            if str(li['class'][2]) == "name_text1":
                li['style'] = li_active01_css
                li.select_one(".sname")['style'] = p_active01_css
            else:
                li['style'] = li_active02_css
                li.select_one(".sname")['style'] = p_active02_css
        else:
            li['style'] = li_inactive_css

        for p in soupAttendTableList.select(".sname"):
            if str(li['class'][1]) == "active":
                if str(li['class'][2]) == "name_text1":
                    print("출석 css 적용됨 ")
                    p['style'] = p_active01_css
                else:
                    print("결석 css 적용됨")
                    p['style'] = p_active02_css
            else:
                print("빈칸 css 적용됨")
                p['style'] = p_inactive_css
            li.select_one(".sname")['style'] = p_inactive_css

    for div in soupAttendTableList.select(".att_count"):
        div['style'] = div_count_css
    for p in soupAttendTableList.select(".count01"):
        p['style'] = p_count01_css
    for p in soupAttendTableList.select(".count02"):
        p['style'] = p_count02_css
    for span in soupAttendTableList.select(".count01 > span"):
        span['style'] = span_count01_css
    for span in soupAttendTableList.select(".count02 > span"):
        span['style'] = span_count02_css
    # 각 강좌 버튼에 진도 현황 붙이기
    print("*** 각 강좌 버튼에 진도 현황 붙이기 ***")
    for course in soup.select(".course_label_re_03"):
        course.append(soupAttendTableList.select(".user_attendance_table")[0])
    # reformPage.html로 저장
    print("*** reformPage.html로 저장 ***")
    f = open("reformPage.html", "w", encoding="utf-8")
    f.write(str(soup))
    f.close()
    # MacOS
    chrome_path_mac = 'open -a /Applications/Google\ Chrome.app %s'
    # Windows
    chrome_path_windows = 'C:/Program Files (x86)/Google/Chrome/Application/chrome.exe %s'
    # Linux
    chrome_path_linux = '/usr/bin/google-chrome %s'
    # Mac : 'Darwin', Windows : 'Windows', Linux : 'Linux'
    os = platform.system()
    print("os :", os)
    print("*** 창 열림 ***")
    if os == 'Darwin':
        webbrowser.get(chrome_path_mac).open('reformPage.html')
    elif os == 'Windows':
        webbrowser.get(chrome_path_windows).open('reformPage.html')
    elif os == 'Linux':
        webbrowser.get(chrome_path_linux).open('reformPage.html')
    else:
        print("운영체제를 찾지 못했습니다.")
