from pymongo import MongoClient
client = MongoClient('localhost', 27017)
db = client.dbfood

db.food.insert_one({'name':'떡볶이','restaurant':'아찌 떡볶이',
                    'price':'3,000원', '운영 시간': '11:00~18:00',
                    '주소': '서울시 강남구', '전화번호': '02-1234-3456',
                    '음식 총평': '걸쭉 길쭉 떡볶이다. 소스는 되직하고 떡은 길다. 이건 시장 떡볶이다. 25년 내공이다. 이 정도면 명함 내밀 수 있다. 위생이 좋다. 가산점이다. 건대생이라면 모르는 사람이 없다. 2명이서 만원이면 배부르게 먹는다. 수요일 휴무다.'})
