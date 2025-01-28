"""Geometry data structure and functions."""

from pydantic import BaseModel
from .util.types import NDArray
from . import rd
from .util import units
import py3Dmol


class Geometry(BaseModel):
    """Geometry data structure.

    :param symbols: Atomic symbols
    :param coordinates: Atomic coordinates (units: bohr)
    :param charge: Total molecular charge
    :param spin: Total electronic spin (multiplicity - 1)
    """

    symbols: list[str]
    coordinates: NDArray
    charge: int = 0
    spin: int = 0


# constructors
def from_rdkit_molecule(mol: rd.mol.Mol) -> Geometry:
    """Generate geometry from RDKit molecule

    :param mol: Molecule
    :return: Geometry
    """
    mol = rd.mol.with_coordinates(mol)
    return Geometry(
        symbols=rd.mol.symbols(mol),
        coordinates=rd.mol.coordinates(mol),
        charge=rd.mol.charge(mol),
        spin=rd.mol.spin(mol),
    )


# core properties
def count(geo: Geometry) -> int:
    """Get number of atoms.

    :param geo: Geometry
    :return: Number of atoms
    """
    return len(symbols(geo))


def symbols(geo: Geometry) -> list[str]:
    """Get atomic symbols.

    :param geo: Geometry
    :return: Symbols
    """
    return geo.symbols


def coordinates(geo: Geometry, unit: str = units.DISTANCE_UNIT) -> NDArray:
    """Get atomic coordinates.

    :param geo: Geometry
    :return: Coordinates
    """
    return geo.coordinates * units.distance_conversion(units.DISTANCE_UNIT, unit)


def charge(geo: Geometry) -> int:
    """Get total molecular charge.

    :param geo: Geometry
    :return: Charge
    """
    return geo.charge


def spin(geo: Geometry) -> int:
    """Get total electronic spin.

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
def xyz_string(geo: str) -> str:
    """Serialize as XYZ string.

    :param geo: Geometry
    :return: XYZ string
    """
    natms = count(geo)
    symbs = symbols(geo)
    xyzs = coordinates(geo, unit="angstrom")
    return f"{natms}\n\n" + "\n".join(
        f"{s} {x:10.6f} {y:10.6f} {z:10.6f}"
        for s, (x, y, z) in zip(symbs, xyzs, strict=True)
    )


def display(geo: str, width: int = 600, height: int = 450) -> None:
    """Display geometry.

    For now, using QCIO for this.

    :param geo: Geometry
    :param width: Width
    :param height: Height
    """
    viewer = py3Dmol.view(width=width, height=height)
    viewer.addModel(xyz_string(geo), "xyz")
    viewer.setStyle({"stick": {}, "sphere": {"scale": 0.3}})
    viewer.zoomTo()
    viewer.show()
