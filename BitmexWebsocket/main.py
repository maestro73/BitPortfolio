from bitmex_websocket import BitMEXWebsocket
import logging
from time import sleep


# Basic use of websocket.
def run():
    logger = setup_logger()

    # Instantiating the WS will make it connect. Be sure to add your api_key/api_secret.
    ws = BitMEXWebsocket(endpoint="wss://testnet.bitmex.com/realtime", symbol="XBTUSD",
                         api_key="wwvS30igJDo6Ksxa0h2EP1Eq", api_secret="-DOHRIUObpSQilqyr2y18YcTRi5NWFIV95du4i8rG4VveOBI")

    logger.info("Instrument data: {}".format(ws.get_instrument()))

    # Run forever
    while(ws.ws.sock.connected):
        logger.info("Ticker: %s" % ws.get_ticker())
        if ws.config['api_key']:
            logger.info("Funds: %s" % ws.funds())
        logger.info("Market Depth: %s" % ws.market_depth())
        logger.info("Recent Trades: %s\n\n" % ws.recent_trades())
        sleep(10)


def setup_logger():
    # Prints logger info to terminal
    logger = logging.getLogger()
    logger.setLevel(logging.INFO)  # Change this to DEBUG if you want a lot more info
    ch = logging.StreamHandler()
    # create formatter
    formatter = logging.Formatter("%(asctime)s - %(name)s - %(levelname)s - %(message)s")
    # add formatter to ch
    ch.setFormatter(formatter)
    logger.addHandler(ch)
    return logger


if __name__ == "__main__":
    run()
