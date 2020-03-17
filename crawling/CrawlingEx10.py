'''
# requests
url 요청 : get(url)
# Beautifulsoup parsing
html.parser , html5lib, lxm,
# bs 객체 필요한 데이터 검색
find() : 필요한 데이터 한개 가져옴 (가장 먼저 검색되는 요소)
    태그 - find('태그명')
    id - find(id='id속성값')
    class - find(class_='class속성값')
    중복 - find('태그명', id or class)
            find('a', 'test')   : a태그 class속성값이 'test' 인 것 검색
    속성 : 속성값 - find('태그명', attrs={'class':'test'})
find_all() : 전체 태그 반환
select() : CSS 선택자로 찾기
    태그 - select('태그명')
    class - select('.클래스속성값')
    id - select('#id속성값')
    태그+class - select('태그명.class속성값')
    태그+id - select('태그명#id속성값')
    자식 - select('태그명 _a') : 자식을 가르킬때는 띄어쓰기

    <a class='test abc'>...</a>
    select('a.test.abc')

'''