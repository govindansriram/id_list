import json
import os
class id_matic:

    def __init__(self):
        name = input("Enter your name Uppercase first letter: ")
        self.path_name = './users' + name + '.json'
        with open(self.path_name, 'r') as file:
            temp_dict = json.load(file)

        self.id_list = temp_dict['changed_list']
        self.perma_list = temp_dict['perma_list']
        self.name = temp_dict['name']

        self.give_id()


    def give_id(self):
        val = input("Do you want a new id yes/no?: ")

        if val.upper() == 'YES':
            print(self.id_list[0])

            other_val = input("Did that id work yes/no?:")
            if other_val.upper() == 'YES':
                self.id_list.pop(0)
                self.give_id()

            else:
                again = input("Try again yes/no?:")
                if again.upper() == 'YES':
                    self.give_id()
                else:
                    self.id_list.pop(0)
                    self.give_id()
        else:
            print('completed')
            self.save()

    def save(self):
        os.remove(self.path_name)
        temp_dict = {"name":self.name, "perma_list":self.perma_list, "changed_list":self.id_list}

        with open(self.path_name, "a") as file:
            json.dump(temp_dict,file)

if __name__ == '__main__':
    interact = id_matic()
