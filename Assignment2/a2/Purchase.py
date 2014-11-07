

import time

class Purchase(object):
    def getDate(self):
        return self.date
        
    def getStore(self):
        return self.store
        
    def getWarranty(self):
        return self.warranty
        
    def prettyPrint(self):
        print "*** Purchase ***"
        print "Date:",time.asctime(time.localtime(self.date))
        print "Store:",self.store
        print "Warranty:",time.asctime(time.localtime(self.warranty))
        
    def __init__(self, _date, _store, _warranty):
        self.date = _date
        self.store = _store
        self.warranty = _warranty
        
    
