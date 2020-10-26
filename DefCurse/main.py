import signal
import json
import errno
import traceback
import os
import sys

from typing import Callable
from datetime import datetime
from dataclasses import replace, asdict

from DefCurse import constants
from DefCurse import terminal

def wrapper(
    model: object,
    view: Callable[[object], None],
    handler: Callable[[object,str], object],
    exit_condition: Callable[[object], bool],
    crash_log_folder: str = None ,   
    debug: bool = False
) -> object:  
    """Entry function for the programm

    Args:
        model (object): The initial model
        view (Callable[[object], None]): Creates the Graphics from the given model
        handler (Callable[[object,str], object]): Ceates a new model from the old one and a keybord input
        exit_condition (Callable[[object], bool]): Tells the programm when to exit, given the current model. Programm stops it returns True
        crash_log_folder (str, optional): Path to save the crashlogs to. Defaults to None.
        debug (bool,optional): If errors should be outputed.Defaults to False.

    Raises:
        FileNotFoundError: If crash_log_folder is not found 

    Returns:
        object: The final state of the model
    """
    error = None
    try:
        prev_terminal_state = terminal._init_terminal()
  
        
        def redraw(signum, frame):
            terminal._clear_terminal()
            view(model)
            terminal._draw()
               
                        
        # Re-renders Terminal in case of SIGWINCH(resize) event
        signal.signal(signal.SIGWINCH, redraw)
        
        while not exit_condition(model):
            try:
                terminal._clear_terminal()
                view(model)
                terminal._draw()
                
                try:
                    model = handler(model, terminal._get_key())
                except KeyboardInterrupt:
                    break
            except Exception as e:
                if debug:
                    error = e
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
                
                break
    except:
        if debug:
            error = e
            
    finally:
        terminal._restore_terminal(prev_terminal_state)
        if error:
            print(error)
        return model
        