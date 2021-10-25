import mysql.connector

'''FootballPlayers = mysql.connector.connect(
  host="localhost",
  user="root",
  password="oscar0405"
)

mycursor = FootballPlayers.cursor()

mycursor.execute("CREATE DATABASE FootballPlayers")'''


import pandas as pd

mycsv = pd.read_csv("players_21.csv")
print(mycsv.head())

mycsv['goalkeeperSkills'] = (mycsv['goalkeeping_handling'] + mycsv['goalkeeping_diving'] + mycsv['goalkeeping_kicking'] + mycsv['goalkeeping_positioning'] + mycsv['goalkeeping_reflexes']) / 5
mycsv['id'] = mycsv['sofifa_id']

playerTable = mycsv[['id', 'long_name', 'age', 'height_cm', 'weight_kg', 'nationality', 'club_name', 'team_jersey_number']]
playerTable = playerTable[playerTable['team_jersey_number'].notna()]
playerTable['team_jersey_number'] = playerTable['team_jersey_number'].astype(int)

teamTable = mycsv[['club_name', 'league_name', 'league_rank']]

playerPriceTable = mycsv[['id', 'value_eur', 'wage_eur', 'release_clause_eur']]

playerCharacteristicsTable = mycsv[['id', 'team_position', 'preferred_foot', 'pace', 'shooting', 'passing', 'dribbling', 'defending', 'physic', 'goalkeeperSkills', 'player_traits']]

print(playerTable.dtypes)


footballplayers = mysql.connector.connect(
  host="localhost",
  user="root",
  password="oscar0405",
  database="footballplayers"
)

mycursor = footballplayers.cursor()

"""
CREATION OF THE TABLE --> PLAYER 
WARNING : ONLY RUN ONCE

mycursor.execute('CREATE TABLE IF NOT EXISTS player (id int primary key, long_name varchar(255), age int, height_cm int, weight_kg int, nationality varchar(255), club_name varchar(255), team_jersey_number int)')
footballplayers.commit()


for row in playerTable.itertuples():
    mycursor.execute('''
                INSERT INTO player (id, long_name, age, height_cm, weight_kg, nationality, club_name, team_jersey_number)
                VALUES (%s,%s,%s,%s,%s,%s,%s,%s)
                ''',
                (row.id,
                row.long_name,
                row.age,
                row.height_cm,
                row.weight_kg,
                row.nationality,
                row.club_name,
                row.team_jersey_number)
                )
footballplayers.commit()"""
