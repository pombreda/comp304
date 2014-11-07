from ATOM3Text import *
from ATOM3Boolean import *
from ATOM3String import *
from ATOM3Attribute import *
from StatusBar import *
import os, os.path


def RAM(self, pre):
    try:
        if pre:
            prefix = 'MTpre_'
        else:
            prefix = 'MTpost_'
            
        # Rename the meta-model
        self.ASGroot.name.setValue(prefix + self.ASGroot.name.getValue())
        
        # Classes and Associations
        for nt in self.ASGroot.listNodes:
            if nt == 'CD_Class3' or nt == 'CD_Association3':
                for node in self.ASGroot.listNodes[nt]:
                    # Name
                    original_name = node.name.getValue()
                    node.name.setValue(prefix + node.name.getValue())
                    
                    # Attributes
                    attributes = node.attributes.getValue()
                    node.attributes.setActionFlags([ 1, 1, 1, 0])
                    newAttrs = []
                    for i, attr in enumerate(attributes):
                        newAttr = ATOM3Attribute(self.types)
                        newAttr.setValue((prefix + attr.getValue()[0], 'Text', None, ('Key', 0), ('Direct Editing', 0)))
                        if pre:
                            newAttr.initialValue=ATOM3Text("# Specify a boolean condition on the attribute\nreturn True\t# any value is allowed", 80,15 )
                        else:
                            newAttr.initialValue=ATOM3Text("# Specify an action to be performed on the attribute\npass\t# do not modify the value", 80,15 )
                        newAttr.isDerivedAttribute = False
                        newAttrs.append(newAttr)
                    
                    MT_pivot = ATOM3Attribute(self.types)
                    MT_pivot.setValue(('MT_pivot', 'Boolean', None, ('Key', 0), ('Direct Editing', 1)))
                    MT_pivot.initialValue=ATOM3Boolean()
                    MT_pivot.initialValue.setValue(('True', 0))
                    MT_pivot.initialValue.config = 1
                    MT_pivot.isDerivedAttribute = False
                    newAttrs.append(MT_pivot)
                    
                    MT_isProcessed = ATOM3Attribute(self.types)
                    MT_isProcessed.setValue(('MT_isProcessed', 'Boolean', None, ('Key', 0), ('Direct Editing', 1)))
                    MT_isProcessed.initialValue=ATOM3Boolean()
                    MT_isProcessed.initialValue.setValue(('True', 0))
                    MT_isProcessed.initialValue.config = 1
                    MT_isProcessed.isDerivedAttribute = False
                    newAttrs.append(MT_isProcessed)
                    
                    MT_label=ATOM3Attribute(self.types)
                    MT_label.setValue(('MT_label', 'String', None, ('Key', 1), ('Direct Editing', 1)))
                    MT_label.initialValue=ATOM3String(original_name, 20)
                    MT_label.isDerivedAttribute = False
                    newAttrs.append(MT_label)
                    
                    if pre:
                        MT_macthSubType = ATOM3Attribute(self.types)
                        MT_macthSubType.setValue(('MT_macthSubType', 'Boolean', None, ('Key', 0), ('Direct Editing', 1)))
                        MT_macthSubType.initialValue=ATOM3Boolean()
                        MT_macthSubType.initialValue.setValue(('True', 0))
                        MT_macthSubType.initialValue.config = 1
                        MT_macthSubType.isDerivedAttribute = False
                        newAttrs.append(MT_macthSubType)
                    
                    node.attributes.setValue(newAttrs)
                    
                    # Cardinalities
                    cardinalities = node.cardinality.getValue()
                    node.cardinality.setActionFlags([ 0, 1, 0, 0])
                    newCards = []
                    for i, card in enumerate(cardinalities):
                        target, direction, min, max = card.getValue()
                        card.setValue((target, direction, '0', max))
                        newCards.append(card)
                    
                    node.cardinality.setValue(newCards)
                    
                    if nt == 'CD_Class3':
                        # Abstract
                        node.Abstract.setValue((None, 0))
                        node.Abstract.config = 0
        
        # Save the new meta-model
        path = self.statusbar.getState(StatusBar.MODEL)[1][0]
        path = os.path.join(os.path.dirname(path), prefix + os.path.basename(path))
        self.save(0, path)
        
        return os.path.basename(path)
    except e:
        print e