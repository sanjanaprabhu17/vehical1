from vehical import vehicle_details

def test_vehicle_details():
    vehicle_number = "KA-01-1234"
    owner_name = "John Doe"
    vehicle_type = "Car"
    year_of_manufacture = 2020
    expected_output = (
        "Vehicle Number: KA-01-1234\n"
        "Owner Name: John Doe\n"
        "Vehicle Type: Car\n"
        "Year of Manufacture: 2020\n"
    )
    actual_output = vehicle_details(vehicle_number, owner_name, vehicle_type, year_of_manufacture)
    assert actual_output == expected_output
