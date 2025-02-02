import json
import requests
import urllib.parse
import time
import datetime
import random
import os
import subprocess
from cache import cache


max_api_wait_time = 8
max_time = 12
apis = [
    r"https://invidious.jing.rocks/",
    r"https://invidious.nerdvpn.de/",
    r"https://inv.nadeko.net/",
    r"https://invidious.jing.rocks/",
r"https://inv.vern.cc/",
r"https://inv.zzls.xyz/",
r"https://invi.susurrando.com/",
r"https://invidious.epicsite.xyz/",
r"https://invidious.esmailelbob.xyz/",
r"https://invidious.garudalinux.org/",
r"https://invidious.kavin.rocks/",
r"https://invidious.lidarshield.cloud/",
r"https://invidious.lunar.icu/",
r"https://yt-us.discard.no/",
r"https://invidious.nerdvpn.de/",
r"https://invidious.privacydev.net/",
r"https://invidious.sethforprivacy.com/",
r"https://invidious.slipfox.xyz/",
r"https://yt-no.discard.no/",
r"https://invidious.snopyta.org/",
r"https://invidious.tiekoetter.com/",
r"https://invidious.vpsburti.com/",
r"https://invidious.weblibre.org/",
r"https://invidious.pufe.org/",
r"https://iv.ggtyler.dev/",
r"https://iv.melmac.space/",
r"https://vid.puffyan.us/",
r"https://watch.thekitty.zone/",
r"https://yewtu.be/",
r"https://youtube.moe.ngo/",
r"https://yt.31337.one/",
r"https://yt.funami.tech/",
r"https://yt.oelrichsgarcia.de/",
r"https://yt.wkwkwk.fun/",
r"https://youtube.076.ne.jp/",
r"https://invidious.projectsegfau.lt/",
r"https://invidious.fdn.fr/",
r"https://i.oyster.men/",
r"https://invidious.domain.glass/",
r"https://inv.skrep.eu/",
r"https://clips.im.allmendenetz.de/",
r"https://ytb.trom.tf/",
r"https://invidious.pcgamingfreaks.at/",
r"https://youtube.notrack.ch/",
r"https://iv.ok0.org/",
r"https://youtube.vpn-home-net.de/",
r"http://144.126.251.186/",
r"https://invidious.citizen4.eu/",
r"https://yt.sebaorrego.net/",
r"https://invidious.pesso.al/",
r"https://invidious.manasiwibi.com/",
r"https://toob.unternet.org/",
r"https://youtube.mosesmang.com/",
r"https://invidious.varishangout.net/",
r"https://invidio.xamh.de/",
r"https://yt.tesaguri.club/",
r"https://video.francevpn.fr/",
r"https://inv.in.projectsegfau.lt/",
r"https://invid.nevaforget.de/",
r"https://tube.foss.wtf/",
r"https://invidious.777.tf/",
r"https://inv.tux.pizza/",
r"https://youtube.076.ne.jp",
r"https://invidious.osi.kr/",
r"https://inv.riverside.rocks/",
r"https://inv.bp.mutahar.rocks/",
r"https://invidious.namazso.eu/",
r"https://tube.cthd.icu/",
r"https://invidious.snopyta.org/",
r"https://yewtu.be/",
r"https://invidious.privacy.gd/",
r"https://invidious.lunar.icu/",
r"https://vid.puffyan.us/",
r"https://invidious.weblibre.org/",
r"https://invidious.esmailelbob.xyz/",
r"https://invidio.xamh.de/",
r"https://invidious.kavin.rocks/",
r"https://invidious-us.kavin.rocks/",
r"https://invidious.mutahar.rocks/",
r"https://invidious.zee.li/",
r"https://tube.connect.cafe/",
r"https://invidious.zapashcanon.fr/",
r"https://invidious.poast.org/",
r"https://ytb.trom.tf/",
r"https://invidious.froth.zone/",
r"https://invidious.domain.glass/",
r"https://invidious.sp-codes.de/",
r"http://144.126.251.186/",
r"https://yt.512mb.org/",
r"https://invidious.fdn.fr/",
r"https://invidious.pcgamingfreaks.at/",
r"https://tube.meowz.moe/",
r"https://clips.im.allmendenetz.de/",
r"https://inv.skrep.eu/",
r"https://invidious.frbin.com/",
r"https://dev.invidio.us/",
r"https://invidious.site/",
r"https://invidious.sethforprivacy.com/",
r"https://invidious.stemy.me/",
r"https://betamax.cybre.club/",
r"https://invidious.com/",
r"https://invidious.snopyta.org",
r"https://yewtu.be",
r"https://invidious.kavin.rocks",
r"https://vid.puffyan.us",
r"https://inv.riverside.rocks",
r"https://invidious.not.futbol/",
r"https://youtube.076.ne.jp",
r"https://yt.artemislena.eu",
r"https://invidious.esmailelbob.xyz",
r"https://invidious.projectsegfau.lt",
r"https://invidious.dhusch.de/",
r"https://inv.odyssey346.dev/"
]
url = requests.get(r'https://raw.githubusercontent.com/mochidukiyukimi/yuki-youtube-instance/main/instance.txt').text.rstrip()
version = "1.0"

