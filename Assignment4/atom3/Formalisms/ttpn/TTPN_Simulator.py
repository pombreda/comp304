from ATOM3 import ATOM3
from ATOM3Integer import ATOM3Integer
from ATOM3TypeDialog import ATOM3TypeDialog

class TTPN_SimulatorEvent:
    def __init__(self, time, transition):
        self.time = time
        self.transition = transition

    def getTime(self):
        return self.time

    def getTransition(self):
        return self.transition


class TTPN_SimulatorEventQueue:
    def __init__(self):
        self.queue = []

    def size(self):
        return len(self.queue)

    def addEvents(self, events):
        # add new events to event queue
        self.queue += events

        # sort event queue by scheduled execution time
        self.queue.sort(compareEventsByTime)
 
    def popNextEvent(self):
        event = self.queue[0]
        del self.queue[0]
        return event

    def printEvents(self):
        print "\tEvent Queue:"
        for event in self.queue:
            print "\t\t[", event.getTime(), ",", event.getTransition().name.getValue(), "]"
        

class TTPN_Simulator:
    def __init__(self, atom3):
        self.atom3 = atom3


    def reset(self):
        # initialize the usedTokens variable of all places to zero
        placeList = self.atom3.ASGroot.listNodes['TTPN_Place']    
        for place in placeList:
            place.usedTokens = 0

        # initialize the usedProcesses variable of all transitions to zero
        transitionList = self.atom3.ASGroot.listNodes['TTPN_Transition']    
        for transition in transitionList:
            transition.usedProcesses = 0

        # initialize time to zero
        self.time = 0
        print "\nTime =", self.time
    
        # create empty event queue
        self.eventQueue = TTPN_SimulatorEventQueue()


    def run(self):
        print "\nStarting simulation"

        self.reset()

        # start simulation
        continueSimulation = 1
        while continueSimulation:
            continueSimulation = self.step()

        print "\nEnd of simulation" #FIXME: use message dialog


    def step(self):
        # add new events to event queue
        self.eventQueue.addEvents(self.getNewEvents())

        # print the currently scheduled events
        self.eventQueue.printEvents()
        
        # show the current time and wait for the user to press the OK button
        atomTime = ATOM3Integer(self.time)
        atomTimeDialog = ATOM3TypeDialog(self.atom3, atomTime)
        
        # stop the simulation, if either the event queue is empty or the
        # user canceled the simulation
        if self.eventQueue.size() == 0 or not atomTimeDialog.result_ok:
            return 0 # stop simulation
        
        # get the next event
        event = self.eventQueue.popNextEvent()

        # update the current time 
        self.time = event.getTime()
        print "\nTime =", self.time
        
        # execute the first event
        transition = event.getTransition()
        fireTransition(transition)

        return 1 # continue simulation


    def getNewEvents(self):
        # FIXME: resolver conflicto si hay dos transiciones activas en el
        # mismo instante de tiempo

        newEvents = []

        transitionList = getAllTransitionsSortByTime(self.atom3)

        for transition in transitionList:
            while isTransitionActivated(transition):
                newEvents.append(self.createEvent(transition, self.time))

        return newEvents


    def createEvent(self, transition, currentTime):
        if not isTransitionActivated(transition):
            print "WARNING: Ignoring createEvent for inactive transition"
            #FIXME
            return
        for inRel in transition.in_connections_:
            place = inRel.in_connections_[0]
            if transition.atomic.getValue()[1]:
                place.usedTokens += inRel.weight.getValue()
            else:
                place.tokens.setValue(place.tokens.getValue() - inRel.weight.getValue())
                place.graphObject_.ModifyAttribute("tokens", place.tokens.toString())

        transition.usedProcesses += 1
        print "\tTransition", transition.name.getValue(), "uses", transition.usedProcesses,"of", transition.processes.getValue(), "processes"
        
        return TTPN_SimulatorEvent(currentTime + transition.time.getValue(), transition)

 
def compareEventsByTime(event1, event2):
    return cmp(event1.getTime(), event2.getTime())


def getAllTransitionsSortByTime(atom3):
    transitionList = atom3.ASGroot.listNodes['TTPN_Transition'][:]

    transitionList.sort(compareTransitionsByTime)

    return transitionList


def compareTransitionsByTime(transition1, transition2):
    return cmp(transition1.time.getValue(), transition2.time.getValue())


def getAvailablePlaceTokens(place):
    return place.tokens.getValue() - place.usedTokens


def isTransitionActivated(transition):
    if transition.processes.getValue() >= 0 and transition.usedProcesses >= transition.processes.getValue():
        return 0

    for inRel in transition.in_connections_:
        place = inRel.in_connections_[0]
        if getAvailablePlaceTokens(place) < inRel.weight.getValue():
            return 0
    return 1


def fireTransition(transition):
    print "\tFiring transition", transition.name.getValue()
    
    for inRel in transition.in_connections_:
        place = inRel.in_connections_[0]
        if transition.atomic.getValue()[1]:
            place.usedTokens -= inRel.weight.getValue()
            place.tokens.setValue(place.tokens.getValue() - inRel.weight.getValue())
            place.graphObject_.ModifyAttribute("tokens", place.tokens.toString())

    for outRel in transition.out_connections_:
        place = outRel.out_connections_[0]
        place.tokens.setValue(place.tokens.getValue() + outRel.weight.getValue())
        place.graphObject_.ModifyAttribute("tokens", place.tokens.toString())

    transition.usedProcesses -= 1
    print "\tTransition", transition.name.getValue(), "uses", transition.usedProcesses,"of", transition.processes.getValue(), "processes"
