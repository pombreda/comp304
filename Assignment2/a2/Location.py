

class Location(object):
    def getMaintenanceEmployee(self):
        return self.maintenanceEmployee
        
    def setMaintenanceEmployee(self, value):
        self.maintenanceEmployee = value
        self.maintenanceCoordinates = value.getCoordinates()
        
    def getName(self):
        return self.name
        
    def setName(self, value):
        self.name = value
        
    def getOfficeCount(self):
        return self.officeCount
        
    def setOfficeCount(self, value):
        self.officeCount = value
        
    def getMaintenanceCoordinates(self):
        return self.maintenanceCoordinates
        
    def getEmployees(self):
        return tuple(self.employees)
        
    def setEmployees(self, value):
        self.employees = value
        for e in value:
        	e.setLocation(self)
        
    def addEmployee(self, _employee):
        """Add an employee to this Location"""
        self.employees.append(_employee)
        _employee.setLocation(self)
        
    def removeEmployee(self, _employee):
        """Remove an Employee from the Location, ignores attempts to remove employees that do not work here."""
        if (hasEmployee(_employee)):
        	employees.remove(_employee)
        	_employee.setLocation(None)
        
    def hasEmployee(self, _employee):
        """Check if an employee works at this Location"""
        return _employee in set(self.employees)
        
    def getEquipment(self):
        return self.equipment
        
    def setEquipment(self, value):
        self.equipment = value
        
    def addEquipment(self, _equipment):
        if (not self.hasEquipment(_equipment)):
        	self.equipment.append(_equipment)
        	_equipment.setLocation(self)
        
    def removeEquipment(self, _equipment):
        if (self.hasEquipment(_equipment)):
        	self.equipment.remove(_equipment)
        	_equipment.setLocation(None)
        
    def hasEquipment(self, _equipment):
        return _equipment in set(self.equipment)
        
    def prettyPrint(self):
        print "*** Location ***"
        print "Name:",self.name
        print "Office Count:",self.officeCount
        print "Maintenance Employee:",self.maintenanceEmployee.prettyPrint()
        print "Maintenance Coordinates:",self.getMaintenanceCoordinates().prettyPrint()
        print "Employees:"
        for e in self.employees:
        	e.prettyPrint()
        print "Equipment:"
        for e in self.equipment:
        	e.prettyPrint()
        
    def __init__(self):
        self.name = None
        self.officeCount = None
        #The Employee who maintains this Location
        self.maintenanceEmployee = None
        self.maintenanceCoordinates = None
        #A list of employees at this location
        self.employees = list()
        self.equipment = list()
        pass
    
