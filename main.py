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

def calc_total_cost(row,wage):
    return (wage/60)*row["Time(mins)"]+ row["Price(₹)"]

def get_fare_details(transport_fares,employee_wages):
    hourly_wages = employee_wages["hourly_wage(₹)"].tolist()
    min_list,max_list=[],[]
    for wage in hourly_wages:
        transport_fares["total_cost"] = transport_fares.apply(calc_total_cost,axis=1,args=(wage,))
        min_list.append(transport_fares["total_cost"].min())
        max_list.append(transport_fares["total_cost"].max())
    fare_details =  {
        "min":min_list,
        "max":max_list}
    return fare_details

def calc_optimal_cost(transport_fares,employee_wages):
    fare_details = get_fare_details(transport_fares,employee_wages)
    employee_wages["min"] = fare_details["min"]
    employee_wages["max"] = fare_details["max"]
    return employee_wages

def main():
    file_paths = read_json("config.json")
    employee_wages = read_csv(file_paths["employee_wages_path"])
    transport_fares = read_csv(file_paths["transport_fares_path"])
    employee_wages_df = calc_optimal_cost(transport_fares,employee_wages)
    display_optimal_cost(employee_wages_df)

main()

