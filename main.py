import asyncio
import pymysql
import os
import sys
import json
import aiohttp
import importlib
import datetime

from math import trunc
from sanic import Sanic
from pytz import timezone
import sanic.response as response

from log_config import LOGGING_CONFIG

app = Sanic(__name__, log_config=LOGGING_CONFIG)
platform_name = ["Steam","Kakao","XBOX","PS","Stadia"]
platform_site = ["steam","kakao","xbox","psn","stadia"]
DB_platform = ["Steam","Kakao","XBOX","PSN","Stadia"]

directory = os.path.dirname(os.path.abspath(__file__)).replace("\\","/")
db_f = open(f"{directory}/data/database.json",mode='r')
db = db_f.read()
db_f.close()
db_json = json.loads(db)

db_ip = db_json["mysql"]["ip"]
db_user = db_json["mysql"]["user"]
db_pw = db_json["mysql"]["password"]
db_name = db_json["mysql"]["database"]

connect = pymysql.connect(host=db_ip, user=db_user, password=db_pw,db=db_name, charset='utf8') #클라이언트 API키 불러오기.
cur = connect.cursor()
cur.execute("SELECT * from PUBG_BOT")
client_list = cur.fetchall()
pubg_token = client_list[0][2]
connect.close()

sys.path.append(directory + "/modules") #다른 파일내 함수추가
p_info = importlib.import_module("player")
s_info = importlib.import_module("status")

header = {
  "Authorization": "Bearer " + pubg_token,
  "Accept": "application/vnd.api+json"
}

sample_f = open(f"{directory}/data/last_update_sample.json",mode='r')
sample1 = json.loads(sample_f.read())
sample_f.close()

async def get_season(pubg_platform):
    connect = pymysql.connect(host=db_ip, user=db_user, password=db_pw, db='PUBG_BOT', charset='utf8')
    cur = connect.cursor()
    sql = f"SELECT {DB_platform[pubg_platform]} FROM SEASON_STATUS"
    cur.execute(sql)
    cache = cur.fetchone()
    html = cache[0]
    data_json = json.loads(html)['data']
    for i in data_json:
        if i['attributes']['isCurrentSeason']:
            least_season = i
    return least_season['id']

def time_num(f_playtime):
    playtime = datetime.datetime.fromtimestamp(f_playtime, timezone('UTC'))
    if playtime.month == 1:
        if playtime.day == 1:
            if playtime.hour == 0:
                if  playtime.minute == 0: return f"{playtime.second}초"
                return f"{playtime.minute}분 {playtime.second}초"
            return f"{playtime.hour}시간 {playtime.minute}분 {playtime.second}초"
        return f"{playtime.day-1}일 {playtime.hour}시간 {playtime.minute}분 {playtime.second}초"
    return f"{playtime.month-1}달 {playtime.day-1}일 {playtime.hour}시간 {playtime.minute}분 {playtime.second}초"

@app.route("/api/PUBG/")
async def main(request):
    return response.redirect("https://github.com/team-alpha-kr/PUBG-API")

@app.route("/api/PUBG/player")
async def player(request):
    args = request.get_args(keep_blank_values=True)
    if not ("nickname" in args): return response.json({'code':'01', 'msg':"Please write your nickname."}, status=400)
    else: nickname = args['nickname'][0]
    connect = pymysql.connect(host=db_ip, user=db_user, password=db_pw,db=db_name, charset='utf8')
    cur = connect.cursor()
    exist_nickname = pymysql.escape_string("SELECT EXISTS (SELECT name FROM player WHERE name=%s) as succees;")
    cur.execute(exist_nickname,(nickname))
    exist = cur.fetchone()
    if exist[0]:
        command = pymysql.escape_string("SELECT id, name, platform, last_update FROM player WHERE name=%s")
        cur.execute(command,(nickname))
        fetch = cur.fetchone()
        connect.close()
        data = {
            "id":fetch[0],
            "nickname":fetch[1],
            "platform":fetch[2],
            "lastupdate":json.loads(fetch[3])
        }
        return response.json(data,status=200)
    else:
        if not ("platform" in args): return response.json({"code":"02","msg":"The value is not stored in DB, so you need to create a platform."},status=400)
        else:
            try: platform = int(args['platform'][0])
            except ValueError: return response.json({'code':'06', 'msg':"Platform values can only contain numbers."}, status=400)
            if not (platform >= 0 and platform < 5): return response.json({'code':'07', 'msg':"Platform values can contain only 0-4 values."}, status=400)
        async with aiohttp.ClientSession() as session:
            async with session.get(f"https://api.pubg.com/shards/{platform_site[platform]}/players?filter[playerNames]={nickname}", headers=header) as resp:
                if resp.status == 200:
                    json_data = await resp.json()
                else:
                    e_resp = s_info.response_num(resp.status)
                    print(await resp.json(),resp.status)
                    return response.json({'code': e_resp[1], 'msg': e_resp[2]}, status=e_resp[0])
        data = {
            "id":json_data["data"][0]["id"],
            "nickname":json_data["data"][0]["attributes"]["name"],
            "platform":platform,
            "lastupdate":sample1
        }
        command = pymysql.escape_string("insert into player(id,name,last_update,platform) value(%s,%s,%s,%s)")
        cur.execute(command,(json_data["data"][0]["id"],json_data["data"][0]["attributes"]["name"],json.dumps(sample1),platform))
        connect.commit()
        connect.close()
        return response.json(data,status=200)

