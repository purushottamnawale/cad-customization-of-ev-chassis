# Author- Purushottam Nawale
# Description- CAD Customization of an EV Chassis

import adsk.core
import adsk.fusion
import adsk.cam
import traceback


def run(context):
    ui = None
    try:
        app = adsk.core.Application.get()
        ui = app.userInterface
        doc = app.documents.add(adsk.core.DocumentTypes.FusionDesignDocumentType)
        design = adsk.fusion.Design.cast(app.activeProduct)
        unitsMgr = design.unitsManager
        rootComp = design.rootComponent
        sketches = rootComp.sketches
        planes = rootComp.constructionPlanes
        features = rootComp.features
        sweeps = rootComp.features.sweepFeatures
        extrudes = rootComp.features.extrudeFeatures



        # # User Parameters
        # width='Width'
        # widthValue='134.8 cm'
        # # newInputName=ui.inputBox("Enter a new User Parameter Name: ", "New User Parameter",Width)
        # newInputNumber=ui.inputBox("Enter width of chassis: ","User Parameter Width",widthValue)
        # # realInputNumber=unitsMgr.evaluateExpression(widthValue,unitsMgr.defaultLengthUnits)
        # Width=unitsMgr.evaluateExpression(newInputNumber[0],unitsMgr.defaultLengthUnits)
        # realValueInput1=adsk.core.ValueInput.createByReal(Width)
        # # value=design.userParameters.add(newInputName[0],realValueInput,unitsMgr.defaultLengthUnits,'')
        # value1=design.userParameters.add(width,realValueInput1,unitsMgr.defaultLengthUnits,'')

        # Wheelbase='Wheelbase'
        # wheebaseValue='245 cm'
        # newInputNumber2=ui.inputBox("Enter wheelbase of chassis: ","User Parameter Wheelbase",wheebaseValue)
        # WheelBase=unitsMgr.evaluateExpression(newInputNumber2[0],unitsMgr.defaultLengthUnits)
        # realValueInput2=adsk.core.ValueInput.createByReal(WheelBase)
        # value2=design.userParameters.add(Wheelbase,realValueInput2,unitsMgr.defaultLengthUnits,'')

        # CSWidth = 'csWidth'
        # csWidthValue='8.6 cm'
        # newInputNumber3=ui.inputBox("Enter Width of Rectangular Cross Section: ","User Parameter Width",csWidthValue)
        # csWidth=unitsMgr.evaluateExpression(newInputNumber3[0],unitsMgr.defaultLengthUnits)
        # realValueInput3 = adsk.core.ValueInput.createByReal(csWidth)
        # value3=design.userParameters.add(CSWidth, realValueInput3,unitsMgr.defaultLengthUnits, '')

        # CSHeight = 'csHeight'
        # csHeightValue='12.9 cm'
        # newInputNumber4=ui.inputBox("Enter Height of Rectangular Cross Section: ","User Parameter csHeight",csHeightValue)
        # csHeight=unitsMgr.evaluateExpression(newInputNumber4[0],unitsMgr.defaultLengthUnits)
        # realValueInput4 = adsk.core.ValueInput.createByReal(csHeight)
        # value4=design.userParameters.add(CSHeight, realValueInput4,unitsMgr.defaultLengthUnits, '')

        # thickness = 'Thickness'
        # csHeightValue='0.76 cm'
        # newInputNumber5=ui.inputBox("Enter the Thickness: ","User Parameter Thickness",csHeightValue)
        # Thickness=unitsMgr.evaluateExpression(newInputNumber5[0],unitsMgr.defaultLengthUnits)
        # realValueInput5 = adsk.core.ValueInput.createByReal(Thickness)
        # value5=design.userParameters.add(thickness, realValueInput5,unitsMgr.defaultLengthUnits, '')


        # ICSWidth = 'icsWidth'
        # icsWidthValue='5.5 cm'
        # newInputNumber6=ui.inputBox("Enter Width of Rectangular Cross Section: ","User Parameter Width",icsWidthValue)
        # icsWidth=unitsMgr.evaluateExpression(newInputNumber6[0],unitsMgr.defaultLengthUnits)
        # realValueInput6 = adsk.core.ValueInput.createByReal(icsWidth)
        # value6=design.userParameters.add(ICSWidth, realValueInput6,unitsMgr.defaultLengthUnits, '')

        # ICSHeight = 'icsHeight'
        # icsHeightValue= '8.2 cm'
        # newInputNumber7=ui.inputBox("Enter Height of Rectangular Cross Section: ","User Parameter csHeight",icsHeightValue)
        # icsHeight=unitsMgr.evaluateExpression(newInputNumber7[0],unitsMgr.defaultLengthUnits)
        # realValueInput7 = adsk.core.ValueInput.createByReal(icsHeight)
        # value7=design.userParameters.add(ICSHeight, realValueInput7,unitsMgr.defaultLengthUnits, '')

        Width=131.4
        WheelBase=245
        csWidth=8.6
        csHeight=12.9
        Thickness=0.76
        icsWidth=5.5
        icsHeight=8.2

    
        w=csWidth-2*Thickness
        h=csHeight-2*Thickness

        w2=icsWidth-1
        h2=icsHeight-1
        

        xyPlane = rootComp.xYConstructionPlane
        yzPlane = rootComp.yZConstructionPlane
        xzPlane = rootComp.xZConstructionPlane
        sketch1 = sketches.add(xyPlane)
        sketch2 = sketches.add(yzPlane)
        sketch3 = sketches.add(xzPlane)
        lines1 = sketch1.sketchCurves.sketchLines
        lines2 = sketch2.sketchCurves.sketchLines
        lines3 = sketch3.sketchCurves.sketchLines
        sketchPoints1 = sketch1.sketchPoints
        sketchPoints2 = sketch2.sketchPoints
        sketchPoints3 = sketch3.sketchPoints

        pointA = adsk.core.Point3D.create(0, 0, 0)
        pointB = adsk.core.Point3D.create(0, 62, 0)
        # pointC = adsk.core.Point3D.create(25, 88.2,0)
        pointC = adsk.core.Point3D.create(25, 62+(WheelBase*0.1069),-10)
        # pointD = adsk.core.Point3D.create(25, 267, 0)
        pointD = adsk.core.Point3D.create(25, 62+(WheelBase*0.1069)+(WheelBase*0.7297), -10)
        # pointE = adsk.core.Point3D.create(-10, 307, 0)
        pointE = adsk.core.Point3D.create(-10, 62+(WheelBase*0.1069)+(WheelBase*0.7297)+(WheelBase*0.1633), -10)
        # pointF = adsk.core.Point3D.create(-10, 398, 0)
        pointF = adsk.core.Point3D.create(-10, 62+91+(WheelBase*0.1069)+(WheelBase*0.7297)+(WheelBase*0.1633), -10)
        number=62+91+(WheelBase*0.1069)+(WheelBase*0.7265)+(WheelBase*0.1633)
        lineAB = lines2.addByTwoPoints(pointA, pointB)
        lineBC = lines2.addByTwoPoints(pointB, pointC)
        lineCD = lines2.addByTwoPoints(pointC, pointD)
        lineDE = lines2.addByTwoPoints(pointD, pointE)
        lineEF = lines2.addByTwoPoints(pointE, pointF)
        arc1 = sketch2.sketchCurves.sketchArcs.addFillet(lineAB, lineAB.endSketchPoint.geometry, lineBC, lineBC.startSketchPoint.geometry, 30)  # Last argument is the radius of arc
        arc2 = sketch2.sketchCurves.sketchArcs.addFillet(lineBC, lineBC.endSketchPoint.geometry, lineCD, lineCD.startSketchPoint.geometry, 30)
        arc3 = sketch2.sketchCurves.sketchArcs.addFillet(lineCD, lineCD.endSketchPoint.geometry, lineDE, lineDE.startSketchPoint.geometry, 30)
        arc4 = sketch2.sketchCurves.sketchArcs.addFillet(lineDE, lineDE.endSketchPoint.geometry, lineEF, lineEF.startSketchPoint.geometry, 30)

        # Create the rectangle 1 using the center points and cornerpoints
        centerPoint = adsk.core.Point3D.create(0, 0, 0)
        origin = sketchPoints3.add(centerPoint)
        rectangles = sketch3.sketchCurves.sketchLines
        # cornerPoint1 = adsk.core.Point3D.create(3.55, 5.7, 0) #7.1/2=3.55 11.4/2=5.7
        # cornerPoint2 = adsk.core.Point3D.create(4.3, 6.45, 0) # 8.6/2=4.3 12.9/2=64.5
        cornerPoint1 = adsk.core.Point3D.create(w/2, h/2, 0) #7.1/2=3.55 11.4/2=5.7
        cornerPoint2 = adsk.core.Point3D.create(csWidth/2, csHeight/2, 0) # 8.6/2=4.3 12.9/2=64.5
        rectangle1 = rectangles.addCenterPointRectangle(centerPoint, cornerPoint1)
        rectangle2 = rectangles.addCenterPointRectangle(centerPoint, cornerPoint2)

        prof = sketch3.profiles.item(1)
        # Added all lines to the Collection, So Sweep follows all those lines
        collection = adsk.core.ObjectCollection.create()
        collection.add(lineAB)
        collection.add(arc1) 
        collection.add(lineBC)
        collection.add(arc2) 
        collection.add(lineCD)
        collection.add(arc3) 
        collection.add(lineDE) 
        collection.add(arc4) 
        collection.add(lineEF) 
        path = features.createPath(collection)
        # Create a sweep input
        sweepInput = sweeps.createInput(prof, path, adsk.fusion.FeatureOperations.NewBodyFeatureOperation)
        sweepInput.isDirectionFlipped = False
        sweepInput.profileScaling = adsk.fusion.SweepProfileScalingOptions.SweepProfileScaleOption
        # Create the sweep.
        sweep=sweeps.add(sweepInput)


        body1 = sweep.bodies.item(0)
        # Get a face of the body
        # face1 = body1.faces.item(39)
        face1 = body1.faces.item(55)

        ui.activeSelections.add(body1.faces.item(39))
        ui.activeSelections.add(body1.faces.item(55))


        # Create a Plane for a Mirror
        planeInput = planes.createInput()
        # offsetDistance = adsk.core.ValueInput.createByString('65.7 cm') #131.4/2=65.7
        # offsetDistance = adsk.core.ValueInput.createByString(width)
        offsetDistance = adsk.core.ValueInput.createByReal(Width/2)
        planeInput.setByOffset(face1, offsetDistance)
        plane = planes.add(planeInput)
        plane.isLightBulbOn=False
        # Create input entities for mirror feature
        inputEntites = adsk.core.ObjectCollection.create()
        inputEntites.add(body1)
        # Create the input for mirror feature
        mirrorFeatures = features.mirrorFeatures
        mirrorInput = mirrorFeatures.createInput(inputEntites, plane)
        # Create the mirror feature
        mirrorFeature = mirrorFeatures.add(mirrorInput)
        body2=mirrorFeature.bodies.item(0)
        face2 = body2.faces.item(39)

        # Create a construction plane by offset
        planeInput21 = planes.createInput()
        # offsetDistance21 = adsk.core.ValueInput.createByString('4.3 cm')
        # planeInput21.setByOffset(yzPlane, offsetDistance21)
        realValueInput3 = adsk.core.ValueInput.createByReal(csWidth/2)
        planeInput21.setByOffset(yzPlane, realValueInput3)
        offsetPlane21 = planes.add(planeInput21)
        sketch21=sketches.add(offsetPlane21)
        sketchPoints21 = sketch21.sketchPoints
        rectangles21 = sketch21.sketchCurves.sketchLines


        # Create the rectangle 1 using the center points and cornerpoints
        # centerPoint = adsk.core.Point3D.create(0, 45, 0)
        # cornerPoint1 = adsk.core.Point3D.create(3.75, 47.5, 0)
        # cornerPoint2 = adsk.core.Point3D.create(4.5, 48, 0)
        centerPoint = adsk.core.Point3D.create(0, 45, 0)
        cornerPoint1 = adsk.core.Point3D.create(h2/2, 45+w2/2, 0)
        cornerPoint2 = adsk.core.Point3D.create(icsHeight/2, 45+icsWidth/2, 0)
        rectangle1 = rectangles21.addCenterPointRectangle(centerPoint, cornerPoint1)
        rectangle2 = rectangles21.addCenterPointRectangle(centerPoint, cornerPoint2)

        # Create a construction plane by offset
        planeInput22 = planes.createInput()
        # offsetDistance21 = adsk.core.ValueInput.createByString('4.3 cm')
        # planeInput21.setByOffset(yzPlane, offsetDistance21)
        realValueInput3 = adsk.core.ValueInput.createByReal(csWidth/2-10)
        planeInput22.setByOffset(yzPlane, realValueInput3)
        offsetPlane22 = planes.add(planeInput22)
        sketch22=sketches.add(offsetPlane22)
        sketchPoints22 = sketch22.sketchPoints
        rectangles22 = sketch22.sketchCurves.sketchLines

        # Create the rectangle 2 using the center points and cornerpoints
        # centerPoint = adsk.core.Point3D.create(25.25, 110, 0)
        # cornerPoint1 = adsk.core.Point3D.create(29, 112.5, 0)
        # cornerPoint2 = adsk.core.Point3D.create(29.75, 113, 0)
        centerPoint = adsk.core.Point3D.create(25.25, 62+(WheelBase*0.1959), 0)
        cornerPoint1 = adsk.core.Point3D.create(25.25+w2/2, 62+h2/2+(WheelBase*0.1959), 0)
        cornerPoint2 = adsk.core.Point3D.create(25.25+icsWidth/2, 62+icsHeight/2+(WheelBase*0.1959), 0)
        rectangle1 = rectangles22.addCenterPointRectangle(centerPoint, cornerPoint1)
        rectangle2 = rectangles22.addCenterPointRectangle(centerPoint, cornerPoint2)

        # Create the rectangle 3 using the center points and cornerpoints
        # centerPoint = adsk.core.Point3D.create(25.25, 180, 0)
        # cornerPoint1 = adsk.core.Point3D.create(29, 182.5, 0)
        # cornerPoint2 = adsk.core.Point3D.create(29.75, 183, 0)
        centerPoint = adsk.core.Point3D.create(25.25, 62+(WheelBase*0.1959)+(WheelBase*0.2857), 0)
        cornerPoint1 = adsk.core.Point3D.create(25.25+w2/2, 62+h2/2+(WheelBase*0.1959)+(WheelBase*0.2857), 0)
        cornerPoint2 = adsk.core.Point3D.create(25.25+icsWidth/2, 62+icsHeight/2+(WheelBase*0.1959)+(WheelBase*0.2857), 0)
        rectangle1 = rectangles22.addCenterPointRectangle(centerPoint, cornerPoint1)
        rectangle2 = rectangles22.addCenterPointRectangle(centerPoint, cornerPoint2)

        # Create the rectangle 4 using the center points and cornerpoints
        # centerPoint = adsk.core.Point3D.create(25.25, 250, 0)
        # cornerPoint1 = adsk.core.Point3D.create(29, 252.5, 0)
        # cornerPoint2 = adsk.core.Point3D.create(29.75, 253, 0)
        centerPoint = adsk.core.Point3D.create(25.25, 62+(WheelBase*0.1959)+(WheelBase*0.2857*2), 0)
        cornerPoint1 = adsk.core.Point3D.create(25.25+w2/2, 62+h2/2+(WheelBase*0.1959)+(WheelBase*0.2857*2), 0)
        cornerPoint2 = adsk.core.Point3D.create(25.25+icsWidth/2, 62+icsHeight/2+(WheelBase*0.1959)+(WheelBase*0.2857*2), 0)
        rectangle1 = rectangles22.addCenterPointRectangle(centerPoint, cornerPoint1)
        rectangle2 = rectangles22.addCenterPointRectangle(centerPoint, cornerPoint2)


        # Create the rectangle 5 using the center points and cornerpoints
        # centerPoint = adsk.core.Point3D.create(-10, 325, 0)
        # cornerPoint1 = adsk.core.Point3D.create(-15.7,328.55 , 0)
        # cornerPoint2 = adsk.core.Point3D.create(-16.45, 329.3, 0)
        centerPoint = adsk.core.Point3D.create(-10, 62+(WheelBase*0.1959)+(WheelBase*0.2857*2)+(WheelBase*0.2326)+18, 0)
        cornerPoint1 = adsk.core.Point3D.create(-10-h2/2,62+w2/2+(WheelBase*0.1959)+(WheelBase*0.2857*2)+(WheelBase*0.2326)+18 , 0)
        cornerPoint2 = adsk.core.Point3D.create(-10-icsHeight/2, 62+icsWidth/2+(WheelBase*0.1959)+(WheelBase*0.2857*2)+(WheelBase*0.2326)+18, 0)
        rectangle1 = rectangles22.addCenterPointRectangle(centerPoint, cornerPoint1)
        rectangle2 = rectangles22.addCenterPointRectangle(centerPoint, cornerPoint2)


        prof1 = sketch21.profiles.item(1)
        prof2 = sketch22.profiles.item(1)
        prof3 = sketch22.profiles.item(2)
        prof4 = sketch22.profiles.item(5)
        prof5 = sketch22.profiles.item(6)


        collection2 = adsk.core.ObjectCollection.create()
        collection2.add(prof1)
        collection2.add(prof2)
        collection2.add(prof3)
        collection2.add(prof4)
        collection2.add(prof5)

        # Create an extrusion that goes from the profile to a specified entity.
        extrudeInput = extrudes.createInput(collection2, adsk.fusion.FeatureOperations.NewBodyFeatureOperation)
        # Create a to-entity extent definition
        isChained = True
        extent_toentity = adsk.fusion.ToEntityExtentDefinition.create(body2, isChained)
        # Set the one side extent with the to-entity-extent-definition, and with a taper angle of 0 degree
        extrudeInput.setOneSideExtent(extent_toentity, adsk.fusion.ExtentDirections.PositiveExtentDirection)
        # Create the extrusion
        extrude = extrudes.add(extrudeInput)


        body3=extrude.bodies.item(0)
        body4=extrude.bodies.item(1)
        body5=extrude.bodies.item(2)
        body6=extrude.bodies.item(3)
        body7=extrude.bodies.item(4)

        # Create a construction plane by offset
        planeInput22 = planes.createInput()
        offsetDistance22 = adsk.core.ValueInput.createByString('-34.3 cm')
        planeInput22.setByOffset(yzPlane, offsetDistance22)
        offsetPlane22 = planes.add(planeInput22)
        sketch22=sketches.add(offsetPlane22)
        sketchPoints22 = sketch22.sketchPoints
        rectangles22 = sketch22.sketchCurves.sketchLines

        # Create the rectangle 2 using the center points and cornerpoints
        # centerPoint = adsk.core.Point3D.create(-10, 402.426, 0)
        # cornerPoint1 = adsk.core.Point3D.create(-15.7,405.976 , 0)
        # cornerPoint2 = adsk.core.Point3D.create(-16.45, 406.726, 0)
        # cornerPoint1 = adsk.core.Point3D.create(-10-5.7,4.3+3.55+62+91+(WheelBase*0.1069)+(WheelBase*0.7297)+(WheelBase*0.1633) , 0)
        # cornerPoint2 = adsk.core.Point3D.create(-10-6.45, 4.3+4.3+62+91+(WheelBase*0.1069)+(WheelBase*0.7297)+(WheelBase*0.1633), 0)
        centerPoint = adsk.core.Point3D.create(-10, csWidth/2+62+91+(WheelBase*0.1069)+(WheelBase*0.7297)+(WheelBase*0.1633), 0)
        cornerPoint1 = adsk.core.Point3D.create(-10-h/2,csWidth/2+w/2+62+91+(WheelBase*0.1069)+(WheelBase*0.7297)+(WheelBase*0.1633) , 0)
        cornerPoint2 = adsk.core.Point3D.create(-10-csHeight/2, csWidth/2+csWidth/2+62+91+(WheelBase*0.1069)+(WheelBase*0.7297)+(WheelBase*0.1633), 0)
        rectangle41 = rectangles22.addCenterPointRectangle(centerPoint, cornerPoint1)
        rectangle42 = rectangles22.addCenterPointRectangle(centerPoint, cornerPoint2)

        prof22 = sketch22.profiles.item(0)
        # distance22 = adsk.core.ValueInput.createByReal(188.6)
        distance22 = adsk.core.ValueInput.createByReal(Width+77.2)
        extrude22 = extrudes.addSimple(prof22, distance22, adsk.fusion.FeatureOperations.NewBodyFeatureOperation)
        body8=extrude22.bodies.item(0)


        # Create the rectangle 3 using the center points and cornerpoints
        centerPoint = adsk.core.Point3D.create(0, -csWidth/2, 0)
        rectangles2 = sketch2.sketchCurves.sketchLines
        # cornerPoint1 = adsk.core.Point3D.create(-5.7, -0.75, 0) # z y -x
        # cornerPoint2 = adsk.core.Point3D.create(-6.45, 0, 0)
        cornerPoint1 = adsk.core.Point3D.create(-h/2, -0.75, 0) # z y -x
        cornerPoint2 = adsk.core.Point3D.create(-csHeight/2, 0, 0)
        rectangle1 = rectangles2.addCenterPointRectangle(centerPoint, cornerPoint1)
        rectangle2 = rectangles2.addCenterPointRectangle(centerPoint, cornerPoint2)

        
        # Width = design.userParameters.itemByName(Width).value
        pointA = adsk.core.Point3D.create(-15, -4.3, 0)
        pointB = adsk.core.Point3D.create(Width+23.6, -4.3, 0) # width,realinputnumber works in point3d
        # value1,2,realvalueinput,newinputnumber,newinputname doesn't work in point3d
        # pointB = adsk.core.Point3D.create(155, -4.3, 0)
        # pointC = adsk.core.Point3D.create(165, 0, 0)
        pointC = adsk.core.Point3D.create(Width+33.6, 0, 0)
        pointD = adsk.core.Point3D.create(-25, 0, 0)
        origin=sketchPoints1.add(centerPoint)
        lineAB = lines1.addByTwoPoints(pointA, pointB)
        lineAD = lines1.addByTwoPoints(pointA, pointD)
        lineBC = lines1.addByTwoPoints(pointB, pointC)

        arc1 = sketch1.sketchCurves.sketchArcs.addFillet(lineAB, lineAB.endSketchPoint.geometry, lineBC, lineBC.startSketchPoint.geometry, 30)  # Last argument is the radius of arc
        arc2 = sketch1.sketchCurves.sketchArcs.addFillet(lineAB, lineAB.endSketchPoint.geometry, lineAD, lineAD.startSketchPoint.geometry, 30)  # Last argument is the radius of arc

        prof = sketch2.profiles.item(0)
        # Added all lines to the Collection, So Sweep follows all those lines
        collection = adsk.core.ObjectCollection.create()
        collection.add(lineAD)
        collection.add(arc2) 
        collection.add(lineAB)
        collection.add(arc1) 
        collection.add(lineBC)

        path = features.createPath(collection)
        # Create a sweep input
        sweepInput = sweeps.createInput(prof, path, adsk.fusion.FeatureOperations.NewBodyFeatureOperation)
        sweepInput.isDirectionFlipped = False
        sweepInput.profileScaling = adsk.fusion.SweepProfileScalingOptions.SweepProfileScaleOption
        # Create the sweep.
        sweep=sweeps.add(sweepInput)
        body9=sweep.bodies.item(0)

        ui.activeSelections.add(body1)
        ui.activeSelections.add(body2)
        ui.activeSelections.add(body3)
        ui.activeSelections.add(body4)
        ui.activeSelections.add(body5)
        ui.activeSelections.add(body6)
        ui.activeSelections.add(body7)
        ui.activeSelections.add(body8)
        ui.activeSelections.add(body9)


        cmdDef = ui.commandDefinitions.itemById(commandId)
        if not cmdDef:
            cmdDef = ui.commandDefinitions.addButtonDefinition(commandId, commandName, commandDescription) # no resource folder is specified, the default one will be used

        onCommandCreated = ApplyMaterialToSelectionCommandCreatedHandler()
        cmdDef.commandCreated.add(onCommandCreated)
        # keep the handler referenced beyond this function
        handlers.append(onCommandCreated)

        inputs = adsk.core.NamedValues.create()
        cmdDef.execute(inputs)

        # prevent this module from being terminate when the script returns, because we are waiting for event handlers to fire
        adsk.autoTerminate(False)

    except:
        if ui:
            ui.messageBox('Failed:\n{}'.format(traceback.format_exc()))


