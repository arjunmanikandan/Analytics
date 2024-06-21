import pandas as pd
import numpy as np
import json,sys

def read_csv(csv_path):
    df = pd.read_csv(csv_path)
    return df

def read_json(json_path):
    with open(json_path,"r") as file:
        data = json.load(file)
    return data

def display_optimal_cost(df):
    print(df)

def calc_optimal_fares(transport_fares):
    optimal_fares={
    "min_cost" : [transport_fares.loc[0,"total_cost"]],
    "max_cost" : [transport_fares.loc[1,"total_cost"]],
    "min_company" :[ transport_fares.loc[0,"Company"]],
    "max_company" : [transport_fares.loc[1,"Company"]]
    }
    return pd.DataFrame(optimal_fares)

def get_fare_details(employee_wages,transport_fares):
    df_list=[]
    for i in range(0,len(employee_wages.index)):
        wage = employee_wages.loc[i]["hourly_wage(₹)"]
        transport_fares["total_cost"] = transport_fares.apply(
            lambda row:(wage/60)*row["Time(mins)"]+row["Price(₹)"],axis=1)
        min_index = transport_fares["total_cost"].idxmin()
        max_index = transport_fares["total_cost"].idxmax()
        fare_details = transport_fares.loc[[min_index,max_index],["total_cost","Company"]].reset_index(drop=True)
        optimal_fare = calc_optimal_fares(fare_details)
        df_list.append(optimal_fare)
    df = pd.concat(df_list, ignore_index=True)
    return employee_wages.join(df)

def main():
    file_paths = read_json(sys.argv[1])
    employee_wages = read_csv(file_paths["employee_wages_path"])
    transport_fares = read_csv(file_paths["transport_fares_path"])
    employee_wages_df = get_fare_details(employee_wages,transport_fares)
    display_optimal_cost(employee_wages_df)

main()