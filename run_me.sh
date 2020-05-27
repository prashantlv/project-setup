    #!/bin/bash
    
    function create(){
       cd 
       python ./pro_init.py $1
       cd path/to/your/projects/directory/$1
       touch Readme.md
       git init
       git add .
       git commit -m "first commit"
       git remote add origin   		https://github.com/<your_git_username>/$1.git
       git push -u origin master
       code . #opens up new directory in vs code
    }
