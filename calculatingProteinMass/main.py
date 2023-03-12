# This is a sample Python script.

# Press Shift+F10 to execute it or replace it with your code.
# Press Double Shift to search everywhere for classes, files, tool windows, actions, and settings.




# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    masses = {}
    sum = 0
    with open("mass_table.txt", 'r') as f:
        while(True):
            str = f.readline()
            if not str:
                break
            nums = str.split()
            masses[str[0]] = nums[1]

    with open("mass_db.txt", 'r') as f:
        a = f.read()
        a = a[:-1]
        for i in a:
            sum+=float(masses[i])
    print(sum)


# See PyCharm help at https://www.jetbrains.com/help/pycharm/
