#!/bin/bash
# vitaminInfo

set -e

case $1 in
	"ei")
		if [ $# -ne 1 ];
			then
				python vitaminInfo.py -error
			else
				python vitaminInfo.py -ei
		fi
	;;
	"extendedInfo")
		if [ $# -ne 1 ];
			then
				python vitaminInfo.py -error
			else
				python vitaminInfo.py -ei
		fi
	;;
	"lf")
		if [ $# -ne 1 ];
			then
				python vitaminInfo.py -error
			else
				python vitaminInfo.py -lf
		fi
	;;
	"listFood")
		if [ $# -ne 1 ];
			then
				python vitaminInfo.py -error
			else
				python vitaminInfo.py -lf
		fi
	;;
	"lv")
		if [ $# -ne 1 ];
			then
				python vitaminInfo.py -error
			else
				python vitaminInfo.py -lv
		fi
	;;
	"listVitamin")
		if [ $# -ne 1 ];
			then
				python vitaminInfo.py -error
			else
				python vitaminInfo.py -lv
		fi
	;;
	"vi")
		if [ $# -ne 2 ];
			then
				python vitaminInfo.py -error
			else
				python vitaminInfo.py -vi $2
		fi
	;;
	"vitaminInfo")
		if [ $# -ne 2 ];
			then
				python vitaminInfo.py -error
			else
				python vitaminInfo.py -vi $2
		fi
	;;
	"v")
		if [ $# -ne 2 ];
			then
				python vitaminInfo.py -error
			else
				python vitaminInfo.py -v $2
		fi
	;;
	"vitamin")
		if [ $# -ne 2 ];
			then
				python vitaminInfo.py -error
			else
				python vitaminInfo.py -v $2
		fi
	;;
	"f")
		if [ $# -ne 2 ];
			then
				python vitaminInfo.py -error
			else
				python vitaminInfo.py -f $2
		fi
	;;
	"food")
		if [ $# -ne 2 ];
			then
				python vitaminInfo.py -error
			else
				python vitaminInfo.py -f $2
		fi
	;;
	"vf")
		if [ $# -ne 3 ];
			then
				python vitaminInfo.py -error
			else
				python vitaminInfo.py -vf $2 $3
		fi
	;;
	"vitaminAmountInFood")
		if [ $# -ne 3 ];
			then
				python vitaminInfo.py -error
			else
				python vitaminInfo.py -vf $2 $3
		fi
	;;
	"h")
		if [ $# -ne 1 ];
			then
				python vitaminInfo.py -error
			else
				python vitaminInfo.py -h
		fi
	;;
	"help")
		if [ $# -ne 1 ];
			then
				python vitaminInfo.py -error
			else
				python vitaminInfo.py -h
		fi
	;;
  	*)
	    echo "Usage: $0 (extendedInfo|listFood|listVitamin|vitaminInfo|vitamin $1|food $1|vitaminAmountInFood $1 $2)"
	    exit 1
	    ;;

esac
