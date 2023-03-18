# encoding:utf-8
import requests
import base64
import cv2
capture = cv2.VideoCapture(0)

while(True):
    # 获取一帧
    ret, frame = capture.read()

    cv2.imshow('CTB', frame)
    if cv2.waitKey(1) == ord('q'):
        break
    if cv2.waitKey(1) == ord('s'):
        cv2.imwrite("CTB.png", frame)
        cv2.destroyAllWindows()
        # client_id 为官网获取的AK， client_secret 为官网获取的SK
        host = 'https://aip.baidubce.com/oauth/2.0/token?grant_type=client_credentials&client_id=TWGSNCGpMZ4I24OxazCtK4uT&client_secret=rmAcvTqgmaMSG9tyZDkyWnHcSDlO1eOh'
        response = requests.get(host)
        if response:
            access_token = response.json()['access_token']
            request_url = "https://aip.baidubce.com/rest/2.0/image-classify/v2/advanced_general"
            # 二进制方式打开图片文件
            f = open('CTB.png', 'rb')
            img = base64.b64encode(f.read())
            params = {"image":img}
            request_url = request_url + "?access_token=" + access_token
            headers = {'content-type': 'application/x-www-form-urlencoded'}
            response = requests.post(request_url, data=params, headers=headers)
            if response:
                result = response.json()['result'][0]['keyword']
                print("Item:", result)
                classify_url = "https://service.xiaoyuan.net.cn/garbage/index/search?kw="
                response = requests.get(classify_url+result)
                if response:
                    category = response.json()['data'][0]['category']
                    print("category:", category)
                    if category == "干垃圾":
                        # 控制硬件的干垃圾桶打开
                        pass
                    elif category == "湿垃圾":
                        # 控制硬件的湿垃圾桶打开
                        pass
                    elif category == "可回收物":
                        # 控制硬件的可回收物桶打开
                        pass
                    elif category == "有害垃圾":
                        # 控制硬件的有害垃圾桶打开
                        pass
cv2.destroyAllWindows()        


