from desert import Desert

size_of_desert = [0,0]

print ("Welcome to Rat Simulator 2022")
print ("This project was originally coded in Java for a college course")
print ("As a personal project, I redid the program in Python, adhering to the same design specifications")

rows = input("How many rows? ")
columns = input("How many columns? ")

try: 
    size_of_desert[0] = int(rows)
except Exception as e:
    print("exception type: ", e)
    print("Assigning rows a value of 5")
    size_of_desert[0] = 5
try: 
    size_of_desert[1] = int(columns)
except Exception as e:
    print("exception type: ", e)
    print("Assigning columns a value of 5")
    size_of_desert[1] = 5

desert = Desert(size_of_desert)

for row in range(desert.rows):
    for column in range(desert.columns):
        size_of_desert[0] = row
        size_of_desert[1] = column
        print(desert.get_cell_type(size_of_desert), end=" ")
    print()

desert.start_rat()
desert.move_rat()