import pandas as pd
import sys
import locale
from tabulate import tabulate

def read_csv(csv_path):
    df = pd.read_csv(csv_path)
    return df

def display_optimal_cost(optimal_cost,wage_per_min,wage_per_hour):
    print("Wages/Hour: ",locale.currency(wage_per_hour))
    print("Wages/min: ",locale.currency(wage_per_min))
    print(tabulate(optimal_cost.values.tolist(),headers=optimal_cost.columns,tablefmt="grid"))

def calc_optimal_cost(transport_prices,wage_per_hour):
    wage_per_min = round(wage_per_hour/60,2)
    transport_prices["TotalCost"] = transport_prices["Time(mins)"] * wage_per_min + transport_prices["Price(₹)"]
    transport_prices.sort_values(by="TotalCost",ascending=True,inplace=True,ignore_index=True)
    return transport_prices,wage_per_min

def main():
    csv_path = sys.argv[1]
    wage_per_hour = int(sys.argv[2])
    locale.setlocale(locale.LC_ALL, 'en_IN')
    transport_prices = read_csv(csv_path)
    optimal_cost,wage_per_min = calc_optimal_cost(transport_prices,wage_per_hour)
    display_optimal_cost(optimal_cost,wage_per_min,wage_per_hour)
    
main()
