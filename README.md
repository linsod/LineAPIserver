# How to build a own LineBOT

## Before starting 
```
1. Create a account with Line  (free) 
2. Create a account with Heroku(free) 
```

## The main idea
Since there is many earthquake in Taiwan
if need to know the information of eqrthquake in Taiwan.<br>
This process can know information from ```https://data.gov.tw/dataset/xxxx```
```
1. Get a free website server【Heroku】 
2. Get Messaging API from channel token【Line Developers】
3. Set a linbot program【Python】
```

## STEP 1： Create a Heroku project
Login to Heroku, in the Heroku page，select New -> Create New App.<br>
Then the project can be created.<br><br>
<img src="pic/create_app.png" width="600" /><br>

## STEP 2： Get Messaging API from and channel token【Line Developers】
Cause create a need process of the LineBot need the authorization, token and something else form Line Developers.<br><br>
<img src="pic/secret.jpg" width="600" /><br>
<img src="pic/token.jpg" width="600" /><br>

## STEP 3： Set a linbot program【Python】

Heroku application need some files，
let it know the type of application you have enabled,
what environment it needs, what conditions it has, what additional packages and so on.
These special files are Procfile, requirements.txt, and runtime.txt.<br><br>

1. Procfile 

Talk to Heroku,what type of application needed and what the program in the file need to do.
This LineBot is the ```web``` type, so assume that the program is app_core,
therefore the **Procfile** will wirte like this.<br><br>
```web gunicorn app:app```

2. requirements.txt

Talk the **Heroku** need to install what kits.
Heroku provides server is this program where it actually runs,
and in this project need the install kits are<br><br>
```
flask
gunicorn
line-bot-sdk
```

In the code the ```@app.route``` is relate about the webiste location.<br>
```@app.route("/callback", methods=['POST'])``` can check token/channel from the server.<br>
And the whole code is on ```app.py```<br><br>
<img src="/pic/line_user.jpg" width="600" /><br>

Seocnd, create a new project<br>

Third, go：Tools/File Manager, pop the code you write on STEP 1(remember to change the name to "index.html")<br>
<img src="/pic/000webhost3.png" width="600" /><br>

Now your code is on ```xxxxxxx.000webhostapp.com```.<br>

But the website link which 000webhost provides is too long and hard memroize. Fortunately, we could use the other domain which Freenom provide from to shorter our website link.<br><br>
Fourth, go：Tools/Set Web Address to **Park domain**<br>
<img src="/pic/000webhost4.png" width="600" /><br>

Type the Domain name.<br>


## STEP 3： Get a free website server and domainfrom 【Heroku】
<b>Heroku</b> provide a free website domain and some API just in Heroku ...<br>

First,  create a account and sign in.<br>
<img src="/pic/freenom1.png" width="600" /><br>

Second, choose the domian you want.(under 12 months is free, and if 12 months is done, it will ask you wheather want to extend)<br>
It will mail you when your domian is ready.<br>
<img src="/pic/freenom2.png" width="600" /><br>

Third,  go to： freenom/my domain/Management Tools/Use custom nameservers and type：<br><br>
  Nameserver 1<br>
  ```ns01.000webhost.com```<br>
  Nameserver 2<br>
  ```ns02.000webhost.com```<br><br>
to link to 000webhost.com<br>
<img src="/pic/freenom3.png" width="600" /><br>

After serveral times(usually 1 day), check 000webhost<br>
<img src="/pic/000webhost5.png" width="600" /><br>

If you see the subdomian your website is ready on ```xxxxxxx.ga``` !<br>
<img src="/pic/freenom4.png" width="600" /><br>

##
if you want to know more clearly about the process, welcome to watch my youtube channel.<br>
<a href="https://majaja068.github.io/build-a-own-website/cal_v2.html">on github.io</a>
