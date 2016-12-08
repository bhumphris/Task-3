from datetime import datetime
fileIn = 'customerList.txt'
today = datetime.today()

def main_menu():
    print '1. Returning Customer'
    print '2. New Customer'
    print '3. Guest'
def brew_menu():
    print '1. Coffee Brews'
    print '2. Teas'
    print '3. Hot Chocolate'
def find_customer():
    customer = raw_input('\nPlease enter your customer id: ')
    return customer

def find_customer(customer):
    try:
        with open(fileIn, 'r') as f:
            customer_list = f.readlines()
            for item in customer_list:
                record = item.split(',')
                if customer == record[0]:
                    return record
        return 'none'
    except IOError as e:
        print "I/O error({0}): {1}".format(e.errno, e.strerror) + ': ' + fileIn

def confirm_customer():
    confirm = raw_input('\nPlease confirm if this information is correct (Y/N): ')
    return confirm.upper()

def returning_customer():
    my_customer = get_customer()
    record = find_customer(my_customer)

    if record == 'none':

        print '\nThere is no record of the customer id you entered, please try again.\n'
        returning_customer()

    else:

        phone = record[7]
        print '\nYour information is as follows: \n'
        print 'Customer Id: ' + record[0]
        print record[1], record[2]
        print record[3]
        print record[4] + ', ' + record[5] + '  ' + record[6]
        print '(' + phone[0:3] + ') ' + phone[3:6] + '-' + phone[6:10]

        response = confirm_customer()

        if response == 'Y':

            print "\n\nHere is our Brew Menu: \n"

            brew_menu()

        else:

            print "\nthis is not the correct customer information, let's try that again."
            returning_customer()
    return


def new_customer():
    print "\nWelcome"
    return

def guest_customer():
    print "\nWelcome"
    return


def wrongnumber():
    print('\nPlease enter the appropriate number for your customer type: 1, 2, or 3. ')
    return


while selection >= 0:

    main_menu()

    try:
        selection = int(raw_input('\n\nPlease make the appropriate customer selection: '))

    except ValueError:
        print("\nInvalid entry.\n")
        continue

    else:

        if selection < 1 or selection > 3:
            selection = int(raw_input('Please select your customer type. It must be a number equal to 1, 2, or 3.  '))

        if selection == 1:
            print '\nYou have selected the Returning Customer Option.'
            returning_customer()
            selection = - 1

        elif selection == 2:
            print '\nYou have selected the New Customer Option.'
            new_customer()
            selection = - 1

        elif selection == 3:
            print '\nYou have selected the Guest Customer Option.'
            guest_customer()
            print "\n\nHere is our Brew Menu: \n"
            brew_menu()
            selection = - 1

        else:
            wrongnumber()

