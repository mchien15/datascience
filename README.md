# Find similar players using Cosine similarity

## Clone the repo
```
git clone https://github.com/mchien15/datascience.git
```
then navigate to repo's folder

## Install required packages
```
pip install -r requirements.txt
```

This application also requires `Docker`, so if you haven't already installed it on your computer, please follow this [INTRUCTION](https://docs.docker.com/engine/install/)

## Prepare the data

### Start our data lake infrastructure
```
docker compose -f docker-compose.yml up -d
```
### Generate data and push them to MinIO
```
python utils/export_data_to_datalake.py
```

### Create data schema
After pushing your files to `MinIO`, please run the following command to execute the trino container:
```
docker exec -ti datalake-trino bash
```

When you are already inside the `trino` container, run `trino` to enter the interactive mode

After that, run the following command to register a new schema for the data:

```sql
CREATE SCHEMA IF NOT EXISTS datalake.data_big_5_leagues
WITH (location = 's3://data-big-5-leagues/');

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
    xA DOUBLE,
    KP DOUBLE,
    PassFinThird DOUBLE,
    PPA DOUBLE,
    CrsPA DOUBLE,
    PassProg DOUBLE,
    SCA DOUBLE,
    PassLiveShot DOUBLE,
    PassDeadShot DOUBLE,
    DribShot DOUBLE,
    ShLSh DOUBLE,
    Fld DOUBLE,
    DefShot DOUBLE,
    GCA DOUBLE,
    PassLiveGoal DOUBLE,
    PassDeadGoal DOUBLE,
    DribGoal DOUBLE,
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
    Past DOUBLE,
    Press DOUBLE,
    SuccPress DOUBLE,
    SuccPressPct DOUBLE,
    PressDef3rd DOUBLE,
    PressMid3rd DOUBLE,
    PressAtt3rd DOUBLE,
    Blocks DOUBLE,
    BlockSh DOUBLE,
    ShSv DOUBLE,
    Pass DOUBLE,
    Int DOUBLE,
    TklInt DOUBLE,
    Clr DOUBLE,
    Err DOUBLE,
    Touches DOUBLE,
    DefPen DOUBLE,
    TouchDef3rd DOUBLE,
    TouchMid3rd DOUBLE,
    TouchAtt3rd DOUBLE,
    AttPen DOUBLE,
    Live DOUBLE,
    Succ DOUBLE,
    Att DOUBLE,
    SuccPct DOUBLE,
    NumPl DOUBLE,
    Megs DOUBLE,
    Carries DOUBLE,
    TotDist DOUBLE,
    PrgDist DOUBLE,
    ProgCarries DOUBLE,
    CarriesFinThird DOUBLE,
    CPA DOUBLE,
    Mis DOUBLE,
    Dis DOUBLE,
    Targ DOUBLE,
    Rec DOUBLE,
    RecPct DOUBLE,
    ProgPassRec DOUBLE,
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

```


## Run the Streamlit app

Open the new terminal or type `exit` twice, then run this command

```
streamlit run app.py
```

Visit the URL displayed in the terminal (usually http://localhost:8501) to interact with the app