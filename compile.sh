#!/bin/bash
rm compiled/*.txt

for filename in version_control/*.txt; do
    cat $filename >> compiled/version_control.txt
    cat $filename >> compiled/all.txt
done