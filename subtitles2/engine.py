import srtfile
import db
import datetime


class Engine(object):
    def __init__(self,src_path,src_title):
        self.title = src_title
        src_file = open(src_path,'rb')
        src = srtfile.SrtIterator(src_file)
        self.chunk_start_time = 0
        time_end = datetime.timedelta(0)
        while True:
            try:
                old_end = time_end
                time_start, time_end, text = src.next()
                dialogue_pause = time_start - old_end
                if dialogue_pause.total_seconds()<30.:
                    self.chunk_dialogue += text
                    continue
                #quite a pause, must be new movie scene, treat as a separate dialogue chunk
                self.chunk_dialogue = text
                self.chunk_start_time = time_start.total_seconds()
                self.dump_chunk()
            except:
                self.dump_chunk()
                break

    def dump_chunk(self):
        db.add_chunk(self.title, int(self.chunk_start_time),
            self.chunk_dialogue)










