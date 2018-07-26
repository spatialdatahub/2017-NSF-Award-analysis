 #!/bin/bash
 # Epic, going to extract all of the like 11 thousand lines into a file
 for i in $( ls awards_2017);
   do
     xmllint --xpath 'string(//AwardAmount)' awards_2017/$i >> myfile.txt
    echo $"\n" >> myfile.txt
done

sed '/^\s*$/d' myfile.txt >> award_amounts_files/nsf_awards_2017.txt
