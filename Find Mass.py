# Fusion360API Python script

import traceback
import adsk.core as core
import adsk.fusion as fusion

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

        show_physicalProperties(sel.entity)
        a=1

    except:
        if ui:
            ui.messageBox('Failed:\n{}'.format(traceback.format_exc()))


def show_physicalProperties(
    entity: core.Base,
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

    # infos = [	
    #     f'Mass \t\t{props.mass}',	
    #     f'Volume \t\t{props.volume}',	
    #     f'Density \t\t{props.density}',	
    #     f'Area \t\t{props.area}',	
    #     f'World X,Y,Z \t\t{worldXYZ}',	
    #     f'CenterOfMass \t{props.centerOfMass.asArray()}',	
    # ]	


    app: core.Application = core.Application.get()
    ui: core.UserInterface = app.userInterface
    ui.messageBox('\n'.join(infos))


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

