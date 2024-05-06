import pandas as pd 
from prc import process_data
import psycopg2

def data_from_trino():
    conn = psycopg2.connect(
                host="localhost",
                database="dw",
                user="datawarehouse",
                password="datawarehouse",
                port= '5432'
                )
    df = pd.read_sql_query('select * from data_warehouse.data_all_leagues ',con=conn)
    new_headers = [
            "Date", "Name", "Round", "Venue", "Result", "Squad", "Opponent", "Start", "Pos",
            "Min", "Cmp", "PassAtt", "CmpPct", "PassTotDist", "PassPrgDist", "Cmp1", "Att1",
            "CmpPct1", "Cmp2", "Att2", "CmpPct2", "Cmp3", "Att3", "CmpPct3", "Ast", "xAG", "xA",
            "KP", "PassFinThird", "PPA", "CrsPA", "PrgP", "ID", "SCA", "PassLiveShot",
            "PassDeadShot", "TakeOns", "ShLSh", "Fld", "DefShot", "GCA", "PassLiveGoal", "PassDeadGoal",
            "TO1", "ShGoal", "FldGoal", "DefGoal", "Tkl", "TklW", "TacklesDef3rd", "TacklesMid3rd",
            "TacklesAtt3rd", "DribTackled", "DribContest", "DribTackledPct", "Lost", "Blocks",
            "BlockSh", "Pass", "Int", "TklPlusInt", "Clr", "Err", "Touches", "DefPen",
            "TouchDef3rd", "TouchMid3rd", "TouchAtt3rd", "AttPen", "Live", "Att", "Succ", "SuccPct",
            "Tkld", "TkldPct", "Carries", "TotDist", "PrgDist", "PrgC", "CarriesFinThird", "CPA",
            "Mis", "Dis", "Rec", "PrgR", "Gls", "PK", "PKatt", "Sh", "SoT", "CrdY", "CrdR", "xG",
            "npxG"
        ]

    df.columns=new_headers
    return df
def final_data():
    conn = psycopg2.connect(
                host="localhost",
                database="dw",
                user="datawarehouse",
                password="datawarehouse",
                port= '5432'
                )
    df = pd.read_sql_query('select * from data_warehouse.data_after_feature_engineering ',con=conn)
    new_headers = [
            "ID", "Min", "Name", "Squad", "Pos",
            "Cmp", "PassAtt", "CmpPct", "PassTotDist", "PassPrgDist", "Cmp1", "Att1",
            "CmpPct1", "Cmp2", "Att2", "CmpPct2", "Cmp3", "Att3", "CmpPct3", "Ast", "xAG", "xA",
            "KP", "PassFinThird", "PPA", "CrsPA", "PrgP",  "SCA", "PassLiveShot",
            "PassDeadShot", "TakeOns", "ShLSh", "Fld", "DefShot", "GCA", "PassLiveGoal", "PassDeadGoal",
            "TO1", "ShGoal", "FldGoal", "DefGoal", "Tkl", "TklW", "TacklesDef3rd", "TacklesMid3rd",
            "TacklesAtt3rd", "DribTackled", "DribContest", "DribTackledPct", "Lost", "Blocks",
            "BlockSh", "Pass", "Int", "TklPlusInt", "Clr", "Err", "Touches", "DefPen",
            "TouchDef3rd", "TouchMid3rd", "TouchAtt3rd", "AttPen", "Live", "Att", "Succ", "SuccPct",
            "Tkld", "TkldPct", "Carries", "TotDist", "PrgDist", "PrgC", "CarriesFinThird", "CPA",
            "Mis", "Dis", "Rec", "PrgR", "Gls", "PK", "PKatt", "Sh", "SoT", "CrdY", "CrdR", "xG",
            "npxG"
        ]

    df.columns=new_headers
    return df