set number

"搜索忽略大小写

set ignorecase

"搜索逐字符高亮

set hlsearch

set incsearch

set completeopt=longest,menu

"""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""

" CTags的设定  

"""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""

let Tlist_Sort_Type = "name"    " 按照名称排序  

let Tlist_Use_Right_Window = 1  " 在右侧显示窗口  

let Tlist_Compart_Format = 1    " 压缩方式  

let Tlist_Exist_OnlyWindow = 1  " 如果只有一个buffer，kill窗口也kill掉buffer  

let Tlist_File_Fold_Auto_Close = 0  " 不要关闭其他文件的tags  

let Tlist_Enable_Fold_Column = 0    " 不要显示折叠树  

autocmd FileType java set tags+=D:\tools\java\tags  

"autocmd FileType h,cpp,cc,c set tags+=D:\tools\cpp\tags  

"let Tlist_Show_One_File=1            "不同时显示多个文件的tag，只显示当前文件的

"设置tags  

set tags=tags;

set autochdir



""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""

"其他东东

"""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""

"默认打开Taglist 

let Tlist_Auto_Open=1 

"""""""""""""""""""""""""""""" 

" Tag list (ctags) 

"""""""""""""""""""""""""""""""" 

let Tlist_Ctags_Cmd = '/usr/bin/ctags' 

let Tlist_Show_One_File = 1 "不同时显示多个文件的tag，只显示当前文件的 

let Tlist_Exit_OnlyWindow = 1 "如果taglist窗口是最后一个窗口，则退出vim 

let Tlist_Use_Right_Window = 1 "在右侧窗口中显示taglist窗口

" minibufexpl插件的一般设置

let g:miniBufExplMapWindowNavVim = 1
let g:miniBufExplMapWindowNavArrows = 1
let g:miniBufExplMapCTabSwitchBufs = 1
let g:miniBufExplModSelTarget = 1

"set tags=/home/jason/workpsace/algorithm/v4l2/tags
if has("cscope")
            set cscopetag   " 使支持用 Ctrl+]  和 Ctrl+t 快捷键在代码间跳来跳去
            " check cscope for definition of a symbol before checking ctags:
            " set to 1 if you want the reverse search order.
             set csto=1

             " add any cscope database in current directory
             if filereadable("cscope.out")
                 cs add cscope.out
             " else add the database pointed to by environment variable
             elseif $CSCOPE_DB !=""
                 cs add $CSCOPE_DB
             endif

             " show msg when any other cscope db added
             set cscopeverbose

             nmap <C-_>s :cs find s <C-R>=expand("<cword>")<CR><CR>
             nmap <C-_>g :cs find g <C-R>=expand("<cword>")<CR><CR>
             nmap <C-_>c :cs find c <C-R>=expand("<cword>")<CR><CR>
             nmap <C-_>t :cs find t <C-R>=expand("<cword>")<CR><CR>
             nmap <C-_>e :cs find e <C-R>=expand("<cword>")<CR><CR>
             nmap <C-_>f :cs find f <C-R>=expand("<cfile>")<CR><CR>
             nmap <C-_>i :cs find i ^<C-R>=expand("<cfile>")<CR>$<CR>
             nmap <C-_>d :cs find d <C-R>=expand("<cword>")<CR><CR>
endif


" 按F8按钮，在窗口的左侧出现taglist的窗口,像vc的左侧的workpace
nnoremap <silent> <F8> :TlistToggle<CR><CR>
" :Tlist              调用TagList
let Tlist_Show_One_File=0                    " 只显示当前文件的tags
let Tlist_Exit_OnlyWindow=1                  " 如果Taglist窗口是最后一个窗口则退出Vim
let Tlist_Use_Right_Window=1                 " 在右侧窗口中显示
let Tlist_File_Fold_Auto_Close=1             " 自动折叠

set nocp
filetype plugin on

set completeopt=menu,menuone
let OmniCpp_MayCompleteDot=1 "打开  . 操作符
let OmniCpp_MayCompleteArrow=1  "打开 -> 操作符
let OmniCpp_MayCompleteScope=1  "打开 :: 操作符
let OmniCpp_NamespaceSearch=1   "打开命名空间
let OmniCpp_GlobalScopeSearch=1
let OmniCpp_DefaultNamespace=["std"]
let OmniCpp_ShowPrototypeInAbbr=1  "打开显示函数原型
let OmniCpp_SelectFirstItem = 2 "自动弹出时自动跳至第一个
"set autochdir
