from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
import pandas as pd
import time

def get_player_name(path):

    browser = webdriver.Chrome(service=Service(path))
    player = {}

    seasons = ['2022-2023','2021-2022','2020-2021']
    # seasons = ['2022-2023']
    
    # cái này điền ID và tên của team, ID lấy từ trên web, cứu search tên đội ra là nó có thêm ID ở URL
    # dấu cách thì thay bằng dấu gạch ngang 

   #  EPL_dict = {
   # '361ca564':'Totenham-Hotspur',
   # 'd3fd31cc':'Everton',
   # '822bd0ba':'Liverpool',
   # 'cff3d9bb':'Chelsea',
   # '47c64c55':'Crystal-Palace',
   # '19538871':'Manchester-United',
   # '5bfb9659':'Leeds-United',
   # '33c895d4':'Southampton',
   # 'b8fd03ef':'Manchester-City',
   # '7c21e445':'West-Ham-United',
   # 'a2d435b3':'Leicester-City',
   # '8cec06e1':'Wolverhampton-Wanderers',
   # 'd07537b9':'Brighton-and-Hove-Albion',
   # '18bb7c10':'Arsenal',
   # 'cd051869':'Brentford',
   # '943e8050':'Burnley',
   # '1c781004':'Norwich-City',
   # '2abfe087':'Watford',
   #  'b2b47a98':'Newcastle-United',
   #  '8602292d':'Aston-Villa'
# }
    
    Laliga_dict = {
   '9024a00a':'Girona',
   '53a2f082':'Real-Madrid',
   '206d90db':'Barcelona',
   'db3b9613':'Atletico-Madrid',
   '2b390eca':'Athletic-Club',
   'e31d1cd9':'Real-Sociedad',
   'fc536746':'Real-Betis',
   '0049d422':'Las-Palmas',
   'dcc91a7b':'Valencia',
   '98e8af82':'Rayo-Vallecano',
   '7848bd64':'Getafe',
   '03c57e2b':'Osasuna',
   'ad2be733':'Sevilla',
   '2a8183b3':'Villarreal',
   '8d6fd021':'Alaves',
   'ee7c297c':'Cadiz',
   '2aa12281':'Mallorca',
   'f25da7fb':'Celta-Vigo',
    'a0435291':'Granada',
    '78ecf4bb':'Almeria',
    '17859612':'Valladolid',
    'a8661628':'Espanyol',
    '6c8b07df':'Elche',
    '9800b6a1':'Levante',
    'c6c493e6':'Huesca',
    'bea5c710':'Eibar'
}
    
    # for team in EPL_dict:
    #     for year in seasons:
    #         try:
    #             browser.get('https://fbref.com/en/squads/'+team+'/'+year+'/'+EPL_dict[team]+'-Stats')
    #             tbody = browser.find_element(By.XPATH, '//*[@id="stats_standard_9"]/tbody')

    #             elements = tbody.find_elements(By.TAG_NAME, 'tr')
    #             for element in elements:
    #                 element2 = element.find_element(By.TAG_NAME, 'th')
    #                 id = element2.get_attribute('data-append-csv')
    #                 name1 = element2.get_attribute('csk')
    #                 if id == None or name1 == None:
    #                     continue
    #                 player[id] = name1
    #         except:
    #             print("Invalid Team", EPL_dict[team])
    # browser.quit()
    # return player

    for team in Laliga_dict:
        for year in seasons:
            try:
                browser.get('https://fbref.com/en/squads/'+team+'/'+year+'/'+Laliga_dict[team]+'-Stats')
                tbody = browser.find_element(By.XPATH, '//*[@id="stats_standard_12"]/tbody')

                elements = tbody.find_elements(By.TAG_NAME, 'tr')
                for element in elements:
                    element2 = element.find_element(By.TAG_NAME, 'th')
                    id = element2.get_attribute('data-append-csv')
                    name1 = element2.get_attribute('csk')
                    if id == None or name1 == None:
                        continue
                    player[id] = name1
            except:
                print("Invalid Team", Laliga_dict[team])
    browser.quit()
    return player

