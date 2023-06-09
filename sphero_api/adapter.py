import asyncio
import threading
from typing import Coroutine

import bleak
from bleak.backends.device import BLEDevice


class BTAdapter:
    @classmethod
    def find_toys(cls, timeout: float = 5.0):
        return asyncio.run(bleak.BleakScanner.discover(timeout))

    def __init__(self, addr: BLEDevice) -> None:
        self.__event_loop = asyncio.new_event_loop()
        self.__interface = bleak.BleakClient(addr, timeout=5.0)
        self.__lock = threading.Lock()
        self.__thread = threading.Thread(target=self.__event_loop.run_forever)
        self.__thread.start()

    def __execute(self, coroutine: Coroutine):
        with self.__lock:
            return asyncio.run_coroutine_threadsafe(coroutine, self.__event_loop).result()

    def close(self, disconnect: bool = True) -> None:
        if disconnect:
            self.__execute(self.__interface.disconnect())
        with self.__lock:
            self.__event_loop.call_soon_threadsafe(self.__event_loop.stop)
            self.__thread.join()
        self.__event_loop.close()

    def set_callback(self, uuid, cb):
        self.__execute(self.__interface.start_notify(uuid, cb))

    def write(self, uuid, data):
        self.__execute(self.__interface.write_gatt_char(uuid, data, True))