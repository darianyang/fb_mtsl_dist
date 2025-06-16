#!/bin/bash

for i in {1..5}; do
    infile="p${i}.pdb"
    outfile="p${i}_modified.pdb"

    if [[ -f "$infile" ]]; then
        echo "Processing $infile -> $outfile"

        # Generate a temporary .cxc script with substituted paths
        cat > trp_cys_mod.cxc <<EOF
open $infile

build modify /?:37@HZ3 F 1 name FZ3 resName W5F
build modify /?:74@HZ3 F 1 name FZ3 resName W5F
build modify /?:108@HZ3 F 1 name FZ3 resName W5F
build modify /?:121@HZ3 F 1 name FZ3 resName W5F
build modify /?:152@HZ3 F 1 name FZ3 resName W5F

swapaa #1/?:24 CYS criteria 1 rotLib Dunbrack
swapaa #1/?:79 CYS criteria 1 rotLib Dunbrack
swapaa #1/?:104 CYS criteria 1 rotLib Dunbrack

save $outfile format pdb
exit
EOF

        # Run ChimeraX with the temp script
        chimerax --nogui trp_cys_mod.cxc

    else
        echo "$infile not found, skipping."
    fi
done

