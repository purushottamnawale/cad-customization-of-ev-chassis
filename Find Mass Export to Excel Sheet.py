# Fusion360API Python script

import traceback
import adsk.core as core
import adsk.fusion as fusion
import csv
import os

def run(context):
    ui: core.UserInterface = None
    try:
        app: core.Application = core.Application.get()
        ui = app.userInterface

        msg: str = 'Select Entity'
        selFilter: str = 'Bodies,Occurrences,RootComponents'
        sel: core.Selection = selectEnt(msg, selFilter)
        if not sel:
            return
        

        # show_physicalProperties(sel.entity)
        show_physicalProperties(sel.entity, 'D:/Documents/file.csv')
        a=1

        ui.messageBox('Properties written to file.csv')

    except:
        if ui:
            ui.messageBox('Failed:\n{}'.format(traceback.format_exc()))


def show_physicalProperties(
    entity: core.Base, filepath: str
):

    if not hasattr(entity, 'physicalProperties'):
        return

    props: fusion.PhysicalProperties = entity.physicalProperties
    if hasattr(entity, 'transform2'):
        origin, _, _, _ = entity.transform2.getAsCoordinateSystem()
        worldXYZ = origin.asArray()
    else:
        worldXYZ = '-'

    infos = [
        f'Mass \t\t{round(props.mass)}  kg',
        f'Volume \t\t{round(props.volume)}  cm^3',
        f'Density \t\t{round(props.density*1000)}  g/cm^3',
        f'Area \t\t{round(props.area)}  cm^2',
        f'World X,Y,Z \t\t{worldXYZ}',
        f'CenterOfMass \t{props.centerOfMass.asArray()}',
    ]

    

    app: core.Application = core.Application.get()
    ui: core.UserInterface = app.userInterface
    ui.messageBox('\n'.join(infos))

    if not hasattr(entity, 'physicalProperties'):
        return

    props: fusion.PhysicalProperties = entity.physicalProperties
    if hasattr(entity, 'transform2'):
        origin, _, _, _ = entity.transform2.getAsCoordinateSystem()
        worldXYZ = origin.asArray()
    else:
        worldXYZ = '-'

    infos = {
        'Mass (kg)': round(props.mass),
        'Volume (cm^3)': round(props.volume),
        'Density (g/cm^3)': round(props.density*1000),
        'Area (cm^2)': round(props.area),
        'CenterOfMass X': props.centerOfMass.x,
        'CenterOfMass Y': props.centerOfMass.y,
        'CenterOfMass Z': props.centerOfMass.z,
    }

    if not os.path.exists(filepath):
        with open(filepath, 'w', newline='') as csvfile:
            writer = csv.DictWriter(csvfile, fieldnames=list(infos.keys()))
            writer.writeheader()

    with open(filepath, 'a', newline='') as csvfile:
        writer = csv.DictWriter(csvfile, fieldnames=list(infos.keys()))
        writer.writerow(infos)


def selectEnt(
    msg: str,
    filterStr: str
) -> core.Selection:

    try:
        app: core.Application = core.Application.get()
        ui: core.UserInterface = app.userInterface
        sel = ui.selectEntity(msg, filterStr)
        return sel
    except:
        return None

