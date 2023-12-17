import trino
import pandas as pd
from preprocess_data import process_dataframe

host = 'localhost'
port = 8080
user = 'root'
catalog = 'datalake'
schema = 'data_big_5_leagues'


conn = trino.dbapi.connect(
    host=host,
    port=port,
    user=user,
    catalog=catalog,
    schema=schema
)

cur = conn.cursor()

# Đổi tên cột
def data():
    # cur.execute('SELECT * FROM all_leagues')
    # rows = cur.fetchall()
    # columns = [desc[0] for desc in cur.description]
    # df = pd.DataFrame(rows, columns=columns)
    df = pd.read_sql('SELECT * FROM all_leagues',conn)
    new_headers = [
        'Date', 'Name', 'Round', 'Venue', 'Result', 'Squad', 'Opponent', 'Start', 'Pos', 'Min',
        'Cmp', 'PassAtt', 'Cmp%', 'PassTotDist', 'PassPrgDist', 'Cmp.1', 'Att.1', 'Cmp%.1',
        'Cmp.2', 'Att.2', 'Cmp%.2', 'Cmp.3', 'Att.3', 'Cmp%.3', 'Ast', 'xA', 'KP', 'PassFinThird',
        'PPA', 'CrsPA', 'PassProg', 'SCA', 'PassLiveShot', 'PassDeadShot', 'DribShot', 'ShLSh',
        'Fld', 'DefShot', 'GCA', 'PassLiveGoal', 'PassDeadGoal', 'DribGoal', 'ShGoal', 'FldGoal',
        'DefGoal', 'Tkl', 'TklW', 'TacklesDef3rd', 'TacklesMid3rd', 'TacklesAtt3rd', 'DribTackled',
        'DribContest', 'DribTackled%', 'Past', 'Press', 'SuccPress', 'SuccPress%',
        'PressDef3rd', 'PressMid3rd', 'PressAtt3rd', 'Blocks', 'BlockSh', 'ShSv', 'Pass', 'Int',
        'Tkl+Int', 'Clr', 'Err', 'Touches', 'Def Pen', 'TouchDef3rd', 'TouchMid3rd', 'TouchAtt3rd',
        'AttPen', 'Live', 'Succ', 'Att', 'Succ%', '#Pl', 'Megs', 'Carries', 'TotDist', 'PrgDist',
        'ProgCarries', 'CarriesFinThird', 'CPA', 'Mis', 'Dis', 'Targ', 'Rec', 'Rec%',
        'ProgPassRec', 'Gls', 'PK', 'PKatt', 'Sh', 'SoT', 'CrdY', 'CrdR', 'xG', 'npxG'
    ]
    df.columns=new_headers
    # d=process_dataframe(df)
    return df