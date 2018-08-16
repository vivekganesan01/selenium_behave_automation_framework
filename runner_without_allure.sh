#!/bin/bash
# __author__ = "Vivek Ganesan"

echo "**** Executing ****"

echo "*** Running tags $1"
echo "*** Feature File $2"

behave --no-logcapture --tags=$1 $2

echo "-------------------------------------------END-----------------------------------------------------------------"
