"""PT: Seletor de regiao do sujeito. EN: Subject region picker."""

AJUDA = {
    'reference_image': (
        'Ligue aqui a MESMA imagem que vai para o Camera H3. Ela aparece no painel abaixo e você arrasta o '
        'retângulo em cima do sujeito. Sem imagem ligada o painel fica vazio, mas os quatro números continuam '
        'editáveis à mão.',
        'Connect the SAME image you feed to Camera H3. It shows in the panel below and you drag the rectangle over '
        'the subject. With no image connected the panel stays empty, but the four numbers remain editable by hand.'),
    'left': (
        'Borda esquerda do retângulo, em fração da largura do quadro. 0 é a borda esquerda da imagem, 1 é a direita. '
        'O painel escreve este valor quando você arrasta.',
        'Left edge of the rectangle, as a fraction of the frame width. 0 is the left edge of the image, 1 the right. '
        'The panel writes this value when you drag.'),
    'top': (
        'Borda superior do retângulo, em fração da altura do quadro. 0 é o topo da imagem, 1 é a base.',
        'Top edge of the rectangle, as a fraction of the frame height. 0 is the top of the image, 1 the bottom.'),
    'width': (
        'Largura do retângulo, em fração da largura do quadro. Somada a left nunca passa de 1.',
        'Width of the rectangle, as a fraction of the frame width. Added to left it never exceeds 1.'),
    'height': (
        'Altura do retângulo, em fração da altura do quadro. Somada a top nunca passa de 1.',
        'Height of the rectangle, as a fraction of the frame height. Added to top it never exceeds 1.'),
}


def ajuda(nome):
    pt, en = AJUDA[nome]
    return 'PT: ' + pt + '\nEN: ' + en


def _limita(valor, minimo, maximo):
    return max(minimo, min(maximo, float(valor)))


def formata_box(left, top, width, height):
    """PT: Monta a string no formato que o Camera H3 espera.
    EN: Builds the string in the format Camera H3 expects."""
    left = _limita(left, 0.0, 1.0)
    top = _limita(top, 0.0, 1.0)
    # A caixa nunca pode vazar do quadro: o prompt trata as quatro fracoes como do quadro
    # inteiro, entao left+width acima de 1 descreveria uma regiao que nao existe.
    width = _limita(width, 0.001, 1.0 - left)
    height = _limita(height, 0.001, 1.0 - top)
    return f'[L={left:.3f}, T={top:.3f}, W={width:.3f}, H={height:.3f}]'


class SubjectBoxPicker:
    DESCRIPTION = (
        'PT: Desenha a caixa do sujeito arrastando em cima da sua imagem e devolve a string pronta para o '
        'subject_box do Camera H3. Ele só descreve uma região do primeiro frame: não recorta, não faz zoom e não '
        'detecta nada sozinho.\n'
        'EN: Draw the subject box by dragging over your image and get the string ready for the subject_box input of '
        'Camera H3. It only describes a region of the first frame: it does not crop, zoom or detect anything by '
        'itself.')
    CATEGORY = 'bruxosdovfx/Camera H3'
    FUNCTION = 'run'
    RETURN_TYPES = ('STRING',)
    RETURN_NAMES = ('subject_box',)
    OUTPUT_TOOLTIPS = (
        'PT: A região no formato [L=..., T=..., W=..., H=...]. Ligue no subject_box do Camera H3.\n'
        'EN: The region as [L=..., T=..., W=..., H=...]. Wire it into the subject_box input of Camera H3.',)

    @classmethod
    def INPUT_TYPES(cls):
        fracao = lambda nome, padrao: ('FLOAT', {'default': padrao, 'min': 0.0, 'max': 1.0, 'step': 0.001,
                                                 'tooltip': ajuda(nome)})
        return {
            'required': {
                'left': fracao('left', 0.35),
                'top': fracao('top', 0.20),
                'width': fracao('width', 0.30),
                'height': fracao('height', 0.60),
            },
            'optional': {
                'reference_image': ('IMAGE', {'tooltip': ajuda('reference_image')}),
            },
        }

    def run(self, left, top, width, height, reference_image=None):
        return (formata_box(left, top, width, height),)


NODE_CLASS_MAPPINGS = {'BruxosH3SubjectBox': SubjectBoxPicker}
NODE_DISPLAY_NAME_MAPPINGS = {'BruxosH3SubjectBox': 'bruxosdovfx • H3 Subject Box'}
