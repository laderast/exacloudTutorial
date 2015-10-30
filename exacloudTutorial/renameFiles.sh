#!/usr/bin/env bash

 n=0
 for file in data.*  
 do 
   mv $file data.$n 
   n=$((n+1))  
 done