@app.route("/api/PUBG/normal")
async def normal_status(request):
    args = request.get_args(keep_blank_values=True)
    if not ("id" in args): return response.json({'code':'01', 'msg':"Please write your id."}, status=400)
    else: pubg_id = args['id'][0]
    connect = pymysql.connect(host=db_ip, user=db_user, password=db_pw,db=db_name, charset='utf8')
    cur = connect.cursor()
    exist_nickname = pymysql.escape_string("SELECT EXISTS (SELECT name FROM player WHERE id=%s) as succees;")
    cur.execute(exist_nickname,(pubg_id))
    fetch1 = cur.fetchone()
    if fetch1[0]:
        command = pymysql.escape_string("SELECT platform FROM player WHERE id=%s")
        cur.execute(command, (pubg_id))
        platform_info = cur.fetchone()[0]
    else: return response.json({'code':'05', 'msg':"No information about the user was found. Please proceed with \"/PUBG/player\" first."}, status=400)
    if ("season" in args):
        try: season = int(args['season'][0])
        except ValueError: return response.json({'code':'08', 'msg':"Season values can only contain numbers."}, status=400)
        if platform_info >= 0 and platform_info <= 1: type_season = "pc-2018"
        else: type_season = "console"
        if len(str(season)) < 2: season = f"division.bro.official.{type_season}-0{season}"
        else: season = f"division.bro.official.{type_season}-{season}"
    else: season = await get_season(platform_info)
    status, html = await s_info.season_status(pubg_id,platform_info,season)
    if not status:
        return response.json({'code': html[1], 'msg': html[2]}, status=html[0])
    else:
        data = {
            "id":pubg_id,
            "gameMode":{}
        }
        gamestat = html['data']['attributes']['gameModeStats']
        for i in ['solo','solo-fpp','duo','duo-fpp','squad','squad-fpp']:
            modestat = gamestat[i]
            losses = modestat['losses']
            if losses == 0:
                losses = 1
            KDA_point = round((modestat['assists'] + modestat['kills']) / losses,2)
            KD_point = round(modestat['kills'] / losses,2)
            i_data = {
                i:{
                    "assists":modestat['assists'],
                    "boosts": modestat['boosts'],
                    "dBNOs": modestat['dBNOs'],
                    "dailyKills": modestat['dailyKills'],
                    "dailyWins": modestat['dailyWins'],
                    "damageDealt": modestat['damageDealt'],
                    "days": modestat['days'],
                    "headshotKills": modestat['headshotKills'],
                    "heals": modestat['heals'],
                    "KDA_point": KDA_point,
                    "KD_point": KD_point,
                    "kills": modestat['kills'],
                    "longestKill": modestat['longestKill'],
                    "longestTimeSurvived": modestat['longestTimeSurvived'],
                    "longestTimeSurvivedAnswer": time_num(modestat['longestTimeSurvived']),
                    "losses": modestat['losses'],
                    "maxKillStreaks": modestat['maxKillStreaks'],
                    "mostSurvivalTime": modestat['mostSurvivalTime'],
                    "revives": modestat['revives'],
                    "rideDistance": modestat['rideDistance'],
                    "roadKills": modestat['roadKills'],
                    "roundMostKills": modestat['roundMostKills'],
                    "roundsPlayed": modestat['roundsPlayed'],
                    "suicides": modestat['suicides'],
                    "swimDistance": modestat['swimDistance'],
                    "teamKills": modestat['teamKills'],
                    "timeSurvived": modestat['timeSurvived'],
                    "timeSurvivedAnswer": time_num(modestat['timeSurvived']),
                    "top10s": modestat['top10s'],
                    "vehicleDestroys": modestat['vehicleDestroys'],
                    "walkDistance": modestat['walkDistance'],
                    "weaponsAcquired": modestat['weaponsAcquired'],
                    "weeklyKills": modestat['weeklyKills'],
                    "weeklyWins": modestat['weeklyWins'],
                    "wins": modestat['wins']
                }
            }
            data['gameMode'].update(i_data)
        return response.json(data, status=200)

