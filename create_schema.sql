CREATE SCHEMA IF NOT EXISTS datalake.data_big_5_leagues WITH (location = 's3://data-big-5-leagues/');

CREATE TABLE IF NOT EXISTS datalake.data_big_5_leagues.all_leagues (
    Date VARCHAR,
    Name VARCHAR,
    Round VARCHAR,
    Venue VARCHAR,
    Result VARCHAR,
    Squad VARCHAR,
    Opponent VARCHAR,
    Start VARCHAR,
    Pos VARCHAR,
    Min DOUBLE,
    Cmp DOUBLE,
    PassAtt DOUBLE,
    CmpPct DOUBLE,
    PassTotDist DOUBLE,
    PassPrgDist DOUBLE,
    Cmp1 DOUBLE,
    Att1 DOUBLE,
    CmpPct1 DOUBLE,
    Cmp2 DOUBLE,
    Att2 DOUBLE,
    CmpPct2 DOUBLE,
    Cmp3 DOUBLE,
    Att3 DOUBLE,
    CmpPct3 DOUBLE,
    Ast DOUBLE,
    xAG DOUBLE,
    xA DOUBLE,
    KP DOUBLE,
    PassFinThird DOUBLE,
    PPA DOUBLE,
    CrsPA DOUBLE,
    PrgP DOUBLE,
    ID VARCHAR,
    SCA DOUBLE,
    PassLiveShot DOUBLE,
    PassDeadShot DOUBLE,
    TO DOUBLE,
    ShLSh DOUBLE,
    Fld DOUBLE,
    DefShot DOUBLE,
    GCA DOUBLE,
    PassLiveGoal DOUBLE,
    PassDeadGoal DOUBLE,
    TO1 DOUBLE,
    ShGoal DOUBLE,
    FldGoal DOUBLE,
    DefGoal DOUBLE,
    Tkl DOUBLE,
    TklW DOUBLE,
    TacklesDef3rd DOUBLE,
    TacklesMid3rd DOUBLE,
    TacklesAtt3rd DOUBLE,
    DribTackled DOUBLE,
    DribContest DOUBLE,
    DribTackledPct DOUBLE,
    Lost DOUBLE,
    Blocks DOUBLE,
    BlockSh DOUBLE,
    Pass DOUBLE,
    Int DOUBLE,
    TklPlusInt DOUBLE,
    Clr DOUBLE,
    Err DOUBLE,
    Touches DOUBLE,
    DefPen DOUBLE,
    TouchDef3rd DOUBLE,
    TouchMid3rd DOUBLE,
    TouchAtt3rd DOUBLE,
    AttPen DOUBLE,
    Live DOUBLE,
    Att DOUBLE,
    Succ DOUBLE,
    SuccPct DOUBLE,
    Tkld DOUBLE,
    TkldPct DOUBLE,
    Carries DOUBLE,
    TotDist DOUBLE,
    PrgDist DOUBLE,
    PrgC DOUBLE,
    CarriesFinThird DOUBLE,
    CPA DOUBLE,
    Mis DOUBLE,
    Dis DOUBLE,
    Rec DOUBLE,
    PrgR DOUBLE,
    Gls DOUBLE,
    PK DOUBLE,
    PKatt DOUBLE,
    Sh DOUBLE,
    SoT DOUBLE,
    CrdY DOUBLE,
    CrdR DOUBLE,
    xG DOUBLE,
    npxG DOUBLE
) WITH (
    external_location = 's3://data-big-5-leagues/players/',
    format = 'PARQUET'
);