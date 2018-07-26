#!/bin/bash

# make destination folder
echo "make directories"
mkdir awards_2017_temp
mkdir awards_2017

# first I have to download the zip file and extract it to a folder
echo "download file"
curl -o awards.zip 'https://www.nsf.gov/awardsearch/download?DownloadFileName=2017&All=true' -H 'Connection: keep-alive' -H 'Upgrade-Insecure-Requests: 1'  --compressed

# extract awards.zip to destination folder
echo "unzipping file"
unzip awards.zip -d awards_2017_temp

# because bash is very frustrating I am going to make two for loops
echo "converting files to utf-8"
for i in $(ls awards_2017_temp);
  do
    iconv -f ISO-8859-1 -t UTF-8 < awards_2017_temp/$i > awards_2017/$i;
done

# Here I am going to extract all of the like 11 thousand lines into a file
echo "extracting award amounts from xml files"
for i in $(ls awards_2017);
  do
    xmllint --xpath 'string(//AwardAmount)' awards_2017/$i >> myfile.txt;
    echo $'\n' >> myfile.txt;
done

echo "writing award amounts without extra lines to file"
sed '/^\s*$/d' myfile.txt >> award_amounts_files/nsf_awards_2017.txt

echo "finished, check awards_amounts_files/nsf_awards_2017.txt"
