#!/bin/bash

for i in {1..5}; do
    infile="p${i}.pdb"
    outfile="p${i}_wiz.pdb"

    if [[ -f "$infile" ]]; then
        echo "Processing $infile -> $outfile"
        # run pdb-tools to reduce the PDB file, add chain A, select altloc, and tidy/format
        pdb_delelem -H $infile | pdb_chain -A | pdb_selaltloc | pdb_tidy > $outfile
    else
        echo "$infile not found, skipping."
    fi
done

