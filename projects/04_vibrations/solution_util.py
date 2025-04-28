"""Utility functions for Project 1"""

from protomol import qc, geom
import qcio
import qcop
import numpy
import functools
from numpy.typing import ArrayLike, NDArray


# Geometry
def equilibrium_geometry(
    geo0: geom.Geometry, prog: str, model: qcio.Model
) -> geom.Geometry:
    """Optimize equilibrium geometry.

    :param geo: Starting geometry
    :param prog: Electronic structure program
    :param model: Electronic structure model
    :return: Equilibrium geometry
    """
    struc = qc.struc.from_geometry(geo0)
    prog_inp = qcio.ProgramInput(structure=struc, calctype="optimization", model=model)
    prog_out = qcop.compute(prog, prog_inp)
    return qc.struc.geometry(prog_out.results.final_structure)


# Hessian
def hessian_direct(
    geo0: geom.Geometry, prog: str, model: qcio.Model
) -> NDArray[numpy.float64]:
    """Calculate Hessian directly from program.

    :param geo: Starting geometry
    :param prog: Electronic structure program
    :param model: Electronic structure model
    :return: Hessian
    """
    struc = qc.struc.from_geometry(geo0)
    prog_inp = qcio.ProgramInput(structure=struc, calctype="hessian", model=model)
    prog_out = qcop.compute(prog, prog_inp)
    return prog_out.results.hessian


def hessian(
    geo0: geom.Geometry, prog: str, model: qcio.Model, step_size: float = 0.005
) -> NDArray[numpy.float64]:
    """Calculate Hessian matrix.

    :param geo0: Geometry
    :param prog: Electronic structure program
    :param model: Electronic structure model
    :param step_size: Displacement step size in Bohr, defaults to 0.005
    :return: Hessian matrix
    """
    # Get initial input and reference geometry
    struc0 = qc.struc.from_geometry(geo0)
    prog_inp0 = qcio.ProgramInput(structure=struc0, calctype="energy", model=model)

    # Define a function to calculate the energy of a given displacement
    @functools.cache
    def energy(idx: int = 0, step: int = 0, idx2: int = 0, step2: int = 0):
        # Generate displaced geometry
        geo = step_displace_coordinate(geo0, idx=idx, step=step, step_size=step_size)
        geo = step_displace_coordinate(geo, idx=idx2, step=step2, step_size=step_size)
        # Copy energy input and replace with displaced geometry
        prog_inp = prog_inp0.model_copy(
            update={"structure": qc.struc.from_geometry(geo)}
        )
        prog_out = qcop.compute(prog, prog_inp)
        return prog_out.results.energy

    # Create an empty Hessian matrix
    ncoord = coordinate_count(geo0)
    hess = numpy.zeros((ncoord, ncoord))

    # Calculate diagonal elements of Hessian matrix
    for idx in range(ncoord):
        hess[idx, idx] = (
            energy(idx=idx, step=+1) + energy(idx=idx, step=-1) - 2 * energy()
        ) / (step_size**2)

    # Calculate off-diagonal elements of Hessian matrix
    # (Iterate over lower triangle to avoid duplicate calculations)
    for idx1 in range(ncoord):
        for idx2 in range(idx1):
            hess[idx1, idx2] = hess[idx2, idx1] = (
                energy(idx=idx1, step=+1, idx2=idx2, step2=+1)
                + energy(idx=idx1, step=-1, idx2=idx2, step2=-1)
                - energy(idx=idx1, step=+1)
                - energy(idx=idx1, step=-1)
                - energy(idx=idx2, step=+1)
                - energy(idx=idx2, step=-1)
                + 2 * energy()
            ) / (2 * step_size**2)

    return hess


def coordinate_count(geo: geom.Geometry) -> int:
    """Count number of coordinates in geometry.

    (Generic function that could be added to protomol.geom.)

    :param geo: Geometry
    :return: Number of coordinates
    """
    return geom.count(geo) * 3


def displace(geo: geom.Geometry, disp: ArrayLike) -> geom.Geometry:
    """Displace geometry by arbitrary coordinate vector.

    (Generic function that could be added to protomol.geom.)

    :param geo: Geometry
    :param disp: Displacement vector
    :return: Displaced geometry
    """
    geo = geo.model_copy()
    natms = geom.count(geo)
    geo.coordinates = geo.coordinates + numpy.reshape(disp, (natms, 3))
    return geo


def step_displace_coordinate(
    geo: geom.Geometry, idx: int, step: int = 1, step_size: float = 0.005
) -> geom.Geometry:
    """Step-displace geometry coordinate.

    (Project-specific helper function that could be added to util.py)

    :param geo: Geometry
    :param idx: Flat coordinate index, 0, 1, ..., 3 * n
    :param step: Number of steps to displace (positive or negative)
    :param step_size: Displacement step size
    :return: Geometry
    """
    ncoord = coordinate_count(geo)
    disp = numpy.eye(ncoord, ncoord)[idx] * step * step_size
    return displace(geo, disp)
