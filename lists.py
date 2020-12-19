import json

class vid_giver:

    def __init__(self):
        with open("./captionedVidList.json","r") as file:
            data = json.load(file)

            self.id_list = []

            for x in data:
                self.id_list.append(x['video_id'])

    def get_id(self,number):
        return self.id_list[number]

class add_user:

    def __init__(self, name, range_one, range_two):

        vid_id = vid_giver()
        perma_list = []
        changed_list = []
        for x in range(range_one, range_two + 1):
            perma_list.append(vid_id.get_id(x))
            changed_list.append(vid_id.get_id(x))
        temp_dict = {"name":name, "perma_list":perma_list, "changed_list":changed_list}

        path_name = "./users" + name + ".json"
        with open(path_name, "a") as file:
            json.dump(temp_dict,file)





#if __name__ == '__main__':

    #sriram = add_user('Sriram',0,29)
    #aneesh = add_user('Aneesh',30,59)
    #edgar = add_user('Edgar',60,89)
    #matt = add_user('Matt',90,119)
    #nanar = add_user('Nanar',120,149)
    #Jon = add_user('Jon',0,149)


    # Sriram 0 - 29 currently finished:
    # Aneesh 30 - 59 currently finished:
    # Edgar 60 - 89 currently finished:
    # Matt 90 - 119 currently finished:
    # Nanar 120 - 149 currently finished:
