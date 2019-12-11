## Payment File Merger

The purpose of this script is to merge oTree and Z-Tree payment files into one Z-Tree formatted payment file.

Usage
-----
The oTree and Z-Tree input files must be placed in the in folder and named `otree.xlsx` and `ztree.pay`, respectively.

To run the script execute the following command:
`python -m merge`

Output
------
The combined payoffs will be placed in the out folder and named **Payoff_\<iso_timestamp\>.pay**, where
**<iso_timestamp>** is the appended iso timestamp corresponding to the date and time the merger script was executed.
