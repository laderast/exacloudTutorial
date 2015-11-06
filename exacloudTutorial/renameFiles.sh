#!/usr/bin/env bash
#script takes an single argument, prefix
#and renames everything that has that prefix numerically
#with no padding (i.e. data0, data1, data2, data3, etc.)
 prefix = $1

 n=0
 for file in $1*
 do
   mv $file data$n
   n=$((n+1))
 done
