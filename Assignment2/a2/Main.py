

import Employee
import Location
import Equipment
import Purchase
import Coordinate
import time

class Main(object):
    def main():
        employee = Employee.Employee("Steve Jobs", 1)
        employee.setTitle("CEO")
        location = Location.Location()
        purchase = Purchase.Purchase(time.time(), "Walmart", time.time())
        equipment = Equipment.Equipment(purchase, 1234, "Computer", "FFD123", "1134D")
        location.addEmployee(employee)
        employee.setLocation(location)
        location.addEquipment(equipment)
        equipment.setAssignee(employee)
        employee.addEquipment(equipment)
        coordinates = Coordinate.Coordinate()
        coordinates.setAddress("One Redmond Way, Redmond, WA")
        coordinates.setCellPhone("(206) 246-1342")
        coordinates.setWorkPhone("(425) 422-1356")
        employee.setCoordinates(coordinates)
        equipment.setLocation(location)
        location.setMaintenanceEmployee(employee)
        employee.setSupervisor(employee)
        location.prettyPrint()
    def __init__(self):
        pass
    
    main()
    	
