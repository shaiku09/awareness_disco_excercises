import pandas as pd 

def change_age(df_in):
    df_out = df_in.copy()
    widowed_25a = df_out[(df_out['Age']<=25) & (df_out['Marital Status']=='Widowed')]
    df_out.loc[widowed_25a.index, 'Age'] = 25
    return df_out

