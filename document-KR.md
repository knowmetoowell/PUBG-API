# PUBG OPEN API 공식문서
이곳에서는 PUBG Open-API 사용법에 대해 서술되어 있습니다.

#### 유의사항
* URL: 기본적으로 https://yhs.kr/api/PUBG 으로 시작합니다.
* 응답형식: 오류를 포함한, 모든 응답은 json(application/json) 형태로 반환됩니다.
* 날짜: 기본적으로 UTC+9(한국, 서울)로 설정되어있습니다.

매개변수의 경우 params 형태로 GET을 통해 보내주시기 바랍니다.

#### 플랫폼 정보
플랫폼 정보의 경우 0~4라는 숫자값을 통해 보낼 수 있습니다.
* 0: 스팀
* 1: 카카오
* 2: XBOX (콘솔)
* 3:플레이스테이션 (콘솔)
* 4: 스테디아(클라우드)

## 종류
**<목차>**
* [/player](#player)
* [/normal](#normal)
* [/ranked](#ranked)
* [/normal](#normalupdate)
* [/ranked/update](#rankedupdate)
* [/change_platform](#change_platform)

### /player
유저의 DB 업데이트 시간과, 플랫폼 정보, 유저 정보를 반환합니다. 최초 1회 검색시에는 꼭 플랫폼 정보를 작성해야 합니다.
```
https://yhs.kr/api/PUBG/player
```

#### 매개변수
<table>
    <tr>
        <th>/</th>
        <th>platform</th>
        <th>nickname</th>
    </tr>
	<tr>
		<th>요청하는 정보</th>
		<td>플랫폼 정보</td>
		<td>유저명</td>		
	</tr>
	<tr>
		<th>요청 형태</th>
		<td>number(숫자)</td>		
		<td>string(문자)</td>
	</tr>
</table>

#### 반환 값
```json
{
    "id": "user id",
    "nickname": "nickname",
    "platform": 0,
    "lastupdate": {
        "weapon": {
            "years": 1,
            "months": 1,
            "days": 1,
            "hours": 0,
            "minutes": 0
        },
        "matches": {
            "years": 1,
            "months": 1,
            "days": 1,
            "hours": 0,
            "minutes": 0
        },
        "normal": {
            "years": 1,
            "months": 1,
            "days": 1,
            "hours": 0,
            "minutes": 0
        },
        "ranked": {
            "years": 1,
            "months": 1,
            "days": 1,
            "hours": 0,
            "minutes": 0
        }
    }
}
```
##### 기본
* id: 유저의 ID [문자]
* nickname: 유저의 닉네임 [문자]
* platform: 해당 유저의 플랫폼 정보 [숫자]
* last_update: 유저 DB 업데이트 정보 [json]

##### 유저 업데이트 정보
* weapon: 미사용
* normal: 일반전 DB 업데이트 정보 [json]
* ranked: 경쟁전 DB 업데이트 정보 [json]
* matches: 미사용

### /normal
검색하는 유저에 일반 전적을 불러옵니다.
```
https://yhs.kr/api/PUBG/normal
```

#### 매개변수
<table>
    <tr>
        <th>/</th>
        <th>id</th>
        <th>season</th>
    </tr>
	<tr>
		<th>요청하는 정보</th>
		<td>유저의 ID</td>
		<td>시즌(옵션)</td>		
	</tr>
	<tr>
		<th>요청 형태</th>
		<td>string(문자)</td>		
		<td>string(문자)</td>
	</tr>
</table>

#### 반환 값
```json
{
    "id": "유저의 ID",
    "gameMode": {
        "solo": {
            "assists": 0,
            "boosts": 0,
            "dBNOs": 0,
            "dailyKills": 0,
            "dailyWins": 0,
            "damageDealt": 0,
            "days": 0,
            "headshotKills": 0,
            "heals": 0,
            "KDA_point": 0.0,
            "KD_point": 0.0,
            "kills": 0,
            "longestKill": 0,
            "longestTimeSurvived": 0,
            "longestTimeSurvivedAnswer": "0초",
            "losses": 0,
            "maxKillStreaks": 0,
            "mostSurvivalTime": 0,
            "revives": 0,
            "rideDistance": 0,
            "roadKills": 0,
            "roundMostKills": 0,
            "roundsPlayed": 0,
            "suicides": 0,
            "swimDistance": 0,
            "teamKills": 0,
            "timeSurvived": 0,
            "timeSurvivedAnswer": "0초",
            "top10s": 0,
            "vehicleDestroys": 0,
            "walkDistance": 0,
            "weaponsAcquired": 0,
            "weeklyKills": 0,
            "weeklyWins": 0,
            "wins": 0
        },
        "solo-fpp": {
            "assists": 0,
            "boosts": 0,
            "dBNOs": 0,
            "dailyKills": 0,
            "dailyWins": 0,
            "damageDealt": 0,
            "days": 0,
            "headshotKills": 0,
            "heals": 0,
            "KDA_point": 0.0,
            "KD_point": 0.0,
            "kills": 0,
            "longestKill": 0,
            "longestTimeSurvived": 0,
            "longestTimeSurvivedAnswer": "0초",
            "losses": 0,
            "maxKillStreaks": 0,
            "mostSurvivalTime": 0,
            "revives": 0,
            "rideDistance": 0,
            "roadKills": 0,
            "roundMostKills": 0,
            "roundsPlayed": 0,
            "suicides": 0,
            "swimDistance": 0,
            "teamKills": 0,
            "timeSurvived": 0,
            "timeSurvivedAnswer": "0초",
            "top10s": 0,
            "vehicleDestroys": 0,
            "walkDistance": 0,
            "weaponsAcquired": 0,
            "weeklyKills": 0,
            "weeklyWins": 0,
            "wins": 0
        },
        "duo": {
            "assists": 0,
            "boosts": 0,
            "dBNOs": 0,
            "dailyKills": 0,
            "dailyWins": 0,
            "damageDealt": 0,
            "days": 0,
            "headshotKills": 0,
            "heals": 0,
            "KDA_point": 0.0,
            "KD_point": 0.0,
            "kills": 0,
            "longestKill": 0,
            "longestTimeSurvived": 0,
            "longestTimeSurvivedAnswer": "0초",
            "losses": 0,
            "maxKillStreaks": 0,
            "mostSurvivalTime": 0,
            "revives": 0,
            "rideDistance": 0,
            "roadKills": 0,
            "roundMostKills": 0,
            "roundsPlayed": 0,
            "suicides": 0,
            "swimDistance": 0,
            "teamKills": 0,
            "timeSurvived": 0,
            "timeSurvivedAnswer": "0초",
            "top10s": 0,
            "vehicleDestroys": 0,
            "walkDistance": 0,
            "weaponsAcquired": 0,
            "weeklyKills": 0,
            "weeklyWins": 0,
            "wins": 0
        },
        "duo-fpp": {
            "assists": 0,
            "boosts": 0,
            "dBNOs": 0,
            "dailyKills": 0,
            "dailyWins": 0,
            "damageDealt": 0,
            "days": 0,
            "headshotKills": 0,
            "heals": 0,
            "KDA_point": 0.0,
            "KD_point": 0.0,
            "kills": 0,
            "longestKill": 0,
            "longestTimeSurvived": 0,
            "longestTimeSurvivedAnswer": "0초",
            "losses": 0,
            "maxKillStreaks": 0,
            "mostSurvivalTime": 0,
            "revives": 0,
            "rideDistance": 0,
            "roadKills": 0,
            "roundMostKills": 0,
            "roundsPlayed": 0,
            "suicides": 0,
            "swimDistance": 0,
            "teamKills": 0,
            "timeSurvived": 0,
            "timeSurvivedAnswer": "0초",
            "top10s": 0,
            "vehicleDestroys": 0,
            "walkDistance": 0,
            "weaponsAcquired": 0,
            "weeklyKills": 0,
            "weeklyWins": 0,
            "wins": 0
        },
        "squad": {
            "assists": 0,
            "boosts": 0,
            "dBNOs": 0,
            "dailyKills": 0,
            "dailyWins": 0,
            "damageDealt": 0,
            "days": 0,
            "headshotKills": 0,
            "heals": 0,
            "KDA_point": 0.0,
            "KD_point": 0.0,
            "kills": 0,
            "longestKill": 0,
            "longestTimeSurvived": 0,
            "longestTimeSurvivedAnswer": "0초",
            "losses": 0,
            "maxKillStreaks": 0,
            "mostSurvivalTime": 0,
            "revives": 0,
            "rideDistance": 0,
            "roadKills": 0,
            "roundMostKills": 0,
            "roundsPlayed": 0,
            "suicides": 0,
            "swimDistance": 0,
            "teamKills": 0,
            "timeSurvived": 0,
            "timeSurvivedAnswer": "0초",
            "top10s": 0,
            "vehicleDestroys": 0,
            "walkDistance": 0,
            "weaponsAcquired": 0,
            "weeklyKills": 0,
            "weeklyWins": 0,
            "wins": 0
        },
        "squad-fpp": {
            "assists": 0,
            "boosts": 0,
            "dBNOs": 0,
            "dailyKills": 0,
            "dailyWins": 0,
            "damageDealt": 0,
            "days": 0,
            "headshotKills": 0,
            "heals": 0,
            "KDA_point": 0.0,
            "KD_point": 0.0,
            "kills": 0,
            "longestKill": 0,
            "longestTimeSurvived": 0,
            "longestTimeSurvivedAnswer": "0초",
            "losses": 0,
            "maxKillStreaks": 0,
            "mostSurvivalTime": 0,
            "revives": 0,
            "rideDistance": 0,
            "roadKills": 0,
            "roundMostKills": 0,
            "roundsPlayed": 0,
            "suicides": 0,
            "swimDistance": 0,
            "teamKills": 0,
            "timeSurvived": 0,
            "timeSurvivedAnswer": "0초",
            "top10s": 0,
            "vehicleDestroys": 0,
            "walkDistance": 0,
            "weaponsAcquired": 0,
            "weeklyKills": 0,
            "weeklyWins": 0,
            "wins": 0
        }
    }
}
```
##### 기본
* id: 유저의 ID(문자)
* gamemode: 게임모드 별 전적을 반환합니다. [solo, solo-fpp, duo, duo-fpp, squad, squad-fpp] (json)

##### 게임모드 별 정보(gamemode)
* assists: 어시스트 [숫자]
* boosts: 도핑 아이템 사용횟수 [숫자]
* dBNOs: dBNO(Down But Not Out, 기절하였지만 아웃으로 처리되지 않은 것)횟수 [숫자]
* dailyKills: 일당 킬 횟수 [숫자]
* dailyWins: 일당 우승 횟수 [숫자]
* damageDealt: 평균 피해량 [숫자]
* days: 플레이시간(일)만 반환합니다. [숫자]
* headshotKills: 헤드샷 횟수 [숫자]
* heals: 힐 아이템(구급상자, 붕대, 의료용 키트)사용 횟수 [숫자]
* KDA_point: 킬/데스/어시스트 점수 [소수]
* KD_point": 킬/데스 점수 [소수]
* kills: 킬 횟수 [숫자]
* longestKill: 최대 저격 거리 [소수]
* longestTimeSurvived: 생존시간(초) [소수]
* longestTimeSurvivedAnswer: 생존시간 [문자]
* losses: 패배(사망) 횟수 [숫자]
* maxKillStreaks: 여포 횟수 [숫자]
* mostSurvivalTime: 평균 생존 시간(초) [소수]
* revives: 소생 횟수 [숫자]
* rideDistance: 자동차, 오토바이등을 이용한 이동 거리 [소수]
* roadKills: 로드킬(고라니) 횟수 [숫자]
* roundMostKills: 라운드별 평균 킬 [숫자]
* roundsPlayed: 플레이 횟수 [숫자]
* suicides: 자살 횟수 [숫자]
* swimDistance: 수영을 이용한 이동 거리 [소수]
* teamKills: 팀킬 횟수 [숫자]
* timeSurvived: 생존 시간(초) [소수]
* timeSurvivedAnswer: 생존 시간 [문자]
* top10s: top10 횟수 [숫자]
* vehicleDestroys: 차량 파괴 횟수 [숫자]
* walkDistance: 걸어서 이동한 거리 [소수]
* weaponsAcquired: 무기 획득한 횟수 [숫자]
* weeklyKills: 주당 킬 횟수 [숫자]
* weeklyWins: 주당 우승 횟수 [숫자]
* wins: 우승 [숫자]

### /ranked
검색하는 유저에 경쟁 전적을 불러옵니다.
```
https://yhs.kr/api/PUBG/ranked
```

#### 매개변수
<table>
    <tr>
        <th>/</th>
        <th>id</th>
        <th>season</th>
    </tr>
	<tr>
		<th>요청하는 정보</th>
		<td>유저의 ID</td>
		<td>시즌(옵션)</td>		
	</tr>
	<tr>
		<th>요청 형태</th>
		<td>string(문자)</td>		
		<td>string(문자)</td>
	</tr>
</table>

#### 반환 값
```json
{
    "id": "유저의 ID",
    "gameMode": {
        "solo": {
            "assists": 0,
            "avgRank": 0,
            "currentRank": {
                "tier": "Unranked",
                "subTier": "1"
            },
            "currentRankAnswer": "Unranked",
            "currentRankPoint": 0,
            "bestRank": {
                "tier": "Unranked",
                "subTier": "1"
            },
            "bestRankAnswer": "Unranked",
            "bestRankPoint": 0,
            "damageDealt": 0,
            "deaths": 0,
            "dBNOs": 0,
            "KDA_point": 0,
            "KD_point": 0,
            "kills": 0,
            "roundsPlayed": 0,
            "top10s": 0,
            "top10_point": 0,
            "wins": 0,
            "win_point": 0
        },
        "solo-fpp": {
            "assists": 0,
            "avgRank": 0,
            "currentRank": {
                "tier": "Unranked",
                "subTier": "1"
            },
            "currentRankAnswer": "Unranked",
            "currentRankPoint": 0,
            "bestRank": {
                "tier": "Unranked",
                "subTier": "1"
            },
            "bestRankAnswer": "Unranked",
            "bestRankPoint": 0,
            "damageDealt": 0,
            "deaths": 0,
            "dBNOs": 0,
            "KDA_point": 0,
            "KD_point": 0,
            "kills": 0,
            "roundsPlayed": 0,
            "top10s": 0,
            "top10_point": 0,
            "wins": 0,
            "win_point": 0
        },
        "squad": {
            "assists": 0,
            "avgRank": 0,
            "currentRank": {
                "tier": "Unranked",
                "subTier": "1"
            },
            "currentRankAnswer": "Unranked",
            "currentRankPoint": 0,
            "bestRank": {
                "tier": "Unranked",
                "subTier": "1"
            },
            "bestRankAnswer": "Unranked",
            "bestRankPoint": 0,
            "damageDealt": 0,
            "deaths": 0,
            "dBNOs": 0,
            "KDA_point": 0,
            "KD_point": 0,
            "kills": 0,
            "roundsPlayed": 0,
            "top10s": 0,
            "top10_point": 0,
            "wins": 0,
            "win_point": 0
        },
        "squad-fpp": {
            "assists": 0,
            "avgRank": 0,
            "currentRank": {
                "tier": "Unranked",
                "subTier": "1"
            },
            "currentRankAnswer": "Unranked",
            "currentRankPoint": 0,
            "bestRank": {
                "tier": "Unranked",
                "subTier": "1"
            },
            "bestRankAnswer": "Unranked",
            "bestRankPoint": 0,
            "damageDealt": 0,
            "deaths": 0,
            "dBNOs": 0,
            "KDA_point": 0,
            "KD_point": 0,
            "kills": 0,
            "roundsPlayed": 0,
            "top10s": 0,
            "top10_point": 0,
            "wins": 0,
            "win_point": 0
        }
    }
}
```
##### 기본
* id: 유저의 ID(문자)
* gamemode: 게임모드 별 전적을 반환합니다. [solo, solo-fpp, squad, squad-fpp] (json)

##### 게임모드 별 정보(gamemode)
* assists: 어시스트 [숫자]
* avgRank: 평균 순위 [숫자]
* bestRank 최대 랭크 [json]
* bestRankAnswer: 최대 랭크(한 문자로 통합시켰습니다.) [문자]
* bestRankPoint: 최대 랭크 점수 [숫자]
* currentRank 현재 랭크 [json]
* currentRankAnswer: 현재 랭크(한 문자로 통합시켰습니다.) [문자]
* currentRankPoint: 현재 랭크 점수 [숫자]
* dBNOs: dBNO(Down But Not Out, 기절하였지만 아웃으로 처리되지 않은 것)횟수 [숫자]
* damageDealt: 평균 피해량 [숫자]
* deaths: 패배(사망) 횟수 [숫자]
* KDA_point: 킬/데스/어시스트 점수 [소수]
* KD_point": 킬/데스 점수 [소수]
* kills: 킬 횟수 [숫자]
* roundsPlayed: 플레이 횟수 [숫자]
* top10s: 탑률 [숫자]
* top10s_point: top10 점수 [소수]
* wins: 우승 횟수 [숫자]
* wins_point: 승률 [소수]


### /normal/update
검색하는 유저에 일반 전적을 업데이트 합니다.
```
https://yhs.kr/api/PUBG/ranked/update
```

#### 매개변수
<table>
    <tr>
        <th>/</th>
        <th>id</th>
        <th>season</th>
    </tr>
	<tr>
		<th>요청하는 정보</th>
		<td>유저의 ID</td>
		<td>시즌(옵션)</td>		
	</tr>
	<tr>
		<th>요청 형태</th>
		<td>string(문자)</td>		
		<td>string(문자)</td>
	</tr>
</table>

### /ranked/update
검색하는 유저에 경쟁 전적을 업데이트 합니다.
```
https://yhs.kr/api/PUBG/ranked/update
```

#### 매개변수
<table>
    <tr>
        <th>/</th>
        <th>id</th>
        <th>season</th>
    </tr>
	<tr>
		<th>요청하는 정보</th>
		<td>유저의 ID</td>
		<td>시즌(옵션)</td>		
	</tr>
	<tr>
		<th>요청 형태</th>
		<td>string(문자)</td>		
		<td>string(문자)</td>
	</tr>
</table>

### /change_platform
만약 유저 플랫폼 정보를 잘못 등록했을 경우 위 기능을 통하여 변경하실 수 있습니다.
```
https://yhs.kr/api/PUBG/change_platform
```

#### 매개변수
<table>
    <tr>
        <th>/</th>
        <th>platform</th>
        <th>nickname</th>
    </tr>
	<tr>
		<th>요청하는 정보</th>
		<td>플랫폼 정보</td>
		<td>유저명</td>		
	</tr>
	<tr>
		<th>요청 형태</th>
		<td>number(숫자)</td>		
		<td>string(문자)</td>
	</tr>
</table>

## 오류 반환 정보
오류의 정보는 status code와 오류내 반환값을 통해 를 통해 확인하실 수 있습니다.
반환해야하는 정보가 굳이 없는 경우 아래의 값이 반환됩니다.
```json
{
    "code": "00",
    "msg": "successfully."
}
```

* 200(00): 성공적으로 반환됨.
* 400(01,02): 누락된 정보(msg 확인 요망)
* 400(05): /PUBG/player를 통해 유저를 DB에 우선적으로 등록해주기 바람.
* 400(06): platform 매개변수의 값이 형태가 잘못됨.
* 400(07): platform 매개변수의 값이 잘못됨. (0-4)의 정보만 받을수 있음.
* 400(08): 시즌 정보는 오직 숫자를 통해 받을 수 있음.
* 401(03): DB로 부터 불러오는 것을 실패함. 
* 404(04): 정보를 찾을 수 없음
* 431(31): 콘텐츠 규격이 잘못됨.
* 432(32): 너무 많은 요청이 들어옴.
* 433(33): 알 수없는 오류가 발생함.
