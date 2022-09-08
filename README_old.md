SAXS-WAXS-Data-Analysis

This code should run some real-time analysis of the data from any experiment we perform at the SAXS/WAXS beamline (or any beamline for that matter). #

The steps required for analysis are listed below. Each step is separated by a section, with an explanation on what needs to be done for analysis. #

----Dat2Tif----
        Convert raw image files into .tif for ease of import and analysis. #  
        **Uploaded; checked by paul, might need a fix because i janked it up**

----Read in log files---- (done)
        Read the log file in and plot whatever output variable we need.
        If anything is wrong we should write some code to quickly overplot absorption and motor values, to diagnose any bad stuff  <- I0 is set up for now, can only update on the fly

----DarkField correction.----
        Subtract the dark field images from the frames with the same exposure times.


----Integrated intensity plot----
        Plot the integrated intensity of each of the diffraction images against energy, overplot I0 and separately plot the ratio of intensities (I/I0)


----Reconstruction----
        The majority of this section is completed in the recon_test.py file
    Reconstruct the CTF of the sample in 1D. Steps are as follows below:

        Divide each frame by it's corresponding I0 value

        Convert the 2d image to a 1d diffraction pattern. This is either a line down the center, or we crop the image and sum across the x-axis #
        **DONE!**
        Take the inverse fourier transform of the diffraction pattern. #
        **DONE!**
        The max value, the autocorrelation, will be taken as the value for absorption. Some other analytical steps are required for absolute scaling, but we ignore that for now #
        **DONE!**
        The phase will have to be checked manually, but we just take the angle of the complex transmission function and take the average of a pre-defined flat region #
        ^ this step requires some tweaking, maybe we can find the position that the phase region occurs using a simulation? #
        Half done :'(
        The CTF Absorption and Phase should be overplot to show a complete result #