@app.route("/api/PUBG/normal/update")
async def update_normal_status(request):
    args = request.get_args(keep_blank_values=True)
    if not ("id" in args): return response.json({'code':'01', 'msg':"Please write your id."}, status=400)
    else: pubg_id = args['id'][0]
    connect = pymysql.connect(host=db_ip, user=db_user, password=db_pw,db=db_name, charset='utf8')
    cur = connect.cursor()
    exist_nickname = pymysql.escape_string("SELECT EXISTS (SELECT name FROM player WHERE id=%s) as succees;")
    cur.execute(exist_nickname,(pubg_id))
    fetch1 = cur.fetchone()
    if fetch1[0]:
        command = pymysql.escape_string("SELECT platform FROM player WHERE id=%s")
        cur.execute(command, (pubg_id))
        platform_info = cur.fetchone()[0]
    else: return response.json({'code':'05', 'msg':"No information about the user was found. Please proceed with \"/PUBG/player\" first."}, status=400)
    if ("season" in args):
        try: season = int(args['season'][0])
        except ValueError: return response.json({'code':'08', 'msg':"Season values can only contain numbers."}, status=400)
        if platform_info >= 0 and platform_info <= 1: type_season = "pc-2018"
        else: type_season = "console"
        if len(str(season)) < 2: season = f"division.bro.official.{type_season}-0{season}"
        else: season = f"division.bro.official.{type_season}-{season}"
    else: season = await get_season(platform_info)
    await s_info.normal_status_update(pubg_id, platform_info, season)
    return response.json({
        "code":"00",
        "msg":"Updated successfully."
    },status=200)

@app.route("/api/PUBG/ranked")
async def ranked_status(request):
    args = request.get_args(keep_blank_values=True)
    if not ("id" in args): return response.json({'code':'01', 'msg':"Please write your id."}, status=400)
    else: pubg_id = args['id'][0]
    connect = pymysql.connect(host=db_ip, user=db_user, password=db_pw,db=db_name, charset='utf8')
    cur = connect.cursor()
    exist_nickname = pymysql.escape_string("SELECT EXISTS (SELECT name FROM player WHERE id=%s) as succees;")
    cur.execute(exist_nickname,(pubg_id))
    fetch1 = cur.fetchone()
    if fetch1[0]:
        command = pymysql.escape_string("SELECT platform FROM player WHERE id=%s")
        cur.execute(command, (pubg_id))
        platform_info = cur.fetchone()[0]
    else: return response.json({'code':'05', 'msg':"No information about the user was found. Please proceed with \"/PUBG/player\" first."}, status=400)
    if ("season" in args):
        try: season = int(args['season'][0])
        except ValueError: return response.json({'code':'08', 'msg':"Season values can only contain numbers."}, status=400)
        if platform_info >= 0 and platform_info <= 1: type_season = "pc-2018"
        else: type_season = "console"
        if len(str(season)) < 2: season = f"division.bro.official.{type_season}-0{season}"
        else: season = f"division.bro.official.{type_season}-{season}"
    else: season = await get_season(platform_info)
    status, html = await s_info.ranked_status(pubg_id,platform_info,season)
    if not status:
        return response.json({'code': html[1], 'msg': html[2]}, status=html[0])
    else:
        data = {
            "id":pubg_id,
            "gameMode":{}
        }
        gamestat = html['data']['attributes']['rankedGameModeStats']
        for i in ['solo','solo-fpp','squad','squad-fpp']:
            if not (i in gamestat):
                i_data = {
                    i: {
                        "assists": 0,
                        "avgRank": 0,
                        "currentRank":{
                            "tier":"Unranked",
                            "subTier":"1"
                        },
                        "currentRankAnswer":"Unranked",
                        "currentRankPoint":0,
                        "bestRank":{
                            "tier":"Unranked",
                            "subTier":"1"
                        },
                        "bestRankAnswer":"Unranked",
                        "bestRankPoint": 0,
                        "damageDealt": 0,
                        "deaths": 0,
                        "dBNOs": 0,
                        "KDA_point": 0,
                        "KD_point": 0,
                        "kills": 0,
                        "top10s": 0,
                        "top10_point": 0,
                        "wins": 0,
                        "win_point": 0
                    }
                }
                data['gameMode'].update(i_data)
                continue
            modestat = gamestat[i]
            losses = modestat['deaths']
            if losses == 0:
                losses = 1
            KD_point = round(modestat['kills'] / losses,2)
            currentTier1 = modestat["currentTier"]["tier"]
            currentTier2 = modestat["currentTier"]["subTier"]
            bestTier1 = modestat["bestTier"]["tier"]
            bestTier2 = modestat["bestTier"]["subTier"]
            if currentTier1 == "Unranked" or currentTier1 == "Master": tier_name1 = currentTier1
            else: tier_name1 = f"{currentTier1} {currentTier2}"
            if bestTier1 == "Unranked" or bestTier1 == "Master": tier_name2 = bestTier1
            else: tier_name2 = f"{bestTier1} {bestTier2}"
            i_data = {
                i:{
                    "assists": modestat['assists'],
                    "avgRank": modestat['avgRank'],
                    "currentRank":modestat['currentTier'],
                    "currentRankAnswer":tier_name1,
                    "currentRankPoint":modestat['currentRankPoint'],
                    "bestRank":modestat['bestTier'],
                    "bestRankAnswer":tier_name2,
                    "bestRankPoint": modestat['bestRankPoint'],
                    "damageDealt": modestat['damageDealt'],
                    "deaths": modestat['deaths'],
                    "dBNOs": modestat['dBNOs'],
                    "KDA_point": modestat['kda'],
                    "KD_point": KD_point,
                    "kills": modestat['kills'],
                    "roundsPlayed": modestat['roundsPlayed'],
                    "top10s": trunc(modestat['top10Ratio'] * modestat['roundsPlayed']),
                    "top10_point": modestat['top10Ratio'],
                    "wins": modestat['wins'],
                    "win_point": modestat['winRatio']
                }
            }
            data['gameMode'].update(i_data)
        return response.json(data, status=200)

