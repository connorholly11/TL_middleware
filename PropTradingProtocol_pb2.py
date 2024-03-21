# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: PropTradingProtocol_new.proto
# Protobuf Python Version: 4.25.3
"""Generated protocol buffer code."""
from google.protobuf import descriptor as _descriptor
from google.protobuf import descriptor_pool as _descriptor_pool
from google.protobuf import symbol_database as _symbol_database
from google.protobuf.internal import builder as _builder
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()




DESCRIPTOR = _descriptor_pool.Default().AddSerializedFile(b'\n\x1dPropTradingProtocol_new.proto\x12\x13PropTradingProtocol\"\xbe\x04\n\x10\x43lientRequestMsg\x12\x36\n\x08LoginReq\x18\x01 \x01(\x0b\x32$.PropTradingProtocol.LoginRequestMsg\x12*\n\x04Ping\x18\x02 \x01(\x0b\x32\x1c.PropTradingProtocol.PingMsg\x12\x30\n\x07InfoReq\x18\x03 \x01(\x0b\x32\x1f.PropTradingProtocol.InfoReqMsg\x12\x38\n\x0b\x43ontractReq\x18\x04 \x01(\x0b\x32#.PropTradingProtocol.ContractReqMsg\x12\x34\n\x08\x44\x61ilyPls\x18\x05 \x03(\x0b\x32\".PropTradingProtocol.DailyPlReqMsg\x12,\n\x05Order\x18\x06 \x03(\x0b\x32\x1d.PropTradingProtocol.OrderMsg\x12/\n\x06LogMsg\x18\x07 \x01(\x0b\x32\x1f.PropTradingProtocol.LogInfoMsg\x12=\n\x0cSymbolLookup\x18\x08 \x01(\x0b\x32\'.PropTradingProtocol.SymbolLookupReqMsg\x12<\n\rCancelFlatReq\x18\t \x01(\x0b\x32%.PropTradingProtocol.CancelFlatReqMsg\x12H\n\x13\x41\x63\x63ountSubscribeReq\x18\n \x01(\x0b\x32+.PropTradingProtocol.AccountSubscribeReqMsg\"\xc6\x07\n\x11ServerResponseMsg\x12\x37\n\x08LoginMsg\x18\x01 \x01(\x0b\x32%.PropTradingProtocol.LoginResponseMsg\x12*\n\x04Pong\x18\x02 \x01(\x0b\x32\x1c.PropTradingProtocol.PongMsg\x12\x31\n\x07InfoMsg\x18\x03 \x01(\x0b\x32 .PropTradingProtocol.InfoRespMsg\x12\x34\n\x0b\x42\x61lanceInfo\x18\x04 \x03(\x0b\x32\x1f.PropTradingProtocol.BalanceMsg\x12\x39\n\x0b\x43ontractMsg\x18\x05 \x01(\x0b\x32$.PropTradingProtocol.ContractRespMsg\x12\x35\n\x08\x44\x61ilyPls\x18\x06 \x03(\x0b\x32#.PropTradingProtocol.DailyPlRespMsg\x12\x34\n\tOrderInfo\x18\x07 \x03(\x0b\x32!.PropTradingProtocol.OrderInfoMsg\x12\x34\n\tLoggedOff\x18\x08 \x01(\x0b\x32!.PropTradingProtocol.LoggedOffMsg\x12/\n\x06LogMsg\x18\t \x01(\x0b\x32\x1f.PropTradingProtocol.LogInfoMsg\x12>\n\x0cSymbolLookup\x18\n \x01(\x0b\x32(.PropTradingProtocol.SymbolLookupRespMsg\x12:\n\x0cPositionInfo\x18\x0b \x03(\x0b\x32$.PropTradingProtocol.PositionInfoMsg\x12=\n\rCancelFlatMsg\x18\x0c \x01(\x0b\x32&.PropTradingProtocol.CancelFlatRespMsg\x12\x38\n\x0b\x42racketInfo\x18\r \x03(\x0b\x32#.PropTradingProtocol.BracketInfoMsg\x12H\n\x13\x42racketInsertReport\x18\x0e \x01(\x0b\x32+.PropTradingProtocol.BracketInsertReportMsg\x12J\n\x14\x41\x63\x63ountSubscribeResp\x18\x0f \x01(\x0b\x32,.PropTradingProtocol.AccountSubscribeRespMsg\x12I\n\x14\x41\x63\x63ountStatusUpdates\x18\x10 \x03(\x0b\x32+.PropTradingProtocol.AccountStatusUpdateMsg\"S\n\x0fLoginRequestMsg\x12\r\n\x05Token\x18\x01 \x01(\t\x12\x0f\n\x07OtpCode\x18\x02 \x01(\t\x12 \n\x18IsManualAccountSubscribe\x18\x03 \x01(\x08\"3\n\x10LoginResponseMsg\x12\x0f\n\x07success\x18\x01 \x01(\x08\x12\x0e\n\x06reason\x18\x02 \x01(\t\"\x1e\n\x0cLoggedOffMsg\x12\x0e\n\x06Reason\x18\x01 \x01(\t\"\x1c\n\x07PingMsg\x12\x11\n\tConnected\x18\x01 \x01(\x08\"\x1c\n\x07PongMsg\x12\x11\n\tConnected\x18\x01 \x01(\x08\"\x81\x01\n\x0e\x43ontractReqMsg\x12\x12\n\nFeedSymbol\x18\x01 \x01(\t\x12\x39\n\x08\x43\x61tegory\x18\x02 \x01(\x0e\x32\'.PropTradingProtocol.SymbolCategoryEnum\x12\x12\n\nContractId\x18\x03 \x01(\x12\x12\x0c\n\x04Isin\x18\x04 \x01(\t\"\xb0\x01\n\x0f\x43ontractRespMsg\x12\x12\n\nFeedSymbol\x18\x01 \x01(\t\x12\x39\n\x08\x43\x61tegory\x18\x02 \x01(\x0e\x32\'.PropTradingProtocol.SymbolCategoryEnum\x12\x12\n\nContractId\x18\x03 \x01(\x12\x12:\n\x0c\x63ontractInfo\x18\x04 \x01(\x0b\x32$.PropTradingProtocol.ContractInfoMsg\"\xf2\x01\n\x0f\x43ontractInfoMsg\x12\x14\n\x0c\x43ontractName\x18\x01 \x01(\t\x12\x0e\n\x06Symbol\x18\x02 \x01(\t\x12\x10\n\x08\x45xchange\x18\x03 \x01(\t\x12\x13\n\x0b\x44\x65scription\x18\x04 \x01(\t\x12\x10\n\x08TickSize\x18\x05 \x01(\x01\x12\x11\n\tTickValue\x18\x06 \x01(\x01\x12\x0e\n\x06Margin\x18\x07 \x01(\x12\x12\x17\n\x0fOrderCommission\x18\x08 \x01(\x01\x12\x1f\n\x17IsCommissionPerContract\x18\t \x01(\x08\x12\x0f\n\x07IsStock\x18\n \x01(\x08\x12\x12\n\nFeedSymbol\x18\x0b \x01(\t\"I\n\rDailyPlReqMsg\x12\x12\n\nContractId\x18\x01 \x01(\x12\x12\x11\n\tAccNumber\x18\x02 \x01(\x12\x12\x11\n\tRequestId\x18\x03 \x01(\x12\"\x91\x01\n\x0e\x44\x61ilyPlRespMsg\x12\x12\n\nContractId\x18\x01 \x01(\x12\x12\x11\n\tAccNumber\x18\x02 \x01(\x12\x12\x0f\n\x07\x44\x61ilyPl\x18\x03 \x01(\x01\x12\x12\n\nFeedSymbol\x18\x04 \x01(\t\x12\x11\n\tRequestId\x18\x05 \x01(\x12\x12\x12\n\nDailyNetPl\x18\x06 \x01(\x01\x12\x0c\n\x04Isin\x18\x07 \x01(\t\"\xdd\x01\n\nInfoReqMsg\x12/\n\x04Mode\x18\x01 \x01(\x0e\x32!.PropTradingProtocol.InfoModeEnum\x12\x11\n\tRequestId\x18\x02 \x01(\x12\x12G\n\x17\x41\x63\x63ountListFilterStatus\x18\x03 \x01(\x0e\x32&.PropTradingProtocol.AccountStatusEnum\x12\x10\n\x08\x41\x63\x63ounts\x18\x04 \x03(\x12\x12\x30\n\x05Modes\x18\x05 \x03(\x0e\x32!.PropTradingProtocol.InfoModeEnum\"\x88\x02\n\x0bInfoRespMsg\x12:\n\x0b\x41\x63\x63ountList\x18\x01 \x03(\x0b\x32%.PropTradingProtocol.AccountHeaderMsg\x12\x34\n\tOrderList\x18\x02 \x03(\x0b\x32!.PropTradingProtocol.OrderInfoMsg\x12\x11\n\tRequestId\x18\x03 \x01(\x12\x12:\n\x0cPositionList\x18\x04 \x03(\x0b\x32$.PropTradingProtocol.PositionInfoMsg\x12\x38\n\x0b\x42racketList\x18\x05 \x03(\x0b\x32#.PropTradingProtocol.BracketInfoMsg\"\xe0\x01\n\x10\x41\x63\x63ountHeaderMsg\x12\x15\n\raccountNumber\x18\x01 \x01(\x12\x12\x15\n\raccountHeader\x18\x02 \x01(\t\x12\x1a\n\x12\x61\x63\x63ountDescription\x18\x03 \x01(\t\x12\x30\n\x07\x42\x61lance\x18\x04 \x01(\x0b\x32\x1f.PropTradingProtocol.BalanceMsg\x12\x18\n\x10IsTradingEnabled\x18\x05 \x01(\x08\x12\x36\n\x06Status\x18\x06 \x01(\x0e\x32&.PropTradingProtocol.AccountStatusEnum\"=\n\x16\x41\x63\x63ountSubscribeReqMsg\x12\x11\n\tRequestId\x18\x01 \x01(\x12\x12\x10\n\x08\x41\x63\x63ounts\x18\x02 \x03(\x12\"M\n\x17\x41\x63\x63ountSubscribeRespMsg\x12\x11\n\tRequestId\x18\x01 \x01(\x12\x12\x0f\n\x07Success\x18\x02 \x01(\x08\x12\x0e\n\x06Reason\x18\x03 \x01(\t\"\xb4\x02\n\x08OrderMsg\x12\x38\n\x0bOrderInsert\x18\x01 \x01(\x0b\x32#.PropTradingProtocol.OrderInsertMsg\x12\x38\n\x0bOrderRemove\x18\x02 \x01(\x0b\x32#.PropTradingProtocol.OrderRemoveMsg\x12\x38\n\x0bOrderModify\x18\x03 \x01(\x0b\x32#.PropTradingProtocol.OrderModifyMsg\x12<\n\rBracketInsert\x18\x04 \x01(\x0b\x32%.PropTradingProtocol.BracketInsertMsg\x12<\n\rBracketModify\x18\x05 \x01(\x0b\x32%.PropTradingProtocol.BracketModifyMsg\"\xfc\x01\n\x0eOrderInsertMsg\x12\x12\n\nContractId\x18\x01 \x01(\x12\x12\x13\n\x0bSeqClientId\x18\x02 \x01(\x05\x12\x10\n\x08Quantity\x18\x03 \x01(\x05\x12\r\n\x05Price\x18\x04 \x01(\x01\x12\x35\n\tOrderType\x18\x05 \x01(\x0e\x32\".PropTradingProtocol.OrderTypeEnum\x12\x11\n\tAccNumber\x18\x06 \x01(\x12\x12\x12\n\nLimitPrice\x18\x07 \x01(\x01\x12\x42\n\x0f\x42racketStrategy\x18\x08 \x01(\x0b\x32).PropTradingProtocol.BracketStrategyParam\"\xb7\x01\n\x0eOrderModifyMsg\x12\x12\n\nContractId\x18\x01 \x01(\x12\x12\x13\n\x0bOrgServerId\x18\x02 \x01(\x12\x12\x16\n\x0eNewSeqClientId\x18\x03 \x01(\x05\x12\x10\n\x08Quantity\x18\x04 \x01(\x05\x12\x1c\n\x14Price_OrderModifyMsg\x18\x05 \x01(\x01\x12\x11\n\tAccNumber\x18\x06 \x01(\x12\x12!\n\x19LimitPrice_OrderModifyMsg\x18\x07 \x01(\x01\"8\n\x0eOrderRemoveMsg\x12\x13\n\x0bOrgServerId\x18\x01 \x01(\x12\x12\x11\n\tAccNumber\x18\x02 \x01(\x12\"\x81\x04\n\x14\x42racketStrategyParam\x12@\n\x04Type\x18\x01 \x01(\x0e\x32\x32.PropTradingProtocol.BracketStrategyParam.TypeEnum\x12\x30\n\x05Stops\x18\x02 \x03(\x0b\x32!.PropTradingProtocol.BracketParam\x12\x32\n\x07Targets\x18\x03 \x03(\x0b\x32!.PropTradingProtocol.BracketParam\x12T\n\x0cTrailingMode\x18\x04 \x01(\x0e\x32>.PropTradingProtocol.BracketStrategyParam.StopTrailingModeEnum\x12\x15\n\rTrailingTicks\x18\x05 \x01(\x05\x12\x1e\n\x16TrailingMinOffsetTicks\x18\x06 \x01(\x05\"u\n\x08TypeEnum\x12\x13\n\x0fSTOP_AND_TARGET\x10\x00\x12\x1a\n\x16STOP_AND_TARGET_STATIC\x10\x01\x12\x08\n\x04STOP\x10\x02\x12\x0f\n\x0bSTOP_STATIC\x10\x03\x12\n\n\x06TARGET\x10\x04\x12\x11\n\rTARGET_STATIC\x10\x05\"=\n\x14StopTrailingModeEnum\x12\x08\n\x04None\x10\x00\x12\r\n\tBreakeven\x10\x01\x12\x0c\n\x08Trailing\x10\x02\"\xca\x01\n\x0c\x42racketParam\x12\x10\n\x08Quantity\x18\x01 \x01(\x05\x12\x42\n\tPriceMode\x18\x02 \x01(\x0e\x32/.PropTradingProtocol.BracketParam.PriceModeEnum\x12\x13\n\x0bTicksOffset\x18\x03 \x01(\x05\x12\x1a\n\x12Price_BracketParam\x18\x04 \x01(\x01\"3\n\rPriceModeEnum\x12\t\n\x05Ticks\x10\x00\x12\x17\n\x13Price_PriceModeEnum\x10\x01\"\x93\x01\n\x10\x42racketInsertMsg\x12\x11\n\tRequestId\x18\x01 \x01(\x12\x12\x15\n\rParentOrderId\x18\x02 \x01(\x12\x12\x42\n\x0f\x42racketStrategy\x18\x03 \x01(\x0b\x32).PropTradingProtocol.BracketStrategyParam\x12\x11\n\tAccNumber\x18\x04 \x01(\x12\"\x9a\x01\n\x10\x42racketModifyMsg\x12\x15\n\rParentOrderId\x18\x01 \x01(\x12\x12\x11\n\tBracketId\x18\x02 \x01(\x12\x12\x37\n\x0c\x42racketParam\x18\x03 \x01(\x0b\x32!.PropTradingProtocol.BracketParam\x12\x10\n\x08\x43lientId\x18\x04 \x01(\x05\x12\x11\n\tAccNumber\x18\x05 \x01(\x12\"\xc9\x05\n\x0cOrderInfoMsg\x12\x12\n\nContractId\x18\x01 \x01(\x12\x12\x13\n\x0bOrgServerId\x18\x02 \x01(\x12\x12\x13\n\x0bOrgClientId\x18\x03 \x01(\x05\x12\x13\n\x0bSeqServerId\x18\x04 \x01(\x03\x12\x13\n\x0bSeqClientId\x18\x05 \x01(\x05\x12\x12\n\nOrderPrice\x18\x06 \x01(\x01\x12\x17\n\x0fOrderLimitPrice\x18\x07 \x01(\x01\x12\x12\n\nPendingQty\x18\x08 \x01(\x05\x12\x11\n\tFilledQty\x18\t \x01(\x05\x12\x35\n\tOrderType\x18\n \x01(\x0e\x32\".PropTradingProtocol.OrderTypeEnum\x12\x44\n\nOrderState\x18\x0b \x01(\x0e\x32\x30.PropTradingProtocol.OrderInfoMsg.OrderStateEnum\x12\x10\n\x08\x41vgPrice\x18\x0c \x01(\x01\x12@\n\x08SnapType\x18\r \x01(\x0e\x32..PropTradingProtocol.OrderInfoMsg.SnapTypeEnum\x12\x11\n\tAccNumber\x18\x0e \x01(\x12\x12\x0e\n\x06Reason\x18\x0f \x01(\t\x12\x12\n\nFeedSymbol\x18\x10 \x01(\t\x12\x0c\n\x04Isin\x18\x11 \x01(\t\x12\x18\n\x10OcoLinkedGroupId\x18\x12 \x01(\x12\x12\x19\n\x11OcoLinkedOrderIds\x18\x13 \x03(\x12\x12\x18\n\x10OcoParentOrderId\x18\x14 \x01(\x12\"I\n\x0eOrderStateEnum\x12\r\n\tSubmitted\x10\x00\x12\x0c\n\x08\x43\x61nceled\x10\x01\x12\t\n\x05\x45rror\x10\x02\x12\x0f\n\x0b\x45rrorModify\x10\x03\"M\n\x0cSnapTypeEnum\x12\x12\n\x0e\x42lank_choice_0\x10\x00\x12\x0e\n\nHistorical\x10\x01\x12\x0c\n\x08RealTime\x10\x02\x12\x0b\n\x07HistPos\x10\x03\"\xc8\x04\n\x0e\x42racketInfoMsg\x12\x12\n\nContractId\x18\x01 \x01(\x12\x12\x15\n\rParentOrderId\x18\x02 \x01(\x12\x12\x12\n\nOcoGroupId\x18\x03 \x01(\x12\x12\x11\n\tBracketId\x18\x04 \x01(\x12\x12\x13\n\x0bSeqClientId\x18\x05 \x01(\x05\x12\r\n\x05Price\x18\x06 \x01(\x01\x12\r\n\x05Ticks\x18\x07 \x01(\x11\x12\x17\n\x0f\x43\x61lculatedPrice\x18\x08 \x01(\x01\x12\x10\n\x08TotalQty\x18\t \x01(\x05\x12\x13\n\x0bReleasedQty\x18\n \x01(\x05\x12\x10\n\x08IsTarget\x18\x0b \x01(\x08\x12J\n\x0c\x42racketState\x18\x0c \x01(\x0e\x32\x34.PropTradingProtocol.BracketInfoMsg.BracketStateEnum\x12\x42\n\x08SnapType\x18\r \x01(\x0e\x32\x30.PropTradingProtocol.BracketInfoMsg.SnapTypeEnum\x12\x11\n\tAccNumber\x18\x0e \x01(\x12\x12\x0e\n\x06Reason\x18\x0f \x01(\t\x12\x12\n\nFeedSymbol\x18\x10 \x01(\t\x12\x0c\n\x04Isin\x18\x11 \x01(\t\"H\n\x10\x42racketStateEnum\x12\x0b\n\x07Waiting\x10\x00\x12\r\n\tSubmitted\x10\x01\x12\r\n\tCancelled\x10\x02\x12\t\n\x05\x45rror\x10\x03\"@\n\x0cSnapTypeEnum\x12\x12\n\x0e\x42lank_choice_1\x10\x00\x12\x0e\n\nHistorical\x10\x01\x12\x0c\n\x08RealTime\x10\x02\",\n\nLogInfoMsg\x12\x0b\n\x03Msg\x18\x01 \x01(\t\x12\x11\n\tAccNumber\x18\x02 \x01(\x12\"\x94\x03\n\x0fPositionInfoMsg\x12\x12\n\nContractId\x18\x01 \x01(\x12\x12\x14\n\x0cOpenQuantity\x18\x02 \x01(\x12\x12\x11\n\tOpenPrice\x18\x03 \x01(\x01\x12\x12\n\nMarginUsed\x18\x04 \x01(\x01\x12\x13\n\x0b\x44\x61ilyBought\x18\x05 \x01(\x12\x12\x11\n\tDailySold\x18\x06 \x01(\x12\x12\x0f\n\x07\x44\x61ilyPl\x18\x07 \x01(\x01\x12\x11\n\tHasOpenPl\x18\x08 \x01(\x08\x12\x0e\n\x06OpenPl\x18\t \x01(\x01\x12\x18\n\x10\x44\x61ilyCommissions\x18\n \x01(\x01\x12\x43\n\x08SnapType\x18\x0b \x01(\x0e\x32\x31.PropTradingProtocol.PositionInfoMsg.SnapTypeEnum\x12\x11\n\tAccNumber\x18\x0c \x01(\x12\x12\x12\n\nFeedSymbol\x18\r \x01(\t\x12\x0c\n\x04Isin\x18\x0e \x01(\t\"@\n\x0cSnapTypeEnum\x12\x12\n\x0e\x42lank_choice_2\x10\x00\x12\x0e\n\nHistorical\x10\x01\x12\x0c\n\x08RealTime\x10\x02\"\xaa\x01\n\nBalanceMsg\x12\x0f\n\x07\x42\x61lance\x18\x01 \x01(\x01\x12\x11\n\tAccNumber\x18\x02 \x01(\x12\x12\x13\n\x0b\x44\x65scription\x18\x03 \x01(\t\x12\x12\n\nMarginUsed\x18\x04 \x01(\x01\x12\x1b\n\x13StopDrawdownOverall\x18\x05 \x01(\x01\x12\x1c\n\x14StopDrawdownIntraday\x18\x06 \x01(\x01\x12\x14\n\x0cProfitTarget\x18\x07 \x01(\x01\"7\n\x12SymbolLookupReqMsg\x12\x11\n\tRequestId\x18\x01 \x01(\x12\x12\x0e\n\x06\x46ilter\x18\x02 \x01(\t\"`\n\x13SymbolLookupRespMsg\x12\x11\n\tRequestId\x18\x01 \x01(\x12\x12\x36\n\x07Symbols\x18\x02 \x03(\x0b\x32%.PropTradingProtocol.SymbolLookupInfo\"t\n\x10SymbolLookupInfo\x12\x0e\n\x06Symbol\x18\x01 \x01(\t\x12\x13\n\x0b\x44\x65scription\x18\x02 \x01(\t\x12\x10\n\x08\x45xchange\x18\x03 \x01(\t\x12\x10\n\x08TickSize\x18\x04 \x01(\x01\x12\x17\n\x0fOrderCommission\x18\x05 \x01(\x01\"\xc4\x01\n\x10\x43\x61ncelFlatReqMsg\x12\x11\n\tRequestId\x18\x01 \x01(\x12\x12\x11\n\tAccNumber\x18\x02 \x01(\x12\x12\x13\n\x0b\x43ontractsId\x18\x03 \x03(\x12\x12@\n\x06\x41\x63tion\x18\x04 \x01(\x0e\x32\x30.PropTradingProtocol.CancelFlatReqMsg.ActionEnum\"3\n\nActionEnum\x12\x08\n\x04\x46LAT\x10\x00\x12\n\n\x06\x43\x41NCEL\x10\x01\x12\x0f\n\x0b\x46LAT_CANCEL\x10\x02\"u\n\x11\x43\x61ncelFlatRespMsg\x12\x11\n\tRequestId\x18\x01 \x01(\x12\x12\x11\n\tAccNumber\x18\x02 \x01(\x12\x12:\n\x06\x45rrors\x18\x03 \x03(\x0b\x32*.PropTradingProtocol.CancelFlatErrorDetail\":\n\x15\x43\x61ncelFlatErrorDetail\x12\x12\n\nContractId\x18\x01 \x01(\x12\x12\r\n\x05\x45rror\x18\x02 \x01(\t\"L\n\x16\x42racketInsertReportMsg\x12\x11\n\tRequestId\x18\x01 \x01(\x12\x12\x0f\n\x07Success\x18\x02 \x01(\x08\x12\x0e\n\x06Reason\x18\x03 \x01(\t\"\xd7\x01\n\x16\x41\x63\x63ountStatusUpdateMsg\x12\x11\n\tAccountId\x18\x01 \x01(\x12\x12\x46\n\x06\x41\x63tion\x18\x02 \x01(\x0e\x32\x36.PropTradingProtocol.AccountStatusUpdateMsg.ActionEnum\x12\x33\n\x04Info\x18\x03 \x01(\x0b\x32%.PropTradingProtocol.AccountHeaderMsg\"-\n\nActionEnum\x12\x07\n\x03\x41\x44\x44\x10\x00\x12\n\n\x06UPDATE\x10\x01\x12\n\n\x06REMOVE\x10\x02*a\n\x12SymbolCategoryEnum\x12\x12\n\x0e\x42lank_choice_2\x10\x00\x12\n\n\x06\x46uture\x10\x01\x12\t\n\x05\x46orex\x10\x02\x12\t\n\x05Index\x10\x03\x12\n\n\x06Option\x10\x04\x12\t\n\x05Stock\x10\x05*M\n\x0cInfoModeEnum\x12\x12\n\x0e\x42lank_choice_4\x10\x00\x12\x0b\n\x07\x41\x63\x63ount\x10\x01\x12\r\n\tOrdAndPos\x10\x02\x12\r\n\tPositions\x10\x03*j\n\x11\x41\x63\x63ountStatusEnum\x12\x0f\n\x0bINITIALIZED\x10\x00\x12\x10\n\x03\x41LL\x10\xff\xff\xff\xff\xff\xff\xff\xff\xff\x01\x12\x0b\n\x07\x45NABLED\x10\x01\x12\x0b\n\x07SUCCESS\x10\x02\x12\n\n\x06\x46\x41ILED\x10\x04\x12\x0c\n\x08\x44ISABLED\x10\x08*?\n\rOrderTypeEnum\x12\n\n\x06Market\x10\x00\x12\t\n\x05Limit\x10\x01\x12\x08\n\x04Stop\x10\x02\x12\r\n\tStopLimit\x10\x03*=\n\x0fOrderExpireEnum\x12\x12\n\x0e\x62lank_choice_5\x10\x00\x12\t\n\x05Never\x10\x01\x12\x0b\n\x07TillDay\x10\x02\x62\x06proto3')

