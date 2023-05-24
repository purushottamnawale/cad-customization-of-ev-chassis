# Author- Purushottam B. Nawale
# Description- EV Chassis Design 1
# This python can create a 3D model of EV Chassis

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
        yzPlane = rootComp.yZConstructionPlane
        xzPlane = rootComp.xZConstructionPlane
        sketch1 = sketches.add(xyPlane)
        sketch2 = sketches.add(yzPlane)
        sketch3 = sketches.add(xzPlane)
        sketchPoints = sketch1.sketchPoints
        sketchPoints3 = sketch3.sketchPoints
        
        planes = rootComp.constructionPlanes
        features=rootComp.features
        sweeps = rootComp.features.sweepFeatures
        extrudes = rootComp.features.extrudeFeatures

        # # User Parameters
        # defaultInputNumber='5 cm'
        # defaultInputName='Length'
        # newInputName=ui.inputBox("Enter a new User Parametere Name: ", "New User Parameter",defaultInputName)
        # newInputNumber=ui.inputBox("Enter a User Parameter Value: ","New User Parameter",defaultInputNumber)
        # unitsMgr=design.unitsManager
        # realInputNumber=unitsMgr.evaluateExpression(newInputNumber[0],unitsMgr.defaultLengthUnits)
        # realValueInput=adsk.core.ValueInput.createByReal(realInputNumber)
        # value=design.userParameters.add(newInputName[0],realValueInput,unitsMgr.defaultLengthUnits,'')


        # pointS1 = adsk.core.Point3D.create(39.05936, 0, 20)
        # pointS2 = adsk.core.Point3D.create(39.05936, 0, -500)
        # pointT1 = adsk.core.Point3D.create(-50, 0, -227.697)
        # pointT2 = adsk.core.Point3D.create(150, 0, -227.697)

        # ap1=adsk.core.Point3D.create(39.05936, 0, -196.26623)
        # ap2=adsk.core.Point3D.create(39.05936, 0, -259.12777)
        # ap3=adsk.core.Point3D.create(3.01891, 0, -196.26623)
        # ap4=adsk.core.Point3D.create(75.09981, 0, -196.26623)

        pointA = adsk.core.Point3D.create(0, 0, 0)
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
        pointN = adsk.core.Point3D.create(76.55936, 0, -20.7608)
        # pointN = adsk.core.Point3D.create(realInputNumber*2, 0, -20.7608)

        pointO = adsk.core.Point3D.create(76.55936, 0, -20.7608)
        pointP = adsk.core.Point3D.create(76.55936, 0, -20.7608)

        # Create an arc using three points along the arc.
        startPoint = adsk.core.Point3D.create(-46.71551, 0, -24.46138)
        alongPoint = adsk.core.Point3D.create(39.59663, 0, 8.91539)
        endPoint = adsk.core.Point3D.create(125.90877, 0, -24.46138)
        arcs = sketch1.sketchCurves.sketchArcs
        arc = arcs.addByThreePoints(startPoint, alongPoint, endPoint)

        pointQ = adsk.core.Point3D.create(-0.40377, 0, -447.09093)
        pointR = adsk.core.Point3D.create(-0.40377, -23.85027, -433.43228)
        pointS = adsk.core.Point3D.create(-0.40377, -23.85027, -398.43228)
        pointT = adsk.core.Point3D.create(-0.40377, 0, -384.77523)

        pointU = adsk.core.Point3D.create(0, 0, -82.09093)
        pointV = adsk.core.Point3D.create(0, -23.85027 -384.77523)
        pointW = adsk.core.Point3D.create(0, -23.85027, -384.77523)
        pointX = adsk.core.Point3D.create(0, 0, -384.77523)



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
        lineQR = lines.addByTwoPoints(pointQ, pointR)
        lineRS = lines.addByTwoPoints(pointR, pointS)
        lineST = lines.addByTwoPoints(pointS, pointT)
        # lineS1S2 = lines.addByTwoPoints(pointS1, pointS2)
        # lineT1T2 = lines.addByTwoPoints(pointT1, pointT2)



        # Create the rectangle 1 using the center points and cornerpoints
        centerPoint = adsk.core.Point3D.create(0, 0, 0)
        origin = sketchPoints.add(centerPoint)
        rectangles = sketch1.sketchCurves.sketchLines
        cornerPoint11 = adsk.core.Point3D.create(5, 5, 0)
        rectangle11 = rectangles.addCenterPointRectangle(centerPoint, cornerPoint11)
        cornerPoint12 = adsk.core.Point3D.create(4.7, 4.7, 0)
        rectangle12 = rectangles.addCenterPointRectangle(centerPoint, cornerPoint12)
        prof = sketch1.profiles.item(0)
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
        

        # Create a construction plane by offset
        planeInput = planes.createInput()
        offsetDistance = adsk.core.ValueInput.createByString('-30.40337 cm')
        planeInput.setByOffset(yzPlane, offsetDistance)
        offsetPlane = planes.add(planeInput)
        sketch2=sketches.add(offsetPlane)


        # Create the rectangle 2 using the center points and cornerpoints
        centerPoint2 = adsk.core.Point3D.create(486, 0, 0)
        cornerPoint22 = adsk.core.Point3D.create(482, 4, 0)
        cornerPoint23 = adsk.core.Point3D.create(482.3, 3.7, 0)
        rectangles = sketch2.sketchCurves.sketchLines
        rectangle21 = rectangles.addCenterPointRectangle(centerPoint2, cornerPoint22)
        rectangle22 = rectangles.addCenterPointRectangle(centerPoint2, cornerPoint23)
        prof2 = sketch2.profiles.item(0)
        path2 = features.createPath(lineGH)
        # Create a sweep input
        sweepInput2 = sweeps.createInput(prof2, path2, adsk.fusion.FeatureOperations.NewBodyFeatureOperation)
        sweepInput2.isDirectionFlipped = False
        sweepInput2.profileScaling = adsk.fusion.SweepProfileScalingOptions.SweepProfileScaleOption
        # Create the sweep.
        sweep2=sweeps.add(sweepInput2)



        

        # Create the rectangle 3 using the center points and cornerpoints
        centerPoint3 = adsk.core.Point3D.create(450.7608, 0, 35)
        cornerPoint31 = adsk.core.Point3D.create(446, 4, 35)
        cornerPoint32 = adsk.core.Point3D.create(446.3, 3.7, 35)
        rectangles = sketch2.sketchCurves.sketchLines
        rectangle31 = rectangles.addCenterPointRectangle(centerPoint3, cornerPoint31)
        rectangle32 = rectangles.addCenterPointRectangle(centerPoint3, cornerPoint32)
        prof3 = sketch2.profiles.item(0)
        path3 = features.createPath(lineIJ)
        sweepInput3 = sweeps.createInput(prof3, path3, adsk.fusion.FeatureOperations.NewBodyFeatureOperation)
        sweepInput3.isDirectionFlipped = False
        sweepInput3.profileScaling = adsk.fusion.SweepProfileScalingOptions.SweepProfileScaleOption
        sweep3=sweeps.add(sweepInput3)


        # Create the rectangle 4 using the center points and cornerpoints
        centerPoint4 = adsk.core.Point3D.create(385.7608, 0, 35)
        cornerPoint41 = adsk.core.Point3D.create(381.7608, 4, 35)
        cornerPoint42 = adsk.core.Point3D.create(382.0608, 3.7, 35)
        rectangles = sketch2.sketchCurves.sketchLines
        rectangle41 = rectangles.addCenterPointRectangle(centerPoint4, cornerPoint41)
        rectangle42 = rectangles.addCenterPointRectangle(centerPoint4, cornerPoint42)
        prof4 = sketch2.profiles.item(3)
        path4 = features.createPath(lineKL)
        sweepInput4 = sweeps.createInput(prof4, path4, adsk.fusion.FeatureOperations.NewBodyFeatureOperation)
        sweepInput4.isDirectionFlipped = False
        sweepInput4.profileScaling = adsk.fusion.SweepProfileScalingOptions.SweepProfileScaleOption
        sweep4=sweeps.add(sweepInput4)


        # Create the rectangle 5 using the center points and cornerpoints
        centerPoint5 = adsk.core.Point3D.create(20.7608, 0, 35)
        cornerPoint51 = adsk.core.Point3D.create(16.7608, 4, 35)
        cornerPoint52 = adsk.core.Point3D.create(17.0608, 3.7, 35)
        rectangles = sketch2.sketchCurves.sketchLines
        rectangle51 = rectangles.addCenterPointRectangle(centerPoint5, cornerPoint51)
        rectangle52 = rectangles.addCenterPointRectangle(centerPoint5, cornerPoint52)
        prof5 = sketch2.profiles.item(4)
        path5 = features.createPath(lineMN)
        sweepInput5 = sweeps.createInput(prof5, path5, adsk.fusion.FeatureOperations.NewBodyFeatureOperation)
        sweepInput5.isDirectionFlipped = False
        sweepInput5.profileScaling = adsk.fusion.SweepProfileScalingOptions.SweepProfileScaleOption
        sweep5=sweeps.add(sweepInput5)


        # Create the rectangle 6 using the center points and cornerpoints
        centerPoint6 = adsk.core.Point3D.create(24.46138, 0, -16.31214)
        cornerPoint61 = adsk.core.Point3D.create(20.46138, 4, -16.31214)
        cornerPoint62 = adsk.core.Point3D.create(20.76138, 3.7, -16.31214)
        rectangles = sketch2.sketchCurves.sketchLines
        rectangle61 = rectangles.addCenterPointRectangle(centerPoint6, cornerPoint61)
        rectangle62 = rectangles.addCenterPointRectangle(centerPoint6, cornerPoint62)
        prof6 = sketch2.profiles.item(8)
        path6 = features.createPath(arc)
        sweepInput6 = sweeps.createInput(prof6, path6, adsk.fusion.FeatureOperations.NewBodyFeatureOperation)
        sweepInput6.isDirectionFlipped = False
        sweepInput6.profileScaling = adsk.fusion.SweepProfileScalingOptions.SweepProfileScaleOption
        sweep6=sweeps.add(sweepInput6)

        # Create the rectangle 7 using the center points and cornerpoints
        centerPoint7 = adsk.core.Point3D.create(-0.40377, 447.09093, 0)
        cornerPoint71 = adsk.core.Point3D.create(2.09623, 444.59093, 0)
        cornerPoint72 = adsk.core.Point3D.create(1.79623, 444.89093, 0)
        rectangles = sketch3.sketchCurves.sketchLines
        rectangle71 = rectangles.addCenterPointRectangle(centerPoint7, cornerPoint71)
        rectangle72 = rectangles.addCenterPointRectangle(centerPoint7, cornerPoint72)
        prof7 = sketch3.profiles.item(0)
        
        collection = adsk.core.ObjectCollection.create()
        collection.add(lineQR)
        collection.add(lineRS)
        collection.add(lineST)
        path7 = features.createPath(collection)
        sweepInput7 = sweeps.createInput(prof7, path7, adsk.fusion.FeatureOperations.NewBodyFeatureOperation)
        sweepInput7.isDirectionFlipped = False
        sweepInput7.profileScaling = adsk.fusion.SweepProfileScalingOptions.SweepProfileScaleOption
        sweep7=sweeps.add(sweepInput7)

        body2 = sweep7.bodies.item(0)
        xAxis = rootComp.xConstructionAxis
        yAxis = rootComp.yConstructionAxis
        zAxis = rootComp.zConstructionAxis
        quantity1 = adsk.core.ValueInput.createByString('2')
        distance1 = adsk.core.ValueInput.createByString('80 cm')
        quantityTwo = adsk.core.ValueInput.createByString('2')
        distanceTwo = adsk.core.ValueInput.createByString('365 cm')
        inputEntites = adsk.core.ObjectCollection.create()
        inputEntites.add(body2)
        rectangularPatterns = rootComp.features.rectangularPatternFeatures
        rectangularPatternInput = rectangularPatterns.createInput(inputEntites, xAxis, quantity1, distance1, adsk.fusion.PatternDistanceType.SpacingPatternDistanceType)
        # Set the data for second direction
        rectangularPatternInput.setDirectionTwo(zAxis, quantityTwo, distanceTwo)
        # Create the rectangular pattern
        rectangularFeature = rectangularPatterns.add(rectangularPatternInput)


        # Create a Plane for a Mirror
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


        # Create a Plane for a Mirror
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


        middlePoint=adsk.core.Point3D.create(39.05936, 0, -227.697)
        middleOrigin = sketchPoints.add(middlePoint)
        lines3 = sketch3.sketchCurves.sketchLines
        arcs3 = sketch3.sketchCurves.sketchArcs

        # Create an arc1 using three points along the arc.
        startPoint1 = adsk.core.Point3D.create(23.61315, 212.86973, 0)
        alongPoint = adsk.core.Point3D.create(28.48476, 227.697, 0)
        endPoint1 = adsk.core.Point3D.create(23.61315, 242.52427, 0)
        arc = arcs3.addByThreePoints(startPoint1, alongPoint, endPoint1)
        lineEnd11 = adsk.core.Point3D.create(-31.99199, 137.38439, 0)
        lineEnd12 = adsk.core.Point3D.create(-31.99199, 318.00961, 0)
        line11 = lines3.addByTwoPoints(startPoint1, lineEnd11)
        line12 = lines3.addByTwoPoints(endPoint1, lineEnd12)
        

        # Create an arc2 using three points along the arc.
        startPoint2 = adsk.core.Point3D.create(29.20993, 251.71413, 0)
        alongPoint = adsk.core.Point3D.create(39.05936, 246.62777, 0)
        endPoint2 = adsk.core.Point3D.create(48.90879, 251.71413, 0)
        arc = arcs3.addByThreePoints(startPoint2, alongPoint, endPoint2)
        lineEnd21 = adsk.core.Point3D.create(-26.99199, 328.00961, 0)
        lineEnd22 = adsk.core.Point3D.create(105.11071, 328.00961, 0)
        line21 = lines3.addByTwoPoints(startPoint2, lineEnd21)
        line22 = lines3.addByTwoPoints(endPoint2, lineEnd22)
        

        # Create an arc3 using three points along the arc.
        startPoint3 = adsk.core.Point3D.create(54.50557, 212.86973, 0)
        alongPoint = adsk.core.Point3D.create(49.63396, 227.697, 0)
        endPoint3 = adsk.core.Point3D.create(54.50557, 242.52427, 0)
        arc = arcs3.addByThreePoints(startPoint3, alongPoint, endPoint3)
        lineEnd31 = adsk.core.Point3D.create(110.11071, 318.00961, 0)
        lineEnd32 = adsk.core.Point3D.create(110.11071, 137.38439, 0)
        line31 = lines3.addByTwoPoints(endPoint3, lineEnd31)
        line32 = lines3.addByTwoPoints(startPoint3, lineEnd32)

        # Create an arc4 using three points along the arc.
        startPoint4 = adsk.core.Point3D.create(29.20993, 203.67987, 0)
        alongPoint = adsk.core.Point3D.create(39.05936, 208.76623, 0)
        endPoint4 = adsk.core.Point3D.create(48.90879, 203.67987, 0)
        arc = arcs3.addByThreePoints(startPoint4, alongPoint, endPoint4)
        lineEnd41 = adsk.core.Point3D.create(-26.991995, 127.38439, 0)
        lineEnd42 = adsk.core.Point3D.create(105.11071, 127.38439, 0)
        line41 = lines3.addByTwoPoints(startPoint4, lineEnd41)
        line42 = lines3.addByTwoPoints(endPoint4, lineEnd42)

        line51 = lines3.addByTwoPoints(lineEnd41, lineEnd11)
        line52 = lines3.addByTwoPoints(lineEnd12, lineEnd21)
        line53 = lines3.addByTwoPoints(lineEnd22, lineEnd31)
        line54 = lines3.addByTwoPoints(lineEnd32, lineEnd42)

        prof8 = sketch3.profiles.item(2)
        distance = adsk.core.ValueInput.createByReal(-1)
        face1 = body.faces.item(22)
        extrudeInput = extrudes.createInput(prof8, adsk.fusion.FeatureOperations.NewBodyFeatureOperation)
        extent_distance = adsk.fusion.DistanceExtentDefinition.create(distance)
        start_from = adsk.fusion.FromEntityStartDefinition.create(face1, distance)
        extrudeInput.setOneSideExtent(extent_distance, adsk.fusion.ExtentDirections.PositiveExtentDirection)        
        extrudeInput.startExtent = start_from
        extrude3 = extrudes.add(extrudeInput)

    except:
        if ui:
            ui.messageBox('Failed:\n{}'.format(traceback.format_exc()))
