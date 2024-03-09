from os import getenv

def main():
    print('THE SECRET VALUE IS:', getenv('MY_SECRET'))


if __name__ == "__main__":
    main()
