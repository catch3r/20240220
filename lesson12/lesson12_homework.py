import requests
from requests import Response
import time
import pandas as pd
from pprint import pprint

from pydantic import BaseModel, RootModel, Field

class BikeOfSite(BaseModel):
    行政區:str = Field(alias='sarea')
    站點名稱:str = Field(alias='sna')
    時間:str = Field(alias='mday')
    總車輛數:int = Field(alias='tot')
    可借:int = Field(alias='sbi')
    可還:int = Field(alias='bemp')

############################

class BikeOfSites(RootModel):
    root:list[BikeOfSite]

    def __iter__(self):
        return iter(self.root)
    
    def __getitem__(self, idx):
        return self.root[idx]

############################

def get_response() -> Response | None:
    url_path:str = 'https://tcgbusfs.blob.core.windows.net/dotapp/youbike/v2/youbike_immediate.json'

    count:int = 0
    limit:int = 3
    delay:int = 5

    while True and count < limit:
        try:
            print(f'執行第 {count + 1} 次下載:')
            response:Response = requests.get(url_path, timeout=15)
            response.raise_for_status()
        except Exception as e:
            count += 1
            print('連線失敗。')
            print(e)

            if count < limit:
                print(f'等待 {delay} 秒後再次嘗試。')
                time.sleep(delay)
        else:
            if response.status_code != 200:
                count += 1
                print('下載失敗。')
                print(response.reason)
                
                if count < limit:
                    print(f'等待 {delay} 秒後再次嘗試。')
                    time.sleep(delay)
            else:
                break
    
    if count >= limit:
        print(f'失敗已達 {limit} 次，不再執行下載動作。')
        return None
    else:
        print('下載成功')
        return response

############################

def jsonToList(raw:str) -> list[dict] | None:
    try:
        datas:BikeOfSites = BikeOfSites.model_validate_json(raw)
        items:list[dict] = datas.model_dump()
        return items
    except Exception as e:
        print('預想外的格式。')
        print(e)
        return None

############################

# def main():
#     response:Response | None = get_response()

#     if not response:
#         print('dsfghdfh111')
#         return
    
#     rawString:str = response.text
#     download_data:list[dict] | None = jsonToList(rawString)

#     if not download_data:
#         return
    
#     #若寫在main()，則pd.DataFrame()不會顯示Table
#     #沒有報錯，原因不明
#     pd.DataFrame(download_data)
    
# main()
    
response:Response | None = get_response()
    
rawString:str = response.text
download_data:list[dict] | None = jsonToList(rawString)
    
grid = pd.DataFrame(download_data)
print(grid)