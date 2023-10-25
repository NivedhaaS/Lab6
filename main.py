def main():
    while True:
        print('Menu')
        print('------------')
        print('1. Encode')
        print('2. Decode')
        print('3. Quit')

        option = int(input('Please enter an option: '))
        if option == 1:
            password = input('Please enter your password to encode: ')
            encoded_password = encode(password)
            print('Your password has been encoded and stored!')
        if option == 2:
            print('The encoded password is ',encoded_password,', and the original password is ',password,'.')
        if option == 3:
            break

def encode(password):
    encoded_password = ''
    for i in range(0, len(password)):
        encoded_password += str(int(i)+3)
    return encoded_password

if __name__ == "__main__":
    main()