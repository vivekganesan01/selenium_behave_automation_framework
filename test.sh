#!/usr/bin/env bash

while getopts ":i:" opt; do
  case $opt in
    i)
      echo "-a was triggered, Parameter: $OPTARG"
      ;;
    \?)
      echo "Invalid option: -$OPTARG"
      exit 1
      ;;
    :)
      echo "Option -$OPTARG requires an argument."
      exit 1
      ;;
  esac
done