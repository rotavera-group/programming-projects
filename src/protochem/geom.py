"""Geometry data structure and functions."""

from pydantic import BaseModel
from .util.types import NDArray
from . import rd
import qcio
from pint import Quantity

DISTANCE_UNIT = "angstrom"


class Geometry(BaseModel):
    """Geometry data structure."""

    symbols: list[str]
    coordinates: NDArray
    charge: int = 0
    spin: int = 0


# constructors
def from_rdkit_molecule(mol: rd.mol_.Mol) -> Geometry:
    """Generate geometry from RDKit molecule

    :param mol: Molecule
    :return: Geometry
    """
    mol = rd.mol_.with_coordinates(mol)
    return Geometry(
        symbols=rd.mol_.symbols(mol),
        coordinates=rd.mol_.coordinates(mol),
        charge=rd.mol_.charge(mol),
        spin=rd.mol_.spin(mol),
    )


# core properties
def symbols(geo: Geometry) -> list[str]:
    """Get atomic symbols.

    :param geo: Geometry
    :return: Symbols
    """
    return geo.symbols


def coordinates(geo: Geometry, unit: str = DISTANCE_UNIT) -> NDArray:
    """Get atomic coordinates.

    :param geo: Geometry
    :return: Coordinates
    """
    unit_conv = Quantity(DISTANCE_UNIT).m_as(unit) if unit != DISTANCE_UNIT else 1.0
    return geo.coordinates * unit_conv


def charge(geo: Geometry) -> int:
    """Get molecular charge.

    :param geo: Geometry
    :return: Charge
    """
    return geo.charge


def spin(geo: Geometry) -> int:
    """Get spin.

    spin = number of unpaired electrons = multiplicity - 1

    :param geo: Geometry
    :return: Spin
    """
    return geo.spin


# calculated properties
def multiplicity(geo: Geometry) -> int:
    """Get spin multiplicity.

    :param geo: Geometry
    :return: Spin multiplicity
    """
    return spin(geo) + 1


# conversions
def qcio_structure(geo: Geometry) -> qcio.Structure:
    """Generate QCIO structure from geometry.

    :param geo: Geometry
    :return: QCIO structure
    """
    return qcio.Structure(
        symbols=symbols(geo),
        geometry=coordinates(geo, unit="bohr"),
        charge=charge(geo),
        multiplicity=multiplicity(geo),
    )
