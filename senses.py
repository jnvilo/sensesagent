import sensesagent
import sensesagent.collectors.collector
print(sensesagent.version) 

import os
from pathlib import Path

from sensesagent import SensesAgent


def main():
    """Launches the senses agent."""
    
    start_dir = Path(os.path.dirname(os.path.realpath(__file__)))
    sa = SensesAgent(start_dir)
    sa.run_collectors()
    
    
if __name__ == "__main__":
    
    main()