#Author-Autodesk Inc.
#Description-Apply a material to selected bodies or occurrences.

import adsk.core, adsk.fusion, traceback

commandId = 'ApplyMaterialToSelectionCommand'
commandName = 'ApplyMaterialToSelection'
commandDescription = 'Apply a material to selected bodies or occurrences'

app = None
ui = None

# global set of event handlers to keep them referenced for the duration of the command
handlers = []
materialsMap = {}

app = adsk.core.Application.get()
if app:
    ui  = app.userInterface
    
class ApplyMaterialInputChangedHandler(adsk.core.InputChangedEventHandler):
    def __init__(self):
        super().__init__()
    def notify(self, args):
        try:
            cmd = args.firingEvent.sender
            inputs = cmd.commandInputs
            materialListInput = None
            filterInput = None
            materialLibInput = None
            global commandId
            for inputI in inputs:
                if inputI.id == commandId + '_materialList':
                    materialListInput = inputI
                elif inputI.id == commandId + '_filter':
                    filterInput = inputI
                elif inputI.id == commandId + '_materialLib':
                    materialLibInput = inputI
            cmdInput = args.input
            if cmdInput.id == commandId + '_materialLib' or cmdInput.id == commandId + '_filter':
                materials = getMaterialsFromLib(materialLibInput.selectedItem.name, filterInput.value)
                replaceItems(materialListInput, materials)

        except:
            if ui:
                ui.messageBox('Failed:\n{}'.format(traceback.format_exc()))

