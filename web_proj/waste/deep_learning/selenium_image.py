from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from webdriver_manager.chrome import ChromeDriverManager
import json
import os
import urllib
import argparse
from django.core.files.base import ContentFile
from bs4 import BeautifulSoup
import base64
 

def save_image(f_data, f_name,searchterm):
    global succounter
    with open(os.path.join(os.getcwd(), searchterm, f_name),'wb+') as destination:
        for chunk in f_data.chunks():
            destination.write(chunk)
    succounter+=1

    #os.remove("media/"+str(x.name))
    #print(str(x.name)+"삭제완료")
def sel(searchterm,cnt):
    global succounter
    url = "https://www.google.co.in/search?q="+searchterm+"&source=lnms&tbm=isch"
    browser = webdriver.Chrome(ChromeDriverManager().install())
    browser.get(url)
    header={'User-Agent':"Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/43.0.2357.134 Safari/537.36"}
    counter = 0
    
    if not os.path.exists(list_eng[cnt]):
        os.mkdir(list_eng[cnt])
    
    for _ in range(200):
        browser.execute_script("window.scrollBy(0,10000)")
        try:
            browser.find_element_by_xpath('//input[contains(@class,"mye4qd")]').click()
        except:
            print("")
    
    for x in browser.find_elements_by_xpath('//img[contains(@class,"rg_i")]'):
        
        print("Total Count:", counter)
        print("Succsessful Count:", succounter)

        
        imgstr_data = x.get_attribute('src')
        if(imgstr_data is None):
            imgstr_data = x.get_attribute('data-src')
            if(imgstr_data is None):
                continue
        
        counter = counter + 1
        file_name = searchterm + "_" + str(counter) + ".jpg"
        print("imgstr_data : " + imgstr_data)
        if('http' in imgstr_data):
            html = urllib.request.urlopen(imgstr_data)
            urllib.request.urlretrieve(imgstr_data, list_eng[cnt]+"/"+file_name)
            succounter +=1
            continue
        
        format, imgstr = imgstr_data.split(';base64,') 
        ext = format.split('/')[-1] 
        imgstr += "=" * ((4 - len(imgstr) % 4) % 4)
        print("imgstr : " + imgstr)
        print("file_name :" + file_name)
        data = ContentFile(base64.b64decode(imgstr), name=file_name) # You can save this as file instance.
        
        save_image(data, file_name, list_eng[cnt])
        
    print(succounter, "pictures succesfully downloaded")
    browser.close()

list = ['유모차'
#'모뎀',
# '목재'
# '마네킹',
# '믹서기',
# '물탱크',
# '문갑',
# '문짝',
# '청소기',
# '천막',
# '창문',
# '찬장',
# '침대',
# '책꽂이',
# '책상',
# '책장',
# '유모차',
# '유아용목마',
# '유아용자동차',
# '오디오',
# '오락기',
# '온수기',
# '온풍기',
# '어항',
# '아이스박스',
# '안마의자',
# '안마기',
# '이불',
# '인형',
# '의자',
# '우산',
# '액자',
# '에어컨',
# 'DVD',
# '욕조',
# '도마',
# '돗자리',
# '다리미',
# '다리미판',
# '대리석식탁',
# '런닝머신',
# '라지에타',
# '라텍스베개',
# '라켓',
# '렌지대수납장',
# '휴대폰충전기',
# '화이트보드',
# '화환',
# '화분',
# '환풍기',
# '화장대',
# '항아리',
# '휠체어',
# '헤어드라이어',
# '헹거',
# '헬스자전거',
# '보일러',
# '보행기',
# '복사기',
# '방석',
# '바둑판',
# '발마사지기게',
# '발래건조대',
# '비데',
# '비키니옷장',
# '블라인드',
# '분말소화기',
# '배기후드',
# '병풍',
# '벽시게',
# '변기',
# '고무통',
# '공기청정기',
# '골프채가방',
# '거울',
# '거실장',
# '가방',
# '간판',
# '가스오븐레인지',
# '가스레인지',
# '가습기',
# '가정오르간',
# '김치냉장고',
# '기름탱크',
# '금고',
# '개수대',
# '교자상',
# '녹즙기',
# '노트북',
# '난로',
# '냉장고',
# '서랍장',
# '선풍기',
# '쌀통',
# '싱크대',
# '실외기',
# '식기건조기',
# '식기세척기',
# '식탁',
# '신발',
# '신발장',
# '쓰레기통',
# '스탠드옷걸이',
# '스텝퍼',
# '스키세트',
# '스캐너',
# '수도호스',
# '세면대',
# '세단기',
# '세탁기',
# 'TV',
# 'TV받침',
# '쇼파',
# '파렛트',
# '파티션',
# '피아노',
# '프린터',
# '팩시밀리',
# '팬히터',
# '조명기구',
# '정수기',
# '전화기',
# '전기담요',
# '전기밥솥',
# '전기판넬',
# '전자레인지',
# '장롱',
# '장난감',
# '장식장',
# '장판',
# '자동판매기',
# '자전거',
# '진열대',
# '재봉틀',
# '토스터기',
# '타이어',
# '탈수기',
# '탁구대',
# '탁자',
# '텐트',
# '컴퓨터',
# '컬러박스',
# '커피포트',
# '커튼',
# '커튼봉',
# '카세트라디오',
# '킥보드',
# '캐비닛'
]

