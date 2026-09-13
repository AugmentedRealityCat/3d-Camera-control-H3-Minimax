"""PT: Banner de carregamento. EN: Startup banner."""

LOGO = """\
                ##      --=   #
             #######    =-- ###
                ##    -----#####
                      =-=-- ####
                    --------*####
                    =--------####  ###
   #####       ##   ----===---####  ###
  #######    #### -----=------ ###   ###
   #####  ######  ---------==-- ###   ##
        #######    ---=====----
     ##########  -=      -=--  ----=---=--
   #########   ---=-----------------------
    ####%  ---=--===-----=--------------
       ----=--==-=---===-----------=+
    --------=--=-------=-----==++*####
        ----=--==-------=+**##########
                     #    #############
                     ##        ########
                  ########           ###
                     ##
                     ##
"""

def print_banner(node_count):
    """PT: Desenha a logo e o nome no console do ComfyUI, uma vez, na importacao.
    EN: Draws the logo and the name in the ComfyUI console once, at import time."""
    verde, roxo, reset = '\033[38;5;149m', '\033[38;5;141m', '\033[0m'
    linhas = LOGO.strip('\n').split('\n')
    for indice, linha in enumerate(linhas):
        # Metade de cima verde, metade de baixo roxa: as duas cores da marca.
        print((verde if indice < len(linhas) * 0.55 else roxo) + linha + reset)
    titulo = 'H3 Tools Bruxos do VFX'
    print(f"{roxo}{titulo}{reset}  {verde}{node_count} node{'s' if node_count != 1 else ''}{reset}\n")
