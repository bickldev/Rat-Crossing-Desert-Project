from desert import Desert

size_of_desert = [0,0]

rows = input("How many rows? ")
columns = input("How many columns? ")

try: 
    size_of_desert[0] = int(rows)
except Exception as e:
    print(e)
try: 
    size_of_desert[1] = int(columns)
except Exception as e:
    print(e)

desert = Desert(size_of_desert)

for row in range(desert.rows):
    for column in range(desert.columns):
        size_of_desert[0] = row
        size_of_desert[1] = column
        print(desert.get_cell_type(size_of_desert), end=" ")
    print()

desert.start_rat()
desert.move_rat()