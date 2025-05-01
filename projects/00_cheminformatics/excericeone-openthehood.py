import rdkit as rd
from rdkit import Chem
from rdkit.Chem import AllChem
from rdkit.Chem import rdDistGeom
# 1)Use RDkit to read the smiles string into a mol object
smi = "C[CH2]"
mol = Chem.MolFromSmiles(smi)
# 2)Add molecular coordinates to the mol object
mol = Chem.AddHs(mol)
rdDistGeom.EmbedMolecule(mol)
mol

# 3)Determine the atom count, atomic symbols, charge, and spin from the mol object. Store the coordinates as an array
# 4)Convert the coordinates from Angstroms to Bohr using Pint
# 5)Visualize the 3D structure using 3Dmol