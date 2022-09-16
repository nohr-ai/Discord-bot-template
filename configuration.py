import json
import traceback
import logging
from collections import abc


class Configuration(abc.MutableMapping):
    def __init__(self, config_file="config.json"):
        self.log = logging.getLogger(f"{self.__class__.__name__}")
        self.log.debug(f"Initializing  config with file:{config_file}")
        self.config_file = config_file
        self.__config = {}
        self.setup()

    def __getitem__(self, __k: str):
        return self.__config[__k]

    def __getattr__(self, key: str):
        return self.__config[key]

    def __setitem__(self, __k: str, __v: any):
        self.__config[__k] = __v

    def __delitem__(self, __k: str):
        del self.__config[__k]

    def __repr__(self):
        return repr(self.__config)

    def __len__(self) -> int:
        return len(self.__config)

    def __iter__(self) -> iter:
        return iter(self.__config)

    def to_json(self):
        return self.__config

    def from_json(self, json: dict):
        self.__config = json.copy()

    def load(self):
        with open(self.config_file, "r") as f:
            self.from_json(json.load(f))

    def save(self):
        with open(self.config_file, "w") as f:
            json.dump(self.to_json(), f)

    def _setupCfgTerminal(self):
        self.log.debug("Setting up configuration from terminal")
        try:
            keys = "guild role owner_ID team_role_ID broadcast_channel server_ID"
            vals = [
                None, None,
                int(input("OwnerID: ")), int(input("Team role ID: ")),
                input("Name of broadcast channel: "), int(input("Server ID: "))
            ]
            self.__config = {k: v for k, v in zip(keys.split(), vals)}
            self.save()

        except Exception as e:
            self.log.warning("Setup from terminal failed")
            self.log.debug(
                "".join(
                    traceback.TracebackException.from_exception(e).format()
                ))
            raise e.with_traceback(e.__traceback__)

    def setup(self):
        self.log.debug("Configuration  setup")
        loaded = False
        while(not loaded):
            try:
                self.load()
                loaded = True
            except (
                    FileNotFoundError, json.decoder.JSONDecodeError, KeyError
            ) as configError:
                self.log.debug(f"{configError}")
                if input("Would you like to setup the config from the terminal? y/n ") == 'y':
                    self._setupCfgTerminal()
                else:
                    exit(f"Please setup your config: {self.config_file}")
            except Exception as e:
                self.log.warning(
                    "".join(
                        traceback.TracebackException.from_exception(e).format()
                    )
                )
                raise e.with_traceback(e.__traceback__)
