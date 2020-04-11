#!/bin/bash
rm wordlists/*.txt

for filename in version_control/*.txt; do
    cat $filename >> wordlists/version_control.txt
    cat $filename >> wordlists/all.txt
done