os.system("chmod 777 ./yukiverify")

# APIリストのコピーを生成
apichannels = apis.copy()
apicomments = apis.copy()

# 例外クラスの定義
class APItimeoutError(Exception):
    pass

# JSON判定
def is_json(json_str):
    try:
        json.loads(json_str)
        return True
    except json.JSONDecodeError:
        return False

# 汎用リクエスト
def apirequest(url):
    global apis
    starttime = time.time()
    for api in apis:
        if time.time() - starttime >= max_time - 1:
            break
        try:
            res = requests.get(api + url, timeout=max_api_wait_time)
            if res.status_code == 200 and is_json(res.text):
                print(f"その他成功したAPI: {api}")  # 成功したAPIをログに出力
                return res.text
            else:
                print(f"その他エラー: {api}")
                apis.append(api)
                apis.remove(api)
        except:
            print(f"その他タイムアウト: {api}")
            apis.append(api)
            apis.remove(api)
    raise APItimeoutError("APIがタイムアウトしました")

# チャンネル用のリクエスト
def apichannelrequest(url):
    global apichannels
    starttime = time.time()
    for api in apichannels:
        if time.time() - starttime >= max_time - 1:
            break
        try:
            res = requests.get(api + url, timeout=max_api_wait_time)
            if res.status_code == 200 and is_json(res.text):
                print(f"チャンネル成功したAPI: {api}")  # 成功したAPIをログに出力
                return res.text
            else:
                print(f"チャンネルエラー: {api}")
                apichannels.append(api)
                apichannels.remove(api)
        except:
            print(f"チャンネルタイムアウト: {api}")
            apichannels.append(api)
            apichannels.remove(api)
    raise APItimeoutError("APIがタイムアウトしました")

# コメント用のリクエスト
def apicommentsrequest(url):
    global apicomments
    starttime = time.time()
    for api in apicomments:
        if time.time() - starttime >= max_time - 1:
            break
        try:
            res = requests.get(api + url, timeout=max_api_wait_time)
            if res.status_code == 200 and is_json(res.text):
                print(f"コメント成功したAPI: {api}")  # 成功したAPIをログに出力
                return res.text
            else:
                print(f"コメントエラー: {api}")
                apicomments.append(api)
                apicomments.remove(api)
        except:
            print(f"コメントタイムアウト: {api}")
            apicomments.append(api)
            apicomments.remove(api)
    raise APItimeoutError("APIがタイムアウトしました")



video_apis = [
    r"https://invidious.jing.rocks/",
    r"https://invidious.nerdvpn.de/",
    r"https://script.google.com/macros/s/AKfycbxic9NV_JbKs1Ia4m5yw6z7nAZjkQ0mjZ2FGi29ZtLMhX9R6JSEO6jZBuXpNyWHCuRy/exec?videoId=",
    r"https://script.google.com/macros/s/AKfycbzDTu2EJQrGPPU-YS3EFarXbfh9zGB1zR9ky-9AunHl7Yp3Gq83rh1726JYjxbjbEsB/exec?videoId=",
    r"https://script.google.com/macros/s/AKfycbw43HTKJe0khOM3h5lrRbWw2OUONcbQCsnSry7F6c_1bPdtxVjTUotm1_XY2KfqMLWT/exec?videoId=",
    r"https://script.google.com/macros/s/AKfycbxYjOWULjin5kpp-NcjjjGujVX3wy1TEJVUR2AZtR6-5c_q7GBr1Nctl2_Kat4lSboD/exec?videoId=",
]

