from app.core.tasks import BaseTaskHandler
from app.lib.firebase.fcm import send_message


class FirebasePushNotificationTaskHandler(BaseTaskHandler):
    """
    Firebase send push notification task handler
    """
    name = 'firebase.push.send_message'
    state_transition = True
    support_recon = True
    operation_tag = 'send_push_notification'

    def execute(self, params):
        results = send_message(
            params.recipients.split(","), params.message,  dry_run=True
        )
        self.message_obj.data['status']['results'] = results
        return results
