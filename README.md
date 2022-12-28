# 2022 - 0'range Project (Backend, REST API)

2022년 멋쟁이사자처럼 대학 10기 해커톤에서 진행한 프로젝트입니다.

## Description

**Project Name :** 0'range

'0'과 'Range'를 묶은 단어로, '0'이 보이지 않는 것을 나타내는 숫자임에 기반한다. 여기서 보이지 않던 것은 우리들의 '상념'이라고 정의한다. 'Range'는 '범위, 대, 다양성'을 뜻하는 단어이다. 따라서 0'Range, 오렌지는 사람들의 상념을 가시화하여 드러냄으로써 그범위와 다양성을 토대로 퍼스널 브랜딩을 하는 공간을의미한다.




## Function
API 문서(배포 중단) : https://quaint-mercury-243.notion.site/API-docs-16c4dc134c7d4f668ed5d3695a1f83c4
 - 회원가입, 로그인, 로그아웃
 - 프로필 정보 보기, 편집
 - 팔로우, 언팔로우, 팔로워&팔로잉 보기
 - 내부 페르소나(value, weakness, strength, likes) CRUD
 - 외부 페르소나(solve, career, literacy, language, mbti) CRUD
 - 활동 추천(프리즘) 및 CRUD
 - 태그 CRUD
 
## System architecture

[**ER-Diagram**](https://www.erdcloud.com/d/aFsLMfgNiQKkNGeqf)
![orange_main](https://user-images.githubusercontent.com/86937253/209762682-e558bd47-66f5-45c8-bea9-aadfa7befccf.png)


## Environment

**Web Framework :** Django Rest Framework
**Database sys :** MySQL

## Prerequisite

 **requirements**
 
python ver : 3.8 이상
django ver : 3.2
django rest freamework ver : 3.12.2

 **settings.py > SECRET_KEY**
 아래 링크에서 스크릿키 생성 후 작성
 https://djecrety.ir/
