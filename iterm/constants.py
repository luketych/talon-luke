load_ls_script = "nvim ~/.talon/vim_scripts/ls.sh && chmod +x ~/.talon/vim_scripts/ls.sh && ~/.talon/vim_scripts/ls.sh | tee ~/.talon/tmp.log"

load_ls_call_script = "nvim ~/.talon/vim_scripts/ls-call.sh && chmod +x ~/.talon/vim_scripts/ls-call.sh && (printf '\\n\\n\\n\\n' && ~/.talon/vim_scripts/ls-call.sh ) | tee ~/.talon/tmp.log"