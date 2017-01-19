import requests
from bs4 import BeautifulSoup
import os
from pandas import DataFrame
#금수저 웹툰 리스트 만들기
def webtoons_list_f(url):
    # url='http://comic.naver.com/webtoon/list.nhn?titleId=679567&weekday=sat&page=4'
    html=requests.get(url).text
    soup=BeautifulSoup(html,'lxml')


    webtoon_lists_parent=soup.find('td',{'class':'title'}).parent.parent
    webtoon_lists=webtoon_lists_parent.find_all('tr')[2:]

    mylist =[]

    for idx,webtoon_title in enumerate(webtoon_lists[::-1],len(webtoon_lists)):
        list=[]
        title=webtoon_title.img.get('title')
        href=webtoon_title.img.get('src')
        date=webtoon_lists[0].find('td',{'class':'num'}).text
        list.append(title)
        list.append(href)
        list.append(date)
        mylist.append(list)

    return mylist



#제목과 URL주소 리스트를 받아서 파일로 저장하는 함수
# webtoons_list_f의 리턴값 받아서 사용
def image_save_f(result_lists):

    for title,img_url,date in result_lists:

        filename=title
        filepath=os.path.join('data','금수저웹툰리스트',filename)
        dirpath=os.path.dirname(filepath)

        if not os.path.exists(dirpath):
            os.makedirs(dirpath) #그 위치에 디렉토리가 없으면 만들어줌

        if os.path.exists(filepath):
            print('이미 존재',filename)
        else:
            print('다운받을 것입니다.',filename)
        image_data=requests.get(img_url).content

        with open(filepath+'.jpg','wb') as f:
            f.write(image_data)


#URL 생성
#base_url='http://comic.naver.com/webtoon/list.nhn?titleId=679567&weekday&page'
def page_url(base_url):
    html=requests.get(base_url).text
    soup=BeautifulSoup(html,'lxml')
    page_num=len(soup.find_all('em',{'class':'num_page'}))
    url_list=[base_url+'='+str(page) for page in range(page_num,0,-1)]
    return url_list



## 웹툰 이미지 합치기
def save_webtoon(base_url,title,num):
    html=requests.get(base_url).text
    soup=BeautifulSoup(html,'lxml')
    for idx,img_tag in enumerate(soup.select('.wt_viewer img'),1):
        img_url=img_tag['src']
        if idx<10:
            filename = os.path.basename('0'+str(idx))
        else:
            filename = os.path.basename(str(idx))
        filepath = os.path.join("data",title+num, filename)  # 웹툰ID, EP ID, 이미지name
        dirpath = os.path.dirname(filepath)
        if not os.path.exists(dirpath):
            os.makedirs(dirpath)
        if os.path.exists(filepath):
            print('이미 존재:',filename)
        else:
            print('다운받을 것이오: ',filename)
        headers={
            'Referer': base_url,
            #'User-Agent':''
        }
        #TODO 캐싱 적용 가능
        image_data=requests.get(img_url,headers=headers).content

        with open(filepath+'.jpg','wb') as f:
            f.write(image_data)








#실행 방법
'''
## 동작
## 1.베이스 페이지 url을 page_url함수에 넣는다.
## 2.page_url함수 리턴값 url_list를 webtoons_list_f(url) 함수에 하나씩 넣는다.
## 3. 하나씩 넣은 값의 반환값 save_webtoon list를 image_save_f(result_lists) 값에 넣는다.
## 그러면 동작 완료
'''

url_list=page_url('http://comic.naver.com/webtoon/list.nhn?titleId=679567&weekday&page')

result=[]
for url in url_list:
    mylist = webtoons_list_f(url)
    for save in mylist:
        result.append(save)
    image_save_f(mylist)






# result=webtoons_list_f('http://comic.naver.com/webtoon/list.nhn?titleId=679567&weekday=sat&page=4')
# image_save_f(result)

data=DataFrame(result,columns=['title','link','date'])
b=data['title']
del data['title']
print(data.rename(index=b))
print(data)


# 웹툰 한회 저장
save_webtoon('http://comic.naver.com/webtoon/detail.nhn?titleId=626907&no=130&weekday=wed','패션','128화')

