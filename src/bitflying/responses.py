from enum import IntEnum


class BitFlyerEchoAPIError(IntEnum):
    processing = 1  # 処理中
    success = 0  # Echo処理成功
    no_account = -100  # アカウントが特定できない
    insufficient_funds = -101  # 残高不足
    invalid_mailaddr = -102  # メールアドレス不正
    no_shop = -103  # ショップが特定できない
    duplicate_external_transaction_id = -104  # external_transaction_id重複(ただし)
    invalid_tracking_id = -105  # tracking_idが不正で特定できない
    invalid_external_transaction_id = -106  # external_transaction_idが不正で特定できない
    not_specified = -107  # noqa tracking_idもexternal_transaction_idも指定されていない
    invalid_amount = -200  # amountが不正
    invalid_auto_charge = -201  # auto_chargeが不正
    auto_charge_too_small = -202  # auto_chargeがamountより小さい
    refunded = -800  # ユーザがアカウントを作成しなかったので払い戻し済み
    error = -999  # そのほかエラー
