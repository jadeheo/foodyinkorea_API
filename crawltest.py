from bs4 import BeautifulSoup
from selenium import webdriver
from selenium.webdriver.common.keys import Keys

# 크롬창을 띄우지 않는 옵션
options = webdriver.ChromeOptions()
options.add_argument('headless')
options.add_argument('disable-gpu')
driver = webdriver.Chrome('/Users/nhn/Desktop/sparta/foodyinkorea_API/chromedriver', options=options)

# 3초 지연
driver.implicitly_wait(3)

driver.get('https://www.instagram.com/foodyinkorea')
driver.find_element_by_tag_name('body').send_keys(Keys.END) #끝까지 안 내려감

# 게시글 크롤링
soup = BeautifulSoup(driver.page_source, 'html.parser')

imgs = soup.select('.v1Nh3.kIKUG._bz0w')

num = 1
for img in imgs:
    imgurl = 'http://www.instagram.com' + img.a['href']
    imgsrc = img.select_one('.KL4Bh').img['src']
    imgalt = img.select_one('.KL4Bh').img['alt']
    print(imgalt)
    num += 1



# 게시글이 몇 개 크롤링 되었는지 알기 위함
print(num)


driver.close()
