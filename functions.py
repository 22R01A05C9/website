import requests,json,websocket,random,string,os
from bs4 import BeautifulSoup
from time import sleep
from pytube import YouTube
from threading import Thread

def yt_getdatamp4(url):
    data={}
    data['status']=1
    data1={
    "q": url,
    "vt": "home"
    }
    headers1={
        "Sec-Fetch-Dest":"empty",
        "Sec-Fetch-Mode":"cors",
        "Sec-Fetch-Site":"same-origin",
        "Sec-Gpc":"1",
        "User-Agent":"Mozilla/5.0 (iPhone; CPU iPhone OS 16_6 like Mac OS X) AppleWebKit/605.1.15 (KHTML, like Gecko) Version/16.6 Mobile/15E148 Safari/604.1",
        "X-Requested-With":"XMLHttpRequest"
    }
    response1=requests.post(url="https://x2mate.com/api/ajaxSearch",data=data1,headers=headers1)
    op1=json.loads(response1.text)
    try:
        data['title']=str(op1['title'])
    except KeyError:
        data['status']=0
        return data
    data['mp4']={}
    for i in op1['links']['mp4']:
        try:
            data['mp4'][op1['links']['mp4'][i]['q']]=op1['links']['mp4'][i]['size']
        except:
            break
    return data


def yt_getlinkmp4(url,type):
    data={}
    data1={
    "q": url,
    "vt": "home"
    }
    response1=requests.post(url="https://x2mate.com/api/ajaxSearch",data=data1)
    op1=json.loads(response1.text)
    data['vid']=str(op1['vid'])
    data['title']=str(op1['title'])
    data['token']=str(op1['token'])
    data['timeexpire']=str(op1['timeExpires'])
    data2={"v_id": data['vid'],
    "ftype": "mp4",
    "fquality": type,
    "fname":data['title'],
    "token": data['token'],
    "timeExpire": data['timeexpire'],
    "client":"x2mate.com"
    }
    headers2={
        "Sec-Ch-Ua-Mobile":"?0",
        "Sec-Ch-Ua-Platform":"Windows",
        "Sec-Fetch-Dest":"empty",
        "Sec-Fetch-Mode":"cors",
        "Sec-Fetch-Site":"cross-site", 
        "Sec-Gpc":"1",
        "User-Agent":"Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/119.0.0.0 Safari/537.36",
        "X-Requested-Key":"de0cfuirtgf67a"
    }
    response2=requests.post(data=data2,headers=headers2,url="https://backend.svcenter.xyz/api/convert-by-45fc4be8916916ba3b8d61dd6e0d6994")
    op2=json.loads(response2.text)
    cserver=op2['c_server']
    t1=cserver.split('/')
    sublink=t1[-1]
    data3={"v_id": data['vid'],
    "ftype": "mp4",
    "fquality": type,
    "fname":data['title'],
    "token": data['token'],
    "timeExpire": data['timeexpire'],
    }
    header3={
    "Sec-Ch-Ua-Mobile":"?0",
    "Sec-Ch-Ua-Platform":"Windows",
    "Sec-Fetch-Dest":"empty",
    "Sec-Fetch-Mode":"cors",
    "Sec-Fetch-Site":"cross-site",
    "Sec-Gpc":"1",
    "User-Agent":"Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/119.0.0.0 Safari/537.36"}
    link=""
    response3=requests.post(url=f"{cserver}/api/json/convert",data=data3,headers=header3)
    op3=json.loads(response3.text)
    if op3['result']=='Converting':
        
        jobid=op3['jobId']
        url4=f"wss://{sublink}/sub/{jobid}?fname=x2mate.com"
        ws = websocket.WebSocket() 
        ws.connect(url4)
        while(True):
            try:
                message=ws.recv()
                op4=json.loads(message)
            except websocket._exceptions.WebSocketConnectionClosedException:
                break
            except:
                pass
            else:
                if (op4['action']=='success'):
                    link=op4['url']
                    break
    else:
        link=op3['result']
    return link     
    
