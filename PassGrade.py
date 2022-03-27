print('Welcome to PassGrade!')
print('Your one-stop for verification of a secure password!')
print('Add your proposed password and PassGrade will verify its strength and security')

another_Password = 'yes'
password_Upper = False
password_Lower = False
password_Number = False
password_Length = False

while another_Password == 'yes':
    password = input('Enter a password: ')
    if len(password) >= 8:
        password_Length = True
        for x in password:
            if x.isupper():
                password_Upper = True
            if x.islower():
                password_Lower = True
            if x.isdigit():
                password_Number = True
    if password_Length and password_Lower and password_Upper and password_Number:
         print('This password meets the requirements.')
    else:
        print("This password isn't strong enough. Ensure your password is at least eight characters, has one upper and lowercase letter, and has at least one digit.")
    another_Password = input('Do you want to enter another password? (Enter yes or no)')
