# Author- Purushottam B. Nawale
# Description- EV Chassis Design 1

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
        rootComp = design.rootComponent
        sketches = rootComp.sketches
        xyPlane = rootComp.xYConstructionPlane
        sketch1 = sketches.add(xyPlane)
        sketchPoints = sketch1.sketchPoints
        planes = rootComp.constructionPlanes
        features=rootComp.features
        sweeps = rootComp.features.sweepFeatures

        defaultInputNumber='5 cm'
        defaultInputName='Length'

        newInputName=ui.inputBox("Enter a new User Parametere Name: ", "New User Parameter",defaultInputName)
        newInputNumber=ui.inputBox("Enter a User Parameter Value: ","New User Parameter",defaultInputNumber)

        unitsMgr=design.unitsManager
        realInputNumber=unitsMgr.evaluateExpression(newInputNumber[0],unitsMgr.defaultLengthUnits)
        realValueInput=adsk.core.ValueInput.createByReal(realInputNumber)

        # design.userParameters.add(newInputName[0],realValueInput,unitsMgr.defaultLengthUnits,'')
        design.userParameters.add(newInputName[0],realValueInput,unitsMgr.defaultLengthUnits,'')

        ui.messageBox('success')


        # Create the rectangle using the center points and cornerpoints
        centerPoint = adsk.core.Point3D.create(0, 0, 0)
        origin = sketchPoints.add(centerPoint)
        rectangles = sketch1.sketchCurves.sketchLines
        cornerPoint = adsk.core.Point3D.create(5, 5, 0)
        rectangle1 = rectangles.addCenterPointRectangle(centerPoint, cornerPoint)
        cornerPoint2 = adsk.core.Point3D.create(4.7, 4.7, 0)
        rectangle2 = rectangles.addCenterPointRectangle(centerPoint, cornerPoint2)


        pointA = centerPoint
        pointB = adsk.core.Point3D.create(0, 0, -100)
        pointC = adsk.core.Point3D.create(-32.847, 0, -137.697)
        pointD = adsk.core.Point3D.create(-32.847, 0, -317.697)
        pointE = adsk.core.Point3D.create(-0.403, 0, -355.757)
        pointF = adsk.core.Point3D.create(-0.403, 0, -485.7428)

        pointG = adsk.core.Point3D.create(-30.40337, 0, -486.0)
        pointH = adsk.core.Point3D.create(109.59, 0, -486.0)
        pointI = adsk.core.Point3D.create(1.55936, 0, -450.7608)
        pointJ = adsk.core.Point3D.create(76.55936, 0, -450.7608)
        pointK = adsk.core.Point3D.create(1.55936, 0, -385.7608)
        pointL = adsk.core.Point3D.create(76.55936, 0, -385.7608)
        pointM = adsk.core.Point3D.create(1.55936, 0, -20.7608)
        pointN = adsk.core.Point3D.create(realInputNumber, 0, -20.7608)



        lines = sketch1.sketchCurves.sketchLines
        lineAB = lines.addByTwoPoints(pointA, pointB)
        lineBC = lines.addByTwoPoints(pointB, pointC)
        lineCD = lines.addByTwoPoints(pointC, pointD)
        lineDE = lines.addByTwoPoints(pointD, pointE)
        lineEF = lines.addByTwoPoints(pointE, pointF)
        lineGH = lines.addByTwoPoints(pointG, pointH)
        lineIJ = lines.addByTwoPoints(pointI, pointJ)
        lineKL = lines.addByTwoPoints(pointK, pointL)
        lineMN = lines.addByTwoPoints(pointM, pointN)

        prof = sketch1.profiles.item(0)
        features=rootComp.features

        # Added all lines to the Collection, So Sweep follows all those lines
        collection = adsk.core.ObjectCollection.create()
        collection.add(lineAB)
        collection.add(lineBC)
        collection.add(lineCD)
        collection.add(lineDE) 
        collection.add(lineEF) 
        path = features.createPath(collection)

        # Create a sweep input
        sweepInput = sweeps.createInput(prof, path, adsk.fusion.FeatureOperations.NewBodyFeatureOperation)
        sweepInput.isDirectionFlipped = False
        sweepInput.profileScaling = adsk.fusion.SweepProfileScalingOptions.SweepProfileScaleOption
        # Create the sweep.
        sweep=sweeps.add(sweepInput)
        body = sweep.bodies.item(0)
        # Get a face of the body
        face = body.faces.item(23)

        # ui.activeSelections.add() selects particular face or body
        # ui.activeSelections.add(body)
        ui.activeSelections.add(face)


        yzPlane = rootComp.yZConstructionPlane
        # sketch2 = sketches.add(yzPlane)
        # sketchPoints = sketch2.sketchPoints
        # Create a construction plane by offset
        planeInput = planes.createInput()

        offsetDistance = adsk.core.ValueInput.createByString('-30.40337 cm')
        planeInput.setByOffset(yzPlane, offsetDistance)
        offsetPlane = planes.add(planeInput)
        sketch3=sketches.add(offsetPlane)
        sketchPoints3 = sketch3.sketchPoints

        centerPoint2 = adsk.core.Point3D.create(486, 0, 0)
        cornerPoint3 = adsk.core.Point3D.create(482, 4, 0)
        cornerPoint4 = adsk.core.Point3D.create(482.3, 3.7, 0)
        sketchPoint44 = sketchPoints3.add(centerPoint2)
        sketchPoint54 = sketchPoints3.add(cornerPoint3)
        # lines3 = sketch3.sketchCurves.sketchLines

        rectangles = sketch3.sketchCurves.sketchLines
        rectangle33 = rectangles.addCenterPointRectangle(centerPoint2, cornerPoint3)
        rectangle44 = rectangles.addCenterPointRectangle(centerPoint2, cornerPoint4)
        
        prof2 = sketch3.profiles.item(0)
        # Added all lines to the Collection, So Sweep follows all those lines
        path2 = features.createPath(lineGH)

        # Create a sweep input
        sweepInput2 = sweeps.createInput(prof2, path2, adsk.fusion.FeatureOperations.NewBodyFeatureOperation)
        sweepInput2.isDirectionFlipped = False
        sweepInput2.profileScaling = adsk.fusion.SweepProfileScalingOptions.SweepProfileScaleOption
        # Create the sweep.
        sweep2=sweeps.add(sweepInput2)


        
        planeInput = planes.createInput()
        offsetDistance = adsk.core.ValueInput.createByString('34.59663 cm')
        planeInput.setByOffset(face, offsetDistance)
        plane = planes.add(planeInput)
        plane.isLightBulbOn=False


        # Create input entities for mirror feature
        inputEntites = adsk.core.ObjectCollection.create()
        inputEntites.add(body)
        # Create the input for mirror feature
        mirrorFeatures = features.mirrorFeatures
        mirrorInput = mirrorFeatures.createInput(inputEntites, plane)
        # Create the mirror feature
        mirrorFeature = mirrorFeatures.add(mirrorInput)
        

        planeInput2 = planes.createInput()
        offsetDistance2 = adsk.core.ValueInput.createByString('-17.499815 cm')
        planeInput2.setByOffset(yzPlane, offsetDistance)
        offsetPlane2 = planes.add(planeInput2)
        sketch4=sketches.add(offsetPlane2)


        centerPoint3 = adsk.core.Point3D.create(450.7608, 0, 35)
        cornerPoint31 = adsk.core.Point3D.create(446, 4, 35)
        cornerPoint32 = adsk.core.Point3D.create(446.3, 3.7, 35)

        rectangles = sketch3.sketchCurves.sketchLines
        rectangle331 = rectangles.addCenterPointRectangle(centerPoint3, cornerPoint31)
        rectangle332 = rectangles.addCenterPointRectangle(centerPoint3, cornerPoint32)

        prof3 = sketch3.profiles.item(0)
        # Added all lines to the Collection, So Sweep follows all those lines
        path3 = features.createPath(lineIJ)

        # Create a sweep input
        sweepInput3 = sweeps.createInput(prof3, path3, adsk.fusion.FeatureOperations.NewBodyFeatureOperation)
        sweepInput3.isDirectionFlipped = False
        sweepInput3.profileScaling = adsk.fusion.SweepProfileScalingOptions.SweepProfileScaleOption
        # Create the sweep.
        sweep3=sweeps.add(sweepInput3)




        centerPoint4 = adsk.core.Point3D.create(385.7608, 0, 35)
        cornerPoint41 = adsk.core.Point3D.create(381.7608, 4, 35)
        cornerPoint42 = adsk.core.Point3D.create(382.0608, 3.7, 35)
        rectangles = sketch3.sketchCurves.sketchLines
        rectangle441 = rectangles.addCenterPointRectangle(centerPoint4, cornerPoint41)
        rectangle442 = rectangles.addCenterPointRectangle(centerPoint4, cornerPoint42)
        prof4 = sketch3.profiles.item(3)
        # Added all lines to the Collection, So Sweep follows all those lines
        path4 = features.createPath(lineKL)
        ui.activeSelections.add(lineKL)
        # Create a sweep input
        sweepInput4 = sweeps.createInput(prof4, path4, adsk.fusion.FeatureOperations.NewBodyFeatureOperation)
        sweepInput4.isDirectionFlipped = False
        sweepInput4.profileScaling = adsk.fusion.SweepProfileScalingOptions.SweepProfileScaleOption
        # Create the sweep.
        sweep4=sweeps.add(sweepInput4)



        centerPoint5 = adsk.core.Point3D.create(20.7608, 0, 35)
        cornerPoint51 = adsk.core.Point3D.create(16.7608, 4, 35)
        cornerPoint52 = adsk.core.Point3D.create(17.0608, 3.7, 35)
        rectangles = sketch3.sketchCurves.sketchLines
        rectangle551 = rectangles.addCenterPointRectangle(centerPoint5, cornerPoint51)
        rectangle552 = rectangles.addCenterPointRectangle(centerPoint5, cornerPoint52)
        prof5 = sketch3.profiles.item(4)
        ui.activeSelections.add(prof5)
        # Added all lines to the Collection, So Sweep follows all those lines
        path5 = features.createPath(lineMN)
        sweepInput5 = sweeps.createInput(prof5, path5, adsk.fusion.FeatureOperations.NewBodyFeatureOperation)
        sweepInput5.isDirectionFlipped = False
        sweepInput5.profileScaling = adsk.fusion.SweepProfileScalingOptions.SweepProfileScaleOption
        # Create the sweep.
        sweep5=sweeps.add(sweepInput5)




    except:
        if ui:
            ui.messageBox('Failed:\n{}'.format(traceback.format_exc()))
