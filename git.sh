
#  git config --global user.email "sjpearce@gmail.com"
#  git config --global user.name "pearcee"

comment = date +"%y.%m.%d.%T"
git status
git add --all .
git commit -m comment
git push -u origin master