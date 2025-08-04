from datetime import datetime
import threading

class Logger():
    Black="\033[30m"
    Red="\033[31m"
    Yellow="\033[33m"
    Green="\033[32m"
    Blue="\033[34m"
    Purple="\033[35m"
    Cyan="\033[36m"
    Default="\033[0m"

    _log_file = None
    _lock = threading.Lock()

    @staticmethod
    def set_file(path):
        Logger._log_file = path

    @staticmethod
    def _write_to_file(prefix, text):
        if Logger._log_file is None:
            raise ValueError("Log dosyası yolu ayarlanmamış. Logger.set_file(path) ile ayarlamalısın.")
        with Logger._lock: 
            with open(Logger._log_file, "a", encoding="utf-8") as f:
                now = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
                f.write(f"[{now}] {prefix} {text}\n")

    @staticmethod
    def warn(text : str):
        print(Logger.Yellow + text + Logger.Default)
        Logger._write_to_file("[WARN]", text)


    @staticmethod
    def info(text : str):
        print(Logger.Cyan + text + Logger.Default)
        Logger._write_to_file("[INFO]", text)
       
    @staticmethod 
    def error(text : str):
        print(Logger.Red + text + Logger.Default)
        Logger._write_to_file("[ERROR]", text)

       
    @staticmethod 
    def success(text : str):
        print(Logger.Green + text + Logger.Default)
        Logger._write_to_file("[SUCCESS]", text)

    #------------------------------------------------

    @staticmethod
    def coreWarn(coreName : str, text : str):
        print(Logger.Yellow + "["+coreName+"] " + Logger.Default + text)
        formatted = f"[{coreName}] {text}"
        Logger._write_to_file("[WARN]", formatted)


    @staticmethod
    def coreInfo(coreName : str, text : str):
        print(Logger.Cyan + "["+coreName+"] " + Logger.Default + text)
        formatted = f"[{coreName}] {text}"
        Logger._write_to_file("[INFO]", formatted)


    @staticmethod 
    def coreError(coreName : str, text : str):
        print(Logger.Red + "["+coreName+"] " + Logger.Default + text)
        formatted = f"[{coreName}] {text}"
        Logger._write_to_file("[ERROR]", formatted)


    @staticmethod 
    def coreSuccess(coreName : str, text : str):
        print(Logger.Green + "["+coreName+"] " + Logger.Default + text)
        formatted = f"[{coreName}] {text}"
        Logger._write_to_file("[SUCCESS]", formatted)

