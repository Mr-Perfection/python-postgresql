from database import add_entry, get_entries, create_table

menu = """Please select one of the following options:
1) Add new entry for today.
2) View entries.
3) Exit.

Your selection:
"""


welcome = "welcome do the journal!"
entries = [
    {"content": "say so", "date": "01/28/1994"},
    {"content": "cool bro", "date": "02/28/1983"},
]
create_table()
while (user_input := input(menu)) != "3":
    if user_input == "1":
        content = input("what have you learned today?")
        date = input("enter the date: ")
        add_entry(content, date)
    elif user_input == "2":
        for entry in get_entries():
            print(f"{entry['date']}\n{entry['content']}\n\n")
    else:
        print("Invalid option, please try again")
