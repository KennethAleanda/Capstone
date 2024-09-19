# Yellow Pages (data kontal telepon)
# initialize database
data = [
    ["Name", "Number", "Email", "City", "Birthday"],
    ["John",  "0888888888881", "john@email.com", "Jakarta", "01-01-2000"],
    ["Jody", "0888888888883", "jody@email.com", "Jakarta", "02-01-2000"],
    ["Gonathan", "0888888888885", "jonathan@email.com", "Overworld", "03-01-2000"],
    [8, 13, 18, 9, 10] # max len of each column
]
# create function
def create(name, number, email, city, birthday):
    temp = data.pop()
    if len(name) > temp[0]:
        temp[0] = len(name)
    if len(number) > temp[1]:
        temp[1] = len(number)
    if len(email) > temp[2]:
        temp[2] = len(email)
    if len(city) > temp[3]:
        temp[3] = len(city)
    if len(birthday) > temp[4]:
        temp[4] = len(birthday)

    data.append([name, number, email, city, birthday])
    data.append(temp)

    return

# create menu function
def mcreate(temp = []):
    if len(temp) > 0: # true if from update
        u = True
    else:
        u = False
    try: 
        if not u:
            print(f"\n{'=' * 5}Create Menu{'=' * 5}")
        while True:
            if not u:
                temp = [] # Placeholder for create data
            full = False
            while True: # name data input
                if len(temp) != 0 and not u: # show current inputted data
                    print(f"current input {temp}")
                if u:
                    x =  temp[0]
                    full = True
                else:
                    x = input("*Masukkan nama (4-35 char) :").strip()
                
                if len(x) == 0: # check if name is inputted
                    print("nama tidak boleh kosong")
                    continue

                if x.count(",") == 4: # check if all data has been inputted from the start
                    temp = [y.strip() for y in x.split(",")]
                    full = True
                    temp[0] = temp[0].lower().title()
                    temp[3] = temp[3].lower().title()
                    x = temp[0]
                
                else:
                    x = x.lower().title()
                
                dup = False # check duplicate
                if not u:
                    for l in data:
                        if l[0] == x:
                            dup = True
                
                if dup:
                    print("nama sudah ada pada phonebook")
                    full = False
                    if u: return False
                    continue

                if len(x) < 4:
                    print("nama terlalu pendek")
                    full = False
                    if u: return False
                    continue
                elif not x.replace(' ','').isalnum():
                    print("format nama hanya alphanumeric")
                    if u: return False
                    full = False
                    continue
                elif len(x) > 35:
                    print(f"nama terlalu panjang, disingkat menjadi {x[:35]}? enter to accept", end='')
                    if len(input()) > 0:
                        full = False
                        if u: return False
                        continue 
                    else:
                        x = x[:35]
                else:
                    if full:
                        break
                    else:
                        if len(temp) >= 5:
                            temp[0] = x
                        else:
                            temp.append(x)
                        break
            
            # if len(temp) != 5 or u: # check if all data is inputted
            while True: # number data input
                if len(temp) != 0 and not u and not full: # show current inputted data
                        print(f"\ncurrent input {temp}")
                
                if full or u:
                    x = temp[1]
                else : 
                    x = input("masukkan nomor (9-15 digit) :").strip()

                if len(x) == 0: # check if number is inputted
                    print("nomor tidak boleh kosong")
                    if u: return False
                    full = False
                    continue

                if not x.isdigit(): # check if digit
                    print("format nomor hanya angka")
                    if u: return False
                    full = False
                    continue
                elif len(x) < 9:
                    print("digit nomor terlalu sedikit min.9")
                    if u: return False
                    full = False
                    continue
                elif len(x) > 15: 
                    print("digit nomor terlalu banyak max.15")
                    if u: return False
                    full = False
                    continue
                
                dup = False
                if not u:
                    for l in data:
                        if l[1] == x:
                            dup = True
                
                if dup:
                    print("Nomor sudah ada pada phonebook")
                    if u: return False
                    full = False
                    continue

                else:
                    if full:
                        break
                    else:
                        if len(temp) >= 5:
                            temp[1] = x
                        else:
                            temp.append(x)
                        break
            
            while True: # email data input
                if len(temp) != 0 and not u and not full: # show current inputted data
                        print(f"\ncurrent input {temp}")
                
                if full or u :
                    email = temp[2]
                else : 
                    email = input("masukkan email :").lower().strip() 
                
                if len(email.strip()) == 0: # check if email is inputted
                    if len(temp) >= 5:
                        temp[2] = " "
                    else:
                        temp.append(" ")
                    break

                x = False
                # email format
                if email.count('@') != 1 or '.' not in email.split('@')[1] or len(email.split('@')[0]) == 0 or len(email.split('@')[1].split('.')[0]) == 0 or len(email.split('@')[1].split('.')[1]) == 0:
                    print("Format Email salah (user@hosting.extension)")
                    if u: return False
                    full = False
                    continue

                # check username
                user = email.split('@')[0]
                for c in user :
                    if c.isalnum():
                        continue
                    elif c =='_' or c =='.':
                        continue
                    else:
                        x = True
                        break
                if not user[0].isalnum() or x:
                    print("Format Username yang anda masukkan salah")
                    if u: return False
                    full = False
                    continue

                # check hosting
                if not (not email.split('@')[1].split('.')[0].isdecimal() and email.split('@')[1].split('.')[0].isalnum()):
                    print("Format Hosting yang anda masukkan salah")
                    if u: return False
                    full = False
                    continue

                # check extension
                ext = email.split('@')[1].split('.')[1:]
                for e in ext:
                    if len(e) > 5 or not e.isalpha():
                        x = True
                        break
                if len(ext) > 2 or len(ext) < 1 or x:
                    print("Format Extension yang anda masukkan salah")
                    if u: return False
                    full = False
                    continue
                
                dup = False
                if not u:
                    for l in data:
                        if l[2] == x:
                            dup = True
                
                if dup:
                    print("Email sudah ada pada phonebook")
                    if u: return False
                    continue

                # Email Valid
                if full:
                    break
                else:
                    if len(temp) >= 5:
                        temp[2] = email
                    else:
                        temp.append(email)
                    break

            while True: # city data input
                if len(temp) != 0 and not u and not full: # show current inputted data
                    print(f"\ncurrent input {temp}")

                if full or u:
                    x = temp[3]
                else : 
                    x = input("masukkan kota (2-20 char) :").strip().lower().title()
                
                if len(x.strip()) == 0: # check if city is inputted
                    if len(temp) >= 5:
                        temp[3] = " "
                    else:
                        temp.append(" ")
                    break

                if not x.replace(' ','').isalpha():
                    print("Format kota hanya alpha")
                    if u: return False
                    full = False
                    continue
                else :
                    if full:
                        break
                    else:
                        if len(temp) >= 5:
                            temp[3] = x.title()
                        else:
                            temp.append(x.title())
                        break
            
            while True: # birthday data input
                if len(temp) != 0 and not u and not full:  # show current inputted data
                    print(f"\ncurrent input {temp}")

                if full or u:
                    x = temp[4]
                else : 
                    x = input("Masukkan tanggal lahir (dd-mm-yyyy) :")

                if len(x.strip()) == 0: # check if birthday is inputed
                    if len(temp) >= 5:
                        temp[4] = " "
                    else:
                        temp.append(" ")
                    break

                if x.count("-") == 2 and x.replace("-", "").isnumeric() and len(x.split("-")) == 3:
                    if int(x.split("-")[0]) not in range(1,32):
                        print("maksimum hari 31")
                        if u: return False
                        full = False
                        continue

                    if int(x.split("-")[1]) not in range(1,13):
                        print("maksimum bulan 12")
                        if u: return False
                        full = False
                        continue

                    if int(x.split("-")[2]) not in range(1900,2024):
                        print("tahun minimum 1900 dan maksimum 2023")
                        if u: return False
                        full = False
                        continue

                    else: 
                        x = f"{int(x.split('-')[0]):02}-{int(x.split('-')[1]):02}-{int(x.split('-')[2]):04}"
                        if full:
                            break
                        else:
                            if len(temp) >= 5:
                                temp[4] = x
                            else:
                                temp.append(x)
                            break

                else:
                    print("format tidak tepat (dd-mm-yyyy)")
                    if u: return False
                    full = False
                    continue
        
            r = False
            while True and not u: # check if input is correct, y will create new data, n will loop to start
                x = input(f"{temp}, suday benar(y/n)? ")
                if x[0].lower() == 'y':
                    r = True
                    break
                elif x[0].lower() == 'n':
                    break
            if  u:
                return True # return back to mupdate
            if r and not u:
                create(temp[0], temp[1], temp[2], temp[3], temp[4]) # add temp to data
                read() # print all data
            
            return # back to main menu
    except:
        return  # back to main menu if error

