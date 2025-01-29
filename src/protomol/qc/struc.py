"""QCIO functions."""

import qcio
from qcio.view import view
from ..geom import Geometry
from .. import geom


# constructors
def from_geometry(geo: Geometry) -> qcio.Structure:
    """Generate QCIO structure from geometry.

    :param geo: Geometry
    :return: QCIO structure
    """
    return qcio.Structure(
        symbols=geom.symbols(geo),
        geometry=geom.coordinates(geo, unit="bohr"),
        charge=geom.charge(geo),
        multiplicity=geom.multiplicity(geo),
    )


# conversions
def geometry(struc: qcio.Structure) -> Geometry:
    """Generate geometry from QCIO structure.

    :param struc: QCIO structure
    :return: Geometry
    """
    return Geometry(
        symbols=struc.symbols,
        coordinates=struc.geometry,
        charge=struc.charge,
        spin=struc.multiplicity - 1,
    )


def display(struc: qcio.Structure, width: int = 600, height: int = 450) -> None:
    """Display structure.

    :param struc: QCIO Structure
    :param width: Width
    :param height: Height
    """
    view(struc, width=width, height=height)