max_time = 30  # 最大待機時間の設定
max_api_wait_time = 5  # APIリクエストの最大待機時間

class APItimeoutError(Exception):
    pass

def is_json(myjson):
    try:
        json_object = json.loads(myjson)
    except ValueError as e:
        return False
    return True

# APIリクエスト関数
def apirequest_video(url):
    global video_apis
    starttime = time.time()
    for api in video_apis:
        if time.time() - starttime >= max_time - 1:
            break
        try:
            res = requests.get(api + url, timeout=max_api_wait_time)
            if res.status_code == 200 and is_json(res.text):
                print(f"動画API成功: {api}")  # 成功したAPIをログに出力
                return res.text
            else:
                print(f"エラー: {api}")
                video_apis.append(api)
                video_apis.remove(api)
        except:
            print(f"タイムアウト: {api}")
            video_apis.append(api)
            video_apis.remove(api)
    raise APItimeoutError("動画APIがタイムアウトしました")

def get_data(videoid):
    global logs
    try:
        # 最初に既存の方法でデータを取得しようとする
        t = json.loads(apirequest(r"api/v1/videos/" + urllib.parse.quote(videoid)))
    except (APItimeoutError, json.JSONDecodeError) as e:
        print(f"データ取得に失敗しました: {e}")
        # 失敗したときには代替の方法を使用する
        return getting_data(videoid)

    # 関連動画を解析してリストにする
    related_videos = [
        {
            "id": i["videoId"],
            "title": i["title"],
            "authorId": i["authorId"],
            "author": i["author"],
            "viewCount": i["viewCount"]
        }
        for i in t["recommendedVideos"]
    ]

    return (
        related_videos,  
        list(reversed([i["url"] for i in t["formatStreams"]]))[:2],  
        t["descriptionHtml"].replace("\n", "<br>"),  
        t["title"],  
        t["authorId"],  
        t["author"],  
        t["authorThumbnails"][-1]["url"],  
        t["viewCount"]  
    )

def getting_data(videoid):
    urls = [
        f"https://just-frequent-network.glitch.me/api/{urllib.parse.quote(videoid)}",
        f"https://amenable-charm-lute.glitch.me/api/login/{urllib.parse.quote(videoid)}",
        f"https://free-sudden-kiss.glitch.me/api/login/{urllib.parse.quote(videoid)}",
        f"https://wtserver1.glitch.me/api/login/{urllib.parse.quote(videoid)}",
        f"https://wataamee.glitch.me/api/{urllib.parse.quote(videoid)}",
        f"https://natural-voltaic-titanium.glitch.me/api/login/{urllib.parse.quote(videoid)}",
        f"https://jade-highfalutin-account.glitch.me/api/login/{urllib.parse.quote(videoid)}",
        f"https://watawatawata.glitch.me/api/login/{urllib.parse.quote(videoid)}"
    ]
    
    for url in urls:
        try:
            response = requests.get(url)
            if response.status_code == 200:
                t = response.json()
                
                # 推奨動画情報の取得
                recommended_videos = [{
                    "id": t["videoId"],
                    "title": t["videoTitle"],
                    "authorId": t["channelId"],
                    "author": t["channelName"],
                    "viewCountText": f"{t['videoViews']} views"
                }]
                
                # ストリームURLや他の情報を取得
                stream_url = t.get("stream_url", "")
                description = t.get("videoDes", "").replace("\n", "<br>")
                title = t.get("videoTitle", "")
                authorId = t.get("channelId", "")
                author = t.get("channelName", "")
                author_icon = t.get("channelImage", "")
                
                return recommended_videos, stream_url, description, title, authorId, author, author_icon
            
        except Exception as e:
            print(f"{url} からのデータ取得中にエラーが発生しました: {e}")

