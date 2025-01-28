"""SMILES functions."""
from . import rd
from . import geom
from .geom import Geometry


def geometry(smi: str) -> Geometry:
    """Generate geometry from SMILES.

    :param smi: SMILES
    :return: Geometry
    """
    mol = rd.mol.from_smiles(smi, with_coords=True)
    return geom.from_rdkit_molecule(mol)
