from pymatgen.ext.matproj import MPRester

# Replace with your Materials Project API key
API_KEY = "your_api_key_here"

# Initialize the MPRester with your API key
mpr = MPRester(API_KEY)

# Query the LiCl structure
structure = mpr.get_structure_by_material_id("mp-22862")  # Replace with the correct material_id for LiCl

# Write the structure to a POSCAR file
structure.to(fmt="poscar", filename="POSCAR_LiCl")
