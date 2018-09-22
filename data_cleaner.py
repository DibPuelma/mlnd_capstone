import requests as req
import pandas as pd

# https://twitter.com/RodrigoWagnerB/status/410907897019629568

API_HOST = 'https://api.rutify.cl/rut/'

# get the address, commune and sex for each RUT in the database
def get_data(rut):
    r = req.get(API_HOST + str(rut))
    data = r.json()
    if 'servel' in data:
        return [data['servel']['domicilio electoral'], data['servel']['comuna'], data['sexo']]
    else:
        return ['','','']

# add a verification number or check number to each RUT
# in Chile, the mod11 algorithm is used
def get_verify_number(rut):
    rut = str(rut)
    multiplier = 0
    sum = 0
    for item in rut[::-1]:
        sum += int(item) * ((multiplier % 6) + 2)
        multiplier += 1
    result = (11 - sum%11)
    if result == 11:
        digit = '0'
    elif result == 10:
        digit = 'K'
    else:
        digit = str(result)
    return rut + digit

# clean the wholesale customers from the database,
# these are considered to buy 3 or more items in only one purchase.
# it receives the whole dataframe

def clean_majorists(df):
    count = 0
    last_row = df.iloc[0]
    indexes = [0]
    to_delete = []
    for index, row in df.iterrows():
        if index > 0:
            if last_row['KOEN'] == row['KOEN']:
                indexes.append(index - 1)
                count += 1
            else:
                count = 0
                indexes = []
            if count >= 3:
                to_delete += indexes + [index]
            last_row = row
    df = df.drop(to_delete)
    df = df[df['KOEN'] != '96521550']
    df = df[df['TIDO'] == 'BLV']

    df = df[df['CANTIDAD'] > 0]

    df = df[df['CANTIDAD'] < 5]
    df = add_verify(df)
    return df

# get the age of the customer from the RUT using a regression found in
# https://twitter.com/rodrigowagnerb/status/410907897019629568?lang=es
def get_age(rut):
    result = 2018 - (int(rut)/1000000*3.46 + 1930)
    if result > 12:
        return result
    else:
        return 0

# add the verification number to the dataframe
def add_verify(df):
    verifies = []
    for index, row in df.iterrows():
        verifies.append(get_verify_number(row['KOEN']))
    verify_serie = pd.Series(verifies)
    df['rut_v'] = verify_serie.values
    return df

# add the age to the dataframe
def add_age(df):
    df['age'] = df['rut'].apply(get_age)
    return df

# add the address to the dataframe
def add_address(df):
    data_dict = {'address': [], 'commune': [], 'sex': []}
    rows = df.shape[0]
    for index, row in df.iterrows():
        if index % 25 == 0:
            print('{}/{}'.format(index, rows))
        rut_data = get_data(row['rut_v'])
        data_dict['address'].append(rut_data[0])
        data_dict['commune'].append(rut_data[1])
        data_dict['sex'].append(rut_data[2])

    address_serie = pd.Series(data_dict['address'])
    df['address'] = address_serie.values

    commune_serie = pd.Series(data_dict['commune'])
    df['commune'] = commune_serie.values

    sex_serie = pd.Series(data_dict['sex'])
    df['sex'] = sex_serie.values
    return df

# rename some columns for readability and delete two columns
# that have duplicated information
def clean_columns(df):
    df = df.rename(columns={
                    'FECHA': 'date',
                    'MES': 'month',
                    'AÑO': 'year',
                    'NOKOSU': 'store',
                    'KOEN': 'rut',
                    'NOKOEN': 'name',
                    'EMAIL': 'email',
                    'TIDO': 'purchase_type',
                    'FMPR': 'category',
                    'CANTIDAD': 'quantity',
                    'NETO': 'total_value'})
    df = df.drop(columns=['CAPRCO1', 'VANELI'])
    return df

df = pd.read_csv('capstone_processed_data.csv')
df = add_address(df)
df.to_csv('capstone_processed_data.csv')
