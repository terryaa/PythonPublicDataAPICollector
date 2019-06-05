
def crop_weather_url(start_date,end_date,area,crop):
    url="http://newsky2.kma.go.kr/service/ProductingAreaInfoService/"
    #younghoon's
    key="serviceKey=iNZ8DZg1HFtHVCCUZPQtblw6HEHV8URCt94wA%2Bk4id5T4URik9Gca3t1ZaLARYqmdxiNZRDMh5HYJr6Jy50Syg%3D%3D"
    #sujin's
    #key="serviceKey=jAkk5tTEPGKz1Zs6w%2FbGGpkPBCc%2BrrJcw2QI9LfcrYD77m2cQJWDgzZP14xOPIOpZQWJm2P2nC2ZsaacfYxcLw%3D%3D"
    #어떤 정보를 가져올건지 동작 선택
    operation="DayStats"
    #시작일
    start_ymd="ST_YMD="+start_date
    #끝일
    end_ymd="ED_YMD="+end_date
    areas={'상주':'4725000000','진주':'4817000001','아산':'4420000088','울산':'3100000088','평택':'4122000000','안성':'4155000000','천안':'4413100001','나주':'4617000000','제주':'5011000000'}
    crops={'배':'PA160101','감귤':'PA010101'}
    area_id="AREA_ID="+areas.get(area)
    crop_id="PA_CROP_SPE_ID="+crops.get(crop)
    
    #crop_name="PA_CROP_NAME=배"
    #crop_name에 한글을 넣으면 url에 한글이 들어가 에러가남으로, 가급적 ID찾아서 사용. 
    #url.encode("UTF-8") -> 한글 을넣을꺼면 url을 utf-8로인코딩하여넣는다. 
    page_no="pageNo="

    api_url=url+operation+"?"
    api_url=api_url+start_ymd+"&"+end_ymd+"&"+area_id+"&"+crop_id+"&"+key+"&"+page_no
    #api_url=api_url+"&"+crop_name

    return api_url


def weather_point_url(start_date,end_date):
    url="https://data.kma.go.kr/apiData/"
    key="apiKey=iMugf3SvQ64Tw6TpPj5NJrXdtYKDxzdx6NBI0vBa1Qsynh6%2BcnZJXOjYE2q9ucTi"
    operation="getData"
    doctype="type=xml"
    dataCd="dataCd=ASOS"
    dateCd="dateCd=DAY"
    startDt="startDt="+start_date
    endDt="endDt="+end_date
    pointno="stnIds=232"
    schListcnt="schListCnt=10"
    pageIndex="pageIndex="
    api_url=url+operation+"?"+doctype+"&"+dataCd+"&"+dateCd+"&"+startDt+"&"+endDt+"&"+pointno+"&"\
    +schListcnt+"&"+key+"&"+pageIndex
    
    return api_url