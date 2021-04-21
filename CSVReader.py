import pandas as pd
# Read a CSV file, and convert the file to rows[]
file = open("SampleData.csv","r")
rows=[]
for lines in file:
    row = lines.split(',')
    rows.append(row)
file.close()

for row in rows:
    print ("ticker:"+ row[0])
##
## up to here, this code is the same as yours;
##

# create a new list of list, result_rows, to store the result
# I am using the data structure "list of list" just in case if you want to use panadas.
# You can use list of string if you just want to save it as a CSV file
result_rows=[]

for row in rows:
    temp = []
    temp.append(row[0])
    temp.append(" I want to add something here")
    temp.append(" I want to add more things here")
    # you can add more here
    result_rows.append(temp)

# Have a look at the pandas dataframe and save it as a CSV file
df = pd.DataFrame(result_rows)
print (df)
df.to_csv("pandasCSV.csv",index=False, header=False)

# If you do not want to use pandas, this is how you convert a list of list
# to a CSV file: treat each line as a string, and connect element with comma

new_file = open("plainCSV.csv","w")
for row in result_rows:
    if (len(row)==1):
        print("You didn't append anything!")
        break
    string = "ticker:"
    for i in range(len(row)-1): # loop for every element you have appended
        string += row[i]+"," # separate them with a comma
    string += row[-1] +"\n"
    new_file.write(string)
new_file.close()