def get2_data(videoid):
    urls = [
        f"https://test-blank-page.glitch.me/api/server/v1/{urllib.parse.quote(videoid)}",
        f"https://test-blank-page.glitch.me/api/server/v2/{urllib.parse.quote(videoid)}",
        f"https://test-blank-page.glitch.me/api/server/v3/{urllib.parse.quote(videoid)}",
        f"https://test-blank-page.glitch.me/api/server/v4/{urllib.parse.quote(videoid)}",
        f"https://test-blank-page.glitch.me/api/server/v5/{urllib.parse.quote(videoid)}",
        f"https://test-blank-page.glitch.me/api/server/v7/{urllib.parse.quote(videoid)}"
    ]
    
    for url in urls:
        try:
            response = requests.get(url)
            if response.status_code == 200:
                t = response.json()
                
                # ストリームURLや動画情報を取得
                stream_url = t.get("stream_url", "")
                description = t.get("videoDes", "").replace("\n", "<br>")
                title = t.get("videoTitle", "")
                authorId = t.get("channelId", "")
                author = t.get("channelName", "")
                author_icon = t.get("channelImage", "")
                
                return stream_url, description, title, authorId, author, author_icon
            
        except Exception as e:
            print(f"{url} からのデータ取得中にエラーが発生しました: {e}")

def load_search(i):
    # 動画情報の取得
    if i["type"] == "video":
        return {
            "title": i["title"] if 'title' in i else 'Load Failed',
            "id": i["videoId"] if 'videoId' in i else 'Load Failed',
            "authorId": i["authorId"] if 'authorId' in i else 'Load Failed',
            "author": i["author"] if 'author' in i else 'Load Failed',
            "length": str(datetime.timedelta(seconds=i["lengthSeconds"])),
            "published": i["publishedText"] if 'publishedText' in i else 'Load Failed',
            "type": "video"
        }
    
    # プレイリスト情報の取得
    elif i["type"] == "playlist":
        return {
            "title": i["title"] if 'title' in i else "Load Failed",
            "id": i['videoId'] if 'videoId' in i else "Load Failed",
            "thumbnail": i["videos"][0]["videoId"] if 'videos' in i and len(i["videos"]) and 'videoId' in i['videos'][0] else "Load Failed",
            "count": i["videoCount"] if 'videoCount' in i else "Load Failed",
            "type": "playlist"
        }
    
    # チャンネル情報の取得
    elif 'authorThumbnails' in i and len(i["authorThumbnails"]) > 0 and i["authorThumbnails"][-1]["url"].startswith("https"):
        return {
            "author": i["author"] if 'author' in i else 'Load Failed',
            "id": i["authorId"] if 'authorId' in i else 'Load Failed',
            "thumbnail": i["authorThumbnails"][-1]["url"] if 'authorThumbnails' in i and len(i["authorThumbnails"]) and 'url' in i["authorThumbnails"][-1] else 'Load Failed',
            "type": "channel"
        }
    else:
        return {
            "author": i["author"] if 'author' in i else 'Load Failed',
            "id": i["authorId"] if 'authorId' in i else 'Load Failed',
            "thumbnail": f"https://{i['authorThumbnails'][-1]['url']}",
            "type": "channel"
        }
    
def get_channel(channelid):
    t = json.loads(apirequest(f"/channels/{urllib.parse.quote(channelid)}", invidious_api.channels))
    if not t["latestVideos"]:
        print("APIがチャンネルを返しませんでした")
        apichannels = updateList(apichannels, apichannels[0])
        raise APItimeoutError("APIがチャンネルを返しませんでした")
    
    return [[{"title": i["title"], "id": i["videoId"], "authorId": t["authorId"], "author": t["author"], "published": i["publishedText"], "type":"video"} for i in t["latestVideos"]],
            {"channelname": t["author"], "channelicon": t["authorThumbnails"][-1]["url"], "channelprofile": t["descriptionHtml"]}]

def get_playlist(listid, page):
    t = json.loads(apirequest(f"/playlists/{urllib.parse.quote(listid)}?page={urllib.parse.quote(page)}", invidious_api.videos))["videos"]
    return [{"title": i["title"], "id": i["videoId"], "authorId": i["authorId"], "author": i["author"], "type": "video"} for i in t]

def get_comments(videoid):
    t = json.loads(apirequest(f"/comments/{urllib.parse.quote(videoid)}?hl=jp", invidious_api.comments))["comments"]
    return [{"author": i["author"], "authoricon": i["authorThumbnails"][-1]["url"], "authorid": i["authorId"], "body": i["contentHtml"].replace("\n", "<br>")} for i in t]

