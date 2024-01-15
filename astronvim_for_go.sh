# install required package
apt install neovim git clang python3 lua-language-server yarn golang -y
# clone AstroNvim 
git clone https://GitHub.com/AstroNvim/AstroNvim ~/.config/nvim
# Change font and bgcolor
# open nvim: auto start downloading; when ends press q
nvim
# install gopls
go install golang.org/x/tools/gopls@latest
# append this in ~/.config/nvim/init.lua:
echo -e "\nrequire('lspconfig').gopls.setup{\n\ton_attach = function()\n\tvim.keymap.set("n", "K", vim.lsp.buf.hover, {buffer=0})\n\tend,\n}" >> ~/.config/nvim/init.lua
# export go bin to global path
echo -e "\nexport PATH=$PATH:$HOME/go/bin" >> .bashrc
# restart terminal
exit


# for python type:-
# :LspInstall pyright
