#!/bin/sh
workingdir=$1
app=$2
fn=$3

cd $workingdir && fn create app $app && fn -v build && fn deploy --app $app --local