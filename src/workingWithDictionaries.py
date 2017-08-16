class WorkingWithDictionaries():

    dict = {'Jon':['Jon','smith',18], 'Sam':['Sam', 'Green', 56]}
    
    def getAgeFromName(self, name):
        return self.dict[name][2]
