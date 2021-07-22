"""
Script to retrieve tennis court availabilities on www.openplay.co.uk
"""
#####################################
#       Imports                     #
#####################################

import re
import logging
from typing import Dict
from datetime import datetime

import models

import pandas as pd

from eugenium import BaseWebInteractor

from selenium.webdriver.common.by import By

#####################################
#       OpenPlayInteractor          #
#####################################


class OpenPlayInteractor(BaseWebInteractor):

    # Metadata about the courts on openplay I care about
    COURTS = [{
        "name": "Clissold",
        "id": "3473",
        "slot": "slot-2122"
    }, {
        "name": "Hackney Downs",
        "id": "3633",
        "slot": "slot-2589"
    }, {
        "name": "London Fields",
        "id": "3635",
        "slot": "slot-2606"
    }, {
        "name": "Millfields",
        "id": "3636",
        "slot": "slot-2615"
    }, {
        "name": "Spring Hill",
        "id": "3637",
        "slot": "slot-2619"
    }, {
        "name": "Aske Gardens",
        "id": "3638",
        "slot": "slot-2623"
    }]

    # The hours of the day that courts are bookable on openplay
    time_slots = range(21)[7:]

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.DOMAIN = "www.openplay.co.uk"
        self.BASE_URL = f"https://{self.DOMAIN}/booking/place"
        self.schema = models.config['SCHEMA_NAME']

    def model_court_avaibilities():
        return "Model"

    def single_court_availabilities(self, court: Dict) -> pd.DataFrame:
        """
        Cycles through the dates on a court and adds available time slots to
        a table.

        Returns
        -------
        Pandas DataFrame of court availabilities with columns
            domain : str
            url : str
            openplay_court_id : int
            openplay_court_name : str
            openplay_court_slot : str
            slot_date : date
            slot_hour : int
            slot_available : bool
            datetime_added : timestamp
        """
        data_list = []
        URL = f"{self.BASE_URL}/{court['id']}"
        self.driver.get(URL)
        change_date = self.find(By.ID, "change-date")
        date_options_length = len(
            change_date.find_elements_by_tag_name('option'))
        logging.info(
            f"Checking availabilities at {court['name']} tennis courts with id {court['id']}"
        )
        logging.info(f"num_date_options: {date_options_length}")
        for index in range(date_options_length):
            change_date = self.find(by=By.ID, identifier="change-date")
            date_option = change_date.find_elements_by_tag_name(
                'option')[index]
            this_date = date_option.text
            # logging.info(this_date)
            this_day = re.sub("[ a-zA-Z]", "", this_date)
            this_month = datetime.strptime(this_date[-3:], "%b").month
            now = datetime.now()
            current_month = now.month
            current_year = now.year
            if (current_month == 12 & this_month == 1):
                this_year = current_year + 1
            else:
                this_year = current_year
            this_date_formatted = datetime.strptime(
                f"{this_day}/{this_month}/{this_year}",
                "%d/%m/%Y").strftime("%Y-%m-%d")
            logging.info(this_date_formatted)
            date_option.click()
            try:
                all_slots = self.find_multiple(by=By.CLASS_NAME,
                                               identifier=court['slot'])
                availabilities = [len(s.text) > 0 for s in all_slots]
                for slot in list(zip(availabilities, self.time_slots)):
                    record = {
                        "domain": self.DOMAIN,
                        "url": URL,
                        "openplay_court_id": court['id'],
                        "openplay_court_name": court['name'],
                        "openplay_court_slot": court['slot'],
                        "slot_date": this_date_formatted,
                        "slot_hour": slot[1],
                        "slot_available": slot[0],
                        "datetime_added": datetime.now().strftime("%Y-%m-%d %H:%M:%S")
                    }
                    data_list.append(record)
            except:
                ""
        data = pd.DataFrame.from_records(data=data_list)
        logging.info(data)
        return data

    def all_court_availabilities(self) -> pd.DataFrame:
        data_list = [self.single_court_availabilities(x) for x in self.COURTS]
        data = pd.concat(data_list)
        return data
