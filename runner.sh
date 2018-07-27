#!/bin/bash

echo "**** Executing ****"

echo "*** Running tags $1"
echo "*** Feature File $2"

behave --no-logcapture --tags=$1 $2

echo "-----------------------END-------------------------------------------------------------------------------------"