list_eng = ['dbahck'
# 'ahepa',
# 'ahrwo',
# 'akspzld',
# 'alrtjrl',
# 'anfxodzm',
# 'ansrkq',
# 'answkr',
# 'cjdthrl',
# 'cjsakr',
# 'ckdans',
# 'ckswkd',
# 'claeo',
# 'corrhwdl',
# 'cortkd',
# 'corwkd',
# 'dbahck',
# 'dbdkdydahrak',
# 'dbdkdydwkehdck',
# 'dheldh',
# 'dhfkrrl',
# 'dhstnrl',
# 'dhsvndrl',
# 'djgkd',
# 'dkdltmqkrtm',
# 'dksakdmlwk',
# 'dksakrl',
# 'dlqnf',
# 'dlsgud',
# 'dmlwk',
# 'dntks',
# 'dorwk',
# 'dpdjzjs',
# 'dvd',
# 'dyrwh',
# 'ehak',
# 'ehtwkfl',
# 'ekflal',
# 'ekflalvks',
# 'eofltjrtlrxkr',
# 'fjssldajtls',
# 'fkwldpxk',
# 'fkxprtmqpro',
# 'fkzpt',
# 'fpswleotnskqwkd',
# 'gbeovhscndwjsrl',
# 'ghkdlxmqhem',
# 'ghkghks',
# 'ghkqns',
# 'ghksvndrl',
# 'ghkwkdeo',
# 'gkddkfl',
# 'gnlfcpdj',
# 'gpdjemfkdldj',
# 'gpdrj',
# 'gpftmwkwjsrj',
# 'qhdlffj',
# 'qhgodrl',
# 'qhrtkrl',
# 'qkdtjr',
# 'qkenrvks',
# 'qkfaktkwlrlrp',
# 'qkfforjswheo',
# 'qlep',
# 'qlzlsldhtwkd',
# 'qmffkdlsem',
# 'qnsakfthghkrl',
# 'qorlgnem',
# 'qudvnd',
# 'qurtlrp',
# 'qusrl',
# 'rhanxhd',
# 'rhdrlcjdwjdrl',
# 'rhfvmcorkqkd',
# 'rjdnf',
# 'rjtlfwkd',
# 'rkqkd',
# 'rksvks',
# 'rktmdhqmsfpdlswl',
# 'rktmfpdlswl',
# 'rktmqrl',
# 'rkwjddhfmrks',
# 'rlaclsodwkdrh',
# 'rlfmaxodzm',
# 'rmarh',
# 'rotneo',
# 'rywktkd',
# 'shrwmqrl',
# 'shxmqnr',
# 'sksfh',
# 'sodwkdrh',
# 'tjfkqwkd',
# 'tjsvndrl',
# 'tkfxhd',
# 'tldzmeo',
# 'tlfdhlrl',
# 'tlrrlrjswhrl',
# 'tlrrltpcjrrl',
# 'tlrxkr',
# 'tlsqkf',
# 'tlsqkfwkd',
# 'tmfprlxhd',
# 'tmxosemdhtrjfdl',
# 'tmxpqvj',
# 'tmzltpxm',
# 'tmzosj',
# 'tnehghtm',
# 'tpauseo',
# 'tpeksrl',
# 'tpxkrrl',
# 'tv',
# 'tvqkecla',
# 'tyvk',
# 'vkfptxm',
# 'vkxltus',
# 'vldksh',
# 'vmflsxj',
# 'vortlalffl',
# 'vosglxj',
# 'whaudrlrn',
# 'wjdtnrl',
# 'wjsghkrl',
# 'wjsrlekady',
# 'wjsrlqkqthx',
# 'wjsrlvksspf',
# 'wjswkfpdlswl',
# 'wkdfhd',
# 'wkdsksrka',
# 'wkdtlrwkd',
# 'wkdvks',
# 'wkehdvksaorl',
# 'wkwjsrj',
# 'wlsdufeo',
# 'woqhdxmf',
# 'xhtmxjrl',
# 'xkdldj',
# 'xkftnrl',
# 'xkrrneo',
# 'xkrwk',
# 'xpsxm',
# 'zjavbxj',
# 'zjffjqkrtm',
# 'zjvlvhxm',
# 'zjxms',
# 'zjxmsqhd',
# 'zktpxmfkeldh',
# 'zlrqhem',
#'zoqlslt'
]
cnt = 0
succounter = 0
for i in list:
    sel(i,cnt)
    cnt+=1