_globals = globals()
_builder.BuildMessageAndEnumDescriptors(DESCRIPTOR, _globals)
_builder.BuildTopDescriptorsAndMessages(DESCRIPTOR, 'PropTradingProtocol_new_pb2', _globals)
if _descriptor._USE_C_DESCRIPTORS == False:
  DESCRIPTOR._options = None
  _globals['_SYMBOLCATEGORYENUM']._serialized_start=8183
  _globals['_SYMBOLCATEGORYENUM']._serialized_end=8280
  _globals['_INFOMODEENUM']._serialized_start=8282
  _globals['_INFOMODEENUM']._serialized_end=8359
  _globals['_ACCOUNTSTATUSENUM']._serialized_start=8361
  _globals['_ACCOUNTSTATUSENUM']._serialized_end=8467
  _globals['_ORDERTYPEENUM']._serialized_start=8469
  _globals['_ORDERTYPEENUM']._serialized_end=8532
  _globals['_ORDEREXPIREENUM']._serialized_start=8534
  _globals['_ORDEREXPIREENUM']._serialized_end=8595
  _globals['_CLIENTREQUESTMSG']._serialized_start=55
  _globals['_CLIENTREQUESTMSG']._serialized_end=629
  _globals['_SERVERRESPONSEMSG']._serialized_start=632
  _globals['_SERVERRESPONSEMSG']._serialized_end=1598
  _globals['_LOGINREQUESTMSG']._serialized_start=1600
  _globals['_LOGINREQUESTMSG']._serialized_end=1683
  _globals['_LOGINRESPONSEMSG']._serialized_start=1685
  _globals['_LOGINRESPONSEMSG']._serialized_end=1736
  _globals['_LOGGEDOFFMSG']._serialized_start=1738
  _globals['_LOGGEDOFFMSG']._serialized_end=1768
  _globals['_PINGMSG']._serialized_start=1770
  _globals['_PINGMSG']._serialized_end=1798
  _globals['_PONGMSG']._serialized_start=1800
  _globals['_PONGMSG']._serialized_end=1828
  _globals['_CONTRACTREQMSG']._serialized_start=1831
  _globals['_CONTRACTREQMSG']._serialized_end=1960
  _globals['_CONTRACTRESPMSG']._serialized_start=1963
  _globals['_CONTRACTRESPMSG']._serialized_end=2139
  _globals['_CONTRACTINFOMSG']._serialized_start=2142
  _globals['_CONTRACTINFOMSG']._serialized_end=2384
  _globals['_DAILYPLREQMSG']._serialized_start=2386
  _globals['_DAILYPLREQMSG']._serialized_end=2459
  _globals['_DAILYPLRESPMSG']._serialized_start=2462
  _globals['_DAILYPLRESPMSG']._serialized_end=2607
  _globals['_INFOREQMSG']._serialized_start=2610
  _globals['_INFOREQMSG']._serialized_end=2831
  _globals['_INFORESPMSG']._serialized_start=2834
  _globals['_INFORESPMSG']._serialized_end=3098
  _globals['_ACCOUNTHEADERMSG']._serialized_start=3101
  _globals['_ACCOUNTHEADERMSG']._serialized_end=3325
  _globals['_ACCOUNTSUBSCRIBEREQMSG']._serialized_start=3327
  _globals['_ACCOUNTSUBSCRIBEREQMSG']._serialized_end=3388
  _globals['_ACCOUNTSUBSCRIBERESPMSG']._serialized_start=3390
  _globals['_ACCOUNTSUBSCRIBERESPMSG']._serialized_end=3467
  _globals['_ORDERMSG']._serialized_start=3470
  _globals['_ORDERMSG']._serialized_end=3778
  _globals['_ORDERINSERTMSG']._serialized_start=3781
  _globals['_ORDERINSERTMSG']._serialized_end=4033
  _globals['_ORDERMODIFYMSG']._serialized_start=4036
  _globals['_ORDERMODIFYMSG']._serialized_end=4219
  _globals['_ORDERREMOVEMSG']._serialized_start=4221
  _globals['_ORDERREMOVEMSG']._serialized_end=4277
  _globals['_BRACKETSTRATEGYPARAM']._serialized_start=4280
  _globals['_BRACKETSTRATEGYPARAM']._serialized_end=4793
  _globals['_BRACKETSTRATEGYPARAM_TYPEENUM']._serialized_start=4613
  _globals['_BRACKETSTRATEGYPARAM_TYPEENUM']._serialized_end=4730
  _globals['_BRACKETSTRATEGYPARAM_STOPTRAILINGMODEENUM']._serialized_start=4732
  _globals['_BRACKETSTRATEGYPARAM_STOPTRAILINGMODEENUM']._serialized_end=4793
  _globals['_BRACKETPARAM']._serialized_start=4796
  _globals['_BRACKETPARAM']._serialized_end=4998
  _globals['_BRACKETPARAM_PRICEMODEENUM']._serialized_start=4947
  _globals['_BRACKETPARAM_PRICEMODEENUM']._serialized_end=4998
  _globals['_BRACKETINSERTMSG']._serialized_start=5001
  _globals['_BRACKETINSERTMSG']._serialized_end=5148
  _globals['_BRACKETMODIFYMSG']._serialized_start=5151
  _globals['_BRACKETMODIFYMSG']._serialized_end=5305
  _globals['_ORDERINFOMSG']._serialized_start=5308
  _globals['_ORDERINFOMSG']._serialized_end=6021
  _globals['_ORDERINFOMSG_ORDERSTATEENUM']._serialized_start=5869
  _globals['_ORDERINFOMSG_ORDERSTATEENUM']._serialized_end=5942
  _globals['_ORDERINFOMSG_SNAPTYPEENUM']._serialized_start=5944
  _globals['_ORDERINFOMSG_SNAPTYPEENUM']._serialized_end=6021
  _globals['_BRACKETINFOMSG']._serialized_start=6024
  _globals['_BRACKETINFOMSG']._serialized_end=6608
  _globals['_BRACKETINFOMSG_BRACKETSTATEENUM']._serialized_start=6470
  _globals['_BRACKETINFOMSG_BRACKETSTATEENUM']._serialized_end=6542
  _globals['_BRACKETINFOMSG_SNAPTYPEENUM']._serialized_start=6544
  _globals['_BRACKETINFOMSG_SNAPTYPEENUM']._serialized_end=6608
  _globals['_LOGINFOMSG']._serialized_start=6610
  _globals['_LOGINFOMSG']._serialized_end=6654
  _globals['_POSITIONINFOMSG']._serialized_start=6657
  _globals['_POSITIONINFOMSG']._serialized_end=7061
  _globals['_POSITIONINFOMSG_SNAPTYPEENUM']._serialized_start=6997
  _globals['_POSITIONINFOMSG_SNAPTYPEENUM']._serialized_end=7061
  _globals['_BALANCEMSG']._serialized_start=7064
  _globals['_BALANCEMSG']._serialized_end=7234
  _globals['_SYMBOLLOOKUPREQMSG']._serialized_start=7236
  _globals['_SYMBOLLOOKUPREQMSG']._serialized_end=7291
  _globals['_SYMBOLLOOKUPRESPMSG']._serialized_start=7293
  _globals['_SYMBOLLOOKUPRESPMSG']._serialized_end=7389
  _globals['_SYMBOLLOOKUPINFO']._serialized_start=7391
  _globals['_SYMBOLLOOKUPINFO']._serialized_end=7507
  _globals['_CANCELFLATREQMSG']._serialized_start=7510
  _globals['_CANCELFLATREQMSG']._serialized_end=7706
  _globals['_CANCELFLATREQMSG_ACTIONENUM']._serialized_start=7655
  _globals['_CANCELFLATREQMSG_ACTIONENUM']._serialized_end=7706
  _globals['_CANCELFLATRESPMSG']._serialized_start=7708
  _globals['_CANCELFLATRESPMSG']._serialized_end=7825
  _globals['_CANCELFLATERRORDETAIL']._serialized_start=7827
  _globals['_CANCELFLATERRORDETAIL']._serialized_end=7885
  _globals['_BRACKETINSERTREPORTMSG']._serialized_start=7887
  _globals['_BRACKETINSERTREPORTMSG']._serialized_end=7963
  _globals['_ACCOUNTSTATUSUPDATEMSG']._serialized_start=7966
  _globals['_ACCOUNTSTATUSUPDATEMSG']._serialized_end=8181
  _globals['_ACCOUNTSTATUSUPDATEMSG_ACTIONENUM']._serialized_start=8136
  _globals['_ACCOUNTSTATUSUPDATEMSG_ACTIONENUM']._serialized_end=8181
# @@protoc_insertion_point(module_scope)
