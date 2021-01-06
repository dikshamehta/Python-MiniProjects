'''Write a Python program to convert list to list of dictionaries.
Sample lists: ["Black", "Red", "Maroon", "Yellow"], ["#000000", "#FF0000",
"#800000", "#FFFF00"]
Expected Output: [{'color_name': 'Black', 'color_code': '#000000'},
{'color_name': 'Red', 'color_code': '#FF0000'}, {'color_name': 'Maroon',
'color_code': '#800000'}, {'color_name': 'Yellow', 'color_code': '#FFFF00'}] '''
list1=[1,2,3,4,5,6]
list2=["a","b","c","d","e","f"]
dict={}

for i in range(0,6):
    dict[list1[i]]=list2[i]

print(dict)
