#!/bin/bash

####################################################################
#                   IMILAB AI PROJECT TOOLKIT
# ==================================================================
# @Author:  qinhongjie@imilab.com
# ------------------------------------------------------------------
# @History:
# 2021/03/23 v0.0.1 init/create
####################################################################

########################
#### Global Setting ####
########################

## debug settings
PATH=.:$PATH
set -e # -ex
## script version
VERSION=0.0.1

########################
### Private Function ###
########################

EchoError() {
  echo -e "\033[31;1m[Error ] $@\033[0m"
}

EchoPass() {
  echo -e "\033[32;1m$@\033[0m"
}

########################
####  Main  Region  ####
########################

md5_jpg=$(ls JPEGImages/ | sed 's/.jpg//g'I | md5sum)
md5_ann=$(ls Annotations/ | sed 's/.xml//g'I | md5sum)
md5_txt=$(cat ImageSets/Main/trainval.txt ImageSets/Main/test.txt | sort | sed ':a;N;s/\r//g;ta' | md5sum)
## check md5sum
if [[ x"${md5_jpg}" != x"${md5_ann}" || x"${md5_jpg}" != x"${md5_txt}" ]]; then
    EchoError "md5sum check error!"
    exit 1
fi

cnt_trv=$(cat ImageSets/Main/trainval.txt | wc -l)
cnt_tr_v=$(cat ImageSets/Main/train.txt ImageSets/Main/val.txt | wc -l)
cnt_trv_t=$(cat ImageSets/Main/trainval.txt ImageSets/Main/test.txt | wc -l)
cnt_jpg=$(ls JPEGImages | wc -l)
## check count
if [[ x"${cnt_trv}" != x"${cnt_tr_v}" || x"${cnt_trv_t}" != x"${cnt_jpg}" ]]; then
    EchoError "count check error!"
    exit 1
fi

EchoPass "Good News! VOC dataset check pass!"