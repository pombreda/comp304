

class Employee(object):
    """An employee, which can have equipment, and works at a location"""
    def getGender(self):
        """Determine if the employee is male (true) or female (false)"""
        return self.gender
        
    def getName(self):
        """Get the employee's name"""
        return self.name
        
    def getTitle(self):
        """Get the title of the employee"""
        return self.title
        
    def setTitle(self, value):
        """Set the title of the employee"""
        self.title = value
        
    def getDepartment(self):
        """Get the department of the employee"""
        return self.department
        
    def setDepartment(self, value):
        """Set the department of the employee"""
        self.department = value
        
    def getPreviousEquipment(self):
        """Get all the previous equipment owned by this employee, in the form of tuples containing the equipment bar code and the time.time of the equipment's removal from the employee"""
        prevList = list()
        for key in previousEquipment:
        	prevList.append((key, previousEquipment[key]))
        return tuple(prevList)
        
    def getCoordinates(self):
        """Get the employee's contact information"""
        return self.coordinates
        
    def setCoordinates(self, value):
        """Set the employee's contact information"""
        self.coordinates = value
        
    def getEquipment(self):
        """Get the equipment assigned to this employee as a tuple"""
        return tuple(self.equipment)
        
    def setEquipment(self, value):
        """Set the eqipment assigned to this employee"""
        for lostEquipment in (set(self.equipment) - set(value)):
        	self.previousEquipment[selfEquipment] = time.time()
        self.equipment = value
        
    def getLocation(self):
        return self.location
        
    def setLocation(self, value):
        self.location = value
        
    def hasEquipment(self, _equipment):
        return _equipment in set(self.equipment)
        
    def hadEquipment(self, _equipment):
        return _equipment.getBarCode() in self.previousEquipment
        
    def addEquipment(self, _equipment):
        if (not self.hasEquipment(_equipment)):
        	self.equipment.append(_equipment)
        	_equipment.setAssignee(self)
        	_equipment.setLocation(self.location)
        
    def removeEquipment(self, _equipment):
        if (self.hasEquipment(_equipment)):
        	self.equipment.remove(_equipment)
        	self.previousEquipment[_equipment.getBarCode()] = time.time()
        	_equipment.setAssignee(None)
        
    def prettyPrint(self):
        print "*** Employee ***"
        print "Name:",self.name
        print "Male?:",self.gender
        print "Title:",self.title
        print "Department:",self.department
        print "Supervisor:",self.supervisor.getName()
        print "Location:",self.location.getName()
        print "Coordinates:",self.coordinates.prettyPrint()
        print "Equipment History: Bar Code : Date"
        for key in self.previousEquipment:
        	print key,":",time.asctime(time.localtime(self.previousEquipment[key]))
        print "Equipment:"
        for e in self.equipment:
        	print e.prettyPrint()
        
    def __init__(self, _name, _gender):
        #The employee's name
        self.name = _name
        #The employee's gender where male is true, female is false
        self.gender = _gender
        #Employee's job title
        self.title = None
        #Department the employee works for
        self.department = None
        #A dictionary of equipment bar codes to time.time objects holding a history of previous assignments to the employee
        self.previousEquipment = dict()
        #The employee that this equipment is assigned to
        self.equipment = list()
        #The location that satisfies hasEmployee() to be true for this employee
        self.location = None
        #The supervising employee of this employee
        self.supervisor = None
        #Contact informatino for an employee
        self.coordinates = None
        pass
        
    def getSupervisor(self):
        return self.supervisor
        
    def setSupervisor(self, value):
        self.supervisor = value
        
    
