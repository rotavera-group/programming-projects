from protomol import qc, smiles, geom
import qcio, qcop
import numpy as np
def EnergyCalculationWOO(geometry, x, operand, displacement=0.00005):
    #stands for energy calculation with one operand
    #takes a molecular geometry, the x position, and a (+/-) operand for the offset
    #has a built in displacement of 0.00005 that can be changed using a keyword argument
    if operand == "+":
        coordinates = np.ravel(geometry.coordinates)
        coordinates_copy = coordinates
        coordinates_copy[x] = coordinates[x]+displacement #offsets the coordinate by the displacement
        geometry.coordinates = coordinates_copy.reshape(len(geometry.symbols),3) #returns the simple coordinates to the proper array shape
        structure_temp = qc.struc.from_geometry(geometry)
        Input_Temp = qcio.ProgramInput(structure = structure_temp, calctype = "energy", model = {"method":"gfn2"})
        Output_temp = qcop.compute("crest",Input_Temp)
        Energy_Temp_Result = Output_temp.results.energy
        return Energy_Temp_Result
    else:
        coordinates = np.ravel(geometry.coordinates)
        coordinates_copy = coordinates
        coordinates_copy[x] = coordinates[x]-displacement #offsets the coordinate by the displacement
        geometry.coordinates = coordinates_copy.reshape(len(geometry.symbols),3) #returns the simple coordinates to the proper array shape
        structure_temp = qc.struc.from_geometry(geometry)
        Input_Temp = qcio.ProgramInput(structure = structure_temp, calctype = "energy", model = {"method":"gfn2"})
        Output_temp = qcop.compute("crest",Input_Temp)
        Energy_Temp_Result = Output_temp.results.energy
        return Energy_Temp_Result
def EnergyCalculationWTO(geometry, x, y, operand, displacement=0.00005):
    #operates the same as the previous function, however, it also takes a y index and needs two operands
    #operators should be entered as "++", "+-", "-+", or "--"
    #the first operand enetered will apply to the x value and the second to the y value
    if operand == "++":
        coordinates = np.ravel(geometry.coordinates)
        coordinates_copy = coordinates
        coordinates_copy[x] = coordinates[x]+displacement #offsets the coordinate by the displacement
        coordinates_copy[y] = coordinates[y]+displacement
        geometry.coordinates = coordinates_copy.reshape(len(geometry.symbols),3) #returns the simple coordinates to the proper array shape
        structure_temp = qc.struc.from_geometry(geometry)
        Input_Temp = qcio.ProgramInput(structure = structure_temp, calctype = "energy", model = {"method":"gfn2"})
        Output_temp = qcop.compute("crest",Input_Temp)
        Energy_Temp_Result = Output_temp.results.energy
        return Energy_Temp_Result
    elif operand == "+-":
        coordinates = np.ravel(geometry.coordinates)
        coordinates_copy = coordinates
        coordinates_copy[x] = coordinates[x]+displacement #offsets the coordinate by the displacement
        coordinates_copy[y] = coordinates[y]-displacement
        geometry.coordinates = coordinates_copy.reshape(len(geometry.symbols),3) #returns the simple coordinates to the proper array shape
        structure_temp = qc.struc.from_geometry(geometry)
        Input_Temp = qcio.ProgramInput(structure = structure_temp, calctype = "energy", model = {"method":"gfn2"})
        Output_temp = qcop.compute("crest",Input_Temp)
        Energy_Temp_Result = Output_temp.results.energy
        return Energy_Temp_Result
    elif operand == "-+":
        coordinates = np.ravel(geometry.coordinates)
        coordinates_copy = coordinates
        coordinates_copy[x] = coordinates[x]-displacement #offsets the coordinate by the displacement
        coordinates_copy[y] = coordinates[y]+displacement
        geometry.coordinates = coordinates_copy.reshape(len(geometry.symbols),3) #returns the simple coordinates to the proper array shape
        structure_temp = qc.struc.from_geometry(geometry)
        Input_Temp = qcio.ProgramInput(structure = structure_temp, calctype = "energy", model = {"method":"gfn2"})
        Output_temp = qcop.compute("crest",Input_Temp)
        Energy_Temp_Result = Output_temp.results.energy
        return Energy_Temp_Result
    elif operand == "--":
        coordinates = np.ravel(geometry.coordinates)
        coordinates_copy = coordinates
        coordinates_copy[x] = coordinates[x]-displacement #offsets the coordinate by the displacement
        coordinates_copy[y] = coordinates[y]-displacement
        geometry.coordinates = coordinates_copy.reshape(len(geometry.symbols),3) #returns the simple coordinates to the proper array shape
        structure_temp = qc.struc.from_geometry(geometry)
        Input_Temp = qcio.ProgramInput(structure = structure_temp, calctype = "energy", model = {"method":"gfn2"})
        Output_temp = qcop.compute("crest",Input_Temp)
        Energy_Temp_Result = Output_temp.results.energy
        return Energy_Temp_Result
