import json

class person():
    def __init__(self, id, f_name, l_name, m_name = "", spouse = [], children = [], father = "", mother = ""):
        self.id = id
        self.first_name = f_name
        self.last_name = l_name
        self.middle_name = m_name
        if spouse:
            self.spouse = [i.id for i in spouse]
        else: 
            self.spouse = []
        if children:
            self.children = [i.id for i in children]
        else: 
            self.children = []
        if father != "":
            self.father = father.id
        else: self.father = father
        if mother != "":
            self.mother = mother.id
        else: self.mother = mother

    def add_relation(self, relation, person):
        if relation == "child":
            self.children.add(person.id)
        elif relation == "spouse":
            self.spouse.add(person.id)
        elif relation == "father":
            self.father = person.id
        elif relation == "mother":
            self.mother = person.id
    
    def print_all(self):
        print("id: {}".format(self.id))
        if self.middle_name != "":
            name = self.first_name + " " + self.middle_name + " " + self.last_name
        else:
            name = self.first_name + " " + self.last_name
        print("Name: {}".format(name))
        print("Children: {}".format(self.children))
        print("Parents: {}".format([self.father,self.mother]))
        print("Spouse: {}".format(self.spouse))

    def write_json(self, data = None):
        
        if self.middle_name != "":
            name = self.first_name + " " + self.middle_name + " " + self.last_name
        else:
            name = self.first_name + " " + self.last_name
        if data != None:
            data[self.id] = {
                'name': name,
                'children': self.children,
                'parents': [self.father,self.mother],
                'spouse': self.spouse
            }
            json_string = json.dumps(data)
            print(json_string)  
            with open('family-tree.json', 'w') as outfile:
                outfile.write(json_string) 
        else:
            new_data = {
                self.id: {
                    'name': name,
                    'children': self.children,
                    'parents': [self.father,self.mother],
                    'spouse': self.spouse
                }
            }
            json_string = json.dumps(new_data)
            print(json_string)  
            with open('family-tree.json', 'w') as outfile:
                outfile.write(json_string) 