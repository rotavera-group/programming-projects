"""Geometry data structure and functions."""

from pydantic import BaseModel
from .util.types import NDArray
from . import rd


class Geometry(BaseModel):
    """Geometry data structure."""

    symbols: list[str]
    coordinates: NDArray
    charge: int = 0
    spin: int = 0


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