# 動画取得用APIリクエスト関数を作成
def apirequest_video(url):
    global video_apis
    starttime = time.time()
    for api in video_apis:
        if time.time() - starttime >= max_time - 1:
            break
        try:
            res = requests.get(api + url, timeout=max_api_wait_time)
            if res.status_code == 200 and is_json(res.text):
                print(f"動画API成功: {api}")  # 成功したAPIをログに出力
                return res.text
            else:
                print(f"エラー: {api}")
                video_apis.append(api)
                video_apis.remove(api)
        except:
            print(f"タイムアウト: {api}")
            video_apis.append(api)
            video_apis.remove(api)
    raise APItimeoutError("動画APIがタイムアウトしました")


def get_search(q, page):
    global logs
    results = []

    # Invidious APIを用いた検索
    try:
        t = json.loads(apirequest(fr"api/v1/search?q={urllib.parse.quote(q)}&page={page}&hl=jp"))

        # Invidiousの検索結果
        for i in t:
            if i["type"] == "video":
                results.append({
                    "title": i["title"],
                    "id": i["videoId"],
                    "authorId": i["authorId"],
                    "author": i["author"],
                    "length": str(datetime.timedelta(seconds=i["lengthSeconds"])),
                    "published": i["publishedText"],
                    "type": "video"
                })
            elif i["type"] == "playlist":
                results.append({
                    "title": i["title"],
                    "id": i["playlistId"],
                    "thumbnail": i["videos"][0]["videoId"],
                    "count": i["videoCount"],
                    "type": "playlist"
                })
            else:
                if i["authorThumbnails"][-1]["url"].startswith("https"):
                    results.append({
                        "author": i["author"],
                        "id": i["authorId"],
                        "thumbnail": i["authorThumbnails"][-1]["url"],
                        "type": "channel"
                    })
                else:
                    results.append({
                        "author": i["author"],
                        "id": i["authorId"],
                        "thumbnail": "https://" + i["authorThumbnails"][-1]["url"],
                        "type": "channel"
                    })
    
    except Exception as e:
        print(f"Invidious APIの呼び出しに失敗しました: {e}")
        # Googleの検索候補APIを用いた検索
        google_search_url = f"http://www.google.com/complete/search?client=youtube&hl=ja&ds=yt&q={urllib.parse.quote(q)}"
        google_results = json.loads(requests.get(google_search_url).text[19:-1])[1]

        # Googleの検索候補結果を結果に追加
        results += [{"title": suggestion, "type": "suggestion"} for suggestion in google_results]

    return results

def get_channel(channelid):
    global apichannels
    t = json.loads(apichannelrequest(r"api/v1/channels/"+ urllib.parse.quote(channelid)))
    if t["latestVideos"] == []:
        print("APIがチャンネルを返しませんでした")
        apichannels.append(apichannels[0])
        apichannels.remove(apichannels[0])
        raise APItimeoutError("APIがチャンネルを返しませんでした")
    return [[{"title":i["title"],"id":i["videoId"],"authorId":t["authorId"],"author":t["author"],"published":i["publishedText"],"type":"video"} for i in t["latestVideos"]],{"channelname":t["author"],"channelicon":t["authorThumbnails"][-1]["url"],"channelprofile":t["descriptionHtml"]}]

def get_playlist(listid,page):
    t = json.loads(apirequest(r"/api/v1/playlists/"+ urllib.parse.quote(listid)+"?page="+urllib.parse.quote(page)))["videos"]
    return [{"title":i["title"],"id":i["videoId"],"authorId":i["authorId"],"author":i["author"],"type":"video"} for i in t]

def get_comments(videoid):
    t = json.loads(apicommentsrequest(r"api/v1/comments/"+ urllib.parse.quote(videoid)+"?hl=jp"))["comments"]
    return [{"author":i["author"],"authoricon":i["authorThumbnails"][-1]["url"],"authorid":i["authorId"],"body":i["contentHtml"].replace("\n","<br>")} for i in t]

def get_replies(videoid,key):
    t = json.loads(apicommentsrequest(fr"api/v1/comments/{videoid}?hmac_key={key}&hl=jp&format=html"))["contentHtml"]

def get_level(word):
    for i1 in range(1,13):
        with open(f'Level{i1}.txt', 'r', encoding='UTF-8', newline='\n') as f:
            if word in [i2.rstrip("\r\n") for i2 in f.readlines()]:
                return i1
    return 0


def check_cokie(cookie):
    print(cookie)
    if cookie == "True":
        return True
    return False

def get_verifycode():
    try:
        result = subprocess.run(["./yukiverify"], encoding='utf-8', stdout=subprocess.PIPE)
        hashed_password = result.stdout.strip()
        return hashed_password
    except subprocess.CalledProcessError as e:
        print(f"Error: {e}")
        return None