def crawl_player(player,player_file_name):
    print('Crawling...')
    seasons = ['2022-2023','2021-2022','2020-2021']
    # seasons = ['2022-2023']
    for i in player:
        for year in seasons:
            player_link = 'https://fbref.com/en/players/'+i+'/matchlogs/'+year+'/keeper/'+i+'-Match-Logs'
            new_player_link = player_link.replace("keeper", "passing")
            try:
                df = pd.read_html(new_player_link, header=1)[0]
                df = df.drop(columns=['Match Report'])
                df = df.drop(columns=['Comp'], errors = 'ignore')
                df = df.rename(columns={"Day": "Name"})
                df.dropna(subset=["Date"], inplace=True)
                df['Name'] = df['Name'].replace(
                    ['Mon', 'Tue', 'Wed', 'Thu', 'Fri', 'Sat', 'Sun'], player[i])
                df = df.rename(columns={"Att": "PassAtt"})
                df = df.rename(
                    columns={"TotDist": "PassTotDist"})
                df = df.rename(columns={"PrgDist": "PassPrgDist"})
                df = df.rename(columns={"1/3": "PassFinThird"})
                df = df.rename(columns={"Prog": "PassProg"})
                df.fillna(0, inplace=True)

                time.sleep(3)
                new_player_link = player_link.replace("keeper", "gca")
                df_2 = pd.read_html(new_player_link, header=1)[0]
                df_2 = df_2.drop(columns=['Match Report'])
                df_2 = df_2.drop(columns=['Comp'], errors = 'ignore')
                df_2 = df_2.rename(columns={"Day": "Name"})
                df_2.dropna(subset=["Date"], inplace=True)
                df_2['Name'] = df_2['Name'].replace(
                    ['Mon', 'Tue', 'Wed', 'Thu', 'Fri', 'Sat', 'Sun'], player[i])
                df_2 = df_2.drop(['Date', 'Name', 'Round', 'Venue', 'Result',
                                'Squad', 'Opponent', 'Start', 'Pos', 'Min'], axis=1)
                df_2 = df_2.rename(
                    columns={"PassLive": "PassLiveShot"})
                df_2 = df_2.rename(
                    columns={"PassDead": "PassDeadShot"})
                df_2 = df_2.rename(
                    columns={"Drib": "DribShot"})
                df_2 = df_2.rename(
                    columns={"Sh": "ShLSh"})
                df_2 = df_2.rename(
                    columns={"Def": "DefShot"})
                df_2 = df_2.rename(
                    columns={"PassLive.1": "PassLiveGoal"})
                df_2 = df_2.rename(
                    columns={"PassDead.1": "PassDeadGoal"})
                df_2 = df_2.rename(
                    columns={"Drib.1": "DribGoal"})
                df_2 = df_2.rename(columns={"Sh.1": "ShGoal"})
                df_2 = df_2.rename(columns={"Fld.1": "FldGoal"})
                df_2 = df_2.rename(
                    columns={"Def.1": "DefGoal"})
                df_2.fillna(0, inplace=True)

                time.sleep(3)
                new_player_link = player_link.replace("keeper", "defense")
                df_3 = pd.read_html(new_player_link, header=1)[0]
                df_3 = df_3.drop(columns=['Match Report'])
                df_3 = df_3.drop(columns=['Comp'], errors = 'ignore')
                df_3 = df_3.rename(columns={"Day": "Name"})
                df_3.dropna(subset=["Date"], inplace=True)
                df_3['Name'] = df_3['Name'].replace(
                    ['Mon', 'Tue', 'Wed', 'Thu', 'Fri', 'Sat', 'Sun'], player[i])
                df_3 = df_3.drop(['Date', 'Name', 'Round', 'Venue', 'Result',
                                'Squad', 'Opponent', 'Start', 'Pos', 'Min'], axis=1)
                df_3 = df_3.rename(
                    columns={"Def 3rd": "TacklesDef3rd"})
                df_3 = df_3.rename(
                    columns={"Mid 3rd": "TacklesMid3rd"})
                df_3 = df_3.rename(columns={"Att 3rd": "TacklesAtt3rd"})
                df_3 = df_3.rename(columns={"Tkl.1": "DribTackled"})
                df_3 = df_3.rename(columns={"Att": "DribContest"})
                df_3 = df_3.rename(columns={"Tkl%": "DribTackled%"})
                df_3 = df_3.rename(columns={"Succ": "SuccPress"})
                df_3 = df_3.rename(columns={"%": "SuccPress%"})
                df_3 = df_3.rename(
                    columns={"Def 3rd.1": "PressDef3rd"})
                df_3 = df_3.rename(
                    columns={"Mid 3rd.1": "PressMid3rd"})
                df_3 = df_3.rename(
                    columns={"Att 3rd.1": "PressAtt3rd"})
                df_3 = df_3.rename(
                    columns={"Sh": "BlockSh"})
                df_3.fillna(0, inplace=True)

                time.sleep(3)
                new_player_link = player_link.replace("keeper", "possession")
                df_4 = pd.read_html(new_player_link, header=1)[0]
                df_4 = df_4.drop(columns=['Match Report'])
                df_4 = df_4.drop(columns=['Comp'], errors = 'ignore')
                df_4 = df_4.rename(columns={"Day": "Name"})
                df_4.dropna(subset=["Date"], inplace=True)
                df_4['Name'] = df_4['Name'].replace(
                    ['Mon', 'Tue', 'Wed', 'Thu', 'Fri', 'Sat', 'Sun'], player[i])
                df_4 = df_4.drop(['Date', 'Name', 'Round', 'Venue', 'Result',
                                'Squad', 'Opponent', 'Start', 'Pos', 'Min'], axis=1)
                df_4 = df_4.rename(columns={"Def 3rd": "TouchDef3rd"})
                df_4 = df_4.rename(columns={"Mid 3rd": "TouchMid3rd"})
                df_4 = df_4.rename(columns={"Att 3rd": "TouchAtt3rd"})
                df_4 = df_4.rename(
                    columns={"Att Pen": "AttPen"})
                df_4 = df_4.rename(columns={"Prog": "ProgCarries"})
                df_4 = df_4.rename(columns={"1/3": "CarriesFinThird"})
                df_4 = df_4.rename(columns={"Prog.1": "ProgPassRec"})
                df_4.fillna(0, inplace=True)

                time.sleep(3)
                new_player_link = player_link.replace("keeper", "summary")
                df_5 = pd.read_html(new_player_link, header=1)[0]
                df_5 = df_5.drop(columns=['Match Report'])
                df_5 = df_5.drop(columns=['Comp'], errors = 'ignore')
                df_5 = df_5.drop(columns=['Ast'], errors = 'ignore')
                df_5 = df_5.drop(columns=['Ast'], errors = 'ignore')
                df_5 = df_5.drop(columns=['Press'], errors = 'ignore')
                df_5 = df_5.drop(columns=['Tkl'], errors = 'ignore')
                df_5 = df_5.drop(columns=['Int'], errors = 'ignore')
                df_5 = df_5.drop(columns=['Blocks'], errors = 'ignore')
                df_5 = df_5.drop(columns=['xA'], errors = 'ignore')
                df_5 = df_5.drop(columns=['SCA'], errors = 'ignore')
                df_5 = df_5.drop(columns=['GCA'], errors = 'ignore')

                df_5 = df_5.drop(columns=['Cmp'], errors = 'ignore')
                df_5 = df_5.drop(columns=['Att'], errors = 'ignore')
                df_5 = df_5.drop(columns=['Cmp%'], errors = 'ignore')
                df_5 = df_5.drop(columns=['Prog'], errors = 'ignore')

                df_5 = df_5.drop(columns=['Carries'], errors = 'ignore')
                df_5 = df_5.drop(columns=['Prog.1'], errors = 'ignore')

                df_5 = df_5.drop(columns=['Succ'], errors = 'ignore')
                df_5 = df_5.drop(columns=['Att.1'], errors = 'ignore')

                df_5 = df_5.drop(columns=['Fls'], errors = 'ignore')
                df_5 = df_5.drop(columns=['Fld'], errors = 'ignore')
                df_5 = df_5.drop(columns=['Off'], errors = 'ignore')
                df_5 = df_5.drop(columns=['Crs'], errors = 'ignore')
                df_5 = df_5.drop(columns=['TklW'], errors = 'ignore')
                df_5 = df_5.drop(columns=['OG'], errors = 'ignore')
                df_5 = df_5.drop(columns=['PKwon'], errors = 'ignore')
                df_5 = df_5.drop(columns=['PKcon'], errors = 'ignore')
                df_5 = df_5.drop(columns=['Touches'], errors = 'ignore')

                df_5 = df_5.rename(columns={"Day": "Name"})
                df_5.dropna(subset=["Date"], inplace=True)
                df_5['Name'] = df_5['Name'].replace(
                    ['Mon', 'Tue', 'Wed', 'Thu', 'Fri', 'Sat', 'Sun'], player[i])
                df_5 = df_5.drop(['Date', 'Name', 'Round', 'Venue', 'Result',
                                'Squad', 'Opponent', 'Start', 'Pos', 'Min'], axis=1)
                df_5.fillna(0, inplace=True)
                    
                concatenated = pd.concat([df, df_2, df_3, df_4, df_5], axis=1)
                
                concatenated.drop(
                    concatenated[concatenated["Date"] == "Date"].index, inplace=True)
                concatenated.drop(
                        concatenated[concatenated["Pos"] == "On matchday squad, but did not play"].index, inplace=True)
                concatenated.drop(
                        concatenated[concatenated["Pos"] == "GK"].index, inplace=True)
                concatenated['sort'] = concatenated['Round'].str.extract(
                        '(\d+)', expand=False).astype(float)
                concatenated.sort_values('sort', inplace=True)
                concatenated = concatenated.drop('sort', axis=1)

                try:
                    f = open(player_file_name)
                    concatenated.to_csv(
                        player_file_name, index=False, header=False, mode='a')
                    f.close()
                except:
                    concatenated.to_csv(player_file_name, index=False)
            except Exception as e:
                print(e)
                print("Invalid Outfield Player", player[i])

if __name__ == "__main__":
    path = 'chromedriver'
    player_file_name = "/home/asus/stuDYING/IT/DataScience/project/laliga_20_23.csv"
    player = get_player_name(path)
    crawl_player(player,player_file_name)
    print("_____DONE_____")