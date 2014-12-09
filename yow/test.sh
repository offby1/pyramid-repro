#!/bin/sh

here=$(cd $(dirname $0); pwd)
cd $here

for ini in development.ini production.ini
do
    echo ${ini}
    for u in / /other/ ; do prequest ${ini} $u; done
done
