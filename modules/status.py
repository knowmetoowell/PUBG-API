import aiohttp
import pymysql
import json
import os
import sys
import importlib
import datetime

directory = os.path.dirname(os.path.abspath(__file__)).replace("\\","/").replace("modules","")
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

header = {
  "Authorization": "Bearer " + pubg_token,
  "Accept": "application/vnd.api+json"
}

sys.path.append(directory + "/modules") #다른 파일내 함수추가
p_info = importlib.import_module("player")

platform_site = ["steam","kakao","xbox","psn","stadia"]

def response_num(response):
    if response == 200: return [200,'00',"Successfully called."]
    elif response == 400: return [400,'01',"Please write your nickname."]
    elif response == 401: return [401,'03',"Failed to get DB. Please try again later."]
    elif response == 404: return [404,'04',"Unable to find the user."]
    elif response == 415: return [431,'31',"Invalid content specification. Please contact API manufacturer."]
    elif response == 429: return [432,'32',"Too many requests have been received. Please try again later."]
    else: return [433,'33',"An unknown error has occurred. Please contact the manager."]

async def season_status(player_id,platform,season):
    connect = pymysql.connect(host=db_ip, user=db_user, password=db_pw,db=db_name, charset='utf8')
    cur = connect.cursor()
    player_module = p_info.player(player_id)
    exist_season = pymysql.escape_string("SELECT EXISTS (SELECT id, html, season FROM NORMAL_STATUS WHERE id=%s and season=%s) as succees;")
    cur.execute(exist_season, (player_id, season))
    fetch2 = cur.fetchone()
    if fetch2[0]:
        command = pymysql.escape_string("SELECT html FROM NORMAL_STATUS WHERE id=%s and season=%s")
        cur.execute(command, (player_id, season))
        return_value = json.loads(cur.fetchone()[0])
        if await player_module.autopost("normal"):
            status, return_value = await season_status_update(player_id,platform,season)
            if not status:
                connect.close()
                return False, return_value
    else:
        url = f"https://api.pubg.com/shards/{platform_site[platform]}/players/{player_id}/seasons/{season}"
        async with aiohttp.ClientSession() as session:
            async with session.get(url, headers=header) as resp:
                if resp.status == 200:
                    return_value = await resp.json()
                else:
                    e_resp = response_num(resp)
                    return False, e_resp
        sql = pymysql.escape_string("insert into NORMAL_STATUS(id,html,season) VALUES(%s, %s, %s)")
        insert_data = json.dumps(return_value)
        cur.execute(sql, (player_id,insert_data,season))
        connect.commit()
        await player_module.lastupdate_insert("normal",datetime.datetime.now())
    connect.close()
    return True, return_value

async def season_status_update(player_id,platform,season):
    connect = pymysql.connect(host=db_ip, user=db_user, password=db_pw,db=db_name, charset='utf8')
    cur = connect.cursor()
    player_module = p_info.player(player_id)
    url = f"https://api.pubg.com/shards/{platform_site[platform]}/players/{player_id}/seasons/{season}"
    async with aiohttp.ClientSession() as session:
        async with session.get(url, headers=header) as resp:
            if resp.status == 200:
                return_value = await resp.json()
            else:
                e_resp = response_num(resp)
                return False, e_resp
    sql = pymysql.escape_string("UPDATE NORMAL_STATUS SET html=%s WHERE id=%s and season=%s")
    cur.execute(sql, (json.dumps(return_value), player_id, season))
    connect.commit()
    await player_module.lastupdate_insert("normal", datetime.datetime.now())
    connect.close()
    return True, return_value

async def ranked_status(player_id,platform,season):
    connect = pymysql.connect(host=db_ip, user=db_user, password=db_pw,db=db_name, charset='utf8')
    cur = connect.cursor()
    player_module = p_info.player(player_id)
    exist_season = pymysql.escape_string("SELECT EXISTS (SELECT id, html, season FROM RANKED_STATUS WHERE id=%s and season=%s) as succees;")
    cur.execute(exist_season, (player_id, season))
    fetch2 = cur.fetchone()
    if fetch2[0]:
        command = pymysql.escape_string("SELECT html FROM RANKED_STATUS WHERE id=%s and season=%s")
        cur.execute(command, (player_id, season))
        return_value = json.loads(cur.fetchone()[0])
        if await player_module.autopost("ranked"):
            status, return_value = await ranked_status_update(player_id,platform,season)
            if not status:
                connect.close()
                return False, return_value
    else:
        url = f"https://api.pubg.com/shards/{platform_site[platform]}/players/{player_id}/seasons/{season}/ranked"
        async with aiohttp.ClientSession() as session:
            async with session.get(url, headers=header) as resp:
                if resp.status == 200:
                    return_value = await resp.json()
                else:
                    e_resp = response_num(resp)
                    return False, e_resp
        sql = pymysql.escape_string("insert into RANKED_STATUS(id,html,season) VALUES(%s, %s, %s)")
        insert_data = json.dumps(return_value)
        cur.execute(sql, (player_id,insert_data,season))
        connect.commit()
        await player_module.lastupdate_insert("ranked",datetime.datetime.now())
    connect.close()
    return True, return_value

async def ranked_status_update(player_id,platform,season):
    connect = pymysql.connect(host=db_ip, user=db_user, password=db_pw,db=db_name, charset='utf8')
    cur = connect.cursor()
    player_module = p_info.player(player_id)
    url = f"https://api.pubg.com/shards/{platform_site[platform]}/players/{player_id}/seasons/{season}/ranked"
    async with aiohttp.ClientSession() as session:
        async with session.get(url, headers=header) as resp:
            if resp.status == 200:
                return_value = await resp.json()
            else:
                e_resp = response_num(resp)
                return False, e_resp
    sql = pymysql.escape_string("UPDATE RANKED_STATUS SET html=%s WHERE id=%s and season=%s")
    cur.execute(sql, (json.dumps(return_value), player_id, season))
    connect.commit()
    await player_module.lastupdate_insert("ranked", datetime.datetime.now())
    connect.close()
    return True, return_value