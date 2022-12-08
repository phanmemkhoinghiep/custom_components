import datetime
import logging
import requests
import voluptuous as vol
from homeassistant.components.sensor import PLATFORM_SCHEMA
from homeassistant.const import (CONF_DISPLAY_OPTIONS, CONF_TYPE, CONF_SCAN_INTERVAL, CONF_NAME)
from homeassistant.util import Throttle
from homeassistant.helpers.entity import Entity
import homeassistant.helpers.config_validation as cv
import json
_LOGGER = logging.getLogger(__name__)

DOMAIN = "lunar_calenda"
name = ''
SENSOR_TYPES = {
    'lunarDay': ['Ngày âm ', 'mdi:calendar-month'],
    'lunarMonth': ['Tháng âm ', 'mdi:calendar-month'],
    'lunarYear': ['Năm ', 'mdi:calendar-month'],        
    'firstMonth': ['Mồng một ', 'mdi:calendar-month'],    
    'fullMonth': ['Rằm ', 'mdi:calendar-month']        

}
DEFAULT_TYPE_ = 'lunarDay'

SCAN_INTERVAL = datetime.timedelta(seconds=3600)  # 1 hour

PLATFORM_SCHEMA = PLATFORM_SCHEMA.extend({
    vol.Optional(CONF_NAME, default={CONF_TYPE: name}): cv.string,
    vol.Optional(CONF_DISPLAY_OPTIONS, default={CONF_TYPE: DEFAULT_TYPE_}):
        vol.All(
            cv.ensure_list, [vol.In(SENSOR_TYPES)]
        )
})

def setup_platform(hass, config, add_entities, discovery_info=None):
    """Set up the system monitor sensors."""
    global name
    devices = []
    for variable in config[CONF_DISPLAY_OPTIONS]:
        device = lunar_calendar_class(variable)
        devices.append(device)
    add_entities(devices, True)

class lunar_calendar_class(Entity):

    def __init__(self, sensor_type):
        global name
        self._name = SENSOR_TYPES[sensor_type][0] + name
        self.type = sensor_type
        self._state = None
        self._author = 'Nguyễn Duy: phanmemkhoinghiep'
        self._description = 'Version 1.1 - 2022-12-05'
        self.update()
        
    @property
    def name(self):
        return self._name.rstrip()

    @property
    def state(self):
        return self._state

    @property
    def icon(self):
        """Return the icon of the sensor"""
        return SENSOR_TYPES[self.type][1]

    @property
    def device_state_attributes(self):
        return {'Chú thích': self._description, 'Tác giả': self._author}

    @Throttle(SCAN_INTERVAL)
    def update(self):
        data = getData()
        if self.type == 'lunarDay':
            self._state = data[0]
        elif self.type == 'lunarMonth':
            self._state = data[1]            
        elif self.type == 'lunarYear':
            self._state = data[2]               
        elif self.type == 'firstMonth':
            self._state = data[3]                
        elif self.type == 'fullMonth':
            self._state = data[4]                            
                         
            
def getData():
    list_thang = ["tháng Giêng","tháng Hai","tháng Ba","tháng Tư","tháng Năm","tháng Sáu","tháng Bảy","tháng Tám","tháng Chín","tháng Mười","tháng Mười một","tháng Chạp"]  
    lunarDay=1
    lunarMonth=1
    lunarYear=''
    firstMonth=False
    fullMonth=False
    url = "http://vietbot.xyz:5000/api"
    headers = {'Content-Type': 'application/json; charset=utf-8'}
    payload1 = {'data': 'hôm nay âm lịch là mồng mấy'}
    try:
        response = requests.post(url, headers=headers, data= json.dumps(payload1))
        # print(str(response.json()))
        payload2 = response.json()
        answer_text=payload2['answer_text']
        lunarYear=answer_text.split(' năm ')[1]
        if 'mùng' in answer_text:
            if 'mùng một' in answer_text:
                firstMonth=True                
                lunarDay=1
            else:
                lunarDay=int(answer_text.split(' là ')[1].split(' tháng ')[0].split('mùng ')[1])
        else:
            if 'rằm' in answer_text:
                fullMonth=True
                lunarDay=15
            else:
                lunarDay=int(answer_text.split(' là ')[1].split(' tháng ')[0])            
        for i in range(len(list_thang)):
            if list_thang[i] == 'tháng '+ answer_text.split(' tháng ')[1].split(' năm ')[0]:
                lunarMonth=i+1
                break       
    except:
        pass
    return lunarDay, lunarMonth, lunarYear, firstMonth, fullMonth