from fastapi import FastAPI, Depends
from fastapi import Response,Cookie,Request
from fastapi.responses import HTMLResponse,PlainTextResponse
from fastapi.responses import RedirectResponse as redirect
from fastapi.middleware.gzip import GZipMiddleware
from fastapi.staticfiles import StaticFiles
from pydantic import BaseModel
from typing import Union


app = FastAPI(docs_url=None, redoc_url=None, openapi_url=None)
app.mount("/css", StaticFiles(directory="./css"), name="static")
app.mount("/sand", StaticFiles(directory="./blog", html=True), name="static")
app.mount("/youtube", StaticFiles(directory="./youtube", html=True), name="static")
app.mount("/ai", StaticFiles(directory="./ai", html=True), name="static")
app.add_middleware(GZipMiddleware, minimum_size=1000)

from fastapi.templating import Jinja2Templates
template = Jinja2Templates(directory='templates').TemplateResponse






@app.get("/", response_class=HTMLResponse)
def home(response: Response,request: Request,yuki: Union[str] = Cookie(None)):
    if check_cokie(yuki):
        response.set_cookie("yuki","True",max_age=60 * 60 * 24 * 7)
        return template("home.html",{"request": request})
    print(check_cokie(yuki))
    return redirect("/sand")

@app.get("/search", response_class=HTMLResponse,)
def search(q:str,response: Response,request: Request,page:Union[int,None]=1,yuki: Union[str] = Cookie(None),proxy: Union[str] = Cookie(None)):
    if not(check_cokie(yuki)):
        return redirect("/")
    response.set_cookie("yuki","True",max_age=60 * 60 * 24 * 7)
    return template("search.html", {"request": request,"results":get_search(q,page),"word":q,"next":f"/search?q={q}&page={page + 1}","proxy":proxy})

@app.get("/hashtag/{tag}")
def search(tag:str,response: Response,request: Request,page:Union[int,None]=1,yuki: Union[str] = Cookie(None)):
    if not(check_cokie(yuki)):
        return redirect("/")
    return redirect(f"/search?q={tag}")


@app.get("/channel/{channelid}", response_class=HTMLResponse)
def channel(channelid:str,response: Response,request: Request,yuki: Union[str] = Cookie(None),proxy: Union[str] = Cookie(None)):
    if not(check_cokie(yuki)):
        return redirect("/")
    response.set_cookie("yuki","True",max_age=60 * 60 * 24 * 7)
    t = get_channel(channelid)
    return template("channel.html", {"request": request,"results":t[0],"channelname":t[1]["channelname"],"channelicon":t[1]["channelicon"],"channelprofile":t[1]["channelprofile"],"proxy":proxy})

@app.get("/answer", response_class=HTMLResponse)
def set_cokie(q:str):
    t = get_level(q)
    if t > 5:
        return f"level{t}\n推測を推奨する"
    elif t == 0:
        return "level12以上\nほぼ推測必須"
    return f"level{t}\n覚えておきたいレベル"

@app.get("/playlist", response_class=HTMLResponse)
def playlist(list:str,response: Response,request: Request,page:Union[int,None]=1,yuki: Union[str] = Cookie(None),proxy: Union[str] = Cookie(None)):
    if not(check_cokie(yuki)):
        return redirect("/")
    response.set_cookie("yuki","True",max_age=60 * 60 * 24 * 7)
    return template("search.html", {"request": request,"results":get_playlist(list,str(page)),"word":"","next":f"/playlist?list={list}","proxy":proxy})

@app.get("/info", response_class=HTMLResponse)
def viewlist(response: Response,request: Request,yuki: Union[str] = Cookie(None)):
    global apis,apichannels,apicomments
    if not(check_cokie(yuki)):
        return redirect("/")
    response.set_cookie("yuki","True",max_age=60 * 60 * 24 * 7)
    return template("info.html",{"request": request,"Youtube_API":apis[0],"Channel_API":apichannels[0],"Comments_API":apicomments[0]})

@app.get("/suggest")
def suggest(keyword:str):
    return [i[0] for i in json.loads(requests.get(r"http://www.google.com/complete/search?client=youtube&hl=ja&ds=yt&q="+urllib.parse.quote(keyword)).text[19:-1])[1]]

