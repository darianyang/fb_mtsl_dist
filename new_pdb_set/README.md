# updated pdb set

* note that the PDBs were converted to p1-p5 (ordered by naming scheme):
  
| PDB | p_code |
| --- | ------ |
| T1131TS037_3    | p1    |
| T1131TS074_2    | p2    |
| T1131TS225_2    | p3    |
| T1131TS229_1    | p4    |
| T1131TS498_5    | p5    |

* first, a script to convert PDBs:
    * add protons (pdb4amber), see `pdb_reduce/protonation.sh`
* then a script to use chimerax and convert the following of each, see `trp_cys_mod.sh`
    * convert all TRP to 5F-TRP
        * 37 74 108 121 152
    * convert to CYS: V24 V104 N79