# read function
def read(name = False):
    print()
    border = lambda: print("=" * (21 + sum(data[-1]))) # print border
    row = lambda col, item, data: print(f"| {item[col]}{' ' * (2 + data[-1][col] - len(item[col]))}", end="") # lambda function to print each column in a row
    if not name: # if name = False
        border() 
        for item in data: # loop through each list in data list (row in data)
            if item is data[-1]: # skip the last row in data
                continue
            for col in range(len(item)): # print each row
                row(col, item, data)
            print("|") # closing for each row
            if item is data[0]: # border after the table head for separation
                border()
        border()
        return True
    
    else :
        if name != "Name" and name.title() in [x[0] for x in data]: # check if name is in data
            name = name.title() # change name to titleCase
            border()
            for item in data: # loop through each row in data list
                if item[0] != name and item != data[0]: # only print the first row(table head) and the specified row
                    continue
                for col in range(len(item)): 
                    row(col, item, data)
                print("|")
                if item is data[0]:
                    border()
            border()
            return True

        else : # if name is not on list data
            return False

# read menu function
def mread():
    print(f"\n{'=' * 5}Read Menu{'=' * 5}")
    while True:
        print("Choose Option :\n1. Show All Entries (default)\n2. show spesific entry (nama)\n3.  Back To Main Menu")
        x = input("Pilihan : ")
        try : 
            x = int(x)
            if x > 0 and x < 4: # check if input is right
                if x == 1: # print all
                    read()
                    return
                elif x == 2: # print spesific
                    if read(input("Masukkan Nama : ")):
                        continue
                    else:
                        print("nama yang dimasukkan tidak ditemukan")
                        continue
                elif x == 3: # back
                    return
                
        except:
            if read(x): # check if no input(print all) or if input = name(option 2) or input is not valid
                continue
        
        print("input tidak valid") # only happen if read() returns False in except()