@app.get("/comments")
def comments(request: Request,v:str):
    return template("comments.html",{"request": request,"comments":get_comments(v)})

@app.get("/thumbnail")
def thumbnail(v:str):
    return Response(content = requests.get(fr"https://img.youtube.com/vi/{v}/0.jpg").content,media_type=r"image/jpeg")

@app.get("/bbs",response_class=HTMLResponse)
def view_bbs(request: Request,name: Union[str, None] = "",seed:Union[str,None]="",channel:Union[str,None]="main",verify:Union[str,None]="false",yuki: Union[str] = Cookie(None)):
    if not(check_cokie(yuki)):
        return redirect("/")
    res = HTMLResponse(requests.get(fr"{url}bbs?name={urllib.parse.quote(name)}&seed={urllib.parse.quote(seed)}&channel={urllib.parse.quote(channel)}&verify={urllib.parse.quote(verify)}",cookies={"yuki":"True"}).text)
    return res

@cache(seconds=5)
def bbsapi_cached(verify,channel):
    return requests.get(fr"{url}bbs/api?t={urllib.parse.quote(str(int(time.time()*1000)))}&verify={urllib.parse.quote(verify)}&channel={urllib.parse.quote(channel)}",cookies={"yuki":"True"}).text

@app.get("/bbs/api",response_class=HTMLResponse)
def view_bbs(request: Request,t: str,channel:Union[str,None]="main",verify: Union[str,None] = "false"):
    print(fr"{url}bbs/api?t={urllib.parse.quote(t)}&verify={urllib.parse.quote(verify)}&channel={urllib.parse.quote(channel)}")
    return bbsapi_cached(verify,channel)

@app.get("/bbs/result")
def write_bbs(request: Request,name: str = "",message: str = "",seed:Union[str,None] = "",channel:Union[str,None]="main",verify:Union[str,None]="false",yuki: Union[str] = Cookie(None)):
    if not(check_cokie(yuki)):
        return redirect("/")
    t = requests.get(fr"{url}bbs/result?name={urllib.parse.quote(name)}&message={urllib.parse.quote(message)}&seed={urllib.parse.quote(seed)}&channel={urllib.parse.quote(channel)}&verify={urllib.parse.quote(verify)}&info={urllib.parse.quote(get_info(request))}&serververify={get_verifycode()}",cookies={"yuki":"True"}, allow_redirects=False)
    if t.status_code != 307:
        return HTMLResponse(t.text)
    return redirect(f"/bbs?name={urllib.parse.quote(name)}&seed={urllib.parse.quote(seed)}&channel={urllib.parse.quote(channel)}&verify={urllib.parse.quote(verify)}")

@cache(seconds=30)
def how_cached():
    return requests.get(fr"{url}bbs/how").text

@app.get("/bbs/how",response_class=PlainTextResponse)
def view_commonds(request: Request,yuki: Union[str] = Cookie(None)):
    if not(check_cokie(yuki)):
        return redirect("/")
    return how_cached()

@app.get("/load_instance")
def home():
    global url
    url = requests.get(r'https://raw.githubusercontent.com/mochidukiyukimi/yuki-youtube-instance/main/instance.txt').text.rstrip()

@app.get("/list", response_class=HTMLResponse)
def list_page(response: Response, request: Request):
    # Cookieのチェックをしないため、承諾していない場合でもアクセス可能
    # 必要に応じてデータを取得
    # ここでは単純にurllists.htmlを返す
    return template("urllists.html", {"request": request})

@app.get("/chat", response_class=HTMLResponse)
def list_page(response: Response, request: Request):
    # Cookieのチェックをしないため、承諾していない場合でもアクセス可能
    # 必要に応じてデータを取得
    # ここでは単純にhtmlを返す
    return template("chat.html", {"request": request})

@app.get("/byeschool", response_class=HTMLResponse)
def list_page(response: Response, request: Request):
    # Cookieのチェックをしないため、承諾していない場合でもアクセス可能
    # 必要に応じてデータを取得
    # ここでは単純にhtmlを返す
    return template("bye.html", {"request": request})

@app.get("/justvideo", response_class=HTMLResponse)
def list_page(response: Response, request: Request):
    # Cookieのチェックをしないため、承諾していない場合でもアクセス可能
    # 必要に応じてデータを取得
    # ここでは単純にhtmlを返す
    return template("justvideo.html", {"request": request})

@app.get("/deploy", response_class=HTMLResponse)
def list_page(response: Response, request: Request):
    # Cookieのチェックをしないため、承諾していない場合でもアクセス可能
    # 必要に応じてデータを取得
    # ここでは単純にhtmlを返す
    return template("deploy.html", {"request": request})

@app.get("/shadow", response_class=HTMLResponse)
def list_page(response: Response, request: Request):
    # Cookieのチェックをしないため、承諾していない場合でもアクセス可能
    # 必要に応じてデータを取得
    # ここでは単純にhtmlを返す
    return template("shadow.html", {"request": request})

@app.get("/static", response_class=HTMLResponse)
def list_page(response: Response, request: Request):
    # Cookieのチェックをしないため、承諾していない場合でもアクセス可能
    # 必要に応じてデータを取得
    # ここでは単純にhtmlを返す
    return template("iframe.html", {"request": request})

@app.get("/health", response_class=HTMLResponse)
def list_page(response: Response, request: Request):
    return template("health.html", {"request": request})

@app.get("/tell", response_class=HTMLResponse)
def list_page(response: Response, request: Request):
    return template("tell.html", {"request": request})

@app.get("/instance", response_class=HTMLResponse)
def list_page(response: Response, request: Request):
    return template("instance.html", {"request": request})

    
@app.exception_handler(500)
def page(request: Request,__):
    return template("APIwait.html",{"request": request},status_code=500)

@app.exception_handler(APItimeoutError)
def APIwait(request: Request,exception: APItimeoutError):
    return template("APIwait.html",{"request": request},status_code=500)

g_videoid = None

@app.get('/watch', response_class=HTMLResponse)
def video(
    v: str, 
    response: Response, 
    request: Request, 
    yuki: Union[str] = Cookie(None), 
    proxy: Union[str] = Cookie(None)
):
    global g_videoid  # グローバル変数を使用するために宣言

    # クッキーの確認
    if not check_cokie(yuki):
        return redirect("/")
    
    # クッキーをセット
    response.set_cookie(key="yuki", value="True", max_age=7*24*60*60)

    # 動画IDを取得し、videoidとg_videoidに代入
    videoid = v
    g_videoid = videoid  # グローバル変数に代入

    # データを取得
    t = get_data(videoid)

    # 再度クッキーをセット
    response.set_cookie(key="yuki", value="True", max_age=60 * 60 * 24 * 7)

    # テンプレートに g_videoid を渡す
    return template('video.html', {
        "request": request,
        "videoid": videoid,
        "g_videoid": g_videoid,  # ここで g_videoid をテンプレートに渡す
        "videourls": t[1],
        "res": t[0],
        "description": t[2],
        "videotitle": t[3],
        "authorid": t[4],
        "authoricon": t[6],
        "author": t[5],
        "proxy": proxy
    })

# 新しい変数をteigiした
max_stream_api_wait_time = 7  # ストリームAPIリクエストの最大待機時間

@app.get('/watch/{v}/stream', response_class=HTMLResponse)
def stream(
    v: str, 
    response: Response, 
    request: Request
):
    stream_url = None
    start_time = time.time()  # リクエスト開始時刻を記録

    # タイムアウト処理を考慮してループ
    while True:
        try:
            api_response = requests.get(f"https://new-era-hack.vercel.app/api/sand-smoke/stream/{urllib.parse.quote(v)}", timeout=max_stream_api_wait_time)
            
            if api_response.status_code == 200:
                # ストリームURLを取得
                data = api_response.json()
                stream_url = data.get("stream_url")
                break  # 成功したらループを抜ける
            else:
                print(f"APIエラー: ステータスコード {api_response.status_code}")
        except requests.Timeout:
            print("タイムアウトが発生しました")
            if time.time() - start_time >= max_stream_api_wait_time:
                # 最大待機時間を超えた場合はAPItimeoutErrorを発生させる
                raise APItimeoutError("ストリームAPIがタイムアウトしました")
        except Exception as e:
            print(f"ストリームURLの取得中にエラーが発生しました: {e}")
            break  # それ以外のエラーが発生した場合はループを抜ける

    # テンプレートにストリームURLを渡す
    return template('stream.html', {
        "request": request,
        "videoid": v,
        "stream_url": stream_url  # ストリームURLをテンプレートに渡す
    })
