class Datastructures():

    dict = {'Jon':['Jon','smith',18], 'Sam':['Sam', 'Green', 56]}

    list = ['jon', 'alex', 'sam', 'jane']

    def get_age_from_name_from_dict(self, name):
        if(name in self.dict):
            return self.dict[name][2]
        else:
            return None

    def create_new_list_upper(self):
        newList = [];
        for item in self.list:
            newList.append(item.upper())
        return newList

    def create_new_dict_upper_last_name(self):
        newDict = {}
        for key, val in self.dict.iteritems():
            newDict[key] = [val[0], val[1].upper(), val[2]]
        return newDict

    def get_list(self):
        return self.list
