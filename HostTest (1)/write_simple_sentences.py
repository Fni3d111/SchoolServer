
def get_sentece():
    confirm = 'n'
    while confirm.lower() !='y':
        data = input("What would you like to write on the other computer PAY ATTANTION ONLY STRING,NO COMINATIONS.")
        confirm = input(f'ARE YOU SURE THIS IS ALL YOU WANT TO WRITE? --" {data} " IF YES ENTER Y IF NO ENTER N')
        if confirm.lower() == 'y':
            return data

