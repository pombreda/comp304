

class Coordinate(object):
    def getAddress(self):
        return self.address
        
    def setAddress(self, value):
        self.address = value
        
    def getWorkPhone(self):
        return self.workPhone
        
    def setWorkPhone(self, value):
        self.workPhone = value
        
    def getCellPhone(self):
        return self.cellPhone
        
    def setCellPhone(self, value):
        self.cellPhone = value
        
    def prettyPrint(self):
        print "*** Coordinate ***"
        print "Address:",self.address
        print "Work Phone:",self.workPhone
        print "Cell Phone:",self.cellPhone
        
    def __init__(self):
        self.address = None
        self.workPhone = None
        self.cellPhone = None
        pass
    
