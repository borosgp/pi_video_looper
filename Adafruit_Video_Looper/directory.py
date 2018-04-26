# Copyright 2015 Adafruit Industries.
# Author: Tony DiCola
# License: GNU GPLv2, see LICENSE.txt
class DirectoryReader(object):

    def __init__(self, config):
        """Create an instance of a file reader that just reads a single
        directory on disk.
        """
        self._load_config(config)

    def _load_config(self, config):
        #self._path = config.get('directory', 'path0')
        
        import datetime

        currentDT = datetime.datetime.now()
        print (currentDT.strftime("%Y-%m-%d %H:%M:%S"))
        print (currentDT.strftime("%Y/%m/%d"))
        print (currentDT.strftime("%H:%M:%S"))
        print (currentDT.strftime("%I:%M:%S %p"))
        print (currentDT.strftime("%a, %b %d, %Y"))

        DayofMonth = currentDT.day
        print ('Day of Month is ', DayofMonth)
        DayofWeek = currentDT.strftime('%a')
        print ('Day of Week is ', DayofWeek)

        if (DayofWeek == 'Sun'): ## if a Sunday
            print ('It is a Sunday')
            
            if (DayofMonth > 7) and (DayofMonth < 15): ## 1st Sunday
                print ('It is a first Sunday')
                #read video_looper.ini path=/home/pi/Video_W1
                self._path = config.get('directory', 'path1')
                
        else:
            print ('It is not a Sunday')
            return

    def search_paths(self):
        """Return a list of paths to search for files."""
        return [self._path]

    def is_changed(self):
        """Return true if the file search paths have changed."""
        # For now just return false and assume the path never changes.  In the
        # future it might be interesting to watch for file changes and return
        # true if new files are added/removed from the directory.  This is 
        # called in a tight loop of the main program so it needs to be fast and
        # not resource intensive.
        return False

    def idle_message(self):
        """Return a message to display when idle and no files are found."""
        return 'No files found in {0}'.format(self._path)


def create_file_reader(config):
    """Create new file reader based on reading a directory on disk."""
    return DirectoryReader(config)
