#!/bin/sh

here=$(cd $(dirname $0); pwd)
cd $here

for u in / /other/ ; do prequest development.ini $u; done
