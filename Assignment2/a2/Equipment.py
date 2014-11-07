

class Equipment(object):
    def getType(self):
        return self.type
        
    def getSerialNumber(self):
        return self.serialNumber
        
    def getModelNumber(self):
        return self.modelNumber
        
    def getBarCode(self):
        return self.barCode
        
    def getAssignee(self):
        return self.assignee
        
    def setAssignee(self, value):
        self.assignee = value
        
    def getPurchase(self):
        return self.purchase
        
    def getLocation(self):
        return self.location
        
    def setLocation(self, value):
        self.location = value
        
    def prettyPrint(self):
        print "*** Equipment ***"
        print "Type:",self.type
        print "Serial Number:",self.serialNumber
        print "Model Number:",self.modelNumber
        print "Bar Code:",self.barCode
        print "Assignee:",self.assignee.getName()
        print "Purchase:",self.purchase.prettyPrint()
        print "Location:",self.location.getName()
        
    def __init__(self, _purchase, _barCode, _type, _serialNumber, _modelNumber):
        self.type = _type
        self.serialNumber = _serialNumber
        self.modelNumber = _modelNumber
        self.barCode = _barCode
        #Equipment assigned to the employee, specifically, equipment that satisfy getAssignee() == this employee
        self.assignee = None
        self.purchase = _purchase
        self.location = None
        pass
        
    
