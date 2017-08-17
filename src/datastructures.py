class Datastructures():

    dict = {'Jon':['Jon','smith',18], 'Sam':['Sam', 'Green', 56]}

    def get_age_from_dict(self, name):
        if(name in self.dict):
            return self.dict[name][2]
        else:
            return None
