"""  Mohammad Zaid Tauqir
     PSID: 1900570
"""

def get_age():
    age = int(input())
    # TODO: Raise excpetion for invalid ages
    if 18 <= age <= 75:
        return age
    raise ValueError("Invalid age.")
# TODO: Complete fat_burning_heart_rate() function
def fat_burning_heart_rate(age):
    heart_rate = (220-age)* 0.7
    return heart_rate

if __name__ == "__main__":
    # TODO: Modify to call get_age() and fat_burning_heart_rate()
    #       and handle the exception
    try:
        age = get_age()
        heart_rate = fat_burning_heart_rate(age)
        print('Fat burning heart rate for a', age,  'year-old:', heart_rate, 'bpm')
    except ValueError as young:
        print(young)
        print('Could not calculate heart rate info.\n')
