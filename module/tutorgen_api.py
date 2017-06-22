import requests
from requests.auth import HTTPBasicAuth
from django.conf import settings

auth = HTTPBasicAuth(settings.TUTORGEN_USER,settings.TUTORGEN_PASS)

class Transaction:
    def __init__(self, attempt):
        
        # construct the post request data
        json = {
            'learner': attempt.user.pk,
            'problem': attempt.activity.pk,
            'result': attempt.points==attempt.max_points,
        }

        # send the post request
        self.response = requests.post("{}/transactions/".format(settings.TUTORGEN_URL_BASE),
            auth=auth,
            json=json,
        )
        self.response_data = self.response.json()
        print "TUTORGEN POST TRANSACTION: sent: {}".format(json)

    def success(self):
        '''
        Returns True if the transaction was successfully created for tutorgen
        '''
        return self.response.status_code == 201


class Activity:
    def __init__(self, user_module):
        '''
        Get a recommendation for new activity
        methods used for getting activity_id and whether student is done with module
        #TODO adjust for post
        '''
        json = {
            'learner': user_module.user.pk,
            'cg1': user_module.module.label,
        }
        self.response = requests.post(
            "{}/activities/".format(settings.TUTORGEN_URL_BASE),
            auth=auth,
            json=json,
        )
        self.response_data = self.response.json()
        print "TUTORGEN: GET ACTIVITY, sent: {}, received: {}".format(json,self.response_data)

    def get_activity_id(self):
        if type(self.response_data) == dict:
            activity_id = self.response_data.get('next_activity',None)
            if activity_id: activity_id = int(activity_id)
            return activity_id
        else:
            return None

    def level_up(self):
        if type(self.response_data) == dict:
            return self.response_data.get('level_up', False)
        elif self.response.status_code == 400:
            return True
        else:
            return False
