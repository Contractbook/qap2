from os import environ
import logging
import slack

logging.basicConfig()
logging.root.setLevel(logging.NOTSET)
logger = logging.getLogger("QAP2")


def send_greeting_on_slack():
    slack_token = environ.get('SLACK_TOKEN')
    slack_channel = environ.get('SLACK_CHANNEL')
    slack_thread_ts = environ.get('SLACK_THREAD_TS')
    api_key = environ.get('API_KEY')
    app_label = environ.get('APP_LABEL')
    instance_url = f"https://qap2-{app_label}.review-apps.contractbook.com/docs"
    name = environ.get("USER")

    if not slack_token or not slack_channel:
        return

    try:
        client = slack.WebClient(token=slack_token)
        client.chat_postMessage(
            channel=slack_channel,
            thread_ts=slack_thread_ts,
            icon_url='https://res.cloudinary.com/contractbook-staging/image/upload/v1649283154/company_logos/qactf-y0O1acIpv.png',
            username='QA Challenge Notification',
            attachments=[
                {
                    "color": "#60c",
                    "blocks": [
                        {
                            "type": "header",
                            "text": {
                                "type": "plain_text",
                                "text": f"Hi {name}",
                                "emoji": True
                            }
                        },
                        {
                            "type": "section",
                            "text": {
                                "type": "mrkdwn",
                                "text": f"Welcome to the project quality assurance task, I'm your friendly slack bot"
                                        f" and I just wanted to let you know that there is an instance available for"
                                        f" you at {instance_url}. You can use `{api_key}` to authorize."
                            },
                            "accessory": {
                                "type": "image",
                                "image_url": "https://cdn.dribbble.com/users/9663942/screenshots/17462771/media/e82ea5ed212db7fbc3a540bdf33c394d.jpg?compress=1&resize=400x300",
                                "alt_text": "friendly bot waving"
                            }
                        }
                    ]
                }
            ]
        )
    except Exception as e:
        logger.error(f"Failed to send slack greeting with parameters: name={name}, instance_url={instance_url}."
                     f" Error encountered {e}")