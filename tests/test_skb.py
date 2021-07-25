import skb as skb
from skb import __version__
from skb.skb import KitBuilder

def test_version():
    assert __version__ == __version__

newKit = KitBuilder()
print(newKit)
