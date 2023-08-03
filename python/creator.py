# from asyncore import read
from json import JSONDecodeError
from venv import create
from person import *
from numbers_parser import Document
import pandas as pd
import uuid

# create a person object and return that. 
def create_person(f_name, l_name, m_name = None):
    return person(str(uuid.uuid4()), f_name, l_name, m_name)

def read_json():
    with open('family-tree.json') as json_file:
        try:
            data = json.load(json_file)
            return data
        except JSONDecodeError:
            return None

def write_json(data):
    json_string = json.dumps(data, indent=2, sort_keys=True, default=str)
    with open('json/family-tree.json', 'w') as outfile:
        outfile.write(json_string) 

def main():
    # options; 
    # 1) run script
    # 2) dump json onto terminal
    # 3) create new person
    option = input("Options: \n1. run script for manual writing to json\n2. print json\n3. create a new person\n4. clear JSON file\n5. extract data from excel to make json\nt. run test script\ne. to exit the menu\n")

    # script
    if option == "1":
        g1 = create_person("GrandFather", "1", spouses = [g2], chilren = [p1, p2])
        g2 = create_person("GrandMother", "1", spouses = [g1], chilren = [p1, p2])
        p1 = create_person("Parent", "1", spouses = [s1], chilren = [c1, c2], father = g1, mother = g2)
        s1 = create_person("spouses", "1", spouses = [p1], chilren = [c1, c2])
        p2 = create_person("Parent", "2", spouses = [s2], chilren = [c3, c4], father = g1, mother = g2)
        s2 = create_person("spouses", "2", spouses = [p2], chilren = [c3, c4])
        c1 = create_person("Child_1", "1", father = p1, mother = s1)
        c2 = create_person("Child_2", "1", father = p1, mother = s1)
        c3 = create_person("Child_1", "2", father = p2, mother = s2)
        c4 = create_person("Child_2", "2", father = p2, mother = s2)

    # json dumps print
    elif option == "2":
        data = read_json()
        if data:
            print(json.dumps(data, indent=4, sort_keys=True))
        else: 
            print("\nEMPTY JSON FILE\n")
        main()

    # do create new person
    elif option == "3":
        print("if none exists, press enter to proceed")
        f_name = input("First Name\n:")
        m_name = input("Middle Name\n:")
        l_name = input("Last Name\n:")
        print(m_name == "")
        json_data = read_json()
        per = person(str(uuid.uuid4()), f_name, l_name, m_name)
        if json_data:
            per.write_json(json_data)
        else:
            per.write_json()
       
    # clear the json file
    elif option == "4":
        open("family-tree.json", "w").close()
        main()

    # reads data from excel sheet to write into json file.
    elif option == "5":
        doc = Document("family.numbers")
        sheets = doc.sheets
        tables = sheets[0].tables
        data = tables[0].rows(values_only=True)
        df = pd.DataFrame(data[1:], columns=data[0])
        data = []
        for index, row in df.iterrows():
            if row["middle_name"] != None:
                name = str(row["first_name"]) + " " + str(row["middle_name"]) + " " + str(row["last_name"])
            else:
                name = str(row["first_name"]) + " " + str(row["last_name"])

            new_data = {   
                "id": row["Id"],
                "name": name,
                "gender": row["gender"],
                "born": row["born"],
                "died": row["died"],
                "children": json.loads(row["children"]),
                "spouses": json.loads(row["spouses"]),
                "siblings": json.loads(row["siblings"]),
                "parents": json.loads(row["parents"]),
            }
            data.append(new_data)
        write_json(data) 
    
    elif option == "t":
        pass
    elif option == "e":
        pass
    else:
        # wrong input retry
        print("\nWrong input. please retry\n")
        main()
    
if __name__ == "__main__":
    main()