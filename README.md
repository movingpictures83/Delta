# Delta
# Language: Python
# Input: TXT
# Output: none (screen only)
# Tested with: PluMA 1.1, Python 3.6
# Dependency: numpy==1.16.0

PluMA plugin to output statistics (mean, standard deviation, etc.) on the difference in abundance in taxa between two samples.

The plugin takes as input a TXT file that contain the two CSV files to compare on separate lines.  CSV files are assumed to have samples as rows and columns as abundances.

It will then output all differential statistics to the screen; including mean, standard deviation, and difference in each sample
