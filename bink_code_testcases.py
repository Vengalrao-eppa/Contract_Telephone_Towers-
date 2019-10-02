import unittest
import bink_code_assignment

sample_data = [
    {
        "Units Reference": "14173/001",
        "Unit Name": "\"Baileys Towers Bailey Lane \"",
        "Tenant Name": "CTIL (Vodafone/O2/T Mobile) Cornerstone Telecommunications Infrastructure Ltd",
        "Property Name": "Bailey Lane",
        "Property Address": "LS14 6PY",
        "Lease Start Date": "31-Mar-15",
        "Lease End Date": "n/a",
        "Lease Years": "0",
        "Next Rent Review": "31-Mar-20",
        "Current Rent": "15000",
        "Unit type": "Antenna"
    },
    {
        "Units Reference": "14173/003",
        "Unit Name": "Baileys Towers Bailey Lane",
        "Tenant Name": "The Office of Communications (Ofcom)",
        "Property Name": "Bailey Lane",
        "Property Address": "LS14 6PY",
        "Lease Start Date": "14-Jan-11",
        "Lease End Date": "13-Jan-14",
        "Lease Years": "3",
        "Next Rent Review": "n/a",
        "Current Rent": "996",
        "Unit type": "Antenna"
    }
]


class TestCases(unittest.TestCase):
      
    def setUp(self): 
        pass

    def test_sort_rents(self, test_data=None, sort_elements=2):
        output = bink_code_assignment.sort_rent(sample_data, sort_elements)
        self.assertEqual(len(output), sort_elements)

    def test_get_lease_data(self, lease_years=3):

        lease = [record for record in sample_data if bool(record["Lease Years"]) \
                    and int(record["Lease Years"])==lease_years]
        total_sum = bink_code_assignment.get_lease_data(sample_data, lease_years)

        self.assertEqual(total_sum, 996.0)

    def test_get_tenants_info(self):

        tenants_info = bink_code_assignment.get_tenants_info(sample_data)
        self.assertEqual(type(tenants_info), dict)        
    

if __name__ == '__main__':
    unittest.main() 











        
        
