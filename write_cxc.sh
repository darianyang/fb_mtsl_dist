#!/bin/bash
# write a chimeraX cxc script

TRPs=(37 74 108 121 152)


CMD=""
for TRP in ${TRPs[@]} ; do
    for O in {1..200} ; do

        # assuming model 1 is protein and 2 is MTSLs
        CMD="$CMD distance #1/?:${TRP}@FE3 #2.${O}/A:1@O1 \n"

    done
done

# after creating all distances, write to file
CMD="$CMD distance save ~/Desktop/mtsl_dist/vloose_dists.dat"

# save to cxs file
echo -e $CMD > calc_dists.cxc
