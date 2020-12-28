# PUBG OPEN API official documention
Within this document, you will find detailed instructions on the various functions the PUBG OPEN API allows for.

#### WARING
* URL: All of api is start with https://yhs.kr/api/PUBG by default.
* Response Type: All responses, including errors, are returned in json(application/json) format.
* Date and Time: UTC+9 (Korea, Seoul).

For parameters, send via GET in the form of parameters.

#### Platform info
For platform information, you can send it with a numeric value of 0-4
* 0: Steam
* 1: Kakao
* 2: XBOX (Console)
* 3: Playstation (Console)
* 4: Stadia (Cloud)

## Methods
**<List of Methods>**
* [/player](#player)
* [/normal](#normal)
* [/ranked](#ranked)
* [/normal](#normalupdate)
* [/ranked/update](#rankedupdate)
* [/change_platform](#change_platform)

### /player
Returns the user's DB update time, platform information, and user information. 
You must complete the platform information during first search.
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
		<th>Require Information</th>
		<td>Platform Info</td>
		<td>nickname</td>		
	</tr>
	<tr>
		<th>Type</th>
		<td>number</td>		
		<td>string</td>
	</tr>
</table>

#### Return Value
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
##### Basics
* id: User's ID [String]
* nickname: User's nickname [String]
* platform: Platform Info [number]
* last_update: User's DB update time [json]

##### User's Last_update
* weapon: Unused
* normal: Last Update time of normal status [json]
* ranked: Last Update time of ranked status [json]
* matches: Unused

### /normal
Returns a player's data, such as normal game stats.
```
https://yhs.kr/api/PUBG/normal
```

#### Parameters
<table>
    <tr>
        <th>/</th>
        <th>id</th>
        <th>season</th>
    </tr>
	<tr>
		<th>Require Information</th>
		<td>User's ID</td>
		<td>Season</td>	
	</tr>
	<tr>
		<th>Type</th>
		<td>string</td>		
		<td>number</td>
	</tr>
</table>

#### Return Value
```json
{
    "id": "User's ID",
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
##### Basics
* id: User's ID [string]
* gamemode: Game Stats of User's Gamemode (solo, solo-fpp, duo, duo-fpp, squad, squad-fpp) [json]

##### Information by Game Mode
* assists: Assists [number]
* boosts: Used Boosts [number]
* dBNOs: dBNO(Down But Not Out) count [number]
* dailyKills: Daily Kills count [number]
* dailyWins: Daily Wins count [number]
* damageDealt: damage Dealt [number]
* days: play time (days) [number]
* headshotKills: Headshot Kills count [number]
* heals: Used Heal [number]
* KDA_point: Kill/Deaths/Assists Point [Float]
* KD_point": Kill/Deaths Point [Float]
* kills: Kills count [number]
* longestKill: longest Kill distance [Float]
* longestTimeSurvived: longest Time Survived(Second) [Float]
* longestTimeSurvivedAnswer: longest Time Survived Korean Information [String]
* losses: Losses(Deaths) Count [number]
* maxKillStreaks: Max Kill Streaks [number]
* mostSurvivalTime: Most Survival Time [Float]
* revives: Revives Count [number]
* rideDistance: Distance traveled with car or motorcycle [Float]
* roadKills: kills with car or motorcycle [number]
* roundMostKills: Round Most Kills [number]
* roundsPlayed: Rounds Played [number]
* suicides: Suicides Count [number]
* swimDistance: Distance traveled with swimming [Float]
* teamKills: Team Kills Count [number]
* timeSurvived: Survived time(Second) [Float]
* timeSurvivedAnswer: Survived time Korean Information [String]
* top10s: number of top10 [number]
* vehicleDestroys: vehicle Destroys count [number]
* walkDistance: Distance traveled with walking [Float]
* weaponsAcquired: Number of weapon acquisition [number]
* weeklyKills: Weekly Kills count [number]
* weeklyWins: Weekly Wins count [number]
* wins: Wins count [number]

### /ranked
Returns a player's data, such as ranked game stats.
```
https://yhs.kr/api/PUBG/ranked
```

#### Parameters
<table>
    <tr>
        <th>/</th>
        <th>id</th>
        <th>season</th>
    </tr>
	<tr>
		<th>Require Information</th>
		<td>User's ID</td>
		<td>Season</td>	
	</tr>
	<tr>
		<th>Type</th>
		<td>string</td>		
		<td>number</td>
	</tr>
</table>

#### Return Value
```json
{
    "id": "User's ID",
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
##### Basics
* id: User's ID [string]
* gamemode: Game Stats of User's Gamemode (solo, solo-fpp, duo, duo-fpp, squad, squad-fpp) [json]

##### Information by Game Mode
* assists: Assists [number]
* dBNOs: dBNO(Down But Not Out) count [number]
* bestRank Best Rank [json]
* bestRankAnswer: Best Rank(Integrate into characters) [문자]
* bestRankPoint: Best Rank point [숫자]
* currentRank Current Rank [json]
* currentRankAnswer: Current Rank(Integrate into characters) [문자]
* currentRankPoint: Current Rank [숫자]
* damageDealt: damage Dealt [number]
* deaths: Losses(Deaths) Count [number]
* KDA_point: Kill/Deaths/Assists Point [Float]
* KD_point": Kill/Deaths Point [Float]
* kills: Kills count [number]
* roundsPlayed: Rounds Played [number]
* top10s: number of top10 [number]
* top10s_point: point of top10 [Float]
* wins: Wins count [number]
* wins_point: point of wins [Float]


### /normal/update
update the game stats normal mode
```
https://yhs.kr/api/PUBG/ranked/update
```

#### Parameters
<table>
    <tr>
        <th>/</th>
        <th>id</th>
        <th>season</th>
    </tr>
	<tr>
		<th>Require Information</th>
		<td>User's ID</td>
		<td>Season</td>	
	</tr>
	<tr>
		<th>Type</th>
		<td>string</td>		
		<td>number</td>
	</tr>
</table>

### /ranked/update
update the game stats ranked mode
```
https://yhs.kr/api/PUBG/ranked/update
```

#### Parameters
<table>
    <tr>
        <th>/</th>
        <th>id</th>
        <th>season</th>
    </tr>
	<tr>
		<th>Require Information</th>
		<td>User's ID</td>
		<td>Season</td>	
	</tr>
	<tr>
		<th>Type</th>
		<td>string</td>		
		<td>number</td>
	</tr>
</table>

### /change_platform
If you misregister user platform information, you can change this function.
```
https://yhs.kr/api/PUBG/change_platform
```

#### Parameters
<table>
    <tr>
        <th>/</th>
        <th>platform</th>
        <th>nickname</th>
    </tr>
	<tr>
		<th>Require Information</th>
		<td>Platform Info</td>
		<td>nickname</td>		
	</tr>
	<tr>
		<th>Type</th>
		<td>number</td>		
		<td>string</td>
	</tr>
</table>

## Expection
Information about the error can be found through the status code and the return value within the error.
If no information is required to be returned, the following values are returned.
```json
{
    "code": "00",
    "msg": "successfully."
}
```

* 200(00): Successfully called.
* 400(01,02): Please write something(check msg)
* 400(05): No information about the user was found. Please proceed with "/PUBG/player" first.
* 400(06): Platform values can only contain numbers.
* 400(07): Platform values can contain only 0-4 values.
* 400(08): Season values can only contain numbers.
* 401(03): Failed to get DB.
* 404(04): Unable to find the information.
* 431(31): Invalid content specification.
* 432(32): Too many requests have been received.
* 433(33): An unknown error has occurred.
