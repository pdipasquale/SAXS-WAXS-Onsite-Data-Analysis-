import os
from dat_to_tif import dat_to_tif

def dat_from_file(path_in, path_out, dim=2048, tifsperdat=3, override=False):
    """
    Converts a directory of .dat files into .tif files

    Data from the SAXS/WAXS beamline is saved in a .dat format, comprised of 
    multiple measurements. This function takes in a directory with these 
    .dat files and saves them as .tif images in another location.

    path_in:
        The path to the directory of .dat files
    path_out:
        The location to save the produced .tif images
    dim:
        The height/width of an image in pixels; at SAXS/WAXS this is usually 2048
    tifsperdat:
        The number of .tif images expected for a given .dat file; at SAXS/WAXS 
        this is usually 3. 
    override:
        If set to True, this will delete an existing output directory including 
        all its contents and will replace it with a new one.

    ---------------------------------------------------------------------------

    Author: Jake J. Rogers, La Trobe University
    Date: 6th of September, 2022
    """    
    try:
        os.mkdir(path_out)
    except FileExistsError:
        if not override:
            print(
            """File already exists!
            Set the override tag to True to replace the directory.
            This will delete all files in the output path.""")
            return
        else:
            for file in os.listdir(path_out):
                os.remove(path_out + '/' + file)
            os.rmdir(path_out)
            os.mkdir(path_out)

    for (index, dat_name) in enumerate(os.listdir(path_in), 1):
        print(f"index={index}, dat={dat_name}")
        dat_to_tif(
            path_in + '/' + dat_name, 
            path_out, 
            [str(index*i) for i in range(1,tifsperdat+1)])
        
