"""QCIO functions."""

import qcio
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
