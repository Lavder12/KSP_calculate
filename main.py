def result_me_orbit(change_from, change_to,take_off_delta, total_delta, low_orbit):
    print(f'TakeOff from {change_from}: {take_off_delta} m/s')
    print(f'Transit from {change_from} low orbit to {change_to} low orbit {low_orbit} m/s')
    print(f'Transit from {change_from} to {change_to} total {total_delta} m/s')

# -----------------------------------------------------------------------------------------------------------------
def kerbin_kerbin(change_from,change_to):
    take_off_delta = 3400
    total_delta = 3400
    result_me_orbit(change_from,change_to,take_off_delta,total_delta)

def kerbin_mun(change_from,change_to):
    take_off_delta = 3400
    low_orbit = 1170
    total_delta = 4570
    result_me_orbit(change_from,change_to,take_off_delta,total_delta, low_orbit)
def kerbin_minmus(change_from,change_to):
    take_off_delta = 3400
    low_orbit = '1090-1430'
    total_delta = '4490-4830'
    result_me_orbit(change_from,change_to,take_off_delta,total_delta, low_orbit)

# ----------------------------------------------------------------------------------------------------------------

def kerbin_duna(change_from,change_to):
    take_off_delta = 3400
    low_orbit = '1690-1700'
    total_delta = '5090-5100'
    result_me_orbit(change_from,change_to,take_off_delta,total_delta, low_orbit)



def make_orbit():
    change_from  = input('From: ').lower()
    change_to = input('To: ').lower()

    if change_from == 'kerbin' and change_to == 'kerbin':
        kerbin_kerbin(change_from,change_to)
    elif change_from == 'kerbin' and change_to == 'mun':
        kerbin_mun(change_from,change_to)
    elif change_from == 'kerbin' and change_to == 'minmus':
        kerbin_minmus(change_from,change_to)
    elif change_from == 'kerbin' and change_to == 'duna':\
        kerbin_duna(change_from,change_to)






def landing():
    change_from = input('Change from: ').lower()
    change_to = input('Change to: ').lower()




def main():
    print('1. Make Orbit')
    print('2. Landing')
    print('3. Aerobraking')
    print('4. Return')

    command = input('Enter Command: ')
    if command == '1':
        make_orbit()
    if command == '2':
        landing()





if __name__ == '__main__':
    main()