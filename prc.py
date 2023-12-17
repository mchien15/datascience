from preprocess_data import process_dataframe
from get_data.get_data import data
def process_data():
    d=data()
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
    d.columns=new_headers
    df=process_dataframe(d)
    return df