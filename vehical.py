

def vehicle_details(vehicle_number, owner_name, vehicle_type, year_of_manufacture):
    result = (
        f"Vehicle Number: {vehicle_number}\n"
        f"Owner Name: {owner_name}\n"
        f"Vehicle Type: {vehicle_type}\n"
        f"Year of Manufacture: {year_of_manufacture}\n"
    )
    return result

if __name__ == "__main__":
    vehicle_number = "KA31ca0541"
    owner_name = "sanjana"
    vehicle_type = "two wheeler"
    year_of_manufacture = 2020
    print(vehicle_details(vehicle_number, owner_name, 
                          vehicle_type, year_of_manufacture))