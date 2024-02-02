from flask import Flask,render_template,request,url_for,redirect,Response,render_template_string,session
import requests
import json,time
import functions,sendsms
import threading

app = Flask(__name__)
app.secret_key="link"

@app.route('/')
def main():
    return render_template("home.html")

@app.route('/bmi',methods=['POST','GET'])
def bmi():
    if request.method=='GET':
        return render_template("bmi.html")
    else:
        feet=int(request.form['feet'])
        inches=int(request.form['inches'])
        if(inches>11):
            return render_template('bmi.html',feet=feet,inches=inches,weight=weight,data="Inches cannot me more than 11")
        weight=int(request.form['weight'])
        meter=(feet*0.3048)+(inches*0.0254)
        ans=weight/(meter*meter)
        if(ans<18.5):
            return render_template('bmi.html',data=f'Your BMI is {round(ans,1)}',info='You Are UnderWeight')
        elif(ans>=18.5 and ans<24.9):
            return render_template('bmi.html',data=f'Your BMI is {round(ans,1)}',info='You Are Normal Weigth')
        elif(ans>=25 and ans<29.9):
            return render_template('bmi.html',data=f'Your BMI is {round(ans,1)}',info='You Are Over Weight')
        elif(ans>30):
            return render_template('bmi.html',data=f'Your BMI is {round(ans,1)}',info='You Are Having Obesity')


@app.route('/calculator')
def calculator():
    return render_template('calculator.html')


@app.route('/cmr',methods=['POST','GET'])
def cmr():
    if request.method == "POST":
        rollno = request.form['roll']
        roll = rollno.upper()
        url = 'https://dhondi.cmrithyderabad.edu.in/sharedfiles/e0d341de643812c29a19aac35b9e7d87/studentPhotos/' + roll + '.jpg'
        response = requests.post(url=url)
        if response.status_code == 200:
            return render_template('cmr.html', url=url, roll=roll)
        else:
            return render_template('cmr.html',info="No Roll Number Found",roll=roll)
    else:
        return render_template('cmr.html')


@app.route('/instagram',methods=['POST','GET'])
def instagram():
    if request.method=="POST":
        link=request.form['url']
        data=functions.get_instagram_links(link)
        if(data[0]):
            return render_template('instagram.html',op=data[0],download_link=data[1],image_url=data[2])
        else:
            return render_template('instagram.html',info="Video Not Available")
    else:
        return render_template('instagram.html')
    

@app.route('/url', methods=["POST", "GET"])
def url():
    try:
        if request.method=="POST":
            longurl=request.form['url']
            while(1):
                shorturl=functions.url_shortner()
                text=""
                with open('/home/sai/data/data.txt','r') as file:
                    text=file.read()
                data=json.loads(text)
                if shorturl not in data.keys():
                    data[shorturl]=longurl
                    with open('/home/sai/data/data.txt','w') as file:
                        file.write(str(data).replace("'",'"'))
                    break
            shortnedlink=request.url_root+"url/"+shorturl
            return render_template('url.html',result=shortnedlink,info="URL Successfully Generated")
        else:
            return render_template('url.html')
    except:
        return render_template('url.html',info="Some Unknown Error occured")
    
@app.route('/url/add-custom-url', methods=["POST", "GET"])
def add_custom():
    if request.method=="POST":
        try:
            longurl=request.form['url']
            custom=request.form['custom']
            text=""
            with open('/home/sai/data/data.txt','r') as file:
                text=file.read()
            data=json.loads(text)
            if custom not in data.keys():
                data[custom]=longurl
                with open('/home/sai/data/data.txt','w') as file:
                    file.write(str(data).replace("'",'"'))
                shortnedlink=request.url_root+"url/"+custom
                return render_template('urlcustom.html',result=shortnedlink,info="URL Successfully Generated")
            else:
                return render_template('urlcustom.html',info="Custom Link Already Exists Try Using Another Keyword")     
        except:
            return render_template('urlcustom.html',info="Some Unknown Error occured")
    else:
        return render_template('urlcustom.html')
    
@app.route('/url/<shorturl>')
def redirect_function(shorturl):
    try:
        text=""
        with open('/home/sai/data/data.txt','r') as file:
            text=file.read()
        data=json.loads(text)
        if shorturl in data.keys():
            return redirect(str(data[shorturl]))
        else:
            return render_template_string('PageNotFound {{ errorCode }}', errorCode='404'), 404
    except:
        return "some error occured"
   
   
@app.route('/yt')
def home():
    return render_template('yt.html')

@app.route('/yt/result', methods=["POST"])
def search():
    url=request.form['link']
    session['link']=url
    datamp3=functions.yt_getdatamp3(url)
    if (datamp3['status']==0):
        return render_template('yt.html',info="Video Not Found")
    time.sleep(1)
    datamp4=functions.yt_getdatamp4(url)
    print(datamp4['title'])
    session['title']=datamp4['title']
    return render_template('yt.html',title=datamp4['title'],mp3=datamp3['mp3'],mp4=datamp4['mp4'],link=url)
    
@app.route('/yt/download',methods=['POST'])
def download():
    try:
        url=session['link']
    except KeyError:
        return render_template('yt.html',info="Some Error Occured,Please Try Again.")
    else:
        session.pop('link',None)
        type1=request.form['opti']
        l=type1.split(',')
        if (l[0]=='mp3'):
            endlink=functions.yt_getlinkmp3(url,type=l[-1])
        elif (l[0]=='mp4'):
            endlink=functions.yt_getlinkmp4(url,type=l[-1])
        title=session['title']
        session.pop('title',None)
        return render_template('yt.html',title=title,endlink=endlink)
   
@app.route('/sms')
def smsbomber():
    return render_template('sms.html')

@app.route('/sms/sending',methods=['POST'])
def sending():
    number=request.form['number']
    times=(int)(request.form['times'])
    speed=request.form['speed']
    if(speed=='Fast'):
        atime=1000
    elif(speed=='Medium'):
        atime=1500
    elif(speed=='Slow'):
        atime=2000
    result=functions.sms_check(number)
    if result[0]:
        return render_template('sms.html',info=result[-1],times=times,number=number)
    elif times > 150:
        return render_template('sms.html',info="MAXIMUM 150 SMS ONLY",times=times,number=number)
    else:
        m1=threading.Thread(target=sendsms.main,args=(number,times,atime,))
        m1.start()
        return render_template('sms.html',times=times,speed=atime,number1=number)
 
   
   
   
   
   
   
   
   
    
@app.route('/<any>')
def any(any):
    return redirect(url_for('main'))

if __name__=='__main__':
    app.run(host='0.0.0.0',debug=True)