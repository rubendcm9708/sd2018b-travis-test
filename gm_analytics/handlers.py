import logging
def get_user_info(username=None):
    logging.debug(username)
    logging.info("Get user info returned")
    return {"user_info": username}

def get_commits_info(username=None, time_range=None):
    logging.info("Get commits info returned")
    return [{'commits_count': 10, 'yyyymmdd_date': '20180101'},
            {'commits_count': 10, 'yyyymmdd_date': '20180102'}]

def get_health():
    logging.info("Get health returned")
    return {"message":"OK"}
