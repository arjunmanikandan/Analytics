import pandas as pd

def read_csv(csv_path):
    df = pd.read_csv(csv_path)
    return df

# Function to calculate costs
def calculate_costs(df, wage):
    df['total_cost'] = df.apply(lambda row: (wage / 60) * row['Time(mins)'] + row['Price(₹)'], axis=1)
    return df

# Helper function to get min and max fares for each employee
def get_min_max_fares(emp_row, transport_fares):
    print
    wage = emp_row['hourly_wage(₹)']
    calculated_fares = calculate_costs(transport_fares.copy(), wage)
    min_fare = calculated_fares.loc[calculated_fares['total_cost'].idxmin()]
    max_fare = calculated_fares.loc[calculated_fares['total_cost'].idxmax()]
    
    return {
        'min_total_cost': min_fare['total_cost'],
        'min_company': min_fare['Company'],
        'max_total_cost': max_fare['total_cost'],
        'max_company': max_fare['Company']
    }
# Apply calculations and find min/max costs using lambdas
def get_fare_details(employee_wages, transport_fares):
    fare_details_list = employee_wages.apply(lambda row: get_min_max_fares(row, transport_fares), axis=1)
    fare_details_df = pd.DataFrame(fare_details_list.tolist(), index=employee_wages.index)
    return pd.concat([employee_wages, fare_details_df], axis=1)



# Calculate and display the fare details
employee_wages = read_csv("employee_wages.csv")
transport_fares = read_csv("transport_fares.csv")
fare_details_df = get_fare_details(employee_wages, transport_fares)
print(fare_details_df)

