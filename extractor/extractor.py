from datetime import datetime, timedelta
from jinja2 import Environment
import requests
import jmespath


class Extract:

    def __init__(self, data_str):
        if len(data_str) != 7:
            raise ValueError("Invalid data string")
        self.url = self.get_url(data_str[2])
        self.extractor_type = data_str[3]
        self.extractor_query = data_str[4]
        self.operator = data_str[5]
        self.desired_value = data_str[6]
    
    def get_url(self, url):
        CUSTOM_VARIABLES = {
            "current_date": datetime.now() - timedelta(hours=6) # TODO: fix it with timezone
        }
        env = Environment()
        def format_date(val, format):
            return val.strftime(format)
        def add_minutes(val, min):
            return val + timedelta(minutes=min)
        env.filters['fmt_date'] = format_date
        env.filters['add_mins'] = add_minutes
        template = env.from_string(url)
        return template.render(CUSTOM_VARIABLES)
    
    def send_mail_flag(self):
        operator_dict = {
            "lt": "<",
            "gt": ">",
            "lte": "<=",
            "gte": ">=",
            "eq": "==",
            "ne": "!="
        }
        if self.extractor_type == "JSON":
            resp = requests.get(self.url)
            if resp.status_code == 200:
                resp_dict = resp.json()
                expression = jmespath.compile(self.extractor_query)
                current_val = float(expression.search(resp_dict))
                eval_exp = f"{current_val} {operator_dict[self.operator]} {self.desired_value}"
                print(eval_exp)
                return eval(eval_exp)
        else:
            raise Exception("Not Implemented")
        raise Exception("Something went wrong")