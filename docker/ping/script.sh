#!/bin/bash
for ((; ;)); 
do
  ping -c 1 google.com
  echo -e
  echo -e "##############################"
  echo -e
  sleep 10;
done
