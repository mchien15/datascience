from preprocess_data import process_dataframe
from get_data.get_data import data
def process_data():
    d=data()
    new_headers = [
        'Date', 'Name', 'Round', 'Venue', 'Result', 'Squad', 'Opponent', 'Start', 'Pos', 'Min',
        'Cmp', 'PassAtt', 'Cmp%', 'PassTotDist', 'PassPrgDist', 'Cmp1', 'Att1', 'Cmp%.1',
        'Cmp2', 'Att2', 'Cmp%.2', 'Cmp3', 'Att3', 'Cmp%.3', 'Ast', 'xA', 'KP', 'PassF hird',
        'PPA', 'CrsPA', 'PassProg', 'SCA', 'PassLiveShot', 'PassDeadShot', 'DribShot', 'ShLSh',
        'Fld', 'DefShot', 'GCA', 'PassLiveGoal', 'PassDeadGoal', 'DribGoal', 'ShGoal', 'FldGoal',
        'DefGoal', 'Tkl', 'TklW', 'TacklesDef3rd', 'TacklesMid3rd', 'TacklesAtt3rd', 'DribTackled',
        'DribContest', 'DribTackled%', 'Past', 'Press', 'SuccPress', 'SuccPress%',
        'PressDef3rd', 'PressMid3rd', 'PressAtt3rd', 'Blocks', 'BlockSh', 'ShSv', 'Pass', 'DOUBLE',
        'TklDOUBLE', 'Clr', 'Err', 'Touches', 'DefPen', 'TouchDef3rd', 'TouchMid3rd', 'TouchAtt3rd',
        'AttPen', 'Live', 'Succ', 'Att', 'Succ%', 'NumPl', 'Megs', 'Carries', 'TotDist', 'PrgDist',
        'ProgCarries', 'CarriesFDOUBLEhird', 'CPA', 'Mis', 'Dis', 'Targ', 'Rec', 'Rec%',
        'ProgPassRec', 'Gls', 'PK', 'PKatt', 'Sh', 'SoT', 'CrdY', 'CrdR', 'xG', 'npxG'
    ]
    d.columns=new_headers
    df=process_dataframe(d)
    return df