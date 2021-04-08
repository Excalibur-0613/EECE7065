# Cell object containing the definitions for
#   - object (obj)
#   - agent (agent)
#   - pheremone (ph)
# Variables are private and must be updated through update method(s)

# _ underscore declares private variable (scope is limited to the class)
class cell:
    
    def __init__(self,r=None,c=None,obj=None,agent=None,ph=None):
        self._r = r # row position
        self._c = c # column position
        self._obj = obj # object information
        self._agent = agent # agent information
        self._ph = ph # pheremone information
    
    def updateCell(self,r=None,c=None,obj=None,agent=None,ph=None):
        self._r = r # row position
        self._c = c # column position
        self._obj = obj # object information
        self._agent = agent # agent information
        self._ph = ph # pheremone information
        
    def updateCellRow(self,r=None):
        self._r = r
        
    def updateCellColumn(self,c=None):
        self._c = c
        
    def updateCellObj(self,obj=None):
        self._c = obj
        
    def updateCellAgent(self,agent=None):
        self._agent = agent
        
    def updateCellPh(self,ph=None):
        self._ph = ph
    
    def getr(self):
        return self._r
    
    def getc(self):
        return self._c
    
    def getobj(self):
        return self._obj
    
    def getagent(self):
        return self._agent
    
    def getph(self):
        return self._ph
    
    pass