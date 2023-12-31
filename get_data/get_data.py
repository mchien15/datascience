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
        "Date", "Name", "Round", "Venue", "Result", "Squad", "Opponent", "Start", "Pos",
        "Min", "Cmp", "PassAtt", "CmpPct", "PassTotDist", "PassPrgDist", "Cmp1", "Att1",
        "CmpPct1", "Cmp2", "Att2", "CmpPct2", "Cmp3", "Att3", "CmpPct3", "Ast", "xAG", "xA",
        "KP", "PassFinThird", "PPA", "CrsPA", "PrgP", "ID", "SCA", "PassLiveShot",
        "PassDeadShot", "TO", "ShLSh", "Fld", "DefShot", "GCA", "PassLiveGoal", "PassDeadGoal",
        "TO1", "ShGoal", "FldGoal", "DefGoal", "Tkl", "TklW", "TacklesDef3rd", "TacklesMid3rd",
        "TacklesAtt3rd", "DribTackled", "DribContest", "DribTackledPct", "Lost", "Blocks",
        "BlockSh", "Pass", "Int", "TklPlusInt", "Clr", "Err", "Touches", "DefPen",
        "TouchDef3rd", "TouchMid3rd", "TouchAtt3rd", "AttPen", "Live", "Att", "Succ", "SuccPct",
        "Tkld", "TkldPct", "Carries", "TotDist", "PrgDist", "PrgC", "CarriesFinThird", "CPA",
        "Mis", "Dis", "Rec", "PrgR", "Gls", "PK", "PKatt", "Sh", "SoT", "CrdY", "CrdR", "xG",
        "npxG"
    ]
    df.columns=new_headers
    # d=process_dataframe(df)
    return df