
#!/bin/bash
find ${PWD} -name "*.[ch]" -o -name "*.cpp" > cscope.files
cscope -bR -i cscope.files
ctags -R
