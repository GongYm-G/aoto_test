import requests
import sign

key = 'testapitoken'
data = {
        "UserCode": "api测试",
        "AppKey":"10222",
        "BookVersionId":2101,
        "coursemappingid":25,
        "KnowledgePointOrSectionId":2003478,
        "QuestionCategoryId":1,
        "QuestionLevelId":3,
        "IsOnlyProprietaryQuestion":0,
        "LocationId ":0,
        "IsRemoveSimilarQuestion ":0,
        "QuestionDisplayTypeIds": [1],
        "PageIndex":2,
        "PageSize":20,
        "NonceStr":"greeteryer"
        }
sign_id = {'Sign': sign.sign(data, key)}
data.update(sign_id)
# print(data)

url = 'http://10.0.2.195:99/Search/GetQuestionsByChapterSection'

a = requests.session().post(url, json = data).json()
for i in a:
        print(i,':',a[i])

