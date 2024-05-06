import psycopg2

def data_after_feature_engineering(DataFrame):
    conn = psycopg2.connect(
            host="localhost",
            database="dw",
            user="datawarehouse",
            password="datawarehouse",
            port= '5432'
            )
    cursor = conn.cursor()

    table_creation='''

        CREATE TABLE IF NOT EXISTS data_warehouse.data_after_feature_engineering (
 
            ID VARCHAR,
            Min FLOAT,
            Name VARCHAR,
            Squad VARCHAR,
            Pos VARCHAR,
            Ast FLOAT,
            Att FLOAT,
            Att1 FLOAT,
            Att2 FLOAT,
            Att3 FLOAT,
            AttPen FLOAT,
            BlockSh FLOAT,
            Blocks FLOAT,
            CPA FLOAT,
            Carries FLOAT,
            CarriesFinThird FLOAT,
            Clr FLOAT,
            Cmp FLOAT,
            Cmp1 FLOAT,
            Cmp2 FLOAT,
            Cmp3 FLOAT,
            CrdR FLOAT,
            CrdY FLOAT,
            CrsPA FLOAT,
            DefGoal FLOAT,
            DefPen FLOAT,
            DefShot FLOAT,
            Dis FLOAT,
            DribContest FLOAT,
            DribTackled FLOAT,
            Err FLOAT,
            Fld FLOAT,
            FldGoal FLOAT,
            GCA FLOAT,
            Gls FLOAT,
            Int FLOAT,
            KP FLOAT,
            Live FLOAT,
            Lost FLOAT,
            Mis FLOAT,
            PK FLOAT,
            PKatt FLOAT,
            PPA FLOAT,
            Pass FLOAT,
            PassAtt FLOAT,
            PassDeadGoal FLOAT,
            PassDeadShot FLOAT,
            PassFinThird FLOAT,
            PassLiveGoal FLOAT,
            PassLiveShot FLOAT,
            PassPrgDist FLOAT,
            PassTotDist FLOAT,
            PrgC FLOAT,
            PrgDist FLOAT,
            PrgP FLOAT,
            PrgR FLOAT,
            Rec FLOAT,
            SCA FLOAT,
            Sh FLOAT,
            ShGoal FLOAT,
            ShLSh FLOAT,
            SoT FLOAT,
            Succ FLOAT,
            TO1 FLOAT,
            TacklesAtt3rd FLOAT,
            TacklesDef3rd FLOAT,
            TacklesMid3rd FLOAT,
            TakeOns FLOAT,
            Tkl FLOAT,
            TklPlusInt FLOAT,
            TklW FLOAT,
            Tkld FLOAT,
            TotDist FLOAT,
            TouchAtt3rd FLOAT,
            TouchDef3rd FLOAT,
            TouchMid3rd FLOAT,
            Touches FLOAT,
            npxG FLOAT,
            xA FLOAT,
            xAG FLOAT,
            xG FLOAT,
            CmpPct FLOAT,
            CmpPct1 FLOAT,
            CmpPct2 FLOAT,
            CmpPct3 FLOAT,
            DribTackledPct FLOAT,
            SuccPct FLOAT,
            TkldPct FLOAT
        ) 
    '''

    cursor.execute(table_creation)
    conn.commit()


    data = DataFrame.to_dict(orient='records')

    # Thực hiện lệnh INSERT
    for record in data:
        columns = ', '.join(record.keys())
        values = ', '.join(['%({})s'.format(col) for col in record.keys()])
        insert_query = f"INSERT INTO data_warehouse.data_after_feature_engineering ({columns}) VALUES ({values})"
        cursor.execute(insert_query, record)

    conn.commit()
    cursor.close()
    conn.close()

def data_after_clean(DataFrame):
    conn = psycopg2.connect(
            host="localhost",
            database="dw",
            user="datawarehouse",
            password="datawarehouse",
            port= '5432'
            )
    cursor = conn.cursor()

    table_creation='''

        CREATE SCHEMA IF NOT EXISTS data_warehouse;

        CREATE TABLE IF NOT EXISTS data_warehouse.data_all_leagues (
            Date VARCHAR,
            Name VARCHAR,
            Round VARCHAR,
            Venue VARCHAR,
            Result VARCHAR,
            Squad VARCHAR,
            Opponent VARCHAR,
            Start VARCHAR,
            Pos VARCHAR,
            Min FLOAT,
            Cmp FLOAT,
            PassAtt FLOAT,
            CmpPct FLOAT,
            PassTotDist FLOAT,
            PassPrgDist FLOAT,
            Cmp1 FLOAT,
            Att1 FLOAT,
            CmpPct1 FLOAT,
            Cmp2 FLOAT,
            Att2 FLOAT,
            CmpPct2 FLOAT,
            Cmp3 FLOAT,
            Att3 FLOAT,
            CmpPct3 FLOAT,
            Ast FLOAT,
            xAG FLOAT,
            xA FLOAT,
            KP FLOAT,
            PassFinThird FLOAT,
            PPA FLOAT,
            CrsPA FLOAT,
            PrgP FLOAT,
            ID VARCHAR,
            SCA FLOAT,
            PassLiveShot FLOAT,
            PassDeadShot FLOAT,
            TakeOns FLOAT,
            ShLSh FLOAT,
            Fld FLOAT,
            DefShot FLOAT,
            GCA FLOAT,
            PassLiveGoal FLOAT,
            PassDeadGoal FLOAT,
            TO1 FLOAT,
            ShGoal FLOAT,
            FldGoal FLOAT,
            DefGoal FLOAT,
            Tkl FLOAT,
            TklW FLOAT,
            TacklesDef3rd FLOAT,
            TacklesMid3rd FLOAT,
            TacklesAtt3rd FLOAT,
            DribTackled FLOAT,
            DribContest FLOAT,
            DribTackledPct FLOAT,
            Lost FLOAT,
            Blocks FLOAT,
            BlockSh FLOAT,
            Pass FLOAT,
            Int FLOAT,
            TklPlusInt FLOAT,
            Clr FLOAT,
            Err FLOAT,
            Touches FLOAT,
            DefPen FLOAT,
            TouchDef3rd FLOAT,
            TouchMid3rd FLOAT,
            TouchAtt3rd FLOAT,
            AttPen FLOAT,
            Live FLOAT,
            Att FLOAT,
            Succ FLOAT,
            SuccPct FLOAT,
            Tkld FLOAT,
            TkldPct FLOAT,
            Carries FLOAT,
            TotDist FLOAT,
            PrgDist FLOAT,
            PrgC FLOAT,
            CarriesFinThird FLOAT,
            CPA FLOAT,
            Mis FLOAT,
            Dis FLOAT,
            Rec FLOAT,
            PrgR FLOAT,
            Gls FLOAT,
            PK FLOAT,
            PKatt FLOAT,
            Sh FLOAT,
            SoT FLOAT,
            CrdY FLOAT,
            CrdR FLOAT,
            xG FLOAT,
            npxG FLOAT
        ) 
    '''

    cursor.execute(table_creation)
    conn.commit()


    data = DataFrame.to_dict(orient='records')

    # Thực hiện lệnh INSERT
    for record in data:
        columns = ', '.join(record.keys())
        values = ', '.join(['%({})s'.format(col) for col in record.keys()])
        insert_query = f"INSERT INTO data_warehouse.data_all_leagues ({columns}) VALUES ({values})"
        cursor.execute(insert_query, record)

    conn.commit()
    cursor.close()
    conn.close()

def a(df):
    print(df)
