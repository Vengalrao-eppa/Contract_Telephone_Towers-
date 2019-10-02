# Requirements
"""
1. Read in the attached file and produce a list sorted by Current Rent in ascending order. Obtain the first 5 items from the resultant list and output to the console

2. From the list of all mast data create new list of mast data with Lease Years = 25 years.
        Output the list to the console, include all data fields.
        Output the total rent for all items in this list to the console.

3. Create a dictionary containing tenant name and a count of masts for each tenant. Output the dictionary to the console in a readable form.
        NOTE. Treat "Everything Everywhere Ltd" and "Hutchinson3G Uk Ltd&Everything Everywhere Ltd" as separate entities.

4. List the data for rentals with Lease Start Date between 1 June 1999 and 31 Aug 2007.
        Output the data to the console with dates formatted as DD/MM/YYYY.

"""

import csv 
import sys
import json
import datetime


def load_csv(csv_path):
    """These are the actions to be performed on the Dataset as per the requirement"""
    
    """ 1.	Load the data file, process and output the data in the forms specified.

        2.	Read in, process and present the data as specified in the requirements section.

        3.	Demonstrate usage of list comprehension for at least one of the tasks.

        4.	Allow user input to run all your script or run specific sections."""

    json_list = []
    reader = open(csv_path, "r")
    headers = reader.readline().strip().split(",")

    line = reader.readline()
    while line:
        json_data = dict(zip(headers, line.strip().replace(", ", " ").split(",")))
        json_list.append(json_data)
        line = reader.readline()
    return json_list


def sort_rent(csv_list, sort_elements=5):
    """sort_rent function is to perform requirement 1 from the assignment."""
    """ Requirement 1:Read in the attached file and produce a list sorted by Current Rent in ascending order.
        Obtain the first 5 items from the resultant list and output to the console. """
    try:
        current_rents = sorted(csv_list, key=lambda k: float(k['Current Rent']))
        output = current_rents[:sort_elements]
        print("Top 5 Current Rent Amounts", current_rents[:sort_elements])
        return output
        
    except TypeError:
        raise Exception("Values should be float data types")


def get_lease_data(csv_list, lease_years=25):
    """get_lease_data function is to perform requirement 2 from the assignment."""
    """ Requirement 2: From the list of all mast data create new list of mast data with Lease Years = 25 years.

        Output the list to the console, include all data fields.

        Output the total rent for all items in this list to the console."""
    try:
        lease_25 = [record for record in csv_list if bool(record["Lease Years"]) \
                    and int(record["Lease Years"])==lease_years]
        total_sum = sum([float(record["Current Rent"]) for record in lease_25])
        print("Lease 25 Total Sum: ", total_sum)
        return total_sum
    except TypeError:
        raise Exception("Invalid Datatypes for Lease Years & Current Rent Columns")
    except Exception as error:
        print("Exception Occurred", error)


def get_tenants_info(csv_list):
    """get_tenants_info function is to perform requirement 3 from the assignment."""
    """Requirement 3: Create a dictionary containing tenant name and a count of masts for each tenant.
        Output the dictionary to the console in a readable form."""
    tenant_dict = {}
    if csv_list:
        for record in csv_list:
            tenant_name = record["Tenant Name"]
            if bool(record["Property Name"]):
                if tenant_dict.get(tenant_name):
                    tenant_dict[tenant_name] += 1
                else:
                    tenant_dict[tenant_name] = 1
            else:
                tenant_dict[tenant_name] = 0
        print("Tenats Info", json.dumps(tenant_dict, indent=4))
        return tenant_dict
    else:
        print("No data found..")


def get_lease_range(csv_list, start_date, end_date):
    """get_lease_range function is to perform requirement 4 from the assignment."""
    """Requirement 4: List the data for rentals with Lease Start Date between 1 June 1999 and 31 Aug 2007.

        Output the data to the console with dates formatted as DD/MM/YYYY."""
    try:
        start_range = datetime.datetime.strptime(start_date.strip(), "%d-%b-%Y")
        end_range = datetime.datetime.strptime(end_date.strip(), "%d-%b-%Y")
        in_range = []
        for record in csv_list:
            lease_date = record["Lease Start Date"]
            if lease_date and lease_date!="n/a":
                lease_start_date = datetime.datetime.strptime(record["Lease Start Date"], "%d-%b-%y")
                if start_range < lease_start_date < end_range:
                    in_range.append(lease_start_date.strftime("%d/%m/%Y"))
        if in_range:
            print(json.dumps(in_range, indent=4))
    except ValueError as error:
        print("Please specify the correct date range", error)
    except Exception as error:
        print("Exception Occurred", error)        

        
if __name__ == "__main__":
    
    #csv_path = r"/Users/vengalraoeppa/desktop/assignments/Mobile Phone Masts_2019.csv"
    csv_path = r"/Users/vengalraoeppa/desktop/assignments/Mobile Phone Masts_2016.csv"
    """This path is the location of the Dataset in my laptop, Please change it to your local drive location"""
    
    csv_list = load_csv(csv_path)

    banner = "Please select the below options\n" \
             "  1. List top 5 Current Rent Amounts\n" \
             "  2. Get Lease data equal to 25 years\n" \
             "  3. Get Tenants & Masts information\n" \
             "  4. Get Lease data between 1 June 1999 and 31 Aug 2007\n" \
             "  5. Exit\n\n" \
             "Enter Option: "

    while True:
        option = str(input(banner))

        if option == "1":
            sort_rent(csv_list, sort_elements=5)
        elif option == "2":
            get_lease_data(csv_list, lease_years=25)
        elif option == "3":
            get_tenants_info(csv_list)
        elif option == "4":
            start_date = "01-Jun-1999"
            end_date = "31-Aug-2007"
            get_lease_range(csv_list, start_date, end_date)
        elif option == "5":
            sys.exit(1)
        else:
            print("Please select from given options")
    

    # creates json_file
    #json_path = r"C:\Users\Vijay.Perumalla\Desktop\support_assignment\codingchallenge\json_1.json"
    #if json_path:
    #    with open(json_path, "w") as writer:
    #        json.dump(csv_list, writer, indent=4)
