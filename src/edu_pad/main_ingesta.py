import pandas as pd
from edu_pad.database import Database

def main_2():
    db = Database()
    df = pd.read_csv("src/edu_pad/static/csv/data_extractora.csv")
    df_bd = db.guardar_df(df)
    df_bd2 = db.obtener_datos()
    df_bd2.to_csv("src/edu_pad/static/csv/data_bd.csv", index=False)
    
