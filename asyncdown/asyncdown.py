import aiohttp
import asyncio
import sys
import time

from dataclasses import dataclass
from dataclasses import field

@dataclass
class FileDwld:
    """Represents a file to download."""
    url: str
    bdowned: int = 0
    size: int = field(init=0)
    name: str = field(init='')

    def __post_init__(self):
        self.name = self.url.split('/')[-1]


class Download():

    # concur = 5
    # urls = None
    # verbose = True

    # status= {}
    # file_list = []

    # time_init = None
    # time_end = None


    def __init__(self, urls, concur = 5, verbose=True):

        self.urls = urls
        self.concur = concur
        self.verbose = verbose
        self.time_init = time.perf_counter()
        self.time_end = 0

        loop = asyncio.get_event_loop()
        results = loop.run_until_complete(self.start(self.urls, self.concur))

        self.time_end = time.perf_counter()

        print(f"Exec time: {self.time_end - self.time_init:0.2f} seconds.")


    def pprint(self):

        list_height = len(self.file_list)
        for i in range(0, list_height):
            sys.stdout.write("\x1b[1A\x1b[2K")  # retorna uma linha acima

        s = f'\r\n'.join(
            [f'{obj.name} Size:({obj.size}) Download:{(obj.bdowned/obj.size)*100:,.2f}%  Bytes:{obj.bdowned:,}' for _, obj in self.file_list.items()])
        print(s)


    async def get_content_length(self, file_dwld):
        '''
        le tamanho dos arquivos previamente
        '''
        async with aiohttp.ClientSession() as session:
            async with session.head(file_dwld.url) as request:
                file_dwld.size = request.content_length
                print(f'{file_dwld.name}: {file_dwld.size}')

    async def fetch_file(self, session, semaphore_qtt, file_dwld):
        async with semaphore_qtt:
            async with session.get(file_dwld.url) as response:
                count_timeout = 0
                with open(file_dwld.name, 'wb') as fd:
                    acc = 0
                    try:
                        async for data in response.content.iter_chunked(4*1024):
                            acc += len(data)
                            file_dwld.bdowned = acc
                            fd.write(data)
                            self.pprint()

                    except asyncio.exceptions.TimeoutError:
                        count_timeout+=1
                        await asyncio.sleep(1)


    async def start(self, urls, concur):

        files = [FileDwld(url) for url in urls]
        self.file_list = {file.name: file for file in files}

        async with aiohttp.ClientSession() as session:
            tasks = [self.get_content_length(file_dwld) for file_dwld in self.file_list.values()]
            await asyncio.gather(*tasks)

        semaphore = asyncio.Semaphore(concur)

        async with aiohttp.ClientSession() as session:
            tasks = [self.fetch_file(session, semaphore, file_dwld) for file_dwld in self.file_list.values()]
            # tasks.insert(0, self.wait_to_print())
            return await asyncio.gather(*tasks)
