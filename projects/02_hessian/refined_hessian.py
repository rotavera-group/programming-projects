# %%
def GetHessian(smi):
    ### a simple function to calculate the Hessian of a molecule using an inputed smile string and central difference formula
    ### not as efficient as the in build calculation for a hessian, however, is a good thought experiment
    from protomol import qc, smiles, geom
    import qcio, qcop
    import numpy as np
    #converts the smile string to geometries and structures that can be used for calculations
    geo = smiles.geometry(smi)
    struc = qc.struc.from_geometry(geo)

    #calculate the base optimized energy of the molecule
    Base_input = qcio.ProgramInput(structure = struc, calctype = "optimization", model = {"method":"gfn2"})
    Base_output = qcop.compute("crest",Base_input)
    Base_energy = Base_output.results.final_energy

    #establish the simple list of coordinates, a copy of the list, and a copy of the geo for manipulation in loop
    #the copies allow us to manipulate the data without worry of trying to reset it through complex means
    #also sets the arbitrary displacement to small number of 0.00005, also sets an empty list to store calculated Hessian Values
    Structure = Base_output.results.final_structure
    Opt_Geometry = qc.struc.geometry(Structure)
    displacement = 0.00005
    Coordinates_simple = np.ravel(Opt_Geometry.coordinates)
    Coordinates_simple_copy = Coordinates_simple
    Geometry_Temp = Opt_Geometry
    Hessian = []

    #Creates the dual loops that will iterate through the different coordinates and generate results of 
    #1:1, 1:2, 1:3, 2:1, 2:2, 2:3, 3:1, 3:2, 3:3 and so on for the length of the number of coordinates
    for x in range(len(Opt_Geometry.symbols)*3):
        for y in range(len(Opt_Geometry.symbols)*3):
            energy_values = []  #an empty list created to store the calculated values of the sub calculations of the central
        #difference formula, is placed here in order to ensure it is emptied/reset at the start of each hessian coordinate/calc
            if x == y: #sets the condition for the diagonals of the hessian, uses the more simple central dif formula for a single variable
                for i in range(3): #iterates through sub calculations of central-dif-formula, assigned in order per formula
                    if i == 0:
                        Coordinates_simple_copy[x] = Coordinates_simple[x]+displacement #offsets the coordinate by the displacement
                        Geometry_Temp.coordinates = Coordinates_simple_copy.reshape(len(Opt_Geometry.symbols),3) #returns the simple coordinates to the proper array shape
                        structure_temp = qc.struc.from_geometry(Geometry_Temp)
                        Input_Temp = qcio.ProgramInput(structure = structure_temp, calctype = "energy", model = {"method":"gfn2"})
                        Output_temp = qcop.compute("crest",Input_Temp)
                        Energy_Temp_Result = Output_temp.results.energy
                        energy_values.append(Energy_Temp_Result)
                    elif i == 1:
                        Coordinates_simple_copy[x] = Coordinates_simple[x]-displacement
                        Geometry_Temp.coordinates = Coordinates_simple_copy.reshape(len(Opt_Geometry.symbols),3) 
                        structure_temp = qc.struc.from_geometry(Geometry_Temp)
                        Input_Temp = qcio.ProgramInput(structure = structure_temp, calctype = "energy", model = {"method":"gfn2"})
                        Output_temp = qcop.compute("crest",Input_Temp)
                        Energy_Temp_Result = Output_temp.results.energy
                        energy_values.append(Energy_Temp_Result)
                    
                    #within the loop we need to reset the structure and coordinates to the base in order to prevent inaccurate manipulation
                    Coordinates_simple_copy = Coordinates_simple
                    Geometry_Temp = Opt_Geometry
                #uses the energy values stored in the energy_values list along with the central diff formula to calculate the diagonal hess value
                #the value is the appended to the actual Hessian coordinate list of finished values which is our output once everything is done
                Hessian_Coordinate = (energy_values[0]+energy_values[1]-(2*Base_energy))/(displacement**2)
                Hessian.append(Hessian_Coordinate)
            else:  #calculates the non diagonals, much of the general structure is the same, therefore limited comments
                for n in range(6):
                    if n == 0:
                        Coordinates_simple_copy[x] = Coordinates_simple[x]+displacement
                        Coordinates_simple_copy[y] = Coordinates_simple[y]+displacement
                        Geometry_Temp.coordinates = Coordinates_simple_copy.reshape(len(Opt_Geometry.symbols),3) 
                        structure_temp = qc.struc.from_geometry(Geometry_Temp)
                        Input_Temp = qcio.ProgramInput(structure = structure_temp, calctype = "energy", model = {"method":"gfn2"})
                        Output_temp = qcop.compute("crest",Input_Temp)
                        Energy_Temp_Result = Output_temp.results.energy
                        energy_values.append(Energy_Temp_Result)
                    elif n == 1:
                        Coordinates_simple_copy[x] = Coordinates_simple[x]-displacement
                        Coordinates_simple_copy[y] = Coordinates_simple[y]-displacement
                        Geometry_Temp.coordinates = Coordinates_simple_copy.reshape(len(Opt_Geometry.symbols),3) 
                        structure_temp = qc.struc.from_geometry(Geometry_Temp)
                        Input_Temp = qcio.ProgramInput(structure = structure_temp, calctype = "energy", model = {"method":"gfn2"})
                        Output_temp = qcop.compute("crest",Input_Temp)
                        Energy_Temp_Result = Output_temp.results.energy
                        energy_values.append(Energy_Temp_Result)
                    elif n == 2:
                        Coordinates_simple_copy[x] = Coordinates_simple[x]+displacement
                        Geometry_Temp.coordinates = Coordinates_simple_copy.reshape(len(Opt_Geometry.symbols),3) 
                        structure_temp = qc.struc.from_geometry(Geometry_Temp)
                        Input_Temp = qcio.ProgramInput(structure = structure_temp, calctype = "energy", model = {"method":"gfn2"})
                        Output_temp = qcop.compute("crest",Input_Temp)
                        Energy_Temp_Result = Output_temp.results.energy
                        energy_values.append(Energy_Temp_Result)
                    elif n == 3:
                        Coordinates_simple_copy[x] = Coordinates_simple[x]-displacement
                        Geometry_Temp.coordinates = Coordinates_simple_copy.reshape(len(Opt_Geometry.symbols),3) 
                        structure_temp = qc.struc.from_geometry(Geometry_Temp)
                        Input_Temp = qcio.ProgramInput(structure = structure_temp, calctype = "energy", model = {"method":"gfn2"})
                        Output_temp = qcop.compute("crest",Input_Temp)
                        Energy_Temp_Result = Output_temp.results.energy
                        energy_values.append(Energy_Temp_Result)
                    elif n == 4:
                        Coordinates_simple_copy[y] = Coordinates_simple[y]+displacement
                        Geometry_Temp.coordinates = Coordinates_simple_copy.reshape(len(Opt_Geometry.symbols),3) 
                        structure_temp = qc.struc.from_geometry(Geometry_Temp)
                        Input_Temp = qcio.ProgramInput(structure = structure_temp, calctype = "energy", model = {"method":"gfn2"})
                        Output_temp = qcop.compute("crest",Input_Temp)
                        Energy_Temp_Result = Output_temp.results.energy
                        energy_values.append(Energy_Temp_Result)
                    elif n == 5:
                        Coordinates_simple_copy[y] = Coordinates_simple[y]-displacement
                        Geometry_Temp.coordinates = Coordinates_simple_copy.reshape(len(Opt_Geometry.symbols),3) 
                        structure_temp = qc.struc.from_geometry(Geometry_Temp)
                        Input_Temp = qcio.ProgramInput(structure = structure_temp, calctype = "energy", model = {"method":"gfn2"})
                        Output_temp = qcop.compute("crest",Input_Temp)
                        Energy_Temp_Result = Output_temp.results.energy
                        energy_values.append(Energy_Temp_Result)
                   
                    #value resets
                    Coordinates_simple_copy = Coordinates_simple
                    Geometry_Temp = Opt_Geometry
                #start of calculation using multivariable central difference formula, broken into numerator and denominator for simplicity
                Hessian_Coordinate_Numerator = (energy_values[0]+energy_values[1]-energy_values[2]-energy_values[3]-energy_values[4]-energy_values[5]+(Base_energy*2))
                Hessian_Coordinate_Denominator = 2*(displacement**2)
                Hessian_Coordinate = Hessian_Coordinate_Numerator/Hessian_Coordinate_Denominator
                Hessian.append(Hessian_Coordinate)
    Hessian = np.array(Hessian).reshape(len(Opt_Geometry.symbols)*3,len(Opt_Geometry.symbols)*3)
    return Hessian








