# Author-
# Description-

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



        # User Parameters
        Width='Width'
        widthValue='131.4 cm'
        # newInputName=ui.inputBox("Enter a new User Parameter Name: ", "New User Parameter",Width)
        newInputNumber=ui.inputBox("Enter width of chassis: ","User Parameter Width",widthValue)
        # realInputNumber=unitsMgr.evaluateExpression(widthValue,unitsMgr.defaultLengthUnits)
        realInputNumber=unitsMgr.evaluateExpression(newInputNumber[0],unitsMgr.defaultLengthUnits)
        realValueInput=adsk.core.ValueInput.createByReal(realInputNumber)
        # value=design.userParameters.add(newInputName[0],realValueInput,unitsMgr.defaultLengthUnits,'')
        value=design.userParameters.add(Width,realValueInput,unitsMgr.defaultLengthUnits,'')

        Wheelbase='Wheelbase'
        wheebaseValue='245 cm'
        newInputNumber2=ui.inputBox("Enter wheelbase of chassis: ","User Parameter Wheelbase",wheebaseValue)
        realInputNumber2=unitsMgr.evaluateExpression(newInputNumber2[0],unitsMgr.defaultLengthUnits)
        realValueInput2=adsk.core.ValueInput.createByReal(realInputNumber2)
        value2=design.userParameters.add(Wheelbase,realValueInput2,unitsMgr.defaultLengthUnits,'')

        Height = 'Height'
        heightValue='5.7 cm'
        newInputNumber3=ui.inputBox("Enter Height of Rectangular Cross Section: ","User Parameter Height",heightValue)
        realInputNumber3=unitsMgr.evaluateExpression(newInputNumber3[0],unitsMgr.defaultLengthUnits)
        realValueInput3 = adsk.core.ValueInput.createByReal(realInputNumber3)
        value3=design.userParameters.add(Height, realValueInput3,unitsMgr.defaultLengthUnits, '')


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
        pointC = adsk.core.Point3D.create(25, 62+(realInputNumber2*0.1069),0)
        # pointD = adsk.core.Point3D.create(25, 267, 0)
        pointD = adsk.core.Point3D.create(25, 62+(realInputNumber2*0.1069)+(realInputNumber2*0.7297), 0)
        # pointE = adsk.core.Point3D.create(-10, 307, 0)
        pointE = adsk.core.Point3D.create(-10, 62+(realInputNumber2*0.1069)+(realInputNumber2*0.7297)+(realInputNumber2*0.1633), 0)
        # pointF = adsk.core.Point3D.create(-10, 398, 0)
        pointF = adsk.core.Point3D.create(-10, 62+91+(realInputNumber2*0.1069)+(realInputNumber2*0.7297)+(realInputNumber2*0.1633), 0)
        number=62+91+(realInputNumber2*0.1069)+(realInputNumber2*0.7265)+(realInputNumber2*0.1633)
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
        cornerPoint1 = adsk.core.Point3D.create(3.55, realInputNumber3, 0) #7.1/2=3.55 11.4/2=5.7
        cornerPoint2 = adsk.core.Point3D.create(4.3, 6.45, 0) # 8.6/2=4.3 12.9/2=64.5
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
        face1 = body1.faces.item(39)


        # Create a Plane for a Mirror
        planeInput = planes.createInput()
        # offsetDistance = adsk.core.ValueInput.createByString('65.7 cm') #131.4/2=65.7
        # offsetDistance = adsk.core.ValueInput.createByString(Width)
        offsetDistance = adsk.core.ValueInput.createByReal(realInputNumber/2)
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
        # face2 = body2.faces.item(39)

        # Create a construction plane by offset
        planeInput21 = planes.createInput()
        offsetDistance21 = adsk.core.ValueInput.createByString('4.3 cm')
        planeInput21.setByOffset(yzPlane, offsetDistance21)
        offsetPlane21 = planes.add(planeInput21)
        sketch21=sketches.add(offsetPlane21)
        sketchPoints21 = sketch21.sketchPoints
        rectangles21 = sketch21.sketchCurves.sketchLines

        # Create the rectangle 1 using the center points and cornerpoints
        centerPoint = adsk.core.Point3D.create(0, 45, 0)
        cornerPoint1 = adsk.core.Point3D.create(3.75, 47.5, 0)
        cornerPoint2 = adsk.core.Point3D.create(4.5, 48, 0)
        rectangle1 = rectangles21.addCenterPointRectangle(centerPoint, cornerPoint1)
        rectangle2 = rectangles21.addCenterPointRectangle(centerPoint, cornerPoint2)

        # Create the rectangle 2 using the center points and cornerpoints
        # centerPoint = adsk.core.Point3D.create(25.25, 110, 0)
        # cornerPoint1 = adsk.core.Point3D.create(29, 112.5, 0)
        # cornerPoint2 = adsk.core.Point3D.create(29.75, 113, 0)
        centerPoint = adsk.core.Point3D.create(25.25, 62+(realInputNumber2*0.1959), 0)
        cornerPoint1 = adsk.core.Point3D.create(29, 64.5+(realInputNumber2*0.1959), 0)
        cornerPoint2 = adsk.core.Point3D.create(29.75, 65+(realInputNumber2*0.1959), 0)
        rectangle1 = rectangles21.addCenterPointRectangle(centerPoint, cornerPoint1)
        rectangle2 = rectangles21.addCenterPointRectangle(centerPoint, cornerPoint2)

        # Create the rectangle 3 using the center points and cornerpoints
        # centerPoint = adsk.core.Point3D.create(25.25, 180, 0)
        # cornerPoint1 = adsk.core.Point3D.create(29, 182.5, 0)
        # cornerPoint2 = adsk.core.Point3D.create(29.75, 183, 0)
        centerPoint = adsk.core.Point3D.create(25.25, 62+(realInputNumber2*0.1959)+(realInputNumber2*0.2857), 0)
        cornerPoint1 = adsk.core.Point3D.create(29, 64.5+(realInputNumber2*0.1959)+(realInputNumber2*0.2857), 0)
        cornerPoint2 = adsk.core.Point3D.create(29.75, 65+(realInputNumber2*0.1959)+(realInputNumber2*0.2857), 0)
        rectangle1 = rectangles21.addCenterPointRectangle(centerPoint, cornerPoint1)
        rectangle2 = rectangles21.addCenterPointRectangle(centerPoint, cornerPoint2)

        # Create the rectangle 4 using the center points and cornerpoints
        # centerPoint = adsk.core.Point3D.create(25.25, 250, 0)
        # cornerPoint1 = adsk.core.Point3D.create(29, 252.5, 0)
        # cornerPoint2 = adsk.core.Point3D.create(29.75, 253, 0)
        centerPoint = adsk.core.Point3D.create(25.25, 62+(realInputNumber2*0.1959)+(realInputNumber2*0.2857*2), 0)
        cornerPoint1 = adsk.core.Point3D.create(29, 64.5+(realInputNumber2*0.1959)+(realInputNumber2*0.2857*2), 0)
        cornerPoint2 = adsk.core.Point3D.create(29.75, 65+(realInputNumber2*0.1959)+(realInputNumber2*0.2857*2), 0)
        rectangle1 = rectangles21.addCenterPointRectangle(centerPoint, cornerPoint1)
        rectangle2 = rectangles21.addCenterPointRectangle(centerPoint, cornerPoint2)


        # Create the rectangle 5 using the center points and cornerpoints
        # centerPoint = adsk.core.Point3D.create(-10, 325, 0)
        # cornerPoint1 = adsk.core.Point3D.create(-15.7,328.55 , 0)
        # cornerPoint2 = adsk.core.Point3D.create(-16.45, 329.3, 0)
        centerPoint = adsk.core.Point3D.create(-10, 62+(realInputNumber2*0.1959)+(realInputNumber2*0.2857*2)+(realInputNumber2*0.2326)+18, 0)
        cornerPoint1 = adsk.core.Point3D.create(-15.7,64.5+(realInputNumber2*0.1959)+(realInputNumber2*0.2857*2)+(realInputNumber2*0.2326)+18 , 0)
        cornerPoint2 = adsk.core.Point3D.create(-16.45, 65+(realInputNumber2*0.1959)+(realInputNumber2*0.2857*2)+(realInputNumber2*0.2326)+18, 0)
        rectangle1 = rectangles21.addCenterPointRectangle(centerPoint, cornerPoint1)
        rectangle2 = rectangles21.addCenterPointRectangle(centerPoint, cornerPoint2)


        prof1 = sketch21.profiles.item(1)
        prof3 = sketch21.profiles.item(3)
        prof4 = sketch21.profiles.item(4)
        prof7 = sketch21.profiles.item(7)
        prof8 = sketch21.profiles.item(8)

        collection2 = adsk.core.ObjectCollection.create()
        collection2.add(prof1)
        collection2.add(prof3)
        collection2.add(prof4)
        collection2.add(prof7)
        collection2.add(prof8)

        # Create an extrusion that goes from the profile to a specified entity.
        extrudeInput = extrudes.createInput(collection2, adsk.fusion.FeatureOperations.NewBodyFeatureOperation)
        # Create a to-entity extent definition
        isChained = True
        extent_toentity = adsk.fusion.ToEntityExtentDefinition.create(body2, isChained)
        # Set the one side extent with the to-entity-extent-definition, and with a taper angle of 0 degree
        extrudeInput.setOneSideExtent(extent_toentity, adsk.fusion.ExtentDirections.PositiveExtentDirection)
        # Create the extrusion
        extrude = extrudes.add(extrudeInput)

        # Create a construction plane by offset
        planeInput22 = planes.createInput()
        offsetDistance22 = adsk.core.ValueInput.createByString('-24.3 cm')
        planeInput22.setByOffset(yzPlane, offsetDistance22)
        offsetPlane22 = planes.add(planeInput22)
        sketch22=sketches.add(offsetPlane22)
        sketchPoints22 = sketch22.sketchPoints
        rectangles22 = sketch22.sketchCurves.sketchLines

        # Create the rectangle 2 using the center points and cornerpoints
        # centerPoint = adsk.core.Point3D.create(-10, 402.426, 0)
        # cornerPoint1 = adsk.core.Point3D.create(-15.7,405.976 , 0)
        # cornerPoint2 = adsk.core.Point3D.create(-16.45, 406.726, 0)
        centerPoint = adsk.core.Point3D.create(-10, 4.3+62+91+(realInputNumber2*0.1069)+(realInputNumber2*0.7297)+(realInputNumber2*0.1633), 0)
        cornerPoint1 = adsk.core.Point3D.create(-15.7,4.3+3.55+62+91+(realInputNumber2*0.1069)+(realInputNumber2*0.7297)+(realInputNumber2*0.1633) , 0)
        cornerPoint2 = adsk.core.Point3D.create(-16.45, 4.3+4.3+62+91+(realInputNumber2*0.1069)+(realInputNumber2*0.7297)+(realInputNumber2*0.1633), 0)
        rectangle41 = rectangles22.addCenterPointRectangle(centerPoint, cornerPoint1)
        rectangle42 = rectangles22.addCenterPointRectangle(centerPoint, cornerPoint2)

        prof22 = sketch22.profiles.item(0)
        # distance22 = adsk.core.ValueInput.createByReal(188.6)
        distance22 = adsk.core.ValueInput.createByReal(realInputNumber+57.2)
        extrude22 = extrudes.addSimple(prof22, distance22, adsk.fusion.FeatureOperations.NewBodyFeatureOperation)


        # Create the rectangle 3 using the center points and cornerpoints
        centerPoint = adsk.core.Point3D.create(0, -4.3, 0)
        rectangles2 = sketch2.sketchCurves.sketchLines
        cornerPoint1 = adsk.core.Point3D.create(-5.7, -0.75, 0) # z y -x
        rectangle1 = rectangles2.addCenterPointRectangle(centerPoint, cornerPoint1)
        cornerPoint2 = adsk.core.Point3D.create(-6.45, 0, 0)
        rectangle2 = rectangles2.addCenterPointRectangle(centerPoint, cornerPoint2)

        
        # Width = design.userParameters.itemByName(Width).value
        pointA = adsk.core.Point3D.create(-15, -4.3, 0)
        pointB = adsk.core.Point3D.create(realInputNumber+23.6, -4.3, 0) # width,realinputnumber works in point3d
        # value1,2,realvalueinput,newinputnumber,newinputname doesn't work in point3d




        # pointB = adsk.core.Point3D.create(155, -4.3, 0)
        # pointC = adsk.core.Point3D.create(165, 0, 0)
        pointC = adsk.core.Point3D.create(realInputNumber+33.6, 0, 0)
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


    except:
        if ui:
            ui.messageBox('Failed:\n{}'.format(traceback.format_exc()))
