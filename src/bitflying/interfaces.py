from zope.interface import (
    Attribute,
    Interface,
    )


class IBitFlyer(Interface):
    price = Attribute('レート取得')
    price = Attribute('レート取得')
    price = Attribute('レート取得')


class IBitFlyerAPIClient(Interface):
    pass


class IPrice(Interface):
    mid = Attribute('仲値')
    ask = Attribute('1BTC販売価格')
    bid = Attribute('1BTC買取価格')
