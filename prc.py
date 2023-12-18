from preprocess_data import process_dataframe
from get_data.get_data import data
def process_data():
    d=data()
    new_headers = [
        'Date', 'Name', 'Round', 'Venue', 'Result', 'Squad', 'Opponent', 'Start', 'Pos', 'Min',
        'Cmp', 'PassAtt', 'CmpPct', 'PassTotDist', 'PassPrgDist', 'Cmp1', 'Att1', 'CmpPct1',
        'Cmp2', 'Att2', 'CmpPct2', 'Cmp3', 'Att3', 'CmpPct3', 'Ast', 'xA', 'KP', 'PassFinThird',
        'PPA', 'CrsPA', 'PassProg', 'SCA', 'PassLiveShot', 'PassDeadShot', 'DribShot', 'ShLSh',
        'Fld', 'DefShot', 'GCA', 'PassLiveGoal', 'PassDeadGoal', 'DribGoal', 'ShGoal', 'FldGoal',
        'DefGoal', 'Tkl', 'TklW', 'TacklesDef3rd', 'TacklesMid3rd', 'TacklesAtt3rd', 'DribTackled',
        'DribContest', 'DribTackledPct', 'Past', 'Press', 'SuccPress', 'SuccPressPct',
        'PressDef3rd', 'PressMid3rd', 'PressAtt3rd', 'Blocks', 'BlockSh', 'ShSv', 'Pass', 'Int',
        'TklInt', 'Clr', 'Err', 'Touches', 'DefPen', 'TouchDef3rd', 'TouchMid3rd', 'TouchAtt3rd',
        'AttPen', 'Live', 'Succ', 'Att', 'SuccPct', 'NumPl', 'Megs', 'Carries', 'TotDist', 'PrgDist',
        'ProgCarries', 'CarriesFinThird', 'CPA', 'Mis', 'Dis', 'Targ', 'Rec', 'RecPct',
        'ProgPassRec', 'Gls', 'PK', 'PKatt', 'Sh', 'SoT', 'CrdY', 'CrdR', 'xG', 'npxG'
    ]
    d.columns=new_headers
    df=process_dataframe(d)
    return df