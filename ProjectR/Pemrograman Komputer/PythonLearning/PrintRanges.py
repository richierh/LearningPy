import uno
from com.sun.star.uno import RuntimeException

class Office:
    '''Frequently used methods in office context'''
    def __init__(self, ctx=uno.getComponentContext()):
        self.ctx = ctx
        self.smgr = self.ctx.ServiceManager
        
    def createUnoService(self, service):
        return self.smgr.createInstance(service)

    def getDesktop(self):
        return self.smgr.createInstanceWithContext("com.sun.star.frame.Desktop",self.ctx)

    def getCurrentComponent(self):
        return self.getDesktop().getCurrentComponent()

    def getCurrentFrame(self):
        return self.getDesktop().getCurrentFrame()

    def getCurrentComponentWindow(self):
        return self.getCurrentFrame().getComponentWindow()

    def getCurrentContainerWindow(self):
        return self.getCurrentFrame().getContainerWindow()

    def getCurrentController(self):
        return self.getCurrentFrame().getController()

    def callMRI(self,obj=None):
        '''Create an instance of MRI inspector and inspect the given object (default is selection)'''
        if not obj:
            obj = self.getCurrentController().getSelection()
        mri = self.createUnoService("mytools.Mri")
        mri.inspect(obj)

class OOoRegistry(Office):
    def __init__(self, ctx):
        Office.__init__(self, ctx)
        self.ConfigProvider = self.createUnoService("com.sun.star.configuration.ConfigurationProvider")
        self.Node = None

    def setNode(self, sNodePath, bWritable=False):
        arg = uno.createUnoStruct('com.sun.star.beans.PropertyValue')
        arg.Name = "nodepath"
        arg.Value = sNodePath
        s = "ConfigurationAccess"
        if bWritable:
            s = "ConfigurationUpdateAccess"
        self.Node = self.ConfigProvider.createInstanceWithArguments("com.sun.star.configuration." + s,(arg,))
        
    def getOOoSetupValue(self, sProperty):
        return self.Node.getByName(sProperty)

    def setOOoSetupValue(self, sProperty, sValue):
        try:
            self.Node.setPropertyValue(sProperty, sValue)
            self.Node.commitChanges()
        except:
            return False
        else:
            return True

def getUsedAddress(oSheet):
    '''com.sun.star.table.CellRangeAddress of a sheet's used range'''
    oRg = oSheet.createCursor()
    oRg.gotoStartOfUsedArea(False)
    oRg.gotoEndOfUsedArea(True)
    return oRg.getRangeAddress()

def clearPrintAreas(doc):
    '''remove all print areas from a Calc document'''
    esh = doc.Sheets.createEnumeration()
    while esh.hasMoreElements():
        sh = esh.nextElement()
        sh.setPrintAreas(tuple())
    
def getPrintAreasDict(doc):
    '''return a dict of sheet indices with print areas'''
    d = {}
    esh = doc.Sheets.createEnumeration()
    while esh.hasMoreElements():
        sh = esh.nextElement()
        n = sh.RangeAddress.Sheet
        d[n]= sh.getPrintAreas()
    return d

def setPrintAreasByDict(doc, d, bWholeSheet):
    for k,v in d.items():
        sh = doc.Sheets.getByIndex(k)
        if bWholeSheet:
            v = (getUsedAddress(sh),)
        sh.setPrintAreas(v)

def getTmpURL():
    import unohelper, os
    f = os.tmpnam() +'.pdf'
    return unohelper.systemPathToFileUrl(f)

def getDictFromAddresses(tpla):
    '''Split tuple of addresses into dict of sheet indices.'''
    d = {}
    for i in tpla:
        ish = i.Sheet
        if not d.has_key(ish):
            d[ish] = [i,]
        else:
            d[ish].append(i)

    for k,v in d.items():
        d[k] = tuple(v)

    return d

def printSelectedCells():
    '''Print current selection of (multiple) cell range(s)'''
    printSomething(False)

def printSelectedSheets():
    '''Print used ranges of currently selected sheets'''
    printSomething(True)

def printSomething(bWholeSheet):
    doc = XSCRIPTCONTEXT.getDocument()
    sel = doc.getCurrentSelection()
    ctx = XSCRIPTCONTEXT.getComponentContext()
    reg = OOoRegistry(ctx)
    node = reg.setNode("/org.openoffice.Office.Calc/Print/Other", True)
    bAllSheets = reg.getOOoSetupValue("AllSheets")
    reg.setOOoSetupValue("AllSheets", True)
    # Let's support c.s.s.sheet.SheetCellRanges collection.
    # The intersection of a range with its own address
    # gives a collection having that single range
    if sel.supportsService('com.sun.star.sheet.SheetCellRange'):
        sel = sel.queryIntersection(sel.getRangeAddress())
    elif sel.supportsService('com.sun.star.sheet.SheetCellRanges'):
        pass
    else:
        reg.setOOoSetupValue("AllSheets",bAllSheets)
        raise(Exception, 'NO RANGE SELECTION')

    a = sel.getRangeAddresses()
    # back up current print areas
    d1 = getPrintAreasDict(doc)
    clearPrintAreas(doc)

    d2 = getDictFromAddresses(a)
    setPrintAreasByDict(doc, d2, bWholeSheet)

    p = uno.createUnoStruct('com.sun.star.beans.PropertyValue')
    p.Name = 'FileName'
    p.Value = getTmpURL()
    doc.com_sun_star_view_XPrintable_print((p,))
    
    clearPrintAreas(doc)
    setPrintAreasByDict(doc, d1, False)
    reg.setOOoSetupValue("AllSheets",bAllSheets)

g_exportedScripts = printSelectedCells, printSelectedSheets,