# update function 
def update(old, name, number, email, city, birthday):
    temp = data.pop()
    if len(name) > temp[0]:
        temp[0] = len(name)
    if len(number) > temp[1]:
        temp[1] = len(number)
    if len(email) > temp[2]:
        temp[2] = len(email)
    if len(city) > temp[3]:
        temp[3] = len(city)
    if len(birthday) > temp[4]:
        temp[4] = len(birthday)
    data.append(temp)

    # check for duplicate name/number/email in data that is not the old data
    for row in data:
        if row[0] == name and data.index(row) != data.index(old): #name
            print("update failed, nama duplicate")
            return
        if row[1] == number and data.index(row) != data.index(old):
            print("update failed, number duplicate")
            return
    
    data[data.index(old)] = [name, number, email, city, birthday]
    return

# update menu function 
def mupdate():
    try:
        temp = []
        default = []
        print(f"\n{'=' * 5}Update Menu{'=' * 5}")
        while True:
            x = input("masukkan nama yang ingin di update : ").title()
            if x in [t[0] for t in data] and x != "Name" and not x.isdecimal():
                default = [t for t in data if t[0] == x][0]
                temp = default[:]
                break
            else:
                print("nama tidak ditemukan/format nama salah")

        while True:
            print("\ndata yang akan di update: ")
            read(default[0])
            if default != temp:
                print(f"menjadi : {temp}")
            print("1. ubah nama \n2. ubah nomor \n3. ubah email \n4. ubah kota \n5. ubah tanggal lahir \n6. apply update\n7.back")
            x = input("pilihan : ")
            if not x.isdecimal():
                print("input harus berupa angka")
                continue
            x = int(x)
            if x < 1 or x > 7:
                print("opsi tidak tersedia")
                continue
            
            if x == 1:
                y = input("new name (blank for default) : ").strip().title()
                if y == '':
                    temp[0] = default[0]
                else:
                    temp[0] = y
                continue
            
            if x == 2:
                y = input("new number (blank for default) : ").strip()
                if y == '':
                    temp[1] = default[1]
                else:
                    temp[1] = y
                continue
            
            if x == 3:
                y = input("new email (blank for default) : ")
                if len(y) == 1 and y == " ":
                    temp[2] = y
                elif y.strip() == '':
                    temp[2] = default[2]
                else:
                    temp[2] = y.strip()
                continue
            
            if x == 4:
                y = input("new kota (blank for default) : ").title()
                if len(y) == 1 and y == " ":
                    temp[3] = y
                elif y.strip() == '':
                    temp[3] = default[3]
                else:
                    temp[3] = y.strip()
                continue
            
            if x == 5:
                y = input("new birthday (blank for default) : ")
                if len(y) == 1 and y == " ":
                    temp[4] = y
                elif y.strip() == '':
                    temp[4] = default[4]
                else:
                    temp[4] = y.strip()
                continue
            
            if x == 6:
                if mcreate(temp):
                    update(default, temp[0], temp[1], temp[2], temp[3], temp[4])
                    read(temp[0])
                    break
                continue
            
            if x == 7: 
                return
                
    except:
        return

# delete function 
def delete(name):
    for row in data:
        if row[0] == name:
            data.pop(data.index(row))
    return

# delete menu function 
def mdelete():
    temp = []
    try:
        while True:
            print(f"\n{'=' * 5}Delete Menu{'=' * 5}")
            x = input("masukkan nama yang ingin di delete : ").title()
            if x in [t[0] for t in data] and x != "Name" and not x.isdecimal():
                temp = [t for t in data if t[0] == x][0]
                break
            else:
                print("nama tidak ditemukan/format nama salah")
        
        r = False
        while True:
            read(temp[0])
            x = input("yakin untuk men-delete data diatas (y/n) :")
            if x[0].lower() == 'y':
                delete(temp[0])
                read()
                return
            if x[0].lower() == 'n':
                return
    except:
        return

# main function
def main():
    while True: 
        print(f"\n{'=' * 5}Main Menu{'=' * 5}")
        print("Choose Option :\n1. show Entries\n2. add new Entry \n3. update existing Entry \n4. delete Entry\n5. exit")
        x = input("Pilihan : ")
        if x.isdecimal() and  int(x) < 6 and int(x) > 0:
            x = int(x)
            if x == 1:
                mread() # go to read menu
            elif x == 2:
                mcreate() # go to create menu
            elif x == 3:
                mupdate() # go to update menu
            elif x == 4:
                mdelete() # go to delete menu
            elif x == 5:
                break
        else:
            print("input tidak valid")
            continue
    exit()


if __name__=="__main__":
    main()