class ApplyMaterialToSelectionCommandExecuteHandler(adsk.core.CommandEventHandler):
    def __init__(self):
        super().__init__()
    def notify(self, args):
        try:
            command = args.firingEvent.sender
            inputs = command.commandInputs
            for input in inputs:
                if input.id == commandId + '_selection':
                    selectionInput = input
                elif input.id == commandId + '_materialList':
                    materialListInput = input

            entities = getSelectedEntities(selectionInput)
            if len(entities) == 0:
                return
            
            if not materialListInput.selectedItem:
                if ui:
                    ui.messageBox('Material is not selected.')
                return
                
            material = getMaterial(materialListInput.selectedItem.name)
            if not material:
                return

            applyMaterialToEntities(material, entities)

        except:
            if ui:
                ui.messageBox('Failed:\n{}'.format(traceback.format_exc()))

class ApplyMaterialToSelectionCommandDestroyHandler(adsk.core.CommandEventHandler):
    def __init__(self):
        super().__init__()
    def notify(self, args):
        try:
            # when the command is done, terminate the script
            # this will release all globals which will remove all event handlers
            adsk.terminate()
        except:
            if ui:
                ui.messageBox('Failed:\n{}'.format(traceback.format_exc()))

class ApplyMaterialToSelectionCommandCreatedHandler(adsk.core.CommandCreatedEventHandler):    
    def __init__(self):
        super().__init__()        
    def notify(self, args):
        try:
            cmd = args.command
            cmd.isRepeatable = False
            onExecute = ApplyMaterialToSelectionCommandExecuteHandler()
            cmd.execute.add(onExecute)
            onDestroy = ApplyMaterialToSelectionCommandDestroyHandler()
            cmd.destroy.add(onDestroy)
            onInputChanged = ApplyMaterialInputChangedHandler()
            cmd.inputChanged.add(onInputChanged)
            # keep the handler referenced beyond this function
            handlers.append(onExecute)
            handlers.append(onDestroy)
            handlers.append(onInputChanged)

            # Define the inputs.
            inputs = cmd.commandInputs
            
            global commandId
            selectionInput = inputs.addSelectionInput(commandId + '_selection', 'Select', 'Select bodies or occurrences')
            selectionInput.setSelectionLimits(1)
            selectionInput.selectionFilters = ['SolidBodies', 'Occurrences']
            materialLibInput = inputs.addDropDownCommandInput(commandId + '_materialLib', 'Material Library', adsk.core.DropDownStyles.LabeledIconDropDownStyle)
            listItems = materialLibInput.listItems
            materialLibNames = getMaterialLibNames()
            for materialName in materialLibNames :
                listItems.add(materialName, False, '')
            listItems[0].isSelected = True
            materialListInput = inputs.addDropDownCommandInput(commandId + '_materialList', 'Material', adsk.core.DropDownStyles.TextListDropDownStyle)
            materials = getMaterialsFromLib(materialLibNames[0], '')
            listItems = materialListInput.listItems
            for materialName in materials :
                listItems.add(materialName, False, '')
            listItems[0].isSelected = True
            inputs.addStringValueInput(commandId + '_filter', 'Filter', '')

        except:
            if ui:
                ui.messageBox('Failed:\n{}'.format(traceback.format_exc()))

def getMaterial(materialName):
    materialLibs = app.materialLibraries
    material = None
    for materialLib in materialLibs:
        materials = materialLib.materials
        try:
            material = materials.itemByName(materialName)
        except:
            pass
        if material:
            break
    return material

def getSelectedEntities(selectionInput):
    entities = []
    for x in range(0, selectionInput.selectionCount):
        mySelection = selectionInput.selection(x)
        selectedObj = mySelection.entity
        if type(selectedObj) is adsk.fusion.BRepBody or type(selectedObj) is adsk.fusion.Component:
            entities.append(selectedObj)
        elif type(selectedObj) is adsk.fusion.Occurrence:
            entities.append(selectedObj.component)
    return entities

def applyMaterialToEntities(material, entities):
    for entity in entities:
        entity.material = material
            
def replaceItems(cmdInput, newItems):
    cmdInput.listItems.clear()
    if len(newItems) > 0:
        for item in newItems:
            cmdInput.listItems.add(item, False, '')
        cmdInput.listItems[0].isSelected = True
         
def getMaterialLibNames():
    materialLibs = app.materialLibraries
    libNames = []
    for materialLib in materialLibs:
        if materialLib.materials.count > 0:
            libNames.append(materialLib.name)
    return libNames
    
def getMaterialsFromLib(libName, filterExp):
    global materialsMap
    materialList = None
    if libName in materialsMap:
        materialList = materialsMap[libName]
    else:
        materialLib = app.materialLibraries.itemByName(libName)
        materials = materialLib.materials
        materialNames = []
        for material in materials:
            materialNames.append(material.name)
        materialsMap[libName] = materialNames
        materialList = materialNames

    if filterExp and len(filterExp) > 0:
        filteredList = []
        for materialName in materialList:
            if materialName.lower().find(filterExp.lower()) >= 0:
                filteredList.append(materialName)
        return filteredList
    else:
        return materialList