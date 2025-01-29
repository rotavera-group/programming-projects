"""RDKit molecule functions."""

import numpy
from rdkit import Chem
from rdkit.Chem import Mol
from rdkit.Chem import AllChem, Descriptors
import copy
from ..util.types import NDArray
from ..util import units

RDKIT_DISTANCE_UNIT = "angstrom"


def from_smiles(smi: str, with_coords: bool = False) -> Mol:
    """Generate an RDKit molecule from SMILES.

    :param smi: SMILES
    :param with_coords: Whether to add coordinates to the molecule
    :return: RDKit molecule
    """
    mol = Chem.MolFromSmiles(smi)
    mol = Chem.AddHs(mol)
    if with_coords:
        mol = with_coordinates(mol)
    return mol


# properties
def symbols(mol: Mol) -> list[str]:
    """Get atomic symbols.

    :param mol: RDKit molecule
    :return: Symbols
    """
    return [a.GetSymbol() for a in mol.GetAtoms()]


def coordinates(mol: Mol, unit: str = units.DISTANCE_UNIT) -> NDArray | None:
    """Get atomic coordinates.

    Requires an embedded molecule (otherwise, returns None).

    :param mol: RDKit molecule
    :return: Coordinates
    """
    if not has_coordinates(mol):
        return None

    natms = mol.GetNumAtoms()
    conf = mol.GetConformer()
    coords = [conf.GetAtomPosition(i) for i in range(natms)]
    coords = numpy.array(coords, dtype=numpy.float64)
    return coords * units.distance_conversion(RDKIT_DISTANCE_UNIT, unit)


def charge(mol: Mol) -> int:
    """Get molecular charge.

    :param mol: RDKit molecule
    :return: Charge
    """
    return Chem.GetFormalCharge(mol)


def spin(mol: Mol) -> int:
    """Determine (or guess) molecular spin.

    spin = number of unpaired electrons = multiplicity - 1

    TODO: Add flags to decide between high- and low-spin guess where ambiguous.

    :param mol: RDKit molecule
    :return: Spin
    """
    return Descriptors.NumRadicalElectrons(mol)


# boolean properties
def has_coordinates(mol: Mol) -> str:
    """Determine if RDKit molecule has coordinates.

    :param mol: RDKit molecule
    :return: `True` if it does, `False` if not
    """
    return bool(mol.GetNumConformers())


# transformations
def with_coordinates(mol: Mol) -> Mol:
    """Add coordinates to RDKit molecule, if missing.

    :param mol: RDKit molecule
    :return: RDKit molecule
    """
    if not has_coordinates(mol):
        mol = copy.deepcopy(mol)
        AllChem.EmbedMolecule(mol)
    return mol


# def xyz_string(mol: Mol) -> str:
#     """Generate an XYZ string from an RDKit molecule.

#     :param mol: RDKit molecule
#     :return: XYZ string
#     """
#     return MolToXYZBlock(mol)
