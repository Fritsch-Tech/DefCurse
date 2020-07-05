import signal
import json
import errno
import traceback
import os
import sys

from typing import Callable
from datetime import datetime
from dataclasses import replace, asdict

from CLI_MVC import constants
from CLI_MVC import terminal

def wrapper(
    model: object,
    view: Callable[[object], None],
    handler: Callable[[object,str], object],
    exit_condition: Callable[[object], bool],
    crash_log_folder: str = None    
) -> object:  
    error = None
    try:
        prev_terminal_state = terminal._init_terminal()
  
        
        def redraw(signum, frame):
            terminal._clear_terminal()
            view(model)
            terminal._draw()
               
                        
        # Re-renders Terminal in case of SIGWINCH(resize) event
        signal.signal(signal.SIGWINCH, redraw)
        
        while exit_condition(model):
            try:
                terminal._clear_terminal()
                view(model)
                terminal._draw()
                
                try:
                    model = handler(model, terminal._get_key())
                except KeyboardInterrupt:
                    break
            except Exception:
                if not os.path.exists(crash_log_folder):
                    raise FileNotFoundError(errno.ENOENT, os.strerror(errno.ENOENT), crash_log_folder)
                
                etype, value, tb = sys.exc_info()
                
                crash_report = json.dumps(
                    {
                        "error":  traceback.format_exception(etype, value, tb),
                        "model":asdict(model),
                    },
                    indent=4
                )
                
                crash_log_file_path = os.path.join(
                        crash_log_folder,
                        datetime.now().strftime("%d-%m-%Y_%H:%M:%S")+".json"
                    )
                
                with open(
                    crash_log_file_path,
                    "w+"
                ) as f:
                    f.write(crash_report)

                raise NameError(crash_log_file_path)
            
    finally:
        terminal._restore_terminal(prev_terminal_state)
        if error:
            print(error)
        return model
        