from preprocess_data import process_dataframe
from get_data.get_data import data


def process_data():
    d = data()
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

    d.columns = new_headers
    df = process_dataframe(d)
    return df
