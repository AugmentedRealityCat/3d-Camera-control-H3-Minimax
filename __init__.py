from .experimental import NODE_CLASS_MAPPINGS, NODE_DISPLAY_NAME_MAPPINGS
from .banner import print_banner

# PT: conta so os nodes visiveis; os alias depreciados nao entram na contagem.
# EN: counts only the visible nodes; deprecated aliases are left out.
print_banner(len({c for c in NODE_CLASS_MAPPINGS.values() if not getattr(c, 'DEPRECATED', False)}))

WEB_DIRECTORY = './web'
__all__ = ['NODE_CLASS_MAPPINGS', 'NODE_DISPLAY_NAME_MAPPINGS', 'WEB_DIRECTORY']
