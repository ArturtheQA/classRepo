import csv

def street_validation(state,town,street,zip):
        is_state_valid = state is not None and len(str(state).strip())
        if not is_state_valid:
            return False
        is_town_valid = town is not None and len(str(town).strip())
        if not is_town_valid:
            return False
        is_street_valid = street is not None and len(str(street).strip())
        if not is_street_valid:
            return False
        is_zip_valid = zip is not None and len(str(zip).strip())
        if not is_zip_valid:
            return False
        return True


def adress_input():
    street=input('Please palace some street')
    town = input('please place some town')
    state=input('please place some state')
    zip=input('please place some zip')
    return street,town,state,zip

def adress_verify_engine(state,town,street,zip)
    if street in streets and town in towns and state in states and zip in zips:
        print("adress is correct")
