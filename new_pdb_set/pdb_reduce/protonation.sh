#!/bin/bash

# Loop over p1 to p5
for i in {1..5}; do
    prefix="p${i}"
    input_file=$(ls ${prefix}_*.pdb 2>/dev/null)

    if [[ -n "$input_file" ]]; then
        output_file="${prefix}.pdb"
        echo "Processing $input_file -> $output_file"
        pdb4amber --reduce -i "$input_file" -o "$output_file"
    else
        echo "No file found for prefix $prefix"
    fi
done