def GetHessian(smile, displacement=0.00005):
    #takes a smile string as an argument
    #generates the string and calculates the optimized version
    geo = smiles.geometry(smile)
    struc = qc.struc.from_geometry(geo)
    Optimized_Input = qcio.ProgramInput(structure=struc, calctype="optimization", model={"method":"gfn2"})
    Optimized_Output = qcop.compute("crest", Optimized_Input)
    Optimized_Energy = Optimized_Output.results.final_energy
    Structure = Optimized_Output.results.final_structure
    geometry_op = qc.struc.geometry(Structure)
    Hessian = []
    #starts the loops that iterate through the coordinates of the molecule
    for x in range(len(geometry_op.symbols)*3):
        for y in range(len(geometry_op.symbols)*3):
            energy_values = []
            if x==y:
                for i in range(2):
                    if i == 0:
                        energy_value_temp = EnergyCalculationWOO(geometry_op, x, operand="+")
                        energy_values.append(energy_value_temp)
                    elif i == 1:
                        energy_value_temp = EnergyCalculationWOO(geometry_op, x, operand="-")
                        energy_values.append(energy_value_temp)
                Hessian_Coordinate = (energy_values[0]+energy_values[1]-(2*Optimized_Energy))/(displacement**2)
                Hessian.append(Hessian_Coordinate)
            else:
                for n in range(6):
                    if n == 0:
                        energy_value_temp = EnergyCalculationWTO(geometry_op, x, y, operand="++")
                        energy_values.append(energy_value_temp)
                    elif n == 1:
                        energy_value_temp = EnergyCalculationWTO(geometry_op, x, y, operand="--")
                        energy_values.append(energy_value_temp)
                    elif n == 2:
                        energy_value_temp = EnergyCalculationWOO(geometry_op, x, operand="+")
                        energy_values.append(energy_value_temp)
                    elif n == 3:
                        energy_value_temp = EnergyCalculationWOO(geometry_op, x, operand="-")
                        energy_values.append(energy_value_temp)
                    elif n == 4:
                        energy_value_temp = EnergyCalculationWOO(geometry_op, y, operand="+")
                        energy_values.append(energy_value_temp)
                    elif n == 5:
                        energy_value_temp = EnergyCalculationWOO(geometry_op, y, operand="-")
                        energy_values.append(energy_value_temp)
                Hessian_Coordinate_Numerator = (energy_values[0]+energy_values[1]-energy_values[2]-energy_values[3]-energy_values[4]-energy_values[5]+(Optimized_Energy*2))
                Hessian_Coordinate_Denominator = 2*(displacement**2)
                Hessian_Coordinate = Hessian_Coordinate_Numerator/Hessian_Coordinate_Denominator
                Hessian.append(Hessian_Coordinate)
    Hessian = np.array(Hessian).reshape(len(geometry_op.symbols)*3,len(geometry_op.symbols)*3)
    return Hessian
value = GetHessian("C")
print(value)