@app.route("/api/PUBG/ranked/update")
async def update_ranked_status(request):
    args = request.get_args(keep_blank_values=True)
    if not ("id" in args): return response.json({'code':'01', 'msg':"Please write your id."}, status=400)
    else: pubg_id = args['id'][0]
    connect = pymysql.connect(host=db_ip, user=db_user, password=db_pw,db=db_name, charset='utf8')
    cur = connect.cursor()
    exist_nickname = pymysql.escape_string("SELECT EXISTS (SELECT name FROM player WHERE id=%s) as succees;")
    cur.execute(exist_nickname,(pubg_id))
    fetch1 = cur.fetchone()
    if fetch1[0]:
        command = pymysql.escape_string("SELECT platform FROM player WHERE id=%s")
        cur.execute(command, (pubg_id))
        platform_info = cur.fetchone()[0]
    else: return response.json({'code':'05', 'msg':"No information about the user was found. Please proceed with \"/PUBG/player\" first."}, status=400)
    if ("season" in args):
        try: season = int(args['season'][0])
        except ValueError: return response.json({'code':'08', 'msg':"Season values can only contain numbers."}, status=400)
        if platform_info >= 0 and platform_info <= 1: type_season = "pc-2018"
        else: type_season = "console"
        if len(str(season)) < 2: season = f"division.bro.official.{type_season}-0{season}"
        else: season = f"division.bro.official.{type_season}-{season}"
    else: season = await get_season(platform_info)
    await s_info.ranked_status_update(pubg_id, platform_info, season)
    return response.json({
        "code":"00",
        "msg":"Updated successfully."
    },status=200)


@app.route("/api/PUBG/player/change_platform")
async def change_platform(request):
    args = request.get_args(keep_blank_values=True)
    if not ("nickname" in args): return response.json({'code':'01', 'msg':"Please write your nickname."}, status=400)
    else: nickname = args['nickname'][0]
    connect = pymysql.connect(host=db_ip, user=db_user, password=db_pw,db=db_name, charset='utf8')
    cur = connect.cursor()
    exist_nickname = pymysql.escape_string("SELECT EXISTS (SELECT name FROM player WHERE name=%s) as succees;")
    cur.execute(exist_nickname,(nickname))
    exist = cur.fetchone()
    if exist[0]:
        if not ("platform" in args): return response.json({'code':'02', 'msg':"Please write your platform."}, status=400)
        else:
            try: platform = int(args['platform'][0])
            except ValueError: return response.json({'code':'06', 'msg':"Platform values can only contain numbers."}, status=400)
            if not (platform >= 0 and platform < 5): return response.json({'code':'07', 'msg':"Platform values can contain only 0-4 values."}, status=400)
        command = pymysql.escape_string("UPDATE player SET platform=%s WHERE name=%s")
        cur.execute(command,(platform,nickname))
        connect.commit()
        connect.close()
        return response.json({
            "code":"00",
            "msg":"Updated successfully."
        },status=200)
    else:
        connect.close()
        return response.json({'code': '05','msg': "No information about the user was found. Please proceed with \"/PUBG/player\" first."},status=400)

app.run('127.0.0.1', 3200)