def yt_getlinkmp3(url):
    rand = random.randint(1111,9999)
    y=YouTube(url)
    mapping_table = str.maketrans({" ":"_","|":"","/":"","\\":"",":":"","*":"","?":"","<":"",'"':"",">":""})
    try:
        y.streams.get_audio_only().download(output_path="/home/sai/website/static/files/"+str(rand),filename=y.title.translate(mapping_table)+".mp3")
    except:
        data={"url": url,
        "ajax": "1",
        "lang": "en"
        }
        res1 = requests.post("https://y2mate.com.co/mates/en/analyze/ajax?retry=undefined&platform=youtube",data=data)
        try:
            id = res1.text.split("var k_data_vid = ")[1].split('\"')[1].replace('\\',"")
            title = res1.text.split("var k_data_vtitle =")[1].split('\"')[1].replace('\\',"")
        except IndexError:
            return "Error"
        data2 ={
            "platform": "youtube",
            "url": url,
            "title": title,
            "id": id,
            "ext": "mp3",
            "note": "128k",
            "format": "128k"
        }
        download_link = json.loads(requests.post("https://nearbypro.www-2048.com/mates/en/convert?id="+id,data=data2).text)['downloadUrlX']
        return download_link
    else:
        path="/home/sai/website/static/files/"+str(rand)+"/"+y.title.translate(mapping_table)+".mp3"
        Thread(target=delete_yt_audio,args=(path,rand,)).start()
        return "/static/files/"+str(rand)+"/"+y.title.translate(mapping_table)+".mp3"

    
def delete_yt_audio(path,rand):
    sleep(600)
    os.remove(path)
    os.rmdir("/home/sai/website/static/files/"+str(rand))

def get_instagram_links(url):
    headers={
        "User-Agent":
        "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/120.0.0.0 Safari/537.36"
    }
    data={
        "recaptchaToken": "",
        "q": url,
        "t": "media",
        "lang": "en"
    }
    response = requests.post(url="https://v3.igdownloader.app/api/ajaxSearch",data=data,headers=headers)
    res = json.loads(response.content)
    try:
        soup = BeautifulSoup(res['data'],'html5lib')
    except:
        return [0]
    op=[1]
    unwanted_links=["https://play.google.com/store/apps/details?id=saveinsta.download.video.instagram.photo.reels.story","/"]
    download_link=[]
    titles=[]
    for link in soup.find_all('a'):
        url = link.get('href')
        title = link.get("title")
        if url not in unwanted_links:
            download_link.append(url)
            titles.append(title)   
            
    preview_link=[]
    for link in soup.find_all('img'):
        tlink = link.get('src')
        if tlink=='/imgs/loader.gif':
            tlink = link.get('data-src')
        preview_link.append(str(tlink).replace("amp;",""))
    op.append(download_link)
    op.append(preview_link)
    op.append(titles)
    return op

def url_shortner():
    shorturl=""
    chars=string.ascii_letters + string.digits
    for _ in range(6):
        shorturl+=random.choice(chars)
    return shorturl

def sms_check(number):
    if number=="8639625032":
        return [1,"NUMBER BLOCKED"]
    elif len(number)!=10:
        return [1,"PLEASE ENTER VALID NUMBER"]
    d={'1','2','3','4','5','6','7','8','9','0'}
    flag=1
    for i in number:
        if i not in d:
            flag=0
            break
        else:
            flag=1
    if flag:
        return [0,'none']
    else:
        return [1,"PLEASE MAKE SURE THAT NUMBER DO NOT CONTAIN ANY LETTERS"]
    
    
def files_get_randnum():
    nums={}
    try:
        with open("/home/sai/data/filesnumbers.txt",'r') as file:
            nums = json.loads(file.read())
    except:
        num = random.randint(1111,9999)
        nums[str(num)]="none"
        with open("/home/sai/data/filesnumbers.txt",'w') as file:
                file.write(str(nums).replace("'",'"'))
        return num
    while(1):
        num = random.randint(1111,9999)
        if num not in nums:
            nums[str(num)]="none"
            with open("/home/sai/data/filesnumbers.txt",'w') as file:
                file.write(str(nums).replace("'",'"'))
            return num
        

def files_savedata(randnum,filename):
    data={}
    try:
        with open('/home/sai/data/filesdata.txt','r') as file:
            data=json.loads(file.read())
    except:
        pass
    data[str(randnum)]=filename
    with open('/home/sai/data/filesdata.txt','w') as file:
        file.write(str(data).replace("'",'"'))


def files_rmdata(randnum,filename):
    sleep(7200)
    data={}
    with open('/home/sai/data/filesnumbers.txt','r') as file:
        data=json.loads(file.read())
    data.pop(str(randnum))
    with open("/home/sai/data/filesnumbers.txt","w") as file:
        file.write(str(data).replace("'",'"'))
    with open('/home/sai/data/filesdata.txt','r') as file:
        data=json.loads(file.read())
    data.pop(str(randnum))
    with open("/home/sai/data/filesdata.txt","w") as file:
        file.write(str(data).replace("'",'"'))
    os.remove('static/files/'+str(randnum)+'/'+filename)
    os.rmdir('static/files/'+str(randnum))
    
    
def del_qr_code(ran):
    sleep(600)
    os.remove(f'static/qr_codes/{